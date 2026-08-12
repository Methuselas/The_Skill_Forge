# Burne Hogarth — Dynamic Anatomy (Revised and Expanded) — Source Record

source_id: burne_hogarth_dynamic_anatomy
title: Dynamic Anatomy (Revised and Expanded)
author: Burne Hogarth
publish_date: 2003
media_type: book
payload_path: trash/sources/burne_hogarth_dynamic_anatomy/Dynamic_Anatomy_Revised_Expanded.txt
sha256: 31e23c6912973da1ada63afc2fa8c391e5055991f2fea1b84015814927e297a4
added: 2026-08-10
status: complete
commit_state: committed
closed: 2026-08-10
retired: 2026-08-10
text_layer: usable
visual: true
visual_access: page_images_in_chapter_archives
page_images_path: trash/sources/burne_hogarth_dynamic_anatomy/
page_count: 256 physical scan pages
pdf_page_offset: 2 for numbered body pages (scan page = printed page + 2)

## Payload bundle

The user supplied a searchable full-text transcription plus source-native page-image archives. The text payload is the duplicate-guard identity; visual grounding uses the exact supplied page images. Together the archives cover scan pages 001-256 contiguously with no gaps.

| component | sha256 |
|---|---|
| `Index_Introduction.zip` | `3cce4e25e2b67fe18ab95774b9e708259ea94d4aab288afec7a284bfae35d176` |
| `Ch_1.zip` | `7218370644722aff8f71276f0c20d400ae36e21c0ec1bdd70891b1161922821e` |
| `Ch_2.zip` | `3076aa01a6466ed927f47092bd073cc81d89ecb2db72bf3ccca3dc7011afeaac` |
| `Ch_3.zip` | `9eb3434b3a0f253e172efafaded2c1ed434e8e6609d4190ab78e5dd65cf91da6` |
| `Ch_4.zip` | `b822c4848623853e619cdcb52bd71b68dc54ebd26863f6b8c3e33c73aca08e0c` |
| `Ch_5.zip` | `e30341f9c35aae59c1105c4d05b0a768259291b8adf750c6726b227ff97406e8` |
| `Ch_6.zip` | `380396dbed82e50a18c4e82d328062bf35116d0b74b28e6ca90f52cc58c4ec5b` |

## Locator note

PASS uses the physical scan page numbers encoded in the supplied image filenames for visual receipts, while the source's printed page numbers are retained in unit labels. Numbered body pages use a +2 scan offset: printed p. 15 is scan p. 17, and printed p. 247 is scan p. 249. The index occupies printed pp. 250-256 / scan pp. 250-256 in the supplied archive and is navigation-only.

## Source-role note

This source arrives after the dedicated Hogarth figure, head, and hand work plus Loomis, Bridgman, Hampton, Bammes, Goldfinger, Zarins, Vilppu, and perspective passes. It is therefore a **variant-and-review source first**, not a fresh anatomy foundation. Generic anatomy facts, fixed proportions, and already-owned construction rules are filtered aggressively. Hogarth-specific alternatives survive when they change a practitioner's construction, diagnosis, comparison, or practice decision.

The revised edition's Preface explicitly distinguishes **artistic anatomy** from medical dissection and says the book will stress relationships of masses in movement, their effect on surface form, and the figure in foreshortening/depth. That framing is used as the source boundary: medical nomenclature and exhaustive internal anatomy are supporting evidence, not automatic card candidates.

## Unit scheme and Gate 1 routing

| unit | source section | printed pages | scan pages | Gate 1 route |
|---|---|---:|---:|---|
| u00 | Front matter: Foreword, Preface, Acknowledgments, source map | 7-14 | 7, 9-16 | source intent / review posture |
| u01 | I. The Dualism of Art and Science | 15-28 | 17-30 | Targeted PASS / historical-method framing |
| u02 | II. Toward the Liberating Criteria of Art | 29-42 | 31-44 | Targeted PASS / art-judgment and form criteria |
| u03 | III. The Figure in Art Historically Developed | 43-68 | 45-70 | Targeted PASS / comparative master-analysis and figure types |
| u04 | IV. Observations on Changing Proportions | 69-76 | 71-78 | Deep review / proportion alternatives with strict non-universal filter |
| u05 | V. Details of Anatomy | 77-222 | 79-224 | Deep review / anatomy variants and drills; strict overlap filter |
| u06 | VI. Nine Principles of Foreshortening | 223-247 | 225-249 | Deep PASS / reconcile against Dynamic Figure Drawing and perspective cards |

## Gate 1 summary

Proceed. The strongest expected value is in Chapter IV's proportion alternatives, Chapter V's construction/anatomy review, and Chapter VI's foreshortening variants. Chapters I-III are likely to contribute mostly review, master-analysis framing, or no delta. Chapter V is unusually large; it remains one source-native unit because the user supplied it as one chapter archive, but it will be read and visually inspected in bounded internal section passes before any disposition is finalized.

## Final summary

Reconciled 2026-08-10 after user authorization of u06. All 7 units are closed.

- **Units:** 7 processed / 0 empty / 0 blocked.
- **Objects added:** 2 standalone objects, both Drills.
- **Variants absorbed:** 6 retained variants across 5 existing vNext objects.
- **Objects replaced:** 0.
- **Candidates rejected:** 138 explicit reject rows remained reference, reinforcement, duplicate coverage, historical/polemical framing, over-specific proportion claims, or anatomy detail already owned more strongly elsewhere.
- **Cross-link reconciliation:** no Dynamic Anatomy links point to rejected candidates; the reference gate is clean.
- **Source-prefixed object reconciliation:** none required; both standalone deltas use semantic object filenames.

The source closes as intended: primarily a variant-and-review pass. The durable additions preserve Hogarth-specific figure-style comparison, an anatomy surface-detail ceiling, a bounded heroic proportion scaffold, neck/back/hand/leg construction alternatives, and a nine-check foreshortening diagnostic without duplicating the stronger anatomy, hand, figure-construction, or perspective families.

### Retirement

The working transcription and chapter-image archives are retired under `trash/sources/burne_hogarth_dynamic_anatomy/` as source evidence. The repo-only distributable archive intentionally omits source binaries and extracted/rendered evidence; the recorded SHA-256 hashes remain the duplicate guards and source identity.
