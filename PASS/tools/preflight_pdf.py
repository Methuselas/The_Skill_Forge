#!/usr/bin/env python3
"""Fail-closed readiness check for text and visual PDF sources before admission."""

from __future__ import annotations

import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path

from PIL import Image

from render_pdf import expected_outputs, render_command, renderer_candidates


IMAGE_SUFFIXES = {".bmp", ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}
PAGE_NUMBER_RE = re.compile(r"(\d+)(?!.*\d)")


@dataclass(frozen=True)
class TextReport:
    status: str
    page_count: int
    text_pages: int
    usable_pages: int
    character_count: int
    weak_pages: tuple[int, ...]
    detail: str


@dataclass(frozen=True)
class ImageReport:
    ready: bool
    count: int
    detail: str


def resolve_pdftotext(explicit: Path | None) -> Path:
    if explicit is not None:
        if explicit.is_file():
            return explicit
        raise FileNotFoundError(f"pdftotext does not exist: {explicit}")
    configured = os.environ.get("PASS_PDFTOTEXT")
    if configured:
        candidate = Path(configured)
        if candidate.is_file():
            return candidate
        raise FileNotFoundError(f"PASS_PDFTOTEXT does not exist: {candidate}")
    discovered = shutil.which("pdftotext")
    if discovered:
        return Path(discovered)
    raise FileNotFoundError(
        "pdftotext was not found; install Poppler, add it to PATH, or set PASS_PDFTOTEXT"
    )


def split_extracted_pages(text: str) -> list[str]:
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    return pages


def analyze_extracted_text(text: str) -> TextReport:
    pages = split_extracted_pages(text)
    page_stats: list[tuple[int, int]] = []
    for page in pages:
        words = re.findall(r"[^\W_]+(?:['’-][^\W_]+)*", page, re.UNICODE)
        characters = sum(character.isalnum() for character in page)
        page_stats.append((len(words), characters))

    text_pages = sum(characters >= 12 and words >= 3 for words, characters in page_stats)
    usable_pages = sum(characters >= 40 and words >= 8 for words, characters in page_stats)
    character_count = sum(characters for _words, characters in page_stats)
    page_count = len(pages)
    weak_pages = tuple(
        index for index, (words, characters) in enumerate(page_stats, start=1)
        if characters < 40 or words < 8
    )

    if character_count < 100 or text_pages == 0:
        status = "none"
        detail = "no meaningful extractable text layer"
    elif page_count and text_pages / page_count < 0.10:
        status = "sparse"
        detail = "text exists on fewer than 10% of pages; OCR or manual review is required"
    elif page_count and usable_pages / page_count < 0.60:
        status = "mixed"
        detail = "usable text is mixed with visually sparse or image-only pages"
    else:
        status = "usable"
        detail = "usable text is present across most pages"
    return TextReport(status, page_count, text_pages, usable_pages, character_count, weak_pages, detail)


def extract_pdf_text(source: Path, pdftotext: Path) -> tuple[TextReport, str]:
    result = subprocess.run(
        [str(pdftotext), "-enc", "UTF-8", str(source), "-"],
        capture_output=True,
        check=False,
    )
    stderr = result.stderr.decode("utf-8", errors="replace").strip()
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext failed with exit {result.returncode}: {stderr or 'no detail'}")
    text = result.stdout.decode("utf-8", errors="replace")
    return analyze_extracted_text(text), stderr


def numbered_images(names: list[str]) -> tuple[list[tuple[int, str]], str | None]:
    numbered: list[tuple[int, str]] = []
    for name in names:
        path = Path(name)
        if path.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        match = PAGE_NUMBER_RE.search(path.stem)
        if not match:
            return [], f"image has no final page number in its filename: {name}"
        numbered.append((int(match.group(1)), name))
    if not numbered:
        return [], "no supported page images found"
    numbers = [number for number, _name in numbered]
    if len(numbers) != len(set(numbers)):
        return [], "page-image numbers are not unique"
    expected = list(range(1, len(numbers) + 1))
    if sorted(numbers) != expected:
        return [], f"page-image numbers must be contiguous from 1 through {len(numbers)}"
    return sorted(numbered), None


