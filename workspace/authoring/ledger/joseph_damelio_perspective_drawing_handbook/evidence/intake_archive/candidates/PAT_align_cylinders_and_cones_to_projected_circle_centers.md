---
schema_version: vNext-draft.1
object_id: PAT_align_cylinders_and_cones_to_projected_circle_centers
object_type: pattern
name: Align Cylinders and Cones to Projected Circle Centers
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- cylinder
- cone
- ellipse
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
  - art.drawing.perspective.align_cylinders_and_cones
  requires:
  - art.drawing.perspective.construct_projected_circles
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 82
  load_when:
  - the task needs align cylinders and cones to projected circle centers
  unload_when:
  - the relevant spatial construction or correction is complete
relations:
- rel: supports
  target_object_id: PAT_construct_circles_as_ellipses_on_perspective_planes
- rel: related_to
  target_object_id: PAT_turn_cylinder_end_curves_with_depth
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p83_86
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 83-86
    evidence_type: mixed
    note: Cylinder and cone centerlines follow the projected circle center/minor-axis direction; sides meet circular ends tangentially and remain consistent with the support plane.
  derivations:
  - derivation_id: round_solid_synthesis
    kind: synthesis
    inputs:
    - damelio_p83_86
    note: Combines the cylinder and cone examples around the shared requirement that the solid axis must pass through the projected center of its circular cross-section.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Align Cylinders and Cones to Projected Circle Centers

## Pattern Rule
**IF** a cylinder or cone is built from a circular end in perspective, **THEN** pass the solid's axis through the true projected center of that circle and keep the side generators tangent to the projected circular boundary.

## Do
- Solve the circular end on its plane before extending the solid.
- Run the centerline in the ellipse's minor-axis direction through the circle's projected construction center.
- For a cylinder, keep corresponding end circles on the same axis and connect them with tangent side edges.
- For a cone, place the apex on the same axis and draw side edges tangent to the base ellipse.
- When a cone lies on a supporting plane, let the axis tilt consistently with that support rather than forcing it horizontal.

## Don't
- Start cylinder sides from the visible ellipse midpoint if that point is not the projected circle center.
- Connect two unrelated ellipses and call the result one cylinder.
- Draw cone sides through the base ellipse instead of meeting it tangentially.

## Checklist
- Every circular cross-section shares one coherent solid axis.
- The axis passes through the projected center established by the perspective construction.
- Side edges touch the ellipse without cutting through it incorrectly.
- The solid's direction agrees with the plane and vanishing field around it.

## Boundaries
For loose figure construction, the existing foreshortened-cylinder Pattern remains the lighter diagnostic. Load this exact construction when round solids must sit precisely in a solved scene.

## Notes
This card specializes D'Amelio's metrological circle construction for exact cylindrical and conical solids rather than replacing organic figure methods.
