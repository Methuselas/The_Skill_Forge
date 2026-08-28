# Art Pressure Test Preflight — 2026-08-28

## Baseline

- Repository commit: `8c3fa30fae6f41100f2268a72dbf0614ca35fd36`
- Art cards validate: 547 objects.
- Visual references validate.
- Skillset Memory validates.
- All 182 generated library indexes are current.
- Unrelated non-Art edits were already present and remain outside this run.

## Live Art Inventory

| Kind | Count |
|---|---:|
| Patterns | 370 |
| Drills | 119 |
| APs | 58 |
| Embedded Variants | 535 |
| Pressure-test records | 1,082 |

Every object and embedded Variant has its own generated record and begins as
`NOT_TESTED`.

## Evidence Pool

The user supplied `E:/Books/!Comics` as a read-only collection. It contains 952
comic archives: 820 CBR and 132 CBZ files, spanning Batman: The Dark Knight
Returns, Cyber Force, Savage Dragon, Uncanny X-Men, Wetworks, and WildC.A.T.s.
Both archive formats opened successfully during preflight. Bundled MComix program
files are excluded.

Finished comic pages are outcome evidence, not proof of a particular production
procedure. AP and Drill claims that depend on process require process material or
a host test.

## Current High-Centrality Art Targets

The strongest incoming relationship counts begin with:

1. `PAT_build_gesture_into_clear_masses` — 27
2. `PAT_construct_head_from_cranial_ball_and_facial_wedge` — 26
3. `PAT_preserve_articulated_limb_chain` — 24
4. `PAT_consolidate_resolved_form_with_tone` — 23
5. `PAT_design_whole_picture_as_interlocking_shape_pattern` — 22
6. `PAT_track_force_continuity_through_action` — 19

Centrality is a sequencing aid, not a health score. The first empirical batch is
limited to high-centrality owners that final comic pages can genuinely exercise.

## Proposed First Batch

`ART_PRESSURE_BATCH_001` tests foundational action readability across six owner
Patterns: gesture-to-mass construction, articulated-limb continuity, force
continuity, center-of-gravity pose design, whole-picture shape organization, and
story-serving viewpoint.

The complete batch contract is
`tests/art_pressure/batches/ART_PRESSURE_BATCH_001.yaml`.

Select a small fixture set from at least four unrelated collections. Each owner
gets positive, negative, boundary, adversarial, human-evidence, and
competing-owner cases. Each human fixture receives both diagnostic and learning
passes. Interpretive conflicts remain `NEEDS_MORE_EVIDENCE`.

No Art canon mutation is authorized until the user approves this batch gate.
