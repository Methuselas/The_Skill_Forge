# Lane repair — Art

Written 2026-08-23 from the software-engineering lane, after the `stage_binding`
thesis. Self-contained: you should not need that conversation to act on this.

The convention this asks you to apply now lives in `PASS/docs/PASS_RUN.md` §2.8
("The AP ownership edge"). It is shared across all three lanes. The work is not —
`CLAUDE.md` rule 2 still holds, so Art is repaired in an Art run, by you.

---

## Why this exists

The thesis argued that PASS has a vertical coordinate (`stage_binding`,
refinement) and no horizontal one (which craft is currently authorized), and
proposed a new `execution_scope` field.

The diagnosis is right. The field is the wrong layer, for a reason that is
already written down: `PASS/docs/EXECUTION_CONTRACT.md` states that cards "Can
enforce: **Nothing** — they are declarative." A per-card scope field would be one
more unenforced sentence beside the ten already in `PASS_CONSUMPTION.md`'s
"Ceiling" section, bought with a 1,103-card migration and a permanent taxonomy.

But the sharper finding is this. The thesis assumes AP-first consumption was the
firewall that made the missing coordinate survivable. It was measured:

| lane | patterns | APs | claimed by an AP |
|---|---|---|---|
| art | 222 | 35 | **27%** |
| software-engineering | 462 | 19 | **2%** |
| writing | 131 | 22 | **0%** |

Art was the best case in the repo and still a minority. The firewall was never
built. Before adding a second coordinate to gate activation, build the ownership
graph the existing design already assumes exists.

**Both other lanes have since been repaired, on the same day this was written:**

```
writing                22 APs   134 patterns    75% claimed   22/22 APs name owners
software-engineering   26 APs   462 patterns    29% claimed   24/26 APs name owners
art                    35 APs   222 patterns    27% claimed   25/35 APs name owners
```

Writing is now the reference implementation — every AP claims its Patterns and
names them in the step prose. Art is the only lane still on the old footing, and
it is now the lowest of the three rather than the highest.

---

## The convention, in one paragraph

An AP step that reaches a decision a Pattern owns must do two things: **name** the
Pattern in the step prose, and **carry** it in the AP's `cross_links` as
`rel: supports`. Steps the AP owns itself — ordering, gates, invariants, recovery,
stopping — delegate nothing and produce no link.

Two carriers because they do different jobs. The frontmatter edge is the
machine-readable claim a consumer resolves. The prose naming is what binds the
Pattern to *which step* it enters at — an unordered set of twelve Patterns is
exactly the "unordered bag" the schema's own AP value test warns about.

### `supports` is not `related_to`

- `supports`, AP → Pattern = **ownership**. This protocol claims this decision.
- `related_to` = **adjacency**. Widens what retrieval reaches, says nothing about
  authority.

Your own §5 warned about this and it is the single most important line in the
thesis: *do not use graph isolation to enforce workflow isolation.* The corollary
is the one to act on here — **do not use graph degree as a health metric.** An
orphan with the right owner is healthier than a well-connected card no protocol
claims. Closing a reachability gap with `related_to` makes the graph denser
without making any workflow's claim clearer.

I violated this myself on the SE side (commit `3aec6da`: five unlinked cards,
fourteen `related_to` edges, zero owner edges) and it was the wrong shape. Don't
repeat it.

---

## What Art actually looks like

35 APs. 100 AP-sourced `supports` edges already exist, and 25 of 35 APs already
name IDs in their step prose — Art invented this convention before anyone wrote
it down. This repair is mostly finishing what the lane already started.

### Priority 1 — the two APs with no links at all

```
AP_construct_cast_shadows_in_perspective        0 cross_links, 0 named
AP_project_plan_and_elevation_into_perspective  0 cross_links, 0 named
```

These are almost certainly the missing owners for three of your eight orphans.
Check them first:

```
PAT_measure_true_lengths_on_oblique_planes
PAT_construct_inclined_planes_from_base_vanishing_directions
PAT_block_complex_objects_with_perspective_boxes
```

### Priority 2 — APs whose edges are all `related_to` (re-type, don't re-author)

```
AP_draw_a_figure_through_onion_skinned_stages    13 related_to,  0 supports
AP_gate_staged_visual_work_by_approval            9 related_to,  0 supports
AP_gate_visible_color_development_by_approval     7 related_to,  0 supports
AP_notate_a_figure_in_structural_order            6 related_to,  0 supports
AP_control_foreshortened_form_size_in_stage_two   5 related_to,  0 supports
AP_build_comic_page_from_assigned_beats_to_pencils 4 related_to, 0 supports
```

