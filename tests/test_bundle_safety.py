"""Archive boundaries and tamper detection matter for distributing agent files."""
import importlib.util
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import tempfile
import unittest
import zipfile

SPEC = importlib.util.spec_from_file_location("bundle", Path(__file__).resolve().parents[1] / "scripts/build_bundle.py")
bundle = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bundle)


def archive(entries):
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as z:
        for name, content in entries:
            z.writestr(name, content)
    return output.getvalue()


class BundleSafety(unittest.TestCase):
    def test_escapes_rejected_on_every_platform(self):
        for name in ("../secret", "a/../../secret", "/absolute", "C:\\absolute", "a\\..\\secret", "a:stream", "a/CON.md", "a/./b", "a//b", "a. /file", "a/file."):
            with self.subTest(name=name), self.assertRaises(ValueError):
                bundle.read_archive(archive([(name, b"x")]))
        # Python's ZIP writer truncates NUL names before serialization.
        with self.assertRaises(ValueError):
            bundle.safe_member("a/\x00b")

    def test_legacy_separator_preserves_bytes(self):
        self.assertEqual(bundle.read_archive(archive([("references\\source.md", b"\xef\xbb\xbfunchanged\r\n")])), {"references/source.md": b"\xef\xbb\xbfunchanged\r\n"})

    def test_case_insensitive_collisions_rejected(self):
        with self.assertRaises(ValueError):
            bundle.read_archive(archive([("SKILL.md", b"a"), ("skill.md", b"b")]))

    def test_symlinks_rejected(self):
        info = zipfile.ZipInfo("link")
        info.create_system = 3
        info.external_attr = (stat.S_IFLNK | 0o777) << 16
        with self.assertRaises(ValueError):
            bundle.read_archive(archive([(info, b"../outside")]))

    def test_source_replacement_rejected(self):
        with self.assertRaisesRegex(ValueError, "digest"):
            bundle.prepare(archive([("MANIFEST.json", b"{}")] ))

    def test_changed_payload_and_unlisted_payload_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            expected = {"plugins/example/payload/SKILL.md": b"original"}
            bundle.write_generated(root, expected)
            (root / "plugins/example/payload/SKILL.md").write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "Changed file"):
                bundle.verify_tree(root, expected)
            (root / "plugins/example/payload/SKILL.md").write_bytes(b"original")
            (root / "plugins/example/payload/private.txt").write_bytes(b"unexpected")
            with self.assertRaisesRegex(ValueError, "Unlisted file"):
                bundle.verify_tree(root, expected)

    def test_release_excludes_operational_state_and_is_deterministic(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "package"
            root.mkdir()
            generated = bundle.prepare((bundle.ROOT / bundle.SOURCE_FILE).read_bytes())
            bundle.write_generated(root, generated)
            for name in ("README.md", "START-HERE.md", "LICENSE.md", "LICENSE-NOTICE.md", "licenses/MIT.txt", "licenses/APEX-PERSONAL-COMMERCIAL.md", "AGENTS.md", ".gitignore", ".gitattributes", "scripts/build_bundle.py", "tests/test_bundle_safety.py"):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"public")
            (root / "README.md").write_bytes(b"public")
            (root / ".env").write_bytes(b"private")
            (root / "qa").mkdir()
            (root / "qa/internal.json").write_bytes(b"internal")
            (root / "scripts/private.env").write_bytes(b"private")
            target = root.parent / "release.zip"
            first = bundle.make_zip(root, target)
            self.assertEqual(first, bundle.make_zip(root, target))
            with zipfile.ZipFile(target) as z:
                self.assertIn("apex-skills-free/README.md", z.namelist())
                self.assertNotIn("apex-skills-free/.env", z.namelist())
                self.assertNotIn("apex-skills-free/qa/internal.json", z.namelist())
                self.assertNotIn("apex-skills-free/scripts/private.env", z.namelist())
                self.assertEqual(z.namelist(), sorted(z.namelist()))


