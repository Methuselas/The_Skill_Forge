---
schema_version: vNext-draft.1
object_id: DRILL_correct_wonky_foreshortened_limb_with_pivot_arcs
object_type: drill
name: Correct a Wonky Foreshortened Limb With Pivot Arcs
library_path:
- art
- drawing
- figure_construction
status: candidate
confidence: high
tags:
- figure_drawing
- foreshortening
- correction
- joint_reach
scope:
  role: specialization
  axis: method
  foundation_object_id: PAT_validate_foreshortened_limb_reach_from_joint_pivots
bindings:
  development_stages:
  - legacy_stage_1_skeleton
  - legacy_stage_2_block
  execution_profiles:
  - direct_dream
  - staged
  - teaching
capabilities:
  provides:
  - activation.art.drawing.figure_construction.foreshortened_limb_reach_correction
  requires:
  - art.drawing.figure_construction.validate_foreshortened_limb_reach_from_joint_pivots
  optional:
  - art.drawing.figure_construction.hold_member_identity_with_constant_width
  excludes: []
context:
  residency: transient
  priority: 65
  load_when:
  - a failure signal identifies a stretched, compressed, disconnected, duplicated,
    or otherwise implausible foreshortened limb
  unload_when:
  - drill evaluation completes
relations:
- rel: teaches
  target_object_id: PAT_validate_foreshortened_limb_reach_from_joint_pivots
- rel: related_to
  target_object_id: DRILL_rotate_one_limb_cylinder_while_holding_width
- rel: related_to
  target_object_id: PAT_preserve_articulated_limb_chain
grounding:
  mode: mixed
  evidence:
  - evidence_id: ch5_drill_source
    kind: source
    source_id: burne_hogarth_dynamic_figure_drawing_ocr
    locator: ch05, printed pp. 136-149
    evidence_type: mixed
    note: Source repeatedly varies limb endpoints around pivots and then moves to
      simpler body-part checks in compressed poses.
  - evidence_id: ch5_drill_teacher
    kind: human_teaching
    source_id: project_teacher_session
    locator: 2026-08-07, Chapter 5 review
    evidence_type: text
    note: Teacher identified the chapter as useful specifically for correcting wonky
      anatomy while otherwise redundant.
  derivations:
  - derivation_id: ch5_correction_drill_synthesis
    kind: synthesis
    inputs:
    - ch5_drill_source
    - ch5_drill_teacher
    - PAT_validate_foreshortened_limb_reach_from_joint_pivots
    note: Convert the chapter’s repeated arc exercises into a bounded correction Drill
      that leaves only reach-check residue.
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: PAT_validate_foreshortened_limb_reach_from_joint_pivots
  activation_mode: correction
  residue:
    expected:
    - When a foreshortened limb looks wonky, verify each endpoint from its carrying
      joint before adding anatomy; preserve the articulated chain and designed segment
      length, using temporary arcs only when needed.
    scope: operation
  default_repetitions: 1
---

# Correct a Wonky Foreshortened Limb With Pivot Arcs

## Practice Task
Isolate one failed foreshortened arm or leg and rebuild only its structural chain before returning to the parent drawing.

## Target Skill
Recover believable joint reach and projected length without stretching, duplicating, or detaching the limb.

## Setup
Use the accepted figure state as authority. Mark the parent socket, intermediate joint, and terminal form. Preserve the rest of the pose, camera, and unaffected anatomy.

## Instructions
1. Reduce the failed limb to its socket/joint/endpoint chain.
2. Establish the designed length of the first segment from the accepted figure, a clear partner member, or the existing construction.
3. Treat the parent joint as a pivot and sweep the next joint through a temporary reach arc; choose a position that preserves the intended action and depth.
4. Repeat from the intermediate joint to place the hand/foot or next terminal form.
5. When the pose supplies a useful body contact or alignment limit, use it as a secondary check rather than inventing another guide.
6. Rebuild the simple Stage 2 mass with Chapter 4 width/taper control.
7. Remove or ignore the guide and confirm that the corrected limb still reads without it.

## Success Check
- Exactly one continuous limb chain runs from the parent socket to the terminal form.
- Segment identity is preserved while apparent length changes with depth.
- The corrected endpoint is reachable without a hidden stretch, duplicate joint, or limb exchange.
- The correction does not move unrelated parts of the accepted figure.
- The limb remains convincing after the temporary arc is removed.

## Common Failures
- Drawing prettier anatomy over the same impossible endpoint.
- Treating the guide as more authoritative than the body's actual articulation.
- Fixing one segment by silently lengthening or shortening the other.
- Moving the torso, camera, or opposite limb to avoid correcting the failed chain.
- Keeping multiple exploratory limb paths active after the correction is selected.

## Notes
This is a **correction** Drill, not a compulsory warm-up. It should run only after a real failure signal. Its exercise artifact is non-authoritative; only the compact reach-check residue carries back into the parent operation.