The two staged-drawing gate APs matter most: they are the controllers of the
strict mode that exposed the whole problem, and neither currently claims a single
Pattern.

### Priority 3 — APs with supports but no prose naming

```
AP_render_landscape_to_finished_image              5 supports, 0 named, 14 steps
AP_design_distance_read_poster_...                 5 supports, 0 named, 11 steps
AP_stage_story_scene_from_big_idea_to_camera_rough 5 supports, 0 named, 11 steps
AP_ink_comic_art_for_reproduction_clarity_...      1 supports, 0 named, 13 steps
AP_prepare_artifact_only_image_generation_handoff  1 supports, 0 named, 12 steps
AP_generate_visual_concepts_from_purpose_driven_questionnaire  2 supports, 0 named
AP_construct_a_shared_scene_perspective_field      2 supports, 0 named
```

---

## The eight orphans

Two of them are **not** deferred-owner cases. The owner exists, in the same
directory, and the AP already describes the move in prose:

| orphan | owner | evidence |
|---|---|---|
| `PAT_annotate_exploratory_sketches_with_decision_cues` | `AP_develop_product_concept_from_search_sketch_to_communicable_design` | step 11, *"Exploration may stay cheap and annotated"* |
| `PAT_calibrate_product_redesign_with_reference_underlay` | same AP | step 8, *"Use underlay calibration for redesign tied to existing geometry"* |

The first was the thesis's flagship example of "valid capability whose proper
execution context has not yet been authored." It isn't. Its context is authored
and sitting next to it, missing a `supports` link. Worth knowing before that
example is used to justify anything else.

Remaining six, with a starting guess:

```
PAT_measure_true_lengths_on_oblique_planes         -> AP_project_plan_and_elevation_into_perspective
PAT_construct_inclined_planes_from_base_...        -> AP_project_plan_and_elevation_into_perspective
PAT_block_complex_objects_with_perspective_boxes   -> AP_build_complex_volumes_with_xyz_sections?
PAT_recover_view_field_from_existing_image         -> AP_construct_a_shared_scene_perspective_field?
PAT_use_thirds_to_break_static_equal_divisions     -> a composition AP
PAT_use_subtractive_and_manipulative_marks_...     -> likely a real AP coverage gap
```

A Pattern no AP claims is not automatically broken. It is either a **local
decision** that needs no orchestration, or an **AP coverage gap** where the owner
has not been authored. Both are legitimate. Record which; do not manufacture an
AP to give a Pattern a parent, and do not link one into an unrelated AP to raise
its degree.

---

## On `execution_scope`

Not now. If, after the ownership edges are in place, contamination still happens
in Staged Mode, it has evidence behind it and is worth revisiting. Until then it
stacks a second unenforced mechanism on a first one that is not built.

If you want a ceiling in the meantime, put it in the AP that owns the turn —
`AP_gate_staged_visual_work_by_approval` declaring what Staged Drawing excludes is
roughly six statements, lives where the workflow lives, and is actually in context
at execution time. 367 cards do not each need to know Staged Drawing exists.

Also worth noting for the audit proposal in §9: the nine-question per-object
checklist is a per-card ledger under another name, and that is what the
2026-08-15 cleanup deleted (`CLAUDE.md` rule 4). The mechanical kernel is worth
having — a stateless script that prints orphans, unclaimed Patterns, and coverage
gaps, writing nothing.

---

## Mechanics

Purely additive. No schema change, no card bodies rewritten beyond the step
sentence that names the owner. The validator places no cap on `cross_links`, no
direction constraint on `supports`, and no reciprocity requirement.

```bash
python PASS/tools/validate.py --package art
```

Reference implementations, best first:

- **Writing** — repaired to 75%, all 22 APs claiming and naming their owners.
  Any AP under `library/writing/fiction/` shows the finished shape.
- **Software-engineering** — `library/software-engineering/core/testing/AP_write_a_unit_test_suite.md`
  (6 steps, every one anchored) and
  `.../core/refactoring/AP_replace_a_system_that_is_still_in_use.md` (12 owners
  across 9 steps) for the large case.
- **Art's own** — `AP_paint_directly_from_observation` (11 supports) is the
  closest this lane already has.

## Note on the checkpoint zip

`workspace/SkillForge_Art_StageModeRefPreflight_SourceCheckpoint_2026-08-23.zip`
has been merged into the repo: 14 files advanced (art profile `consumer_instructions`,
`checks_by_stage`, the staged-drawing cards, `--mode`/`--stage` pass-through), the
rosetta contact sheet demoted to `workspace/authoring/art/legacy-visuals/`, and
its two stale library copies deleted. Validator, reference check, and the 99-test
suite all pass. The repo is ahead of that zip now — work from the repo.
