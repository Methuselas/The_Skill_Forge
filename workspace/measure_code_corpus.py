#!/usr/bin/env python3
"""Measure structural properties of a C/C++ corpus.

Why this exists
---------------
Skillset Memory entries about *coding* need evidence, and the person who owns this
repository is not a C++ programmer. For Art, the owner's own eye is the ground
truth. For code there is no equivalent judgement available — so the evidence has
to be mechanical, reproducible, and runnable by someone who cannot read the code
being measured.

That is all this does. It counts a few things and prints them. It makes no
judgements, and a number here is not a verdict.

Usage
-----
    python workspace/measure_code_corpus.py PATH [PATH ...] --label NAME

    # several corpora side by side, one --label per path:
    python workspace/measure_code_corpus.py \
        "D:/Repos/MC2_Remastered/mclib" "D:/Repos/MC2_Remastered/RenderCore" \
        --label "human 2001" --label "agent"

What the numbers mean
---------------------
asserts/kloc     Assertions per thousand non-blank, non-comment lines. An
                 assertion states that something must never be false and stops
                 the program when it is. Low numbers mean broken assumptions
                 travel silently instead of reporting themselves.
guards/kloc      Early-return checks (`if (!x) return ...`). These handle a
                 condition rather than forbidding it. High guards with low
                 asserts is the shape worth noticing.
nodiscard/kloc   Uses of the attribute that makes ignoring a returned failure a
                 compiler warning.
com/code         Comment lines per code line.
median file      Median file length in lines.

Known limits — read these before quoting a number
-------------------------------------------------
* The counts come from regular expressions, not a parser. A project-specific
  assertion macro with an unusual name may be missed; pass --assert-pattern.
* Comment ratio is inflated by house styles that mandate a file prolog.
* Era matters. A 2001 codebase with a cheap project-wide assert macro will
  assert more than a modern one that has to include a header first, and that is
  a fact about the infrastructure as much as about the author.
* Headers are measured by default. Excluding them undersamples any codebase that
  keeps logic in headers, which modern C++ often does — in one corpus measured
  here, implementation files held under a tenth of the code.
* One corpus is one sample. Two corpora that agree are two samples.
"""

from __future__ import annotations

import argparse
import os
import re
import statistics
import sys

IMPL_SUFFIXES = (".cpp", ".c", ".cc", ".cxx")
HEADER_SUFFIXES = (".h", ".hpp", ".hxx", ".inl")
SKIP_DIR_MARKERS = ("3rdparty", "3rd_party", "third_party", "external",
                    "vcpkg", "_deps", "build", "node_modules", ".git")

DEFAULT_ASSERT_PATTERN = r"\b[A-Za-z_]*(?:ASSERT|Assert|assert)\s*\("
GUARD_PATTERN = r"if\s*\(\s*!?\w+(?:\s*(?:==|!=)\s*(?:nullptr|NULL|0))?\s*\)\s*\n?\s*\{?\s*\n?\s*return"
NODISCARD_PATTERN = r"nodiscard"


def collect_sources(root: str, include_headers: bool) -> list[str]:
    suffixes = IMPL_SUFFIXES + (HEADER_SUFFIXES if include_headers else ())
    found: list[str] = []
    for current, dirs, files in os.walk(root):
        lowered = current.lower().replace("\\", "/")
        if any(marker in lowered for marker in SKIP_DIR_MARKERS):
            dirs[:] = []
            continue
        for name in files:
            if name.endswith(suffixes):
                found.append(os.path.join(current, name))
    return sorted(found)


def measure(root: str, assert_pattern: str, include_headers: bool) -> dict | None:
    sources = collect_sources(root, include_headers)
    if not sources:
        return None

    assert_re = re.compile(assert_pattern)
    guard_re = re.compile(GUARD_PATTERN)
    nodiscard_re = re.compile(NODISCARD_PATTERN)

    code = comment = blank = 0
    asserts = guards = nodiscards = 0
    lengths: list[int] = []

    for path in sources:
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue

        lines = text.split("\n")
        lengths.append(len(lines))

        in_block = False
        for raw in lines:
            line = raw.strip()
            if not line:
                blank += 1
                continue
            if in_block:
                comment += 1
                if "*/" in line:
                    in_block = False
                continue
            if line.startswith("//"):
                comment += 1
                continue
            if line.startswith("/*"):
                comment += 1
                if "*/" not in line:
                    in_block = True
                continue
            code += 1

        asserts += len(assert_re.findall(text))
        guards += len(guard_re.findall(text))
        nodiscards += len(nodiscard_re.findall(text))

    per_kloc = lambda n: (n / code * 1000) if code else 0.0
    return {
        "files": len(sources),
        "code": code,
        "comment_ratio": (comment / code) if code else 0.0,
        "blank_ratio": (blank / (code + comment + blank)) if (code + comment + blank) else 0.0,
        "asserts_kloc": per_kloc(asserts),
        "guards_kloc": per_kloc(guards),
        "nodiscard_kloc": per_kloc(nodiscards),
        "median_file": int(statistics.median(lengths)) if lengths else 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Measure structural properties of one or more C/C++ corpora.",
        epilog="Numbers are evidence, not verdicts. See the header of this file for limits.",
    )
    parser.add_argument("paths", nargs="+", help="Directory roots to measure.")
    parser.add_argument("--label", action="append", default=[],
                        help="Label for the corresponding path. Repeat once per path.")
    parser.add_argument("--impl-only", action="store_true",
                        help="Measure only .cpp/.c files. Off by default: modern C++ puts real "
                             "logic in headers, and skipping them undersamples such code badly.")
    parser.add_argument("--assert-pattern", default=DEFAULT_ASSERT_PATTERN,
                        help="Regex for this project's assertion macro, if it has an unusual name.")
    args = parser.parse_args()

    labels = list(args.label)
    while len(labels) < len(args.paths):
        labels.append(os.path.basename(os.path.normpath(args.paths[len(labels)])))

    header = (f"{'corpus':<22}{'files':>7}{'code':>9}{'com/code':>10}"
              f"{'asserts/kloc':>14}{'guards/kloc':>13}{'nodisc/kloc':>13}{'med file':>10}")
    print(header)
    print("-" * len(header))

    missing = False
    for path, label in zip(args.paths, labels):
        if not os.path.isdir(path):
            print(f"{label:<22}  no such directory: {path}")
            missing = True
            continue
        result = measure(path, args.assert_pattern, not args.impl_only)
        if result is None:
            print(f"{label:<22}  no C/C++ sources found under {path}")
            missing = True
            continue
        print(f"{label:<22}{result['files']:>7}{result['code']:>9}"
              f"{result['comment_ratio']:>10.3f}{result['asserts_kloc']:>14.1f}"
              f"{result['guards_kloc']:>13.1f}{result['nodiscard_kloc']:>13.1f}"
              f"{result['median_file']:>10}")

    print()
    print("Counts come from regular expressions, not a parser. Comment ratio is inflated by")
    print("mandatory file prologs. One corpus is one sample.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
