"""Package the approved free bundle for Claude Code, the Claude apps and Codex.

products/ keeps every verified original download byte for byte. plugins/ and
desktop/ hold install copies: each skill sits in skills/<name>/, and a SKILL.md
gets only the frontmatter changes the Claude apps require (a name and
description, no reserved words, a description within the limit). Instruction
bodies and support files keep their original bytes.
"""
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
REPO_URL = "https://github.com/cimbolicproductions/apex-skills-free"
PRODUCT_COUNT = 67
PLUGIN_VERSION = "1.1.0"
APEX_LICENSE = "LicenseRef-Apex-Personal-Commercial-1.0"
LEGACY_PRODUCTS = frozenset({
    "browser-automation", "project-closeout", "upwork-hunter", "website-landlord",
    "seo-keyword-fix", "yt-content-engine", "local-audit", "podcast-wisdom",
    "copywriting-mastery", "product-naming", "web-design-foundations",
    "asset-generator", "ecommerce-listing",
})

# Skill metadata rules shared by the Agent Skills specification and the Claude
# apps: https://agentskills.io/specification and
# https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
NAME_LIMIT = 64
DESCRIPTION_LIMIT = 1024
RESERVED_WORDS = ("anthropic", "claude")
XML_TAG = re.compile(r"<[^>]*>")

# Install-copy metadata for the 13 legacy files, which have no frontmatter.
LEGACY_DESCRIPTIONS = {
    "browser-automation": "Turns a plain-English browser task, such as renaming a Vercel project or downloading invoices from a dashboard, into a step-by-step JSON script an autonomous browser agent can run. Use when the user wants to automate a repetitive website task or needs browser steps for Playwright, Puppeteer or a browser agent.",
    "project-closeout": "Writes a short markdown handoff at the end of a work session: what got done, what is blocked, and the next two or three tasks in priority order. Use when the user is wrapping up a coding or work session, handing work to someone else, or wants a SESSION_HANDOFF.md to resume from.",
    "upwork-hunter": "Scores an Upwork job post from 1 to 10 for automation fit, names the client's core pain point, and drafts a proposal under 200 words. Use when the user pastes an Upwork or freelance job description, asks whether a job is worth bidding on, or wants a proposal written.",
    "website-landlord": "Builds a rank-and-rent plan for a local lead-generation website: domain ideas, page structure, call-focused headline copy, local trust signals and a script for renting the site to a contractor. Use when the user names a niche and city or asks about rank and rent or website landlord sites.",
    "seo-keyword-fix": "Runs a staged SEO pipeline on a website: site audit, keyword research from free sources, topic clusters with pillar pages, and an exact on-page plan for each URL, with an optional apply mode that edits the code and opens a pull request. Use when the user wants an SEO audit, keyword research, a content cluster plan or on-page SEO fixes. Start in plan-only mode.",
    "yt-content-engine": "Turns a raw YouTube or podcast transcript into show notes, a 5-slide LinkedIn carousel outline and a newsletter hook, using only what the speaker actually said. Use when the user pastes a video or audio transcript and wants it repurposed into written content.",
    "local-audit": "Audits a local or small business from a short intake and returns two or three practical automation fixes, each with setup steps and estimated hours or dollars saved per week. Use when the user describes a business and asks where AI or automation could save time or win more customers.",
    "podcast-wisdom": "Turns a long podcast or interview transcript into a concept-based note: core thesis, mental models, verbatim quotes and one action to take today, formatted for Obsidian or Notion. Use when the user shares a podcast transcript or wants an episode turned into second-brain notes.",
    "copywriting-mastery": "Writes direct-response copy for landing pages, emails, ads and social posts using AIDA, PAS or BAB, with benefits over features, plain language, three ranked headlines and one clear call to action. Use when the user asks for sales copy, an ad, an email or a page that needs to convert better.",
    "product-naming": "Generates five or more name options for a product, feature, company or domain, each with a one-line rationale and domain ideas, then picks the top three. Use when the user is naming something new or wants better name ideas.",
    "web-design-foundations": "Reviews a UI description, screenshot or Tailwind code for visual hierarchy, usability and implementation, then gives exactly three specific fixes. Use when the user wants design feedback, a UX or UI review, or asks to roast and improve a page.",
    "asset-generator": "Turns a request for an app or web visual, such as an app icon, splash screen, hero image or social share image, into structured image-model prompts with style, composition and constraint tags plus the right aspect ratio. Use when the user needs prompts for Midjourney, DALL-E, Gemini or another image generator.",
    "ecommerce-listing": "Writes a marketplace listing from item details or a photo: an 80-character keyword title, five to seven item specifics and a mobile-friendly description. Use when the user is listing an item on eBay, Poshmark or Shopify or wants a listing improved.",
}

