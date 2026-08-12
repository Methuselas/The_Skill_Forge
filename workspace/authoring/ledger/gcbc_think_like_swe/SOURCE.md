# Good Code, Bad Code: Think Like a Software Engineer

source_id:    gcbc_think_like_swe
title:        Good Code, Bad Code: Think Like a Software Engineer
author:       Tom Long
publish_date: 2021
media_type:   PDF
payload_path: sources/gcbc_think_like_swe/Good_Code_Bad_Code.pdf
sha256:       35e22cad80526e8d455d2c068937e2a3429fce415ef2275a3a45b40fdebcf6df
pdf_page_offset: 22
added:        2026-07-30
status:       complete
closed:       2026-07-31

## Unit scheme

One source-native chapter per unit (11 chapters, 3 parts). The book's own
structure supports this: Part 1 chapters (1-4) develop theory, Part 2 chapters
(5-9) are each a series of self-contained "consideration/technique" topics, and
Part 3 chapters (10-11) cover unit-testing principles then practices. A chapter
is the smallest instructional scope the author treats as a unit. Dense Part 2
chapters may be read in topic passes but remain one ledger unit unless a chapter
proves too large to ground in one read, in which case the split is recorded here.

Page numbers in locators are the book's printed page numbers. PDF page = book
page + 22 (Ch.1 "Code quality" begins on book p.3 = PDF p.25).

## Summary

Reconciled 2026-07-31. All 11 chapter units processed (0 empty, 0 blocked).

- **Units:** 11 processed / 0 empty / 0 blocked.
- **Objects added:** 122 — 88 patterns, 29 drills, 5 APs.
- **Variants absorbed:** 2 — assertions-as-contract-enforcement (VAR_assertions) into
  PAT_enforce_contracts_at_runtime_with_checks (u03); nullable-return-as-error-signal
  (VAR_error_signal) into PAT_prefer_null_safety_or_optionals (u04).
- **Objects replaced:** 0.
- **Candidates rejected/folded:** 0 rows carry the `reject` disposition, because this
  run recorded rejections as prose in each unit's `## Notes` rather than as table rows.
  Rejections were dispositioned, not skipped — read the per-unit Notes, not this count.
  (Every unit's candidate table is complete: rows match `candidate_count` in all 11.)
  Numerous source sub-topics
  were merged into composite patterns (e.g. the four comment subsections → one
  comment-the-why pattern; mocks/stubs/fakes + schools of thought → one prefer-fakes
  pattern) or captured as context in object Notes rather than emitted as objects. Pure
  definitional material was left unextracted and recorded per unit: the software
  development/deployment vocabulary (u01), the dependency-graph and cohesion vocabulary
  (u02), and the levels/types-of-testing vocabulary — integration, end-to-end,
  regression, golden, fuzz (u11 §11.7). Magic values were deferred by the author from
  Ch.4 to Ch.6 and extracted there (PAT_avoid_returning_magic_values, u06).

### Per-unit object counts

| unit | chapter | patterns | drills | APs | total |
|---|---|---|---|---|---|
| u01 | Code quality | 10 | 1 | 0 | 11 |
| u02 | Layers of abstraction | 9 | 2 | 1 | 12 |
| u03 | Other engineers and code contracts | 6 | 2 | 1 | 9 |
| u04 | Errors | 11 | 3 | 1 | 15 |
| u05 | Make code readable | 10 | 3 | 0 | 13 |
| u06 | Avoid surprises | 7 | 3 | 0 | 10 |
| u07 | Make code hard to misuse | 7 | 3 | 1 | 11 |
| u08 | Make code modular | 7 | 3 | 0 | 10 |
| u09 | Make code reusable and generalizable | 5 | 3 | 0 | 8 |
| u10 | Unit testing principles | 9 | 3 | 0 | 12 |
| u11 | Unit testing practices | 7 | 3 | 1 | 11 |
| **total** | | **88** | **29** | **5** | **122** |

### Library placement

All objects live in the `software-engineering` package under the `foundations/`
lane (added 2026-07-31 for symmetry with the `languages/` lane), in topic folders
that mirror the book's six pillars plus the theory chapters: `code-quality`,
`abstraction`, `contracts`, `error-handling`, `readability`, `avoiding-surprises`,
`hard-to-misuse`, `modularity`, `reusability`, and `testing`. Chapter 1 planted the
pillar foundations; later chapters extracted specializations that cross-link back to
them. Two variants were absorbed into existing foundations (one from Ch.2 null-safety,
one from Ch.3 checks) rather than creating new files.

### Reading receipts

The anti-skim gate (`docs/PASS/PASS_GROUNDING.md`, `tools/verify_grounding.py`)
was introduced after this source closed. Unit u01 carries a verified reading
receipt as the worked example (3 verbatim quotes spanning book pp. 5-21, confirmed
against the payload). Units u02-u11 were read chapter-by-chapter during this
session but predate the receipt format; their receipts are a pending backfill.
All future runs require a verified receipt per processed unit before objects ship.

### Retirement

Payload moved to `trash/sources/gcbc_think_like_swe/` on 2026-07-31 (local cleanup;
`sources/` is gitignored). The SHA-256 above remains the source identity.
