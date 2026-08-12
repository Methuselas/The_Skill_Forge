---
schema_version: vNext-draft.1
object_id: DRILL_rotate_boxes_across_eye_levels
object_type: drill
name: Rotate Boxes Across Eye Levels
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- box
- eye_level
- drill
scope:
  role: specialization
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
  - activation.art.drawing.perspective.box_rotation_warmup
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional: []
  excludes: []
context:
  residency: transient
  priority: 62
  load_when:
  - the task needs rotate boxes across eye levels
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p37_57_drill
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 37-57
    evidence_type: mixed
    note: The cube and one-/two-point sequences repeatedly vary orientation and viewing direction to expose convergence changes.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: PAT_choose_convergence_from_view_and_orientation
  activation_mode: warmup
  residue:
    expected:
    - Apply rotate boxes across eye levels during the current operation without keeping the drill instructions resident.
    scope: operation
  default_repetitions: 6
---

# Rotate Boxes Across Eye Levels

## Practice Task
Draw six simple boxes: two viewed straight out, two from above, and two from below. Change each box's horizontal orientation at least once.

## Target Skill
Choose convergence from the view and object orientation instead of from a memorized perspective label.

## Setup
Use one page. Mark an eye-level line for each pair. Keep the boxes simple and unrendered.

## Instructions
1. For each box, group edges into three direction families.
2. Decide which families are parallel to the picture plane and which recede.
3. Send each receding family to its proper vanishing direction.
4. For the above/below pairs, allow vertical convergence when the view requires it.
5. Compare the six boxes before adding any detail.

## Success Check
Each box reads as a different view of the same kind of solid, and the convergence changes can be explained from view/orientation rather than from a named recipe.

## Common Failures
- Off-center one-point boxes that incorrectly keep the second horizontal family parallel.
- Vertical convergence added only for drama rather than because the view is pitched.
- Different edges from one direction family heading toward different vanishing points.

## Expected Residue
Before drawing detail, identify direction families and solve how each one behaves in the current view.

## Notes
This drill translates D'Amelio's cube prerequisite into a fast activation exercise.
