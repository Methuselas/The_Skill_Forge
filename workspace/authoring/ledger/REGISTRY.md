# PASS Source Registry

status: active
owner: docs/domains/corpus
last_reviewed: 2026-08-15

**This file is the duplicate guard.** Before creating a `source_id` or a
`ledger/<source_id>/` folder, hash the file and search this table for that hash.
If the hash is here, the book has already been processed — stop, and read its row.

```bash
sha256sum "sources/<file>"                       # git bash
```
```powershell
Get-FileHash "sources\<file>" -Algorithm SHA256  # powershell
```

Format and the full decision table: `docs/PASS/PASS_LEDGER.md` → REGISTRY.md.

`status`: `queued` · `in-progress` · `complete` · `low-yield` · `abandoned`

`units` is done/total, where "done" counts `processed` + `empty` + `blocked`.
Ground truth for counts is each source's `UNITS.md`; this table is a summary and
can go stale. If they disagree, the ledger wins.

| source_id | title | author | sha256 (first 12) | status | units | objects | closed |
|---|---|---|---|---|---|---|---|
| burne_hogarth_drawing_dynamic_hands | Drawing Dynamic Hands | Burne Hogarth | 29ed748014e7 | complete | 12/12 | 8 new, 5 variants | committed 2026-08-08 |
| burne_hogarth_drawing_the_human_head | Drawing the Human Head | Burne Hogarth | 013572a68262 | complete | 7/7 | 5 new, 19 variants | committed 2026-08-10 |
| burne_hogarth_dynamic_anatomy | Dynamic Anatomy (Revised and Expanded) | Burne Hogarth | 31e23c691297 | complete | 7/7 | 2 new, 6 variants | committed 2026-08-10 |
| burne_hogarth_dynamic_figure_drawing_ocr | Dynamic Figure Drawing | Burne Hogarth | b0d97d495ca3 | complete | 7/7 | 49 new, 6 variants | committed 2026-08-10 |
| gen1_art_fundamentals_4step | PASS Gen 1 Universal Step 0 + Four-Stage Workflow | Blu + Admin | d53b1c8b031f | complete | 1/1 | 2 | 2026-07-31 |
| guided_staged_visual_validation_2026_08_03 | Guided Staged Visual Validation: Warbot and Zero-G Astronaut | Blu + Admin | 401381d45142 | complete | 1/1 | 3 | 2026-08-03 |
| guided_art_centerline_wusao_2026_08_04 | Guided Art Centerline: Registered Crescendo Construction | Blu + Admin | e2ab32836b3e | complete | 1/1 | 1 | 2026-08-04 |
| guided_stage_density_gates_2026_08_05 | Guided Stage Density Profiles, Visible Gates, and Deferred Color/Light Split | MaDin + GPT | 46fd8c084e68 | complete | 2/2 | 1 new, 2 revised | 2026-08-05 |
| guided_stage0a_rosetta_2026_08_06 | Guided Stage 0A Rosetta Backcast and Approved Observatory Precedent | MaDin + GPT | 136e94ead27f | complete | 1/1 | 1 new, 3 revised | 2026-08-06 |
| guided_stage1_stage3_artist_discretion_2026_08_06 | Guided Stage 1–3 Artist Discretion, Mass Completion, and Commitment Review | MaDin + GPT | f3609792c05e | complete | 1/1 | 3 new, 4 revised | 2026-08-06 |
| guided_nested_four_stage_framework_2026_08_07 | Guided Nested Four-Stage Framework and Stage 3 Ceiling | MaDin + GPT | cb22da9899e7 | complete | 1/1 | revisions only | 2026-08-07 |

| george_bridgman_constructive_anatomy | Constructive Anatomy | George B. Bridgman | dadc7dd89aee | complete | 14/14 | 19 variants | committed |
| george_bridgman_book_of_a_hundred_hands | The Book of a Hundred Hands | George B. Bridgman | 3aafe728e331 | complete | 1/1 | 0 new, 2 variants | committed 2026-08-10 |
| michael_hampton_figure_drawing_design_and_invention | Figure Drawing: Design and Invention | Michael Hampton | 59a7bb127ad7 | complete | 10/10 | 4 new, 14 variants | committed 2026-08-09 |

| andrew_loomis_figure_drawing_for_all_its_worth | Figure Drawing for All It's Worth | Andrew Loomis | 30d591db0940 | complete | 12/12 | 2 new, 15 variants | committed |
| andrew_loomis_drawing_the_head_and_hands | Drawing the Head and Hands | Andrew Loomis | 8572e461e877 | complete | 10/10 | 7 new, 23 variants | committed 2026-08-09 |
| glenn_vilppu_basic_figure_drawing | Drawing Manual: Basic Figure Drawing | Glenn Vilppu | 4de3a62133c5 | complete | 13/13 | 2 new, 11 variants | committed |

| gottfried_bammes_wir_zeichnen_den_menschen | Wir zeichnen den Menschen: Eine Grundlegung | Gottfried Bammes | fa2fab46a0c7 | complete | 9/9 | 4 new, 15 variants | committed |
| gottfried_bammes_artist_guide_to_animal_anatomy | The Artist's Guide to Animal Anatomy | Gottfried Bammes | 57ad055fadae | complete | 34/34 | 59 new, 24 variants | committed 2026-08-13 |

