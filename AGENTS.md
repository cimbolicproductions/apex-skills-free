# Apex free bundle maintenance

- The approved source is `source/Apex-Skills-Free-Bundle.zip`, pinned by SHA256 in `scripts/build_bundle.py`. Never glob a private skills folder into a release.
- Preserve all 67 original product artifacts and every extracted skill/support byte. Only paths are normalized for ZIP entries that use Windows separators.
- Generate with `python scripts/build_bundle.py`. Verify with `python scripts/build_bundle.py --check` and `python -m unittest discover -s tests`.
- Claude Code marketplace validation does not fully validate plugin components. Validate the root and every product plugin, then test installation and inspect the component inventory using an isolated `CLAUDE_CONFIG_DIR`.
- Thirteen legacy skills have no frontmatter. Preserve them; Claude Code accepts them with documented warnings. Avoid `--strict` until a separately approved content migration.
- Count 67 product files and packs separately from inner workflows. The AEO pack retains five related copies as support, not duplicate plugin registrations.
- Preserve the mixed licensing in LICENSE.md: 54 existing MIT products; 13 legacy products under the Apex Personal and Commercial Use License. Plugin LICENSE copies and provenance mappings are generated; never rewrite source payload notices.
- Dominic authorized this public repository and delegated the license decision on 2026-10-20. Further changes need authorization through their task scope. Phase 2 directory submissions and each awesome-list PR need separate fresh approval.
- Run `python scripts/build_bundle.py --check --zip ../dist/apex-skills-free.zip` for a deterministic review archive. Operational QA and local review notes stay outside this folder.
