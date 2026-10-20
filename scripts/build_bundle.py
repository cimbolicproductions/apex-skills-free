"""Package the approved free bundle without altering workflow or support bytes."""
from __future__ import annotations

import argparse
from hashlib import sha256
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA256 = "25f4b3cfe105525d0261181f15eef61ce697aa47e0aa4a3d9bae6f4327f5700e"
SOURCE_URL = "https://apexskills.dev/api/free-bundle"
SOURCE_FILE = "source/Apex-Skills-Free-Bundle.zip"
PRODUCT_COUNT = 67
APEX_LICENSE = "LicenseRef-Apex-Personal-Commercial-1.0"
LEGACY_PRODUCTS = frozenset({
    "browser-automation", "project-closeout", "upwork-hunter", "website-landlord",
    "seo-keyword-fix", "yt-content-engine", "local-audit", "podcast-wisdom",
    "copywriting-mastery", "product-naming", "web-design-foundations",
    "asset-generator", "ecommerce-listing",
})


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def safe_member(name):
    """Convert legacy Windows separators, rejecting escapes on any platform."""
    name = name.replace("\\", "/")
    require(name and not name.startswith("/"), f"Absolute or empty ZIP path: {name!r}")
    require(not any(ord(c) < 32 for c in name), "Control character in ZIP path")
    parts = name.rstrip("/").split("/")
    require(all(p not in ("", ".", "..") for p in parts), f"Unsafe ZIP path: {name!r}")
    require(all(":" not in p and not p.endswith((".", " ")) for p in parts), f"Nonportable ZIP path: {name!r}")
    for part in parts:
        require(not re.fullmatch(r"(?i:con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?", part), f"Reserved ZIP path: {name!r}")
    return PurePosixPath(*parts).as_posix()


def read_archive(data):
    files = {}
    seen = set()
    total = 0
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        for info in archive.infolist():
            name = safe_member(info.orig_filename)
            mode = info.external_attr >> 16
            require(not stat.S_ISLNK(mode), f"ZIP symlink: {info.filename}")
            require(name.casefold() not in seen, f"ZIP path collision: {name}")
            seen.add(name.casefold())
            if info.is_dir() or info.filename.endswith("\\"):
                continue
            total += info.file_size
            require(total <= 20_000_000, "Archive exceeds extraction limit")
            files[name] = archive.read(info)
    return files


def plugin_name(product_id):
    return "apex-" + product_id.removeprefix("claude-")


def skill_name(data, fallback):
    text = data.decode("utf-8-sig")
    if text.startswith("---\n") or text.startswith("---\r\n"):
        frontmatter = re.split(r"\r?\n---(?:\r?\n|$)", text, maxsplit=1)[0]
        match = re.search(r"(?m)^name:\s*['\"]?([^'\"\r\n]+)['\"]?\s*$", frontmatter)
        if match:
            return match.group(1).strip()
    return fallback


def prepare(source):
    require(digest(source) == SOURCE_SHA256, "Source ZIP digest differs from the reviewed release")
    original = read_archive(source)
    manifest = json.loads(original["MANIFEST.json"])
    artifacts = manifest["artifacts"]
    require(manifest["downloadCount"] == len(artifacts) == PRODUCT_COUNT, "Wrong product count")
    require(len({a["id"] for a in artifacts}) == PRODUCT_COUNT, "Duplicate product ID")
    require(set(original) == {"README.md", "MANIFEST.json", *(a["filename"] for a in artifacts)}, "Unexpected source membership")
    require(digest(original["README.md"]) == manifest["readmeSha256"], "Source README hash differs")
    generated = {SOURCE_FILE: source, "source/MANIFEST.json": original["MANIFEST.json"]}
    plugins = []
    products = []
    payloads = []
    catalog = ["# All 67 skill files and packs", "", "Each row is one product from the free bundle. Packs can contain multiple workflows. Original downloads and extracted skill content have identical bytes to the verified source.", "", "Install a selected plugin with `/plugin install <plugin>@apex-skills-free` after adding this marketplace. See [START HERE](START-HERE.md).", "", "| Product | Download | Claude Code plugin | Workflow folders |", "| --- | --- | --- | --- |"]
    for artifact in artifacts:
        product_id = artifact["id"]
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", product_id), "Invalid product ID")
        filename = artifact["filename"]
        require(safe_member(filename) == filename and "/" not in filename, "Invalid product filename")
        data = original[filename]
        require(digest(data) == artifact["sha256"] and len(data) == artifact["sizeBytes"], f"Artifact mismatch: {filename}")
        generated[f"products/{filename}"] = data
        base = f"plugins/{product_id}"
        is_pack = filename.lower().endswith(".zip")
        members = read_archive(data) if is_pack else {f"{product_id}/SKILL.md": data}
        require(all(not n.lower().endswith(".zip") for n in members), "Unexpected archive inside product")
        skill_files = [n for n in members if PurePosixPath(n).name == "SKILL.md" and not n.startswith("related-skills/")]
        require(skill_files, f"No SKILL.md in {filename}")
        skill_dirs = [str(PurePosixPath(n).parent) for n in sorted(skill_files)]
        skill_paths = ["./payload" if n == "." else f"./payload/{n}" for n in skill_dirs]
        commands = [skill_name(members[n], PurePosixPath(n).parent.name if PurePosixPath(n).parent.name else product_id) for n in sorted(skill_files)]
        require(len(set(commands)) == len(commands), f"Duplicate registered skill name in {product_id}")
        for member, content in members.items():
            destination = f"{base}/payload/{member}"
            generated[destination] = content
            payloads.append({"productId": product_id, "sourceMember": member if is_pack else filename, "path": destination, "sha256": digest(content), "sizeBytes": len(content)})
        name = plugin_name(product_id)
        license_id = APEX_LICENSE if product_id in LEGACY_PRODUCTS else "MIT"
        license_path = "licenses/APEX-PERSONAL-COMMERCIAL.md" if product_id in LEGACY_PRODUCTS else "licenses/MIT.txt"
        generated[f"{base}/LICENSE"] = (ROOT / license_path).read_bytes()
        generated[f"{base}/.claude-plugin/plugin.json"] = json_bytes({"name": name, "version": "1.0.0", "description": artifact["title"], "author": {"name": "Apex Skills"}, "license": license_id, "skills": skill_paths})
        plugins.append({"name": name, "source": f"./{base}", "description": artifact["title"]})
        row = {**artifact, "artifactPath": f"products/{filename}", "pluginPath": base, "pluginName": name, "license": license_id, "skillPaths": skill_paths, "skillNames": commands}
        products.append(row)
        links = ", ".join(f"[{command}]({base}/{folder.removeprefix('./')}/SKILL.md)" for command, folder in zip(commands, skill_paths))
        catalog.append(f"| {artifact['title']} | [Original]({row['artifactPath']}) | `{name}` | {links} |")
    require(len({p["name"] for p in plugins}) == PRODUCT_COUNT, "Plugin name collision")
    require({p["id"] for p in products if p["license"] == APEX_LICENSE} == LEGACY_PRODUCTS, "License scope differs from approved legacy inventory")
    generated[".claude-plugin/marketplace.json"] = json_bytes({"name": "apex-skills-free", "owner": {"name": "Apex Skills"}, "metadata": {"description": "67 free AI agent skill files and packs"}, "plugins": plugins})
    generated["CATALOG.md"] = ("\n".join(catalog) + "\n").encode("utf-8")
    generated["PROVENANCE.json"] = json_bytes({"formatVersion": 1, "sourceUrl": SOURCE_URL, "sourceSha256": SOURCE_SHA256, "sourceSizeBytes": len(source), "productCount": PRODUCT_COUNT, "registeredWorkflowCount": sum(len(p["skillNames"]) for p in products), "pathNormalization": "ZIP backslashes become forward slashes; file bytes are unchanged.", "products": products, "payloads": payloads})
    return generated


