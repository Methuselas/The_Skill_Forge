#!/usr/bin/env python3
"""Fail-closed release gate for PASS visual-card references."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from PIL import Image, ImageOps

from validate import discover_objects, parse_object, source_is_first_party, source_is_visual


SIMILARITY_LIMIT = 0.90


def image_similarity(first: Path, second: Path) -> float:
    """Return a conservative average grayscale similarity, 1.0 for identical."""
    with Image.open(first) as left, Image.open(second) as right:
        a = ImageOps.grayscale(left).resize((64, 64))
        b = ImageOps.grayscale(right).resize((64, 64))
        pixels_a, pixels_b = list(a.getdata()), list(b.getdata())
    mean_error = sum(abs(x - y) for x, y in zip(pixels_a, pixels_b)) / (255 * len(pixels_a))
    return 1.0 - mean_error


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


def reference_failures(record: Any, library_root: Path, ledger_root: Path) -> list[str]:
    data = record.data
    source_id = data.get("reference", {}).get("source_id") if isinstance(data.get("reference"), dict) else None
    if not source_is_visual(ledger_root, str(source_id)):
        return []
    failures: list[str] = []
    for ref in data.get("references", []):
        if not isinstance(ref, dict):
            continue
        image = library_root.parent / str(ref.get("image_path", ""))
        if not image.is_file():
            failures.append("reference image is missing")
            continue
        meta = load_sidecar(image)
        if meta is None:
            failures.append(f"{ref['image_path']}: provenance sidecar is missing or invalid")
            continue
        origin = ref.get("origin")
        if meta.get("origin") != origin or not meta.get("generated_at"):
            failures.append(f"{ref['image_path']}: provenance does not establish the declared origin and date")
        if origin == "generated" and not meta.get("generator_model"):
            failures.append(f"{ref['image_path']}: generated provenance has no model")
        if origin == "first_party_source" and not source_is_first_party(ledger_root, str(source_id)):
            failures.append(f"{ref['image_path']}: first-party source reuse lacks SOURCE.md rights: first_party")
        review = meta.get("review")
        if not isinstance(review, dict) or review.get("verdict") != "passed" or not review.get("reviewer") or not review.get("reviewed_at") or not review.get("method"):
            failures.append(f"{ref['image_path']}: no completed human or vision review record")
        renders = meta.get("source_renders")
        if not isinstance(renders, list) or not renders:
            failures.append(f"{ref['image_path']}: provenance has no source render for originality comparison")
            continue
        for render_name in renders:
            render = Path(render_name)
            if not render.is_absolute():
                render = library_root.parent / render
            if not render.is_file():
                failures.append(f"{ref['image_path']}: source render missing: {render_name}")
                continue
            similarity = image_similarity(image, render)
            if origin == "generated" and similarity >= SIMILARITY_LIMIT:
                failures.append(f"{ref['image_path']}: suspected reproduction (similarity {similarity:.3f} to {render_name})")
    return failures


def record_review(card: Path, reference_index: int, reviewer: str, method: str, note: str) -> int:
    raw = card.read_text(encoding="utf-8")
    front, body = raw.split("---\n", 2)[1:]
    data = yaml.safe_load(front)
    ref = data["references"][reference_index]
    image = repo_root_for(card.resolve()) / ref["image_path"]
    meta = load_sidecar(image)
    if meta is None:
        raise ValueError("reference provenance sidecar is missing")
    meta["review"] = {"verdict": "passed", "reviewer": reviewer, "reviewed_at": date.today().isoformat(), "method": method, "note": note}
    sidecar_for(image).write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    ref["review"] = "passed"
    card.write_text("---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n" + body, encoding="utf-8")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--library", type=Path, default=Path("library"))
    parser.add_argument("--ledger", type=Path, default=Path("ledger"))
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
    failures: list[str] = []
    for path in discover_objects(args.library):
        record = parse_object(path, args.library)
        for failure in reference_failures(record, args.library, args.ledger):
            failures.append(f"{record.label}: {failure}")
    if failures:
        print(f"REFERENCE REVIEW FAILED: {len(failures)} issue(s)")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print("REFERENCE REVIEW OK: every visual reference is present, reviewed, and original.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
