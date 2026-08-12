---
schema_version: vNext-draft.1
object_id: DRILL_place_freehand_ellipses_on_minor_axes
object_type: drill
name: Place Freehand Ellipses on Minor Axes
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- ellipse
- warmup
- line_control
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
  - activation.art.drawing.perspective.ellipse_axis_warmup
  requires: []
  optional:
  - art.drawing.perspective.construct_projected_circles
  excludes: []
context:
  residency: transient
  priority: 58
  load_when:
  - a task needs many freehand circles, wheels, cylinders, hinges, or rotated forms and ellipse control is not yet reliable
  unload_when:
  - ellipses can be placed symmetrically around a chosen minor axis with controlled degree and width
relations:
- rel: supports
  target_object_id: PAT_construct_circles_as_ellipses_on_perspective_planes
grounding:
  mode: source_led
  evidence:
  - evidence_id: robertson_pp18_19_ellipse_drill
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 18-19 (physical PDF pp. 16-17)
    evidence_type: mixed
    note: Robertson practices light whole-arm ellipses, checks symmetry, folds/checks the minor axis, then reverses the exercise by drawing the minor axis first and placing ellipses of varied degree and width around it.
  - evidence_id: robertson_pp72_73_ellipse_use
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 72-73 (physical PDF pp. 70-71)
    evidence_type: mixed
    note: The later ellipse chapter makes minor-axis control the practical prerequisite for placing circles on perspective surfaces and varying ellipse degree with viewing angle.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: freehand_ellipse_control
  activation_mode: warmup
  residue:
    expected:
    - Place a smooth, centered freehand ellipse around a chosen minor axis during the current operation without keeping the drill instructions resident.
    scope: operation
  default_repetitions: 12
---

# Place Freehand Ellipses on Minor Axes

## Practice Task
Draw twelve minor axes at different orientations, then place one light ellipse around each while deliberately varying width and degree.

## Target Skill
Control a freehand ellipse around a chosen axis so it is smooth, centered, symmetric, and usable inside later perspective construction.

## Setup
Use a pencil or pen and enough paper to rotate the sheet freely. Draw lightly enough that one committed ellipse remains readable.

## Instructions
1. Warm up with a few loose whole-arm ellipses; do not darken them by circling repeatedly.
2. Draw a minor-axis line first, rotate the paper to a comfortable stroke angle, and place the ellipse over that axis.
3. Check that the ellipse is centered on the axis and that the two halves mirror each other in the narrow direction.
4. Repeat with different ellipse degrees from narrow to open while keeping the same axis logic.
5. Add two guide lines to a few examples and fit the ellipse to a required width without flattening its ends.
6. If an ellipse fails, draw a new one beside it rather than repairing the same loop with many passes.

## Success Check
The ellipses remain smooth and symmetrical, the minor axis passes through their center, and degree can change without the ellipse drifting off its intended axis.

## Common Failures
- Flat spots or pinched corners caused by steering the loop locally.
- A centered-looking ellipse whose minor axis is visibly skewed.
- Dark repeated loops that hide whether the first stroke was controlled.
- Treating this motor-control drill as a substitute for exact projected-circle construction on a difficult plane.

## Notes
This drill extracts Robertson's freehand control exercise, not a universal proof about ellipse axes. Exact circle placement remains governed by the stricter perspective-plane construction when accuracy matters; the broader axis theorem stays queued for the later mathematical audit.
