---
schema_version: vNext-draft.1
object_id: PAT_block_complex_objects_with_perspective_boxes
object_type: pattern
name: Block Complex Objects With Perspective Boxes
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- box
- construction
- object_drawing
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
  - art.drawing.perspective.block_objects_with_boxes
  requires:
  - art.drawing.perspective.choose_convergence_from_view_and_orientation
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 80
  load_when:
  - the task needs block complex objects with perspective boxes
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p37_49
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 37-49
    evidence_type: mixed
    note: D'Amelio uses cubes and rectangular solids as the prerequisite carrier for perspective and demonstrates complex objects reduced to box-like masses before detail.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Block Complex Objects With Perspective Boxes

## Pattern Rule
**IF** an object has complicated contours but occupies a simpler rectilinear volume, **THEN** solve its bounding box or box family first in the scene's perspective and fit the specific form inside that proven volume.

## Do
- Reduce the object to one or more rectangular solids that establish height, width, depth, and orientation.
- Send each box direction to the same vanishing family as other scene edges with that real direction.
- Check the box before adding contour, trim, holes, or surface decoration.
- Subdivide the box when an internal feature needs a true center or measured location.
- Use several joined boxes when one bounding block would hide an important directional change.

## Don't
- Perspective every small contour independently while the object's main volume is still uncertain.
- Let decorative edges drift away from the box field that carries them.
- Keep the box visible as a compulsory final graphic if the resolved object no longer needs it.

## Checklist
- The object can be simplified back to a stable box without changing its placement.
- Box edges agree with the scene vanishing directions.
- Detail fits inside or on the proven volume instead of correcting it after the fact.
- Several objects with shared orientation look like they occupy the same world.

## Boundaries
Curved objects may require the circle/cylinder Patterns after their containing box is established.

## Notes
D'Amelio makes the cube a prerequisite because it exposes the perspective relationship cleanly before complicated forms obscure it.
