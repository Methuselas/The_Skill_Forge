# The Art of Animal Drawing

source_id:    ken_hultgren_art_of_animal_drawing
title:        The Art of Animal Drawing
author:       Ken Hultgren
publish_date: Unknown
media_type:   book
payload_path: trash/sources/ken_hultgren_art_of_animal_drawing/Ken_Hultgren_The_Art_of_Animal_Drawing.pdf
pdf_page_offset: 2
sha256:       74fc2787e54e9b1d84dbf2ec9a38d4ce18927586637016df3252d2b54963c5a3
added:        2026-08-10
closed:       2026-08-10
retired:      2026-08-10
status:       complete
commit_state: committed
text_layer:   mixed
visual:       true
visual_access: rendered_page_images
page_images_path: trash/sources/ken_hultgren_art_of_animal_drawing/rendered/

## Payload boundary

The original supplied payload was an incomplete 52-page extract that omitted most species chapters. On 2026-08-10 the user explicitly replaced it with the complete 136-page Internet Archive scan. The replacement preserves the opening pages already processed in u01 at the same physical locations and then continues through the missing chapters to printed p. 134.

Source-of-record retrieval URL: `https://ia903100.us.archive.org/18/items/theartofanimaldrawing_201911/The%20art%20of%20animal%20drawing_text.pdf`

The replacement payload was preflighted before further PASS work. It has a mixed text layer (66/136 text-bearing pages, 65/136 usable) and therefore remains a visual-source run: OCR/text extraction is paired with rendered page inspection for every processed unit.

The earlier 52-page payload is superseded and is not an evidentiary source for subsequent units. Its only retained value is historical intake context. u01 was rechecked against the replacement scan before user-authorized commit; the source content and physical page alignment for that unit are unchanged.

## Unit scheme

Units follow the source-native named sections present in the complete scan. Printed pagination maps to physical PDF pagination with a constant offset of +2 (`pdf_page_offset: 2`). Short species sections remain separate units because the source presents them as independent named teaching sections.

- u01 — Tips on Drawing Animals / Simplified Skeletons / Sketching in Forms — printed pp. 1-7; physical pp. 3-9
- u02 — Mood and Feeling — printed pp. 8-10; physical pp. 10-12
- u03 — The Use of Line — printed pp. 11-14; physical pp. 13-16
- u04 — Action Analysis — printed pp. 15-16; physical pp. 17-18
- u05 — Brush Technique — printed pp. 17-18; physical pp. 19-20
- u06 — The Horse Family — printed pp. 19-47; physical pp. 21-49
- u07 — The Deer Family — printed pp. 48-56; physical pp. 50-58
- u08 — The Cat Family — printed pp. 57-76; physical pp. 59-78
- u09 — Cows and Bulls — printed pp. 77-81; physical pp. 79-83
- u10 — Giraffes — printed pp. 82-83; physical pp. 84-85
- u11 — Camels — printed pp. 84-85; physical pp. 86-87
- u12 — Gorillas — printed pp. 86-88; physical pp. 88-90
- u13 — Pigs — printed pp. 89-91; physical pp. 91-93
- u14 — Dogs — printed pp. 92-100; physical pp. 94-102
- u15 — Foxes — printed pp. 101-103; physical pp. 103-105
- u16 — Kangaroos — printed pp. 104-107; physical pp. 106-109
- u17 — Rabbits — printed pp. 108-110; physical pp. 110-112
- u18 — Squirrels — printed p. 111; physical p. 113
- u19 — Elephants — printed pp. 112-118; physical pp. 114-120
- u20 — The Bear Family — printed pp. 119-127; physical pp. 121-129
- u21 — Composition in Animal Grouping — printed pp. 128-134; physical pp. 130-136

## Intake note

The complete Internet Archive scan was the active evidentiary payload during processing and is now retired under `trash/sources/ken_hultgren_art_of_animal_drawing/`. The renderer used throughout the run was `/usr/bin/pdftoppm` through `tools/render_pdf.py` using the PDF CropBox. No `vnext/` or `candidate_library/` corpus exists or is to be created.

## Commit state

All 21 source-native units are user-authorized and committed. Source-level reconciliation completed on 2026-08-10. No retained Hultgren skill remains outside canonical `library/`, and no active `vnext/`, `candidate_library/`, migration, intake, or second skill corpus was created.

## Final summary

Reconciled 2026-08-10 after user authorization of u21. The source is closed.

- **Units:** 21 processed / 0 empty / 0 blocked.
- **Objects added:** 26 standalone objects — 22 Patterns and 4 Drills.
- **Variants absorbed:** 30 retained variants into canonical owners.
- **Objects replaced:** 0.
- **Candidates rejected / reinforcement / bounded:** 126 disposition rows.
- **Cross-link reconciliation:** canonical validation finds no unresolved retained candidate targets; u21's new composition Pattern links only to canonical objects.
- **Source-prefixed object reconciliation:** none required; all standalone objects use semantic IDs and all source-specific retained alternatives are variants on canonical owners.
- **Publish boundary:** every retained standalone object and variant is in canonical `library/`; there is no active parallel corpus.

The durable Hultgren delta establishes the initial animal-drawing construction stack (quadruped massing, animal head construction, species-specific construction routes, animal gesture/action, brush handling, caricature/humanization, and group composition) while deliberately filtering broad biological generalizations and under-explained biomechanics for later comparative review against Bammes, Vilppu, Mattesi, and Luard.

### Retirement

The complete Internet Archive PDF and rendered grounding evidence are retired under `trash/sources/ken_hultgren_art_of_animal_drawing/` as recoverable source evidence. The repo-only distributable archive intentionally omits the copyrighted PDF and temporary grounding renders; the recorded SHA-256 remains the source identity and duplicate guard.
