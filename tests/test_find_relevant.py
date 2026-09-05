"""Tests for bounded, package-local PASS card retrieval."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "PASS/tools/find_relevant.py"
SPEC = importlib.util.spec_from_file_location("find_relevant", TOOL)
assert SPEC and SPEC.loader
finder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = finder
SPEC.loader.exec_module(finder)


def write_card(path: Path, object_id: str, object_type: str, name: str, tags: list[str], rule: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        f"object_id: {object_id}\n"
        f"object_type: {object_type}\n"
        f"name: {name}\n"
        "library_path: [demo, topic]\n"
        f"tags: {tags!r}\n"
        "---\n\n"
        f"# {name}\n\n## Pattern Rule\n**IF** {rule}\n**THEN** act\n",
        encoding="utf-8",
    )


class RelevantCardTests(unittest.TestCase):
    def test_ranking_prefers_name_tags_and_decision_over_body_only(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            library = Path(temp_dir) / "library"
            write_card(
                library / "demo/topic/PAT_cache.md", "PAT_cache", "pattern",
                "Invalidate a Cache After Assignment", ["cache", "assignment"],
                "assignment can leave a cached value stale",
            )
            write_card(
                library / "demo/topic/PAT_other.md", "PAT_other", "pattern",
                "Unrelated Decision", ["misc"], "a note mentions cache once",
            )
            matches = finder.find_matches(library, "demo", "cache assignment", limit=2)
            self.assertEqual([item.object_id for item in matches], ["PAT_cache", "PAT_other"])
            self.assertGreater(matches[0].score, matches[1].score)

    def test_search_never_crosses_the_selected_package(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            library = Path(temp_dir) / "library"
            write_card(
                library / "demo/topic/PAT_local.md", "PAT_local", "pattern",
                "Local Cache", ["cache"], "a cache decision",
            )
            write_card(
                library / "other/topic/PAT_foreign.md", "PAT_foreign", "pattern",
                "Foreign Cache", ["cache"], "a cache decision",
            )
            matches = finder.find_matches(library, "demo", "cache")
            self.assertEqual([item.object_id for item in matches], ["PAT_local"])

    def test_type_filter_and_limit_are_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            library = Path(temp_dir) / "library"
            write_card(
                library / "demo/topic/AP_cache.md", "AP_cache", "ap",
                "Review Cache Behavior", ["cache"], "cache behavior needs review",
            )
            write_card(
                library / "demo/topic/PAT_cache.md", "PAT_cache", "pattern",
                "Cache Behavior", ["cache"], "cache behavior needs review",
            )
            matches = finder.find_matches(
                library, "demo", "cache", limit=1, object_types={"pattern"}
            )
            self.assertEqual([item.object_type for item in matches], ["pattern"])

    def test_unknown_package_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            library = Path(temp_dir) / "library"
            library.mkdir()
            with self.assertRaises(ValueError):
                finder.find_matches(library, "missing", "cache")


if __name__ == "__main__":
    unittest.main()
