"""Build temporary review sheets from an extracted image directory.

The output is analysis-only evidence and must remain outside the repository.
"""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

from PIL import Image, ImageDraw


IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}


def natural_key(path: Path) -> list[int | str]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--batch-size", type=int, default=30)
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output.resolve()
    if output == source or source in output.parents:
        raise SystemExit("Output must not be inside the extracted source tree.")

    output.mkdir(parents=True, exist_ok=True)
    for collection in sorted(path for path in source.iterdir() if path.is_dir()):
        if collection.resolve() == output:
            continue
        files = sorted(
            (path for path in collection.rglob("*") if path.suffix.lower() in IMAGE_SUFFIXES),
            key=natural_key,
        )
        for start in range(0, len(files), args.batch_size):
            chunk = files[start : start + args.batch_size]
            rows = math.ceil(len(chunk) / 5)
            sheet = Image.new("RGB", (1100, rows * 330), (25, 25, 25))
            draw = ImageDraw.Draw(sheet)
            for index, path in enumerate(chunk):
                with Image.open(path) as opened:
                    image = opened.convert("RGB")
                    image.thumbnail((212, 296))
                x = (index % 5) * 220
                y = (index // 5) * 330
                sheet.paste(image, (x, y))
                draw.text((x + 4, y + 304), path.name[-32:], fill="white")
            page = start // args.batch_size + 1
            destination = output / f"{collection.name}_{page:02}.jpg"
            sheet.save(destination, quality=88)
            print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
