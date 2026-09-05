#!/usr/bin/env python3
"""Extract a bounded, disposable text view from a source PDF.

This is factory tooling, not PASS state. The output is a convenience copy for a
current reading session and must never become card provenance or a release
dependency.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path


def parse_page_spec(spec: str | None, page_count: int) -> list[int]:
    """Return sorted zero-based page indexes from a one-based range expression."""
    if page_count < 1:
        return []
    if not spec:
        return list(range(page_count))

    selected: set[int] = set()
    for raw_part in spec.split(","):
        part = raw_part.strip()
        if not part:
            raise ValueError("empty page-range component")
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            if not start_text.isdigit() or not end_text.isdigit():
                raise ValueError(f"invalid page range: {part!r}")
            start, end = int(start_text), int(end_text)
            if start > end:
                raise ValueError(f"descending page range: {part!r}")
        elif part.isdigit():
            start = end = int(part)
        else:
            raise ValueError(f"invalid page number: {part!r}")

        if start < 1 or end > page_count:
            raise ValueError(
                f"page range {part!r} is outside 1-{page_count}"
            )
        selected.update(range(start - 1, end))
    return sorted(selected)


def normalize_page_text(text: str, unwrap: bool = False) -> str:
    """Normalize extraction noise without erasing page or paragraph structure."""
    text = unicodedata.normalize("NFC", text or "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u00ad", "")
    text = re.sub(r"(?<=[A-Za-z])-\s*\n\s*(?=[a-z])", "", text)
    lines = [re.sub(r"[ \t]+", " ", line).rstrip() for line in text.split("\n")]

    if unwrap:
        paragraphs: list[str] = []
        current: list[str] = []
        for line in lines:
            if line.strip():
                current.append(line.strip())
            elif current:
                paragraphs.append(" ".join(current))
                current = []
        if current:
            paragraphs.append(" ".join(current))
        return "\n\n".join(paragraphs).strip()

    normalized = "\n".join(lines)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def render_extraction(source_name: str, pages: list[tuple[int, str]]) -> str:
    parts = [f"# Extracted text: {source_name}"]
    for page_number, text in pages:
        parts.append(f"--- PAGE {page_number} ---\n\n{text}".rstrip())
    return "\n\n".join(parts).rstrip() + "\n"


def extract_pages(reader: object, indexes: list[int], unwrap: bool) -> list[tuple[int, str]]:
    pages: list[tuple[int, str]] = []
    for index in indexes:
        try:
            raw = reader.pages[index].extract_text() or ""
        except Exception as exc:
            raise RuntimeError(f"text extraction failed on page {index + 1}: {exc}") from exc
        pages.append((index + 1, normalize_page_text(raw, unwrap=unwrap)))
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract selected PDF pages to UTF-8 text with stable page markers.",
        epilog=(
            "The output is disposable authoring input. Low-text pages should be "
            "inspected visually or sent through OCR rather than treated as empty."
        ),
    )
    parser.add_argument("pdf", type=Path, help="Source PDF.")
    parser.add_argument("output", type=Path, help="Destination UTF-8 text file.")
    parser.add_argument(
        "--pages", metavar="RANGES",
        help="One-based pages such as 1-12,15,18-22. Default: every page.",
    )
    parser.add_argument(
        "--min-text-chars", type=int, default=80,
        help="Report selected pages below this non-whitespace character count (default: 80).",
    )
    parser.add_argument(
        "--unwrap", action="store_true",
        help="Join non-blank lines within each paragraph; leave off when headings/layout matter.",
    )
    parser.add_argument(
        "--report-json", type=Path,
        help="Optional path for a disposable extraction-quality report.",
    )
    parser.add_argument("--force", action="store_true", help="Replace an existing output file.")
    args = parser.parse_args()

    if not args.pdf.is_file():
        parser.error(f"source PDF does not exist: {args.pdf}")
    if args.output.exists() and not args.force:
        parser.error(f"output already exists: {args.output} (use --force to replace it)")
    if args.report_json and args.report_json.exists() and not args.force:
        parser.error(
            f"report already exists: {args.report_json} (use --force to replace it)"
        )
    if args.min_text_chars < 0:
        parser.error("--min-text-chars must be zero or greater")
    source_path = args.pdf.resolve()
    output_path = args.output.resolve()
    report_path = args.report_json.resolve() if args.report_json else None
    if output_path == source_path or report_path == source_path:
        parser.error("output and report paths must not replace the source PDF")
    if report_path == output_path:
        parser.error("output and report paths must be different")

    try:
        from pypdf import PdfReader
        reader = PdfReader(args.pdf)
        if reader.is_encrypted:
            reader.decrypt("")
        page_count = len(reader.pages)
        indexes = parse_page_spec(args.pages, page_count)
        pages = extract_pages(reader, indexes, unwrap=args.unwrap)
    except ImportError as exc:
        parser.error(
            "pypdf is required; run this with the bundled Codex Python runtime "
            "or install pypdf in the active environment"
        )
    except Exception as exc:
        parser.error(str(exc))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_extraction(args.pdf.name, pages), encoding="utf-8")

    counts = {
        page_number: len(re.sub(r"\s+", "", text))
        for page_number, text in pages
    }
    low_text = [
        page_number for page_number, count in counts.items()
        if count < args.min_text_chars
    ]
    report = {
        "source": args.pdf.name,
        "source_page_count": page_count,
        "selected_pages": [number for number, _ in pages],
        "character_counts_without_whitespace": counts,
        "low_text_pages": low_text,
        "low_text_threshold": args.min_text_chars,
    }
    if args.report_json:
        args.report_json.parent.mkdir(parents=True, exist_ok=True)
        args.report_json.write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    print(
        f"wrote {len(pages)} of {page_count} page(s) to {args.output} "
        f"({args.output.stat().st_size} bytes)"
    )
    if low_text:
        joined = ", ".join(map(str, low_text))
        print(
            f"low-text pages below {args.min_text_chars} characters: {joined}; "
            "inspect visually or OCR these pages"
        )
    else:
        print(f"low-text pages below {args.min_text_chars} characters: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