| joseph_damelio_perspective_drawing_handbook | Perspective Drawing Handbook | Joseph D'Amelio | 34463a150ec2 | complete | 1/1 | 14 canonical perspective objects + cumulative variants/patches | committed 2026-08-09 |
| ernest_norling_perspective_made_easy | Perspective Made Easy | Ernest R. Norling | 781c8c782bb3 | complete | 1/1 | 2 canonical perspective objects + cumulative variants/patches | committed 2026-08-09 |
| gwen_white_perspective_guide | Perspective: A Guide for Artists, Architects and Designers | Gwen White | 6220ee967707 | complete | 1/1 | 2 canonical perspective objects + cumulative variants/patches | committed 2026-08-09 |
| robert_w_gill_basic_rendering | Basic Rendering: Effective Drawing for Designers, Artists and Illustrators | Robert W. Gill | ec1c2dd8e951 | complete | 1/1 | 4 rendering objects + cumulative perspective variants/patches | committed 2026-08-10 |
| scott_robertson_how_to_draw | How to Draw: Drawing and Sketching Objects and Environments from Your Imagination | Scott Robertson with Thomas Bertling | c5a54e8bf818 | complete | 1/1 | 6 canonical perspective objects + cumulative variants/patches | committed 2026-08-09 |
| frantz_crannell_viewpoints_mathematical_perspective | Viewpoints: Mathematical Perspective and Fractal Geometry in Art | Marc Frantz and Annalisa Crannell | e2e33af95f58 | complete | 1/1 | 2 canonical perspective objects + cumulative variants/patches | committed 2026-08-09 |

| uldis_zarins_anatomy_for_sculptors | Anatomy for Sculptors: Understanding the Human Figure | Uldis Zarins with Sandis Kondrats | 691881f80830 | complete | 8/8 | 0 new, 11 variants | committed 2026-08-09 |
| ken_hultgren_art_of_animal_drawing | The Art of Animal Drawing | Ken Hultgren | 74fc2787e54e | complete | 21/21 | 26 new, 30 variants | committed 2026-08-10 |

| michael_mattesi_force_animal_drawing | FORCE: Animal Drawing | Michael D. Mattesi | e9a4ac547b34 | complete | 6/6 | 4 new, 16 variants | committed 2026-08-13 |
| lowes_luard_anatomy_action_horse | The Anatomy and Action of the Horse | Lowes D. Luard | 81f6f309ccec | complete | 7/7 | 1 new, 15 variants, 1 revision | committed 2026-08-13 |
| bert_dodson_keys_to_drawing | Keys to Drawing | Bert Dodson | 7cbff579f0ee | complete | 8/8 | 23 new, 6 promotions, 24 variants, 1 revision | committed 2026-08-13 |
| andrew_loomis_fun_with_a_pencil | Fun With a Pencil | Andrew Loomis | 15de53dbf81c | complete | 5/5 | 1 new, 9 variants | committed 2026-08-14 |
| marvel_how_to_draw_comics | How to Draw Comics the Marvel Way | Stan Lee and John Buscema | f5ba454de57c | complete | 12/12 | 6 new, 3 variants | committed 2026-08-14 |
| andrew_loomis_successful_drawing | Successful Drawing | Andrew Loomis | 2d1d0c6915b2 | complete | 11/11 | 1 new, 11 variants | |
| vladimir_mogilevtsev_fundamentals_of_drawing | Fundamentals of Drawing | V. A. Mogilevtsev | 178328b32aaa | complete | 11/11 | 2 new, 12 variants, 2 refinements | committed 2026-08-14 |
| andrew_loomis_creative_illustration | Creative Illustration | Andrew Loomis | 506648bdf3ff | in-progress | 7/22 | 7 new, 10 variants, 1 generalization, 1 refinement | committed through u07 2026-08-15 |

<!-- Shared Teaching grounding dependency included in the Art authoring slice. -->
| david_starkey_creative_writing_four_genres_in_brief_3e | Creative Writing: Four Genres in Brief, Third Edition | David Starkey | 4dcdd06e0727 | in-progress | 3/151 | 18 new, 5 variants | |

<!-- Software engineering. THIRD restoration of this block: it has now been dropped from
     the working copy three times by rewrites of this shared table (2026-08-14, and twice
     on 2026-08-15). Rule 25 catches it, but only after the fact. If you are regenerating
     this file, regenerate every ledger under workspace/authoring/ledger/ rather than the
     rows for one lane, or the other lane's rows will keep disappearing. -->
| gcbc_think_like_swe | Good Code, Bad Code: Think Like a Software Engineer | Tom Long | 35e22cad8052 | complete | 11/11 | 122 | 2026-07-31 |
| programmers_brain | The Programmer's Brain: What Every Programmer Needs to Know About Cognition | Felienne Hermans | 52063e7300c1 | complete | 13/13 | 66 new, 19 variants | 2026-08-13 |
| effective_cpp_3e | Effective C++, 3rd ed. | Scott Meyers | 4f983195c37c | complete | 9/9 | 80 | 2026-08-01 |
| cpp_core_guidelines | C++ Core Guidelines | Stroustrup & Sutter (eds.) | be29ae459bc2 | queued | | | |
| code_complete_2e | Code Complete: A Practical Handbook of Software Construction, 2nd Ed. | Steve McConnell | c321aafe9402 | in-progress | 5/35 | 22 new, 3 variants | |
