#!/usr/bin/env python3
"""Fail-closed release gate for PASS visual-card reference assets.

A card that ships an image ships a runtime artifact, so the image must exist and
must carry a completed review record in its `<image>.meta.json` sidecar. That is
an asset-quality check on the finished library — it does not consult a source
document, a render cache, or any authoring record.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from validate import discover_objects, parse_object
from paths import default_library_root


def sidecar_for(image: Path) -> Path:
    return Path(str(image) + ".meta.json")


def repo_root_for(card: Path) -> Path:
    for parent in (card.parent, *card.parents):
        if parent.name == "library":
            return parent.parent
    raise ValueError("card must sit below a library directory")


def load_sidecar(image: Path) -> dict[str, Any] | None:
    path = sidecar_for(image)
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def reference_failures(record: Any, library_root: Path) -> list[str]:
    references = record.data.get("references") or []
    # A card that ships no reference has nothing to verify. A card that ships one
    # must have it present and reviewed.
    failures: list[str] = []
    for ref in references:
        if not isinstance(ref, dict):
            continue
        image = library_root.parent / str(ref.get("image_path", ""))
        if not image.is_file():
            failures.append("reference image is missing")
            continue
        meta = load_sidecar(image)
        if meta is None:
            failures.append(f"{ref['image_path']}: review sidecar is missing or invalid")
            continue
        origin = ref.get("origin")
        if meta.get("origin") != origin or not meta.get("generated_at"):
            failures.append(f"{ref['image_path']}: sidecar does not establish the declared origin and date")
        if origin == "generated" and not meta.get("generator_model"):
            failures.append(f"{ref['image_path']}: generated image has no model recorded")
        review = meta.get("review")
        if (
            not isinstance(review, dict)
            or review.get("verdict") != "passed"
            or not review.get("reviewer")
            or not review.get("reviewed_at")
            or not review.get("method")
        ):
            failures.append(f"{ref['image_path']}: no completed human or vision review record")
    return failures


def record_review(card: Path, reference_index: int, reviewer: str, method: str, note: str) -> int:
    raw = card.read_text(encoding="utf-8")
    front, body = raw.split("---\n", 2)[1:]
    data = yaml.safe_load(front)
    ref = data["references"][reference_index]
    image = repo_root_for(card.resolve()) / ref["image_path"]
    meta = load_sidecar(image)
    if meta is None:
        raise ValueError("reference review sidecar is missing")
    meta["review"] = {
        "verdict": "passed",
        "reviewer": reviewer,
        "reviewed_at": date.today().isoformat(),
        "method": method,
        "note": note,
    }
    sidecar_for(image).write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    ref["review"] = "passed"
    card.write_text("---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n" + body, encoding="utf-8")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--library", type=Path, default=default_library_root())
    parser.add_argument("--record-review", type=Path, help="card to mark passed after a real human or vision review")
    parser.add_argument("--reference-index", type=int, default=0)
    parser.add_argument("--reviewer")
    parser.add_argument("--method", help="for example: human visual inspection")
    parser.add_argument("--note", default="Depicts the card claim; anatomy and construction checked.")
    args = parser.parse_args()
    if args.record_review:
        if not args.reviewer or not args.method:
            parser.error("--record-review requires --reviewer and --method")
        try:
            return record_review(args.record_review, args.reference_index, args.reviewer, args.method, args.note)
        except (ValueError, IndexError, KeyError) as exc:
            print(f"FAIL: {exc}")
            return 1
    if not args.library.is_dir():
        print(f"FAIL: library root not found: {args.library.as_posix()}", file=sys.stderr)
        return 1
    failures: list[str] = []
    for path in discover_objects(args.library):
        record = parse_object(path, args.library)
        for failure in reference_failures(record, args.library):
            failures.append(f"{record.label}: {failure}")
    if failures:
        print(f"REFERENCE REVIEW FAILED: {len(failures)} issue(s)")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print("REFERENCE REVIEW OK: every visual reference is present and reviewed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