# The apps reject skill names containing a reserved word.
RENAMED_SKILLS = {
    "claude-context-hygiene": "context-hygiene",
    "claude-cost-optimizer": "cost-optimizer",
    "claude-fail-loud": "fail-loud",
    "claude-hook-setup": "hook-setup",
    "claude-mcp-server-builder": "mcp-server-builder",
    "claude-mcp-setup": "mcp-setup",
    "claude-pr-review": "pr-review",
    "claude-session-handoff": "session-handoff",
    "claude-worktree-parallel-setup": "worktree-parallel-setup",
}

# Applied only while the original description is over the limit.
SHORTENED_DESCRIPTIONS = {
    "brand-voice-engine": "Generate a complete brand voice and content engine for your business in one Claude session. Use when the buyer says 'build my brand voice', 'I need a content engine', 'set up my newsletter and blog voice', 'configure brand for my company', '/brand-voice-engine', or any request for brand identity + content workflow setup. Walks the buyer through a 15-question brand interview, researches their niche with whatever research tools the agent has, applies proven copywriting and writing methods (Halbert, Sugarman, Ogilvy, Parr, Handley, King, Graham, Ravikant and Kennedy) to their brand parameters, then generates a personalized brand voice document plus three companion content skills (newsletter, blog and tweet pipelines).",
}

# Plugin descriptions for products that hold more than one skill.
PACK_DESCRIPTIONS = {
    "context-vault": "Eight skills for building and maintaining a personal context vault: folder setup, guided brain dumps, project pages, blocker triage, weekly reviews, AI handoff briefs, a personal operating system map and routing for new notes.",
}

DESKTOP_DIR = "desktop"
ZIP_DATE = (2000, 1, 1, 0, 0, 0)


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


