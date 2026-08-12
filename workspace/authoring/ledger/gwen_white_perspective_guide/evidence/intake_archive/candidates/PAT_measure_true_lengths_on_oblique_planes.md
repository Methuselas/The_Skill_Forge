---
schema_version: vNext-draft.1
object_id: PAT_measure_true_lengths_on_oblique_planes
object_type: pattern
name: Measure True Lengths on Oblique Perspective Planes
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- inclined_plane
- measuring_point
- oblique
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
  - art.drawing.perspective.measure_true_lengths_on_oblique_planes
  requires:
  - art.drawing.perspective.construct_inclined_planes
  - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional:
  - art.drawing.perspective.project_plan_and_elevation
  excludes: []
context:
  residency: triggered
  priority: 88
  load_when:
  - an inclined, ascending, descending, or otherwise oblique plane needs exact true-distance transfer rather than approximate slope construction
  unload_when:
  - the plane's metric construction is fixed or the task returns to ordinary visual perspective
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: white_pp42_49
    kind: source
    source_id: gwen_white_perspective_guide
    locator: printed pp. 42-49 (PDF pp. 43-50)
    evidence_type: mixed
    note: White constructs ascending and descending planes from their horizontal direction, locates plane vanishing lines, derives ascending/descending measuring points, and transfers true lengths through a Picture Line / measuring-point construction.
  derivations:
  - derivation_id: white_oblique_metric_synthesis
    kind: synthesis
    inputs:
    - white_pp42_49
    note: Consolidates White's box-lid, ascending-plane, descending-plane, square, cube, and dart examples into a trigger-only exact metric procedure for straight oblique planes.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Measure True Lengths on Oblique Perspective Planes

## Pattern Rule
**IF** a line or shape lies in an ascending, descending, or otherwise oblique plane and its true length must be transferred exactly, **THEN** solve the plane's direction and vanishing line first, derive the corresponding ascending/descending measuring point, and transfer the real interval from a true-measure Picture Line into that plane rather than measuring the foreshortened image directly.

## Do
- Solve the plane's horizontal/base direction before solving its rise or fall.
- Keep the ascending or descending vanishing point on the vanishing locus required by that plane's direction; for the hinge-like cases White demonstrates, this lies on the vertical vanishing line through the base horizontal vanishing point.
- Use the plane's horizontal trace/contact with the Picture Plane to establish a Picture Line when a true interval must be introduced.
- Establish the auxiliary eye point used by the plane from the measuring point of the base direction; derive the ascending or descending measuring point from the inclined vanishing point and that auxiliary eye relationship.
- Mark the real distance on the Picture Line, project it toward the appropriate measuring point, and intersect the line already traveling toward the inclined vanishing point.
- Use the plane's vanishing line as a validation device: the vanishing points of direction families contained in one plane must lie on that plane's vanishing line.

## Don't
- Measure an oblique edge with a ruler on the finished perspective image and treat that screen-space length as its real length.
- Place an ascending/descending measuring point by convenience after the plane is already drawn.
- Collapse all sloping planes into one shared incline if their directions or tilt angles differ.
- Load this exact construction when a simple visual slope or diagonal subdivision already solves the drawing problem.

## Checklist
- The plane direction and the rise/fall direction belong to one coherent plane vanishing line.
- The true interval enters the construction at a legitimate Picture Line/trace rather than on an arbitrary receding edge.
- The auxiliary measuring point is derived from the plane/view geometry, not eyeballed.
- Repeated equal real lengths compress consistently when carried along the oblique plane.
- The result agrees with a plan/elevation check when one is available.

## Boundaries
This is a precision specialization for planar oblique geometry. It does not replace the simpler inclined-plane Pattern for ordinary roofs, roads, or ramps, and it does not generalize to curved surfaces without an additional surface construction.

## Notes
White's deeper contribution is not merely that sloping lines have different vanishing points; it is that **metric truth can be carried onto the slope** with derived measuring points. Keep the derivation internal unless the task actually requires exact construction.
