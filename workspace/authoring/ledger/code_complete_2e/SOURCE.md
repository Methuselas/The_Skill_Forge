# Code Complete, Second Edition

source_id:    code_complete_2e
title:        "Code Complete: A Practical Handbook of Software Construction, Second Edition"
author:       Steve McConnell
publish_date: 2004
media_type:   PDF
payload_path: sources/programming/Code_Complete_2nd_Edition.pdf
sha256:       c321aafe940280e0c2fe7fe2b85a7e743ff6009bafeed7af0c8f6263b1ed08d3
pdf_page_offset: 37
added:        2026-08-14
status:       in-progress
unit_ledger_contract: 3
teaching_lane_grandfathered_units: u01, u02, u03

## Unit scheme

One source-native chapter per unit — 35 chapters across 7 parts. McConnell writes
each chapter as a self-contained construction topic with its own checklist and
"Key Points" box, which is the smallest scope the author treats as a unit.

Several chapters are long enough to strain a single read: ch. 5 (52 pp.), ch. 31
(48 pp.), ch. 32 (42 pp.), ch. 22 (36 pp.), ch. 26 (37 pp.), ch. 3 (38 pp.). If a
chapter proves too large to ground in one read, split it on its own numbered
section boundaries, record the split here, and give the sub-units suffixed ids
(`u05a`, `u05b`). Do not merge adjacent chapters.

Page numbers in locators are the book's printed page numbers. **PDF page =
printed page + 37.** The offset was verified at three widely separated points:
ch. 1 opens on printed p. 3 / PDF p. 40; ch. 20 opens on printed p. 463 / PDF
p. 500; ch. 35 opens on printed p. 855 / PDF p. 892. Front matter uses roman
numerals whose printed number equals the physical page (printed xx = PDF p. 20).

Chapter start pages in `UNITS.md` were read from the book's own table of contents
(PDF pp. 9-13) and, for chapters 13-19, recovered by scanning chapter opening
pages because TOC page xii is missing from this PDF — the copyright page occupies
PDF p. 12 in its place. **End pages are inferred from the next chapter's start and
must be verified against the chapter text when each unit is claimed.**

## Preflight

`tools/preflight_pdf.py` reports `text_layer: usable` — 923 of 952 physical pages
carry usable text, 1,723,687 characters, `visual_access: none`. The 29 pages it
flags as weak are part dividers and chapter-end blanks. This is a text source;
`visual: true` does not apply.

The book carries numbered figures, tables, and checklists whose layout can carry
meaning text extraction flattens. Count the figures and tables in each unit's
extracted text when it is claimed, and render the pages that carry them rather
than planning visual work from this file. Poppler `pdftoppm` is absent from this
environment; `tools/render_pdf.py` falls back to pypdfium2.

Code listings appear in C++, Java, Visual Basic, and pseudocode. Verify any
code-heavy excerpt against `pdftotext -layout` before quoting — plain extraction
interleaves the book's margin annotations into the listings.

## Placement policy for this source

The library core stays language-agnostic. A card whose IF/THEN can be stated
without naming a language belongs in `library/software-engineering/core/...`,
even when McConnell's illustrating listing is C++ or Java. A card whose rule
cannot be stated without a language-specific construct is a specialization and
belongs under `library/software-engineering/languages/<language>/...`.

## Summary

Not yet reconciled. This source is in progress.
