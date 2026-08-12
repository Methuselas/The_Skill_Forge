---
schema_version: vNext-draft.1
object_id: PAT_validate_foreshortened_limb_reach_from_joint_pivots
object_type: pattern
name: Validate Foreshortened Limb Reach From Joint Pivots
library_path:
- art
- drawing
- figure_construction
status: candidate
confidence: high
tags:
- figure_drawing
- foreshortening
- joint_reach
- proportion
scope:
  role: specialization
  axis: method
  foundation_object_id: PAT_preserve_articulated_limb_chain
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
  - art.drawing.figure_construction.validate_foreshortened_limb_reach_from_joint_pivots
  requires:
  - art.drawing.figure_construction.preserve_articulated_limb_chain
  optional:
  - art.drawing.figure_construction.hold_member_identity_with_constant_width
  excludes: []
context:
  residency: triggered
  priority: 55
  load_when:
  - a foreshortened limb endpoint, member length, or range looks structurally uncertain
  unload_when:
  - the limb chain passes reach and proportion checks or the operation ends
relations:
- rel: specialization_of
  target_object_id: PAT_preserve_articulated_limb_chain
- rel: related_to
  target_object_id: PAT_hold_member_identity_with_constant_width
- rel: supports
  target_object_id: AP_control_foreshortened_form_size_in_stage_two
grounding:
  mode: mixed
  evidence:
  - evidence_id: ch5_source_length
    kind: source
    source_id: burne_hogarth_dynamic_figure_drawing_ocr
    locator: ch05, printed pp. 135-149
    evidence_type: mixed
    note: Source teaches projected-length control using ellipse/radius tracking, a
      leg triangle shortcut, and part-to-part checks in compressed poses.
  - evidence_id: ch5_teacher_range
    kind: human_teaching
    source_id: project_teacher_session
    locator: 2026-08-07, Chapter 5 review
    evidence_type: text
    note: Teacher reframed the practical value as range-of-motion / wonky-anatomy
      correction and judged much of the chapter redundant with existing foundation.
  derivations:
  - derivation_id: ch5_reach_synthesis
    kind: synthesis
    inputs:
    - ch5_source_length
    - ch5_teacher_range
    - PAT_preserve_articulated_limb_chain
    - PAT_hold_member_identity_with_constant_width
    note: Compress Hogarth’s several measuring devices into one optional reach-validation
      rule rather than multiple compulsory geometry cards.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Validate Foreshortened Limb Reach From Joint Pivots

## Pattern Rule
**IF** a foreshortened arm or leg looks too long, too short, disconnected, or otherwise uncertain in depth
**THEN** preserve the designed length of each limb segment, treat its carrying joint as the pivot, and test whether the next joint or terminal form can plausibly occupy the chosen endpoint before anatomy is developed
**ELSE** keep the ordinary articulated-chain and proportion checks when the projected length already reads clearly

## Do
- Establish the parent socket or joint, the next joint, and the terminal form as one traceable chain before refining contour.
- Use the same figure's designed segment length as the reach constraint; apparent screen-space length may compress radically without the physical member changing identity.
- For a two-segment limb, solve the first endpoint from its parent pivot, then solve the second from the intermediate joint.
- Use a temporary ellipse/arc when visual judgment needs help; use part-to-part contact or alignment checks when the pose naturally supplies them.
- Coordinate the reach check with Chapter 4 width/taper control so length and size identity agree.
- Allow the carrying structure itself to participate where the source shows it moving, such as shoulder/collarbone shift during arm elevation.

## Don't
- Stretch or shrink a limb segment merely to make a difficult pose fit the silhouette.
- Turn Hogarth's ellipse, arc, or triangle into compulsory visible construction when the relationship is already clear.
- Treat the pivot as an isolated dot divorced from the moving body structure that carries it.
- Use a pose-specific body contact as a universal anatomical landmark for unrelated poses.
- Preserve a mathematically neat guide when it produces a less believable articulated figure.

## Checklist
- Every distal endpoint is reachable from its parent joint without silently changing the designed member length.
- The socket-to-joint-to-terminal order remains continuous through overlap and foreshortening.
- Width/taper and projected length describe the same member rather than competing solutions.
- Any temporary arc or body-contact check can disappear while the pose remains structurally convincing.
- No extra joint, duplicate limb, or unexplained stretch was introduced to solve the projection.

## Notes
Hogarth frames Chapter 5 as control of projected length. The project-level practical interpretation is narrower: use pivot/radius and body-contact relationships as **range and reach diagnostics** when an invented foreshortened limb becomes wonky. The source itself warns that excessive dependence on ellipse construction can inhibit the drawing, so this Pattern deliberately keeps the geometry optional.
