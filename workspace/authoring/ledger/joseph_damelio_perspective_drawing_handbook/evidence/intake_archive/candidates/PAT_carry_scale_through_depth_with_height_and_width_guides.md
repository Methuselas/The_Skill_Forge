---
schema_version: vNext-draft.1
object_id: PAT_carry_scale_through_depth_with_height_and_width_guides
object_type: pattern
name: Carry Scale Through Depth With Height and Width Guides
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- scale
- height
- width
scope:
  role: foundation
  axis: method
  foundation_object_id: null
bindings:
  development_stages: []
  execution_profiles:
  - direct_dream
  - staged
  - teaching
capabilities:
  provides:
  - art.drawing.perspective.carry_scale_through_depth
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 88
  load_when:
  - the task needs carry scale through depth with height and width guides
  unload_when:
  - the relevant spatial construction or correction is complete
relations:
- rel: related_to
  target_object_id: PAT_build_shared_scene_perspective_from_figure
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p61_67
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 61-67
    evidence_type: mixed
    note: Height and width guide constructions carry known dimensions through depth. Equal-height people on one level plane maintain a constant relationship to the observer's eye level.
  derivations:
  - derivation_id: scale_guide_synthesis
    kind: synthesis
    inputs:
    - damelio_p61_67
    note: Consolidates D'Amelio's height and width examples into a reusable scale-transfer rule.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Carry Scale Through Depth With Height and Width Guides

## Pattern Rule
**IF** equal-height or equal-width subjects must remain consistently scaled at different depths on the same plane, **THEN** establish one trusted measurement and project guide lines through the solved vanishing field instead of resizing each subject by eye.

## Do
- Establish one known vertical height at a trustworthy position.
- Project its top and bottom through the relevant vanishing directions to transfer that height elsewhere on the same plane.
- Use the observer's eye level as a repeated proportion check for equal-height figures on level ground.
- Carry widths through depth with the same vanishing logic, then translate the result vertically or horizontally where needed.
- Treat a change in ground elevation as a change in the height relationship, not as evidence that the eye-level rule failed.

## Don't
- Scale each distant figure independently by intuition after the scene field is solved.
- Apply a level-ground eye-line proportion unchanged to a figure standing uphill, downhill, or on another floor.
- Use screen-space equal spacing as a substitute for perspective scale.

## Checklist
- Equal real-world heights shrink consistently with distance.
- On one level plane, equivalent figure landmarks keep the same relationship to eye level.
- Width and height guides agree with the same vanishing field.
- A moved object can be checked against a known object without re-solving the whole scene.

## Boundaries
This Pattern transfers scale on established planes. Use inclined-plane construction when the supporting plane changes slope.

## Notes
This is the general scene-space counterpart to figure-derived calibration: D'Amelio supplies the independent eye-level and vanishing framework that the earlier Hogarth candidate explicitly left open.
