#!/usr/bin/env python3
"""Prepare and record an original generated visual reference for a PASS card.

This tool deliberately does not call an image API itself. Generate the image with
the approved image model using the printed prompt, then supply that output with
--image. Keeping the model call outside the repo prevents credentials and source
renders from being silently sent by a release script.
"""
from __future__ import annotations

import argparse
import json
import shutil
from datetime import date
from pathlib import Path

import yaml


def load_card(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError("card has no frontmatter")
    front = raw.split("---\n", 2)[1]
    data = yaml.safe_load(front)
    if not isinstance(data, dict):
        raise ValueError("card frontmatter is not a mapping")
    return data


def card_prompt(card: dict, derived_from: str) -> str:
    return "\n".join([
        "Use case: scientific-educational",
        "Asset type: PASS visual skill-card teaching reference",
        f"Primary request: Create a new, original instructional drawing for '{card['name']}'.",
        f"Source role: Study the supplied source render only for the idea identified by {derived_from}; do not copy its composition, pose, linework, labels, or distinctive design.",
        "Style/medium: clean contemporary instructional line art, simple neutral background, readable construction masses.",
        "Composition/framing: a single clear demonstration with enough blank space around the form; use generic anatomy or objects, not a recognizable source plate.",
        "Text: no text, labels, signatures, watermarks, logos, or page borders.",
        "Constraints: original art only; teach the card's rule, Do, and Don't through the construction choice; avoid extra fingers, malformed joints, and ambiguous overlapping forms.",
    ])


def repo_root_for(card: Path) -> Path:
    for parent in (card.parent, *card.parents):
        if parent.name == "library":
            return parent.parent
    raise ValueError("card must sit below a library directory")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("card", type=Path, help="PASS card with one references item")
    parser.add_argument("--reference-index", type=int, default=0)
    parser.add_argument("--image", type=Path, help="original image output returned by the image model")
    parser.add_argument("--source-render", type=Path, action="append", default=[], help="render studied by the model; repeatable")
    parser.add_argument("--model", help="image model name used to create --image")
    parser.add_argument("--origin", choices=("generated", "first_party_source"), default="generated")
    parser.add_argument("--prompt-out", type=Path, help="write the image-model prompt here and exit")
    args = parser.parse_args()

    card = load_card(args.card)
    references = card.get("references")
    if not isinstance(references, list) or not (0 <= args.reference_index < len(references)):
        parser.error("card must contain the selected references item")
    ref = references[args.reference_index]
    if not isinstance(ref, dict) or ref.get("origin") != args.origin:
        parser.error("selected reference origin must match --origin")
    prompt = card_prompt(card, str(ref.get("derived_from", "the cited source")))
    if args.prompt_out:
        args.prompt_out.write_text(prompt + "\n", encoding="utf-8")
        print(f"WROTE PROMPT: {args.prompt_out}")
        return 0
    if not args.image or (args.origin == "generated" and not args.model):
        parser.error("--image is required; generated references also require --model")
    if not args.image.is_file():
        parser.error(f"image does not exist: {args.image}")
    missing = [str(p) for p in args.source_render if not p.is_file()]
    if missing:
        parser.error(f"source render(s) do not exist: {', '.join(missing)}")
    repo_root = repo_root_for(args.card.resolve())
    target = repo_root / str(ref["image_path"])
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(args.image, target)
    sidecar = Path(str(target) + ".meta.json")
    sidecar.write_text(json.dumps({
        "origin": args.origin,
        "generator_model": args.model,
        "generated_at": date.today().isoformat(),
        "prompt": prompt,
        "source_renders": [str(p) for p in args.source_render],
        "review": {"verdict": "pending"},
    }, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE REFERENCE: {target}")
    print(f"WROTE PROVENANCE: {sidecar}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
