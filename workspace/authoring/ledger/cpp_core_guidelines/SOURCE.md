# C++ Core Guidelines

source_id:    cpp_core_guidelines
title:        C++ Core Guidelines
author:       Bjarne Stroustrup & Herb Sutter (editors)
publish_date: living document (snapshot 2026-06-14)
media_type:   markdown
payload_path: sources/cpp_core_guidelines/CppCoreGuidelines.md
sha256:       be29ae459bc206916c0737117ae43a1d4ac601fe2bf18cb6c10186613f083fa2
added:        2026-08-01
status:       queued

## Unit scheme (planned)

One major section per unit, keyed by the document's own letter-prefixed sections:
`P` Philosophy, `I` Interfaces, `F` Functions, `C` Classes and hierarchies,
`Enum`, `R` Resource management, `ES` Expressions and statements, `Per`
Performance, `CP` Concurrency, and the rest. Dense sections (e.g. `C`, `ES`) may
be split by subsection (`C.ctor`, `C.copy`, `ES.dcl`, `ES.expr`...). Triage the
highest-yield sections first (`R`, `C`, `ES`, `F`, `I`); do not process all ~23k
lines linearly.

Locators are **rule IDs**, not page numbers (e.g. `R.11`, `ES.20`, `F.6`) — the
document assigns every rule a stable ID and HTML anchor. There is no
`pdf_page_offset`; this is a text source.

## Grounding note — BLOCKED on tooling

`tools/verify_grounding.py` currently only verifies PDF sources (physical-page
extraction via `pdf_page_offset`). A markdown source has no pages, so this source
cannot be marked `processed` until the grounding tool supports text/markdown
sources (verbatim-quote search in the file, locator = rule ID or line range). See
the `PASS-TOOL-MD-GROUNDING` spec-needed row in `docs/worklogs/assignments.md`.
Do NOT process any unit until that lands — fail-closed.

## Notes

Structure is unusually extraction-friendly: every rule is
`Rule -> ##### Reason -> ##### Example (good/bad) -> ##### Enforcement`, which
maps almost 1:1 onto the pattern schema (Reason -> Notes, Examples -> Do/Don't,
Enforcement -> Checklist). Version-aware (C++11-23), so it pairs with the planned
`cpp<version>` tag convention and is the modern-side source that will `replace` or
`variant` many pre-C++11 Effective C++ cards. Process after Effective Modern C++.
Only two images are referenced by the document (`param-passing-normal.png`,
`param-passing-advanced.png`, in `F.call`); the folder was slimmed to the
markdown, those two PNGs, and `LICENSE` (MIT/CC-BY, kept for provenance).

## Summary

Filled in at reconciliation (not started).
