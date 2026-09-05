#!/usr/bin/env python3
"""Return a bounded, ranked view of cards in one SkillForge package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml


FRONTMATTER_RE = re.compile(
    r"\A---\s*\n(?P<front>.*?)\n---\s*\n(?P<body>.*)\Z", re.DOTALL
)
TERM_RE = re.compile(r"[a-z0-9]+")
CARD_PREFIXES = ("AP_", "PAT_", "DRILL_")
TYPE_ORDER = {"ap": 0, "pattern": 1, "drill": 2}


@dataclass(frozen=True)
class Match:
    score: int
    object_type: str
    object_id: str
    name: str
    path: str
    decision_moment: str


def terms(value: str) -> set[str]:
    return set(TERM_RE.findall(value.casefold()))


def decision_moment(body: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("**IF**"):
            return stripped.removeprefix("**IF**").strip()
    return ""


def read_card(path: Path, library: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path.relative_to(library)} lacks valid frontmatter")
    data = yaml.safe_load(match.group("front"))
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(library)} frontmatter is not a mapping")
    return data, match.group("body")


def score_card(data: dict, body: str, query_terms: set[str], phrase: str) -> int:
    fields = {
        "name": terms(str(data.get("name", ""))),
        "id": terms(str(data.get("object_id", "")).replace("_", " ")),
        "tags": terms(" ".join(map(str, data.get("tags") or []))),
        "path": terms(" ".join(map(str, data.get("library_path") or []))),
        "decision": terms(decision_moment(body)),
        "body": terms(body),
    }
    weights = {"name": 8, "id": 5, "tags": 5, "path": 3, "decision": 4, "body": 1}
    score = sum(
        len(query_terms & field_terms) * weights[field]
        for field, field_terms in fields.items()
    )
    if phrase and phrase in " ".join(str(data.get("name", "")).casefold().split()):
        score += 12
    return score


def find_matches(
    library: Path,
    package: str,
    cues: str,
    limit: int = 8,
    object_types: set[str] | None = None,
) -> list[Match]:
    library = library.resolve()
    package_root = (library / package).resolve()
    if package_root.parent != library or not package_root.is_dir():
        raise ValueError(f"unknown package: {package}")
    query_terms = terms(cues)
    if not query_terms:
        raise ValueError("cues must contain at least one letter or number")
    phrase = " ".join(cues.casefold().split())

    matches: list[Match] = []
    for path in sorted(package_root.rglob("*.md")):
        if not path.name.startswith(CARD_PREFIXES):
            continue
        data, body = read_card(path, library)
        object_type = str(data.get("object_type", ""))
        if object_types and object_type not in object_types:
            continue
        score = score_card(data, body, query_terms, phrase)
        if score < 1:
            continue
        matches.append(
            Match(
                score=score,
                object_type=object_type,
                object_id=str(data.get("object_id", "")),
                name=str(data.get("name", "")),
                path=path.relative_to(library.parent).as_posix(),
                decision_moment=decision_moment(body),
            )
        )

    matches.sort(
        key=lambda item: (
            -item.score,
            TYPE_ORDER.get(item.object_type, 99),
            item.name.casefold(),
            item.path,
        )
    )
    return matches[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find a bounded set of relevant PASS cards inside one package.",
        epilog="The tool is stateless: it reads cards directly and creates no index or registry.",
    )
    parser.add_argument("--package", required=True, help="One package under library/.")
    parser.add_argument("--cues", required=True, help="Short task terms or a decision phrase.")
    parser.add_argument("--limit", type=int, default=8, help="Maximum results, 1-50 (default: 8).")
    parser.add_argument(
        "--type", action="append", dest="object_types",
        choices=sorted(TYPE_ORDER), help="Restrict object type; repeat as needed.",
    )
    parser.add_argument(
        "--library", type=Path,
        default=Path(__file__).resolve().parents[2] / "library",
        help="Library root (default: this repository's library/).",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of compact text.")
    args = parser.parse_args()

    if not 1 <= args.limit <= 50:
        parser.error("--limit must be between 1 and 50")
    try:
        matches = find_matches(
            args.library,
            args.package,
            args.cues,
            limit=args.limit,
            object_types=set(args.object_types) if args.object_types else None,
        )
    except (OSError, ValueError, yaml.YAMLError) as exc:
        parser.error(str(exc))

    if args.json:
        print(json.dumps([asdict(item) for item in matches], indent=2, ensure_ascii=False))
    else:
        for item in matches:
            line = (
                f"{item.score:>3}  {item.object_type:<7}  {item.name}  "
                f"[{item.path}]"
            )
            print(line)
            if item.decision_moment:
                print(f"     IF {item.decision_moment}")
        if not matches:
            print("NO MATCHES")
    return 0


if __name__ == "__main__":
    sys.exit(main())