def split_frontmatter(data):
    """Return (frontmatter text, body bytes); frontmatter is None when absent."""
    text = data.decode("utf-8-sig")
    match = re.match(r"---\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.S)
    if not match:
        return None, data.removeprefix(b"\xef\xbb\xbf")
    return match.group(1), text[match.end():].encode("utf-8")


def scalar(value):
    value = value.strip()
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'"):
        require(value.endswith("'") and len(value) > 1, f"Unterminated quoted value: {value!r}")
        return value[1:-1].replace("''", "'")
    return value


def frontmatter_fields(data):
    """Top-level scalar keys of a SKILL.md frontmatter, or None without one."""
    front, _ = split_frontmatter(data)
    if front is None:
        return None
    fields = {}
    for line in front.splitlines():
        match = re.match(r"([A-Za-z][\w-]*):(.*)$", line)
        if match:
            require(match.group(1) not in fields, f"Duplicate frontmatter key: {match.group(1)}")
            fields[match.group(1)] = scalar(match.group(2))
    return fields


def validate_skill(name, description, folder):
    """Fail the build on metadata the Claude apps or the specification reject."""
    require(isinstance(name, str) and SKILL_NAME.fullmatch(name), f"Invalid skill name: {name!r}")
    require(len(name) <= NAME_LIMIT, f"Skill name over {NAME_LIMIT} characters: {name}")
    require(not any(word in name for word in RESERVED_WORDS), f"Reserved word in skill name: {name}")
    require(folder == name, f"Skill folder {folder!r} differs from its name {name!r}")
    require(isinstance(description, str) and description.strip(), f"Missing description: {name}")
    require(len(description) <= DESCRIPTION_LIMIT, f"Description over {DESCRIPTION_LIMIT} characters: {name}")
    require(not XML_TAG.search(description), f"XML tag in description: {name}")


def replace_field(data, key, value):
    """Replace one top-level frontmatter line, leaving every other byte alone."""
    text = data.decode("utf-8-sig")
    match = re.match(r"---\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.S)
    require(match, "No frontmatter to edit")
    front = match.group(1)
    edited, count = re.subn(rf"(?m)^{re.escape(key)}:[^\r\n]*", lambda _: f"{key}: {value}", front)
    require(count == 1, f"Expected one {key} line, found {count}")
    return (text[:match.start(1)] + edited + text[match.end(1):]).encode("utf-8")


def install_skill(product_id, data, license_id):
    """Return (name, install bytes, change label) for one SKILL.md."""
    fields = frontmatter_fields(data)
    if fields is None:
        require(product_id in LEGACY_PRODUCTS and product_id in LEGACY_DESCRIPTIONS, f"No frontmatter or metadata for {product_id}")
        name = product_id
        header = f"---\nname: {name}\ndescription: {json.dumps(LEGACY_DESCRIPTIONS[product_id])}\nlicense: {license_id}\n---\n\n"
        return name, header.encode("utf-8") + data.removeprefix(b"\xef\xbb\xbf"), "frontmatter-added"
    require(product_id not in LEGACY_DESCRIPTIONS, f"Legacy metadata no longer needed for {product_id}")
    original = fields.get("name", "")
    name = RENAMED_SKILLS.get(original, original)
    changes = []
    if name != original:
        data = replace_field(data, "name", name)
        changes.append("name-changed")
    if product_id in SHORTENED_DESCRIPTIONS:
        require(len(fields.get("description", "")) > DESCRIPTION_LIMIT, f"Shortened description for {product_id} is obsolete")
        data = replace_field(data, "description", json.dumps(SHORTENED_DESCRIPTIONS[product_id]))
        changes.append("description-shortened")
    return name, data, "+".join(changes) or "none"


def desktop_archive(name, files, license_text):
    """One upload-ready ZIP: a single top-level folder named after the skill.

    Entries are stored uncompressed with fixed metadata, so the bytes do not
    depend on the local zlib build.
    """
    entries = dict(files)
    entries.setdefault("LICENSE", license_text)
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for relative in sorted(entries):
            info = zipfile.ZipInfo(f"{name}/{relative}", date_time=ZIP_DATE)
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, entries[relative])
    return stream.getvalue()


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
    archives = []
    all_skills = set()
    catalog = [
        "# All 67 skill files and packs",
        "",
        "Each row is one product from the free bundle. Packs can contain several skills.",
        "",
        "- **Claude desktop app or claude.ai:** download a skill from the Desktop upload column, then go to **Customize > Skills**, click **+**, choose **Create skill**, then **Upload a skill**. On Pro, Max, Team or Enterprise you can instead add the whole marketplace once. See [START HERE](START-HERE.md).",
        "- **Claude Code:** add this marketplace, then run `/plugin install <plugin>@apex-skills-free`.",
        "- **Original download:** the untouched file from the Apex free bundle. The install copies add only the name and description fields the apps require.",
        "",
        "| Product | Desktop upload | Claude Code plugin | Skills | Original download |",
        "| --- | --- | --- | --- | --- |",
    ]
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
        skill_files = sorted(n for n in members if PurePosixPath(n).name == "SKILL.md" and not n.startswith("related-skills/"))
        require(skill_files, f"No SKILL.md in {filename}")
        license_id = APEX_LICENSE if product_id in LEGACY_PRODUCTS else "MIT"
        license_path = "licenses/APEX-PERSONAL-COMMERCIAL.md" if product_id in LEGACY_PRODUCTS else "licenses/MIT.txt"
        license_text = (ROOT / license_path).read_bytes()

        # Map each skill's source folder to its install name and SKILL.md bytes.
        skills = {}
        for member in skill_files:
            folder = str(PurePosixPath(member).parent)
            name, content, change = install_skill(product_id, members[member], license_id)
            fields = frontmatter_fields(content)
            validate_skill(fields.get("name"), fields.get("description"), name)
            require(name not in all_skills, f"Skill name used twice: {name}")
            all_skills.add(name)
            skills[folder] = {"name": name, "member": member, "content": content, "change": change, "originalName": (frontmatter_fields(members[member]) or {}).get("name"), "description": fields["description"]}
        require(len(skills) == 1 or "." not in skills, f"Root skill shares {filename} with other skills")

        def destination(member):
            if "." in skills:
                return f"{base}/skills/{skills['.']['name']}/{member}"
            for folder, skill in skills.items():
                if member.startswith(folder + "/"):
                    return f"{base}/skills/{skill['name']}/{member[len(folder) + 1:]}"
            # Pack-level files sit beside the skills at the plugin root.
            require(not member.startswith(("skills/", ".claude-plugin/")) and member != "LICENSE", f"Pack file collides with plugin layout: {member}")
            return f"{base}/{member}"

        install_bytes = {}
        for member, content in members.items():
            path = destination(member)
            skill = next((s for s in skills.values() if s["member"] == member), None)
            installed = skill["content"] if skill else content
            require(path not in generated, f"Install path collision: {path}")
            generated[path] = installed
            install_bytes[path] = installed
            payloads.append({"productId": product_id, "sourceMember": member if is_pack else filename, "path": path, "sha256": digest(installed), "sizeBytes": len(installed), "sourceSha256": digest(content), "change": skill["change"] if skill else "none"})

        name = plugin_name(product_id)
        ordered = sorted(skills.values(), key=lambda s: s["name"])
        description = ordered[0]["description"] if len(ordered) == 1 else PACK_DESCRIPTIONS[product_id]
        # Plugin cards are new public copy, which avoids em dashes.
        description = description.replace(" — ", " - ").replace("—", " - ")
        generated[f"{base}/LICENSE"] = license_text
        generated[f"{base}/.claude-plugin/plugin.json"] = json_bytes({"name": name, "displayName": artifact["title"], "version": PLUGIN_VERSION, "description": description, "author": {"name": "Apex Skills"}, "license": license_id})
        plugins.append({"name": name, "source": f"./{base}", "description": description})

        desktop = []
        for skill in ordered:
            prefix = f"{base}/skills/{skill['name']}/"
            files = {path[len(prefix):]: content for path, content in install_bytes.items() if path.startswith(prefix)}
            archive = desktop_archive(skill["name"], files, license_text)
            archive_path = f"{DESKTOP_DIR}/{skill['name']}.zip"
            generated[archive_path] = archive
            desktop.append(archive_path)
            archives.append({"skill": skill["name"], "productId": product_id, "path": archive_path, "sha256": digest(archive), "sizeBytes": len(archive), "files": len(files) + ("LICENSE" not in files)})

        row = {**artifact, "artifactPath": f"products/{filename}", "pluginPath": base, "pluginName": name, "license": license_id, "skillNames": [s["name"] for s in ordered], "originalSkillNames": [s["originalName"] for s in ordered], "desktopArchives": desktop}
        products.append(row)
        uploads = ", ".join(f"[{s['name']}.zip]({REPO_URL}/raw/main/{DESKTOP_DIR}/{s['name']}.zip)" for s in ordered)
        links = ", ".join(f"[{s['name']}]({base}/skills/{s['name']}/SKILL.md)" for s in ordered)
        catalog.append(f"| {artifact['title']} | {uploads} | `{name}` | {links} | [{filename}]({row['artifactPath']}) |")
    require(len({p["name"] for p in plugins}) == PRODUCT_COUNT, "Plugin name collision")
    require({p["id"] for p in products if p["license"] == APEX_LICENSE} == LEGACY_PRODUCTS, "License scope differs from approved legacy inventory")
    require(set(RENAMED_SKILLS.values()) <= all_skills, "A skill rename no longer applies")
    generated[".claude-plugin/marketplace.json"] = json_bytes({"name": "apex-skills-free", "owner": {"name": "Apex Skills"}, "metadata": {"description": "67 free AI agent skill files and packs", "version": PLUGIN_VERSION}, "plugins": plugins})
    generated["CATALOG.md"] = ("\n".join(catalog) + "\n").encode("utf-8")
    generated["PROVENANCE.json"] = json_bytes({
        "formatVersion": 2,
        "sourceUrl": SOURCE_URL,
        "sourceSha256": SOURCE_SHA256,
        "sourceSizeBytes": len(source),
        "productCount": PRODUCT_COUNT,
        "registeredWorkflowCount": len(all_skills),
        "pathNormalization": "ZIP backslashes become forward slashes. Install copies place each skill in plugins/<product>/skills/<name>/ and pack-level files at the plugin root.",
        "installChanges": "products/ holds the original bytes. In install copies, frontmatter-added means a name, description and license header was placed before the unchanged original text; name-changed and description-shortened edit only that one frontmatter line. Every other file keeps its source bytes (sourceSha256).",
        "products": products,
        "payloads": payloads,
        "desktopArchives": archives,
    })
    return generated


def verify_tree(root, generated):
    for relative, expected in generated.items():
        path = root / relative
        require(path.is_file() and not path.is_symlink(), f"Missing file or symlink: {relative}")
        require(path.read_bytes() == expected, f"Changed file: {relative}")
    # Fail on stale products, support files or manifests rather than deleting them.
    for directory in ("plugins", "products", "source", ".claude-plugin", DESKTOP_DIR):
        for path in (root / directory).rglob("*"):
            require(not path.is_symlink(), f"Unexpected symlink: {path}")
            if path.is_file():
                require(path.relative_to(root).as_posix() in generated, f"Unlisted file: {path}")
    provenance = json.loads(generated["PROVENANCE.json"])
    return {"products": PRODUCT_COUNT, "skills": provenance["registeredWorkflowCount"], "payloadFiles": len(provenance["payloads"]), "desktopArchives": len(provenance["desktopArchives"]), "generatedFiles": len(generated), "sourceSha256": SOURCE_SHA256}


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
            info = zipfile.ZipInfo(f"apex-skills-free/{relative}", date_time=ZIP_DATE)
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