def sample_indexes(count: int) -> list[int]:
    return sorted({0, count // 2, count - 1})


def verify_image_stream(stream: io.BufferedIOBase | io.BytesIO, label: str) -> str | None:
    try:
        with Image.open(stream) as image:
            image.verify()
    except Exception as exc:  # Pillow exposes several format-specific exceptions.
        return f"cannot decode {label}: {exc}"
    return None


def inspect_page_images(path: Path, expected_pages: int | None = None) -> ImageReport:
    if path.is_dir():
        names = [item.relative_to(path).as_posix() for item in path.rglob("*") if item.is_file()]
        numbered, error = numbered_images(names)
        if error:
            return ImageReport(False, 0, error)
        if expected_pages is not None and len(numbered) != expected_pages:
            return ImageReport(False, len(numbered), f"has {len(numbered)} images but PDF has {expected_pages} pages")
        for index in sample_indexes(len(numbered)):
            _number, name = numbered[index]
            with (path / Path(name)).open("rb") as stream:
                error = verify_image_stream(stream, name)
            if error:
                return ImageReport(False, len(numbered), error)
    elif path.is_file() and path.suffix.lower() == ".zip":
        try:
            with zipfile.ZipFile(path) as archive:
                names = [info.filename for info in archive.infolist() if not info.is_dir()]
                numbered, error = numbered_images(names)
                if error:
                    return ImageReport(False, 0, error)
                if expected_pages is not None and len(numbered) != expected_pages:
                    return ImageReport(False, len(numbered), f"has {len(numbered)} images but PDF has {expected_pages} pages")
                for index in sample_indexes(len(numbered)):
                    _number, name = numbered[index]
                    error = verify_image_stream(io.BytesIO(archive.read(name)), f"{path}::{name}")
                    if error:
                        return ImageReport(False, len(numbered), error)
        except (OSError, zipfile.BadZipFile) as exc:
            return ImageReport(False, 0, f"cannot read page-image archive: {exc}")
    else:
        return ImageReport(False, 0, "page-images path must be a directory or ZIP archive")
    return ImageReport(True, len(numbered), "numbered page set is contiguous; first, middle, and last images decode")


def probe_renderer(source: Path, explicit: Path | None) -> tuple[bool, str]:
    try:
        candidates = renderer_candidates(explicit)
    except FileNotFoundError as exc:
        return False, str(exc)
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="pass-render-probe-") as temp_dir:
        prefix = Path(temp_dir) / "page"
        output = expected_outputs(prefix, 1, 1)[0]
        for renderer in candidates:
            result = subprocess.run(
                render_command(renderer, source, 1, 1, prefix, 72),
                capture_output=True,
                check=False,
            )
            if result.returncode == 0 and output.is_file():
                with output.open("rb") as stream:
                    error = verify_image_stream(stream, str(output))
                if error is None:
                    return True, f"{renderer} rendered page 1 through its visible CropBox"
                failures.append(error)
            else:
                failures.append(f"{renderer} exited {result.returncode} without a verified page")
            if output.exists():
                output.unlink()
    return False, "; ".join(failures)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="PDF source to assess before hashing/admission")
    parser.add_argument("--visual", action="store_true", help="source teaches through images or page layout")
    parser.add_argument("--vision-capable", action="store_true", help="confirm this run can inspect page images")
    parser.add_argument("--page-images", type=Path, help="page-numbered image directory or ZIP archive")
    parser.add_argument("--pdftotext", type=Path, help="explicit pdftotext executable")
    parser.add_argument("--renderer", type=Path, help="explicit pdftoppm executable or wrapper")
    args = parser.parse_args()

    if not args.source.is_file():
        parser.error(f"source does not exist: {args.source}")
    if args.source.suffix.lower() != ".pdf":
        parser.error("source must be a PDF")

    problems: list[str] = []
    try:
        pdftotext = resolve_pdftotext(args.pdftotext)
        text_report, extraction_note = extract_pdf_text(args.source, pdftotext)
        print(f"text_layer: {text_report.status}")
        print(
            f"text_pages: {text_report.text_pages}/{text_report.page_count}; "
            f"usable_pages: {text_report.usable_pages}/{text_report.page_count}; "
            f"characters: {text_report.character_count}"
        )
        if text_report.weak_pages:
            pages = ",".join(str(page) for page in text_report.weak_pages)
            print(f"weak_physical_pages: {pages}")
        print(f"text_detail: {text_report.detail}")
        if extraction_note:
            print(f"pdftotext_note: {extraction_note}")
        if text_report.status in {"none", "sparse"}:
            problems.append("NEEDS_OCR: PDF has no dependable per-page text layer")
    except (FileNotFoundError, RuntimeError) as exc:
        text_report = None
        print(f"text_layer: unavailable ({exc})")
        problems.append("NEEDS_OCR: text extraction could not be verified")

    if args.visual:
        if not args.vision_capable:
            problems.append("NO_VISUAL_MODEL: a vision-capable model is required for a visual source")

        expected_pages = text_report.page_count if text_report and text_report.page_count else None
        renderer_ready, renderer_detail = probe_renderer(args.source, args.renderer)
        print(f"renderer: {'ready' if renderer_ready else 'unavailable'} ({renderer_detail})")

        image_report = None
        if args.page_images:
            image_report = inspect_page_images(args.page_images, expected_pages)
            print(
                f"page_images: {'ready' if image_report.ready else 'invalid'} "
                f"({image_report.count} images; {image_report.detail})"
            )
        else:
            print("page_images: not supplied")

        image_ready = bool(image_report and image_report.ready)
        if renderer_ready and image_ready:
            visual_access = "both"
        elif renderer_ready:
            visual_access = "renderer"
        elif image_ready:
            visual_access = "page_images"
        else:
            visual_access = "none"
        print(f"visual_access: {visual_access}")

        if not renderer_ready and not image_ready:
            problems.append("NO_PAGE_IMAGES: use a working renderer or verified page-image set")
    else:
        print("visual_access: none")

    if problems:
        print("\nNOT READY")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("\nREADY: preflight passed; hash and admit this exact PDF payload next")
    return 0


if __name__ == "__main__":
    sys.exit(main())
