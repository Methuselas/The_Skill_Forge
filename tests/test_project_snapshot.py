"""Tests for the pruned Project-chat snapshot builder."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "workspace/tools/build_project_snapshot.py"
SPEC = importlib.util.spec_from_file_location("build_project_snapshot", TOOL)
assert SPEC and SPEC.loader
snapshot = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(snapshot)


class SnapshotSelectionTests(unittest.TestCase):
    def test_domain_snapshot_includes_only_selected_canon_and_default_metaskills(self) -> None:
        files = snapshot.collect_snapshot_files(ROOT, ["game-design"])
        relative = {path.relative_to(ROOT).as_posix() for path in files}

        self.assertIn("PASS/SKILL.md", relative)
        self.assertIn("library/metaskills/INDEX.md", relative)
        self.assertIn("library/game-design/INDEX.md", relative)
        self.assertIn("memory/game-design/skill_memory.yaml", relative)
        self.assertIn(".claude/skills/game-design/SKILL.md", relative)
        self.assertIn(".agents/skills/game-design/SKILL.md", relative)
        self.assertFalse(any(path.startswith("library/art/") for path in relative))
        self.assertFalse(any(path.startswith("library/writing/") for path in relative))

    def test_snapshot_selection_excludes_sources_archives_and_pdf_files(self) -> None:
        files = snapshot.collect_snapshot_files(ROOT, ["software-engineering"])
        relative = {path.relative_to(ROOT).as_posix() for path in files}

        self.assertFalse(any("workspace/sources" in path for path in relative))
        self.assertFalse(any(path.startswith("archive/") for path in relative))
        self.assertFalse(any(path.casefold().endswith((".pdf", ".zip")) for path in relative))

    def test_written_snapshot_has_one_stable_root_and_no_other_domain(self) -> None:
        files = snapshot.collect_snapshot_files(ROOT, ["game-design"])
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "snapshot.zip"
            root_name = "SkillForge-project-game-design"
            with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                for path in files:
                    relative = path.relative_to(ROOT)
                    archive.write(path, (Path(root_name) / relative).as_posix())

            with zipfile.ZipFile(output) as archive:
                names = archive.namelist()
            self.assertTrue(names)
            self.assertTrue(all(name.startswith(root_name + "/") for name in names))
            self.assertFalse(any("/library/art/" in name for name in names))

    def test_explicit_source_text_gets_a_flat_visible_archive_path(self) -> None:
        path = Path("C:/outside/a-book.txt")
        self.assertEqual(
            snapshot.source_input_name("SkillForge-project-writing", path),
            "SkillForge-project-writing/SOURCE_INPUT/a-book.txt",
        )


if __name__ == "__main__":
    unittest.main()
