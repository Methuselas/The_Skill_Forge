---
schema_version: vNext-draft.1
object_id: PAT_measure_subdivide_and_repeat_on_perspective_planes
object_type: pattern
name: Measure, Subdivide, and Repeat on Perspective Planes
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- measurement
- diagonal
- grid
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
  - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 84
  load_when:
  - the task needs measure, subdivide, and repeat on perspective planes
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p68_72
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 68-72
    evidence_type: mixed
    note: Diagonals locate the true center of perspective rectangles and support equal subdivision and repeated spacing through depth.
  - evidence_id: damelio_p73_76
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 73-76
    evidence_type: mixed
    note: Measuring-line constructions transfer arbitrary intervals, and perspective grids transfer two-dimensional designs onto receding planes.
  derivations:
  - derivation_id: plane_metrology_synthesis
    kind: synthesis
    inputs:
    - damelio_p68_72
    - damelio_p73_76
    note: 'Groups the chapter''s plane-measurement devices by one operational question: how to locate, divide, repeat, and transfer intervals on a receding plane.'
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Measure, Subdivide, and Repeat on Perspective Planes

## Pattern Rule
**IF** a receding plane needs a true center, repeated intervals, subdivisions, or a transferred design, **THEN** construct those relationships inside the perspective plane with diagonals, measuring lines, and a perspective grid rather than judging equal screen-space distances.

## Do
- Use the diagonals of a perspective rectangle to find its true center.
- Continue equal repeated spacing with diagonal constructions instead of copying the visible gap.
- Subdivide large regions first, then subdivide again when regular powers-of-two spacing is enough.
- When intervals are arbitrary rather than simple halves, use a measuring line and its construction vanishing point to transfer them into depth.
- For complex flat designs, mark key positions on a flat grid, reconstruct the grid in perspective, and reconnect the corresponding points.

## Don't
- Assume the image midpoint of a foreshortened rectangle is its true center.
- Make tile, window, column, or figure spacing equal on the page when the real spacing is equal in depth.
- Use the more technical measuring-line method when a diagonal subdivision already answers the question.

## Checklist
- Diagonals meet at the intended plane center.
- Repeated equal intervals compress consistently with depth.
- Arbitrary interval marks land on the receding plane without screen-space guessing.
- A transferred pattern preserves its structure after the plane is tilted into depth.

## Boundaries
Use the simplest construction that proves the relationship. D'Amelio presents measuring lines as a precision aid, not as a reason to turn every sketch into a geometry exercise.

## Notes
This Pattern intentionally consolidates several chapter techniques to keep the operational library smaller while retaining the exact-use cases that matter.