def verify_tree(root, generated):
    for relative, expected in generated.items():
        path = root / relative
        require(path.is_file() and not path.is_symlink(), f"Missing file or symlink: {relative}")
        require(path.read_bytes() == expected, f"Changed file: {relative}")
    # Fail on stale products, support files or manifests rather than deleting them.
    for directory in ("plugins", "products", "source", ".claude-plugin"):
        for path in (root / directory).rglob("*"):
            require(not path.is_symlink(), f"Unexpected symlink: {path}")
            if path.is_file():
                require(path.relative_to(root).as_posix() in generated, f"Unlisted file: {path}")
    return {"products": PRODUCT_COUNT, "payloadFiles": len(json.loads(generated["PROVENANCE.json"])["payloads"]), "generatedFiles": len(generated), "sourceSha256": SOURCE_SHA256}


def write_generated(root, generated):
    # Existing unknown files are never removed, and verification flags them.
    for relative, content in generated.items():
        path = root / relative
        require(not path.is_symlink(), f"Refusing symlink: {path}")
        for parent in path.parents:
            if parent == root.parent:
                break
            require(not parent.is_symlink(), f"Refusing symlink parent: {parent}")
        if path.exists() and path.read_bytes() == content:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        pending = path.with_name(path.name + ".pending")
        with pending.open("xb") as output:
            output.write(content)
        pending.replace(path)


def make_zip(root, target):
    # Exact public file roots prevent QA, config and local review notes leaking.
    generated = prepare((root / SOURCE_FILE).read_bytes())
    verify_tree(root, generated)
    maintained = {"README.md", "START-HERE.md", "LICENSE.md", "LICENSE-NOTICE.md", "licenses/MIT.txt", "licenses/APEX-PERSONAL-COMMERCIAL.md", "AGENTS.md", ".gitignore", ".gitattributes", "scripts/build_bundle.py", "tests/test_bundle_safety.py"}
    names = set(generated) | maintained
    files = []
    for name in names:
        path = root / name
        require(path.is_file() and not path.is_symlink(), f"Missing release file or symlink: {name}")
        files.append(path)
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(files, key=lambda p: p.relative_to(root).as_posix()):
            relative = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(f"apex-skills-free/{relative}", date_time=(2000, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, path.read_bytes())
    data = stream.getvalue()
    target = target.resolve()
    require(not target.is_relative_to(root.resolve()), "Release ZIP must be outside the package")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return {"sha256": digest(data), "sizeBytes": len(data), "files": len(files)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-zip", type=Path, default=ROOT / SOURCE_FILE)
    parser.add_argument("--check", action="store_true", help="Verify without writing generated files")
    parser.add_argument("--zip", type=Path, help="Write a deterministic review ZIP outside the package")
    args = parser.parse_args()
    generated = prepare(args.source_zip.read_bytes())
    if not args.check:
        write_generated(ROOT, generated)
    result = verify_tree(ROOT, generated)
    if args.zip:
        result["releaseZip"] = make_zip(ROOT, args.zip)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
