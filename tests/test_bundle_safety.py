"""Archive boundaries and tamper detection matter for distributing agent files."""
import importlib.util
import io
from pathlib import Path
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


if __name__ == "__main__":
    unittest.main()
