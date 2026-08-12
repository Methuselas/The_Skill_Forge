#!/usr/bin/env python3
"""Render a PDF page range for PASS visual review with Poppler's pdftoppm."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


PAGE_RANGE_RE = re.compile(r"^(\d+)-(\d+)$")


def parse_page_range(value: str) -> tuple[int, int]:
    match = PAGE_RANGE_RE.fullmatch(value)
    if not match:
        raise ValueError("page range must use START-END, for example 44-51")
    first, last = (int(part) for part in match.groups())
    if first < 1 or last < first:
        raise ValueError("page range must begin at page 1 or later and end at or after its start")
    return first, last


def sibling_direct_renderer(renderer: Path) -> Path | None:
    if renderer.name.lower() != "pdftoppm.cmd" or len(renderer.parents) < 3:
        return None
    return renderer.parents[2] / "native" / "poppler" / "Library" / "bin" / "pdftoppm.exe"


def renderer_candidates(explicit: Path | None) -> list[Path]:
    if explicit is not None:
        if explicit.is_file():
            return [explicit]
        raise FileNotFoundError(f"renderer does not exist: {explicit}")
    configured = os.environ.get("PASS_PDFTOPPM")
    if configured:
        candidate = Path(configured)
        if candidate.is_file():
            return [candidate]
        raise FileNotFoundError(f"PASS_PDFTOPPM does not exist: {candidate}")
    discovered = shutil.which("pdftoppm")
    if discovered:
        renderer = Path(discovered)
        candidates = [renderer]
        sibling = sibling_direct_renderer(renderer)
        if sibling is not None and sibling.is_file():
            candidates.append(sibling)
        return candidates
    raise FileNotFoundError("pdftoppm was not found; install Poppler, add it to PATH, or set PASS_PDFTOPPM")


def resolve_renderer(explicit: Path | None) -> Path:
    return renderer_candidates(explicit)[0]


def render_command(
    renderer: Path,
    source: Path,
    first: int,
    last: int,
    output_prefix: Path,
    dpi: int,
    *,
    cropbox: bool = True,
) -> list[str]:
    command = [str(renderer), "-f", str(first), "-l", str(last), "-png", "-r", str(dpi)]
    if cropbox:
        command.append("-cropbox")
    return [*command, str(source), str(output_prefix)]


def expected_outputs(output_prefix: Path, first: int, last: int) -> list[Path]:
    return [output_prefix.parent / f"{output_prefix.name}-{page:03}.png" for page in range(first, last + 1)]


def render_with_pypdfium2(
    source: Path,
    first: int,
    last: int,
    output_prefix: Path,
    dpi: int,
    *,
    cropbox: bool = True,
) -> None:
    """In-process fallback for environments without a Poppler binary.

    Poppler stays the primary path: it is what the procedure names and what the
    Read tool's PDF path uses. This exists so that a missing system binary
    degrades a run to "slower" rather than to "cannot inspect figures at all",
    which is otherwise indistinguishable from a source that genuinely cannot be
    read. Output filenames match pdftoppm's `<prefix>-NNN.png` so callers and
    receipts do not have to care which renderer produced them.
    """
    import pypdfium2 as pdfium  # imported lazily; absent installs fall through to the error path

    document = pdfium.PdfDocument(str(source))
    try:
        if last > len(document):
            raise ValueError(f"page {last} is beyond the document ({len(document)} pages)")
        for page_number in range(first, last + 1):
            page = document[page_number - 1]
            if cropbox:
                # pdftoppm -cropbox renders the visible box; mirror that default so
                # scanner margins do not eat visual context.
                page.set_mediabox(*page.get_cropbox())
            page.render(scale=dpi / 72).to_pil().save(
                output_prefix.parent / f"{output_prefix.name}-{page_number:03}.png"
            )
    finally:
        document.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="PDF source path")
    parser.add_argument("--pages", required=True, help="inclusive page range: START-END")
    parser.add_argument("--output-prefix", required=True, type=Path, help="output path prefix, without page suffix")
    parser.add_argument("--dpi", type=int, default=150, help="render resolution (default: 150)")
    parser.add_argument("--renderer", type=Path, help="explicit pdftoppm executable or wrapper")
    parser.add_argument(
        "--media-box",
        action="store_true",
        help="render the full PDF MediaBox instead of the visible CropBox",
    )
    args = parser.parse_args()
    try:
        first, last = parse_page_range(args.pages)
        if args.dpi < 1:
            raise ValueError("dpi must be positive")
        if not args.source.is_file():
            raise FileNotFoundError(f"source does not exist: {args.source}")
        try:
            renderers = renderer_candidates(args.renderer)
        except FileNotFoundError:
            # No Poppler binary. Fall back only when nothing was explicitly
            # requested -- an explicit --renderer/PASS_PDFTOPPM that does not
            # resolve is a configuration error the caller wants to see.
            if args.renderer or os.environ.get("PASS_PDFTOPPM"):
                raise
            renderers = []
    except (ValueError, FileNotFoundError) as exc:
        parser.error(str(exc))
    outputs = expected_outputs(args.output_prefix, first, last)
    existing = [path for path in outputs if path.exists()]
    if existing:
        parser.error(f"output files already exist; choose a new prefix: {existing[0]}")
    args.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    for renderer in renderers:
        command = render_command(
            renderer, args.source, first, last, args.output_prefix, args.dpi,
            cropbox=not args.media_box,
        )
        result = subprocess.run(command, check=False)
        present = [path for path in outputs if path.is_file()]
        if result.returncode == 0 and len(present) == len(outputs):
            print(f"renderer: {renderer}")
            print("command:", subprocess.list2cmdline(command))
            return 0
        missing = [str(path) for path in outputs if path not in present]
        print(f"renderer failed: {renderer} (exit {result.returncode}; missing {len(missing)} output file(s))", file=sys.stderr)
        if present:
            print("partial render retained; choose a new output prefix before retrying", file=sys.stderr)
            return 1
    try:
        render_with_pypdfium2(
            args.source, first, last, args.output_prefix, args.dpi,
            cropbox=not args.media_box,
        )
    except ImportError:
        print(
            "no renderer available: pdftoppm was not found and pypdfium2 is not installed "
            "(pip install pypdfium2), so figures cannot be inspected",
            file=sys.stderr,
        )
        return 1
    except Exception as exc:  # noqa: BLE001 - report and fail closed, never half-render silently
        print(f"pypdfium2 fallback failed: {exc}", file=sys.stderr)
        return 1
    missing = [str(path) for path in outputs if not path.is_file()]
    if missing:
        print(f"pypdfium2 fallback wrote {len(outputs) - len(missing)}/{len(outputs)} page(s)", file=sys.stderr)
        return 1
    from pypdfium2.version import PYPDFIUM_INFO

    print(f"renderer: pypdfium2 {PYPDFIUM_INFO.version} (in-process fallback; Poppler pdftoppm not found)")
    print(f"pages: {first}-{last} at {args.dpi} DPI, {'cropbox' if not args.media_box else 'mediabox'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
