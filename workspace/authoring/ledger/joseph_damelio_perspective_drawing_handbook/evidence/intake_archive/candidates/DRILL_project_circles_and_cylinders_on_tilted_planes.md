---
schema_version: vNext-draft.1
object_id: DRILL_project_circles_and_cylinders_on_tilted_planes
object_type: drill
name: Project Circles and Cylinders on Tilted Planes
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- ellipse
- cylinder
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
  - activation.art.drawing.perspective.round_form_projection_warmup
  requires:
  - art.drawing.perspective.construct_projected_circles
  - art.drawing.perspective.align_cylinders_and_cones
  optional: []
  excludes: []
context:
  residency: transient
  priority: 62
  load_when:
  - the task needs project circles and cylinders on tilted planes
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p81_86_drill
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 81-86
    evidence_type: mixed
    note: Circle, ellipse, cylinder, and cone examples repeatedly build round solids from perspective squares and true projected centers.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: PAT_align_cylinders_and_cones_to_projected_circle_centers
  activation_mode: warmup
  residue:
    expected:
    - Apply project circles and cylinders on tilted planes during the current operation without keeping the drill instructions resident.
    scope: operation
  default_repetitions: 4
---

# Project Circles and Cylinders on Tilted Planes

## Practice Task
Construct four perspective squares at different tilts. Put a circle in each, then extend two of the circles into cylinders.

## Target Skill
Keep projected circles and round-solid axes tied to the perspective plane and true projected circle center.

## Setup
Use line only. Keep each square large enough to see its diagonals.

## Instructions
1. Build each square in perspective.
2. Draw both diagonals to locate the projected center.
3. Fit the ellipse to the square and plane.
4. On two examples, pass a cylinder axis through the projected center in the proper minor-axis direction.
5. Add the second circular end and tangent side edges.

## Success Check
The ellipses belong to their planes, and the cylinders do not kink or drift away from the square construction.

## Common Failures
- Centering the original circle only by the visible ellipse midpoint.
- Changing ellipse tilt without changing the supporting plane.
- Connecting two independently guessed ellipses.

## Expected Residue
Use a perspective square and its diagonals whenever exact round-solid placement matters more than a loose organic cross-contour.

## Notes
The drill is intentionally mechanical and short; the geometry should become a visual check, not a memorization burden.
