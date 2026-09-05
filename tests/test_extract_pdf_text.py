"""Tests for the disposable workspace PDF text extractor."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "workspace/tools/extract_pdf_text.py"
SPEC = importlib.util.spec_from_file_location("extract_pdf_text", TOOL)
assert SPEC and SPEC.loader
extractor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(extractor)


class PageSelectionTests(unittest.TestCase):
    def test_default_selects_every_page(self) -> None:
        self.assertEqual(extractor.parse_page_spec(None, 4), [0, 1, 2, 3])

    def test_ranges_are_one_based_sorted_and_deduplicated(self) -> None:
        self.assertEqual(extractor.parse_page_spec("4,2-3,3", 5), [1, 2, 3])

    def test_invalid_or_out_of_bounds_ranges_fail(self) -> None:
        for spec in ("0", "3-2", "1,", "six", "2-6"):
            with self.subTest(spec=spec):
                with self.assertRaises(ValueError):
                    extractor.parse_page_spec(spec, 5)


class TextNormalizationTests(unittest.TestCase):
    def test_normalization_removes_soft_and_line_break_hyphenation(self) -> None:
        text = "inter-\nruption and soft\u00adhyphen\n\nNext paragraph"
        self.assertEqual(
            extractor.normalize_page_text(text),
            "interruption and softhyphen\n\nNext paragraph",
        )

    def test_unwrap_joins_lines_inside_paragraphs_only(self) -> None:
        text = "one line\nsecond line\n\nnew paragraph"
        self.assertEqual(
            extractor.normalize_page_text(text, unwrap=True),
            "one line second line\n\nnew paragraph",
        )

    def test_rendering_preserves_source_and_page_boundaries(self) -> None:
        rendered = extractor.render_extraction(
            "book.pdf", [(2, "Second"), (5, "Fifth")]
        )
        self.assertTrue(rendered.startswith("# Extracted text: book.pdf\n\n"))
        self.assertIn("--- PAGE 2 ---\n\nSecond", rendered)
        self.assertIn("--- PAGE 5 ---\n\nFifth", rendered)


if __name__ == "__main__":
    unittest.main()
