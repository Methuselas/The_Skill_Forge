---
schema_version: vNext-draft.1
object_id: PAT_construct_circles_as_ellipses_on_perspective_planes
object_type: pattern
name: Construct Circles as Ellipses on Perspective Planes
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- circle
- ellipse
- center
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
  - art.drawing.perspective.construct_projected_circles
  requires:
  - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 86
  load_when:
  - the task needs construct circles as ellipses on perspective planes
  unload_when:
  - the relevant spatial construction or correction is complete
relations:
- rel: related_to
  target_object_id: PAT_turn_cylinder_end_curves_with_depth
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p81_83
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 81-83
    evidence_type: mixed
    note: A circle parallel to the picture plane remains circular; when turned, it appears elliptical. D'Amelio uses the enclosing perspective square and its diagonals to locate the circle's true projected center, which need not coincide with the ellipse's apparent midpoint.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Construct Circles as Ellipses on Perspective Planes

## Pattern Rule
**IF** a real circle lies on a plane turned away from the picture plane, **THEN** construct its enclosing square in perspective, use the square to locate the circle's true projected center and tangency structure, and draw the visible circle as an ellipse fitted to that plane.

## Do
- Start from a perspective square or rectangle that contains the circle.
- Use the square's diagonals to locate the projected center of the real circle.
- Use the plane's center and edge relationships to place opposite points and tangencies before refining the ellipse.
- Make the ellipse flatter as the circular plane turns farther from a face-on view.
- Keep the major and minor ellipse directions perpendicular in the visible ellipse while distinguishing that geometric ellipse center from the projected center needed for construction.

## Don't
- Bisect the real circle in perspective by simply using the visible ellipse's widest midpoint.
- Freehand an ellipse whose orientation disagrees with the plane carrying it.
- Let the circle float independently of the square or plane perspective.

## Checklist
- The ellipse belongs to the same plane as its enclosing perspective square.
- Opposite structural points correspond through the square's true projected center.
- The amount of ellipse compression agrees with the plane's turn.
- The construction can support a cylinder or cone without shifting the circle afterward.

## Boundaries
This Pattern is about projected circles on planes. Organic cross-contours may use looser ellipse cues when exact circle-center construction is unnecessary.

## Notes
The important D'Amelio delta beyond the existing figure-cylinder card is that the visually centered ellipse is not always the correct metrological center of the original circle in perspective.