class AppCompatibility(unittest.TestCase):
    """The Claude apps refuse skills that break these rules, so the build must too."""

    @classmethod
    def setUpClass(cls):
        cls.generated = bundle.prepare((bundle.ROOT / bundle.SOURCE_FILE).read_bytes())
        cls.provenance = json.loads(cls.generated["PROVENANCE.json"])

    def test_every_skill_meets_app_rules(self):
        skills = [p for p in self.generated if re.fullmatch(r"plugins/[^/]+/skills/[^/]+/SKILL\.md", p)]
        self.assertEqual(len(skills), 74)
        for path in skills:
            with self.subTest(path=path):
                fields = bundle.frontmatter_fields(self.generated[path])
                bundle.validate_skill(fields.get("name"), fields.get("description"), PurePosixPath(path).parent.name)

    def test_metadata_rules_reject_what_the_apps_reject(self):
        too_long = "x" * (bundle.DESCRIPTION_LIMIT + 1)
        for name, description in (("claude-helper", "ok"), ("anthropic-tools", "ok"), ("Bad-Name", "ok"), ("a--b", "ok"), ("-ab", "ok"), ("ab-", "ok"), ("a" * 65, "ok"), ("ok", ""), ("ok", too_long), ("ok", "use <instructions> here")):
            with self.subTest(name=name, description=description[:20]), self.assertRaises(ValueError):
                bundle.validate_skill(name, description, name)
        with self.assertRaises(ValueError):
            bundle.validate_skill("ok", "Fine description.", "payload")
        bundle.validate_skill("ok-name", "Fine description.", "ok-name")

    def test_install_copies_change_only_frontmatter(self):
        originals = {}
        for product in self.provenance["products"]:
            data = self.generated[product["artifactPath"]]
            originals[product["id"]] = bundle.read_archive(data) if product["artifactPath"].endswith(".zip") else {product["filename"]: data}
        changed = 0
        for payload in self.provenance["payloads"]:
            source = originals[payload["productId"]][payload["sourceMember"]]
            installed = self.generated[payload["path"]]
            self.assertEqual(bundle.digest(source), payload["sourceSha256"])
            if payload["change"] == "none":
                self.assertEqual(installed, source, payload["path"])
                continue
            changed += 1
            if payload["change"] == "frontmatter-added":
                self.assertIsNone(bundle.frontmatter_fields(source))
                self.assertEqual(bundle.split_frontmatter(installed)[1], b"\n" + source)
            else:
                self.assertEqual(bundle.split_frontmatter(installed)[1], bundle.split_frontmatter(source)[1])
        self.assertEqual(changed, 23)

    def test_desktop_zips_hold_one_skill_folder(self):
        archives = self.provenance["desktopArchives"]
        self.assertEqual(len(archives), 74)
        plugin_paths = {p["id"]: p["pluginPath"] for p in self.provenance["products"]}
        for entry in archives:
            name = entry["skill"]
            with self.subTest(skill=name), zipfile.ZipFile(io.BytesIO(self.generated[entry["path"]])) as z:
                names = z.namelist()
                self.assertEqual(names, sorted(names))
                self.assertTrue(all(n.startswith(name + "/") for n in names))
                self.assertIn(f"{name}/SKILL.md", names)
                self.assertIn(f"{name}/LICENSE", names)
                for info in z.infolist():
                    self.assertEqual(info.compress_type, zipfile.ZIP_STORED)
                    self.assertEqual(info.date_time, bundle.ZIP_DATE)
                    relative = info.filename[len(name) + 1:]
                    installed = self.generated.get(f"{plugin_paths[entry['productId']]}/skills/{name}/{relative}")
                    if installed is None:
                        self.assertEqual(relative, "LICENSE")
                    else:
                        self.assertEqual(z.read(info), installed)

    def test_plugins_use_the_default_skills_folder(self):
        market = json.loads(self.generated[".claude-plugin/marketplace.json"])
        self.assertEqual(len(market["plugins"]), bundle.PRODUCT_COUNT)
        for plugin in market["plugins"]:
            base = plugin["source"].removeprefix("./")
            manifest = json.loads(self.generated[f"{base}/.claude-plugin/plugin.json"])
            self.assertEqual(manifest["name"], plugin["name"])
            self.assertNotIn("skills", manifest)
            self.assertNotIn("—", manifest["description"])
            self.assertTrue(any(p.startswith(f"{base}/skills/") for p in self.generated))


if __name__ == "__main__":
    unittest.main()
