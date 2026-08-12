---
schema_version: vNext-draft.1
object_id: PAT_project_curves_onto_sectioned_surfaces
object_type: pattern
name: Project Curves Onto Sectioned Surfaces
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- curve
- projection
- sections
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
  - art.drawing.perspective.project_curves_onto_sectioned_surfaces
  requires:
  - art.drawing.perspective.build_complex_volumes_with_xyz_sections
  optional:
  - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
  excludes: []
context:
  residency: triggered
  priority: 89
  load_when:
  - a hole, cut line, graphic, fillet boundary, or design curve must be transferred from a readable plane onto an inclined or curved constructed volume
  unload_when:
  - enough projected points exist to redraw the target curve reliably on the surface
relations:
- rel: specialization_of
  target_object_id: AP_build_complex_volumes_with_xyz_sections
grounding:
  mode: source_led
  evidence:
  - evidence_id: robertson_pp90_91_cutting
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 90-91 (physical PDF pp. 88-89)
    evidence_type: mixed
    note: Robertson projects hole and cut shapes from a flat construction plane into tapered/curved volumes by locating where source-shape projections intersect the volume's section lines.
  - evidence_id: robertson_pp94_99_surface_projection
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 94-99 (physical PDF pp. 92-97)
    evidence_type: mixed
    note: Surface sculpting examples project curves through section networks and introduce a temporary, less-foreshortened construction plane when the target plane is too compressed to draw the controlling curve clearly.
  derivations:
  - derivation_id: section_surface_projection_synthesis
    kind: synthesis
    inputs:
    - robertson_pp90_91_cutting
    - robertson_pp94_99_surface_projection
    note: Consolidates cutting, sculpting, and temporary-plane examples into one transferable projection rule without claiming Robertson's approximate cylinder-label example is an exact non-stretch wrap.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Project Curves Onto Sectioned Surfaces

## Pattern Rule
**IF** a curve is easy to design on a flat/readable construction plane but must land accurately on a curved, tapered, or inclined volume **THEN** keep the source curve on the readable plane, project its control points through the volume's section lines, collect the intersections on the target surface, and redraw the final curve through those surface points.

## Do
- Design the source shape where it is easiest to control: a side plane, ground plane, front plane, or temporary construction plane.
- Use the existing section network as the receiving coordinate system; add another section only where the curve needs another trustworthy point.
- Project source points along the consistent construction direction Robertson uses for that view, then mark where each projection meets the target section/surface.
- For a hole or cut, project both the opening and the affected section boundaries so the far/near edges agree with the volume.
- If the target plane is severely foreshortened, extend the grid to a temporary plane that faces the viewer more clearly, draw the shape there, then project it back into the target.
- Draw the final surface curve smoothly through the solved points rather than mechanically connecting them with corners.

## Don't
- Draw a graphic or cut directly on a highly foreshortened shell and then bend the surrounding volume to fit it.
- Add dozens of sections before knowing where accuracy is actually needed.
- Assume a straight projection produces an exact non-stretch material wrap around every curved surface; Robertson explicitly treats the label-on-cylinder example as an approximation.
- Keep a temporary construction plane in the final drawing after it has served its transfer purpose.

## Checklist
- The source curve remains readable and controllable on its construction plane.
- Every important target point can be traced back through a consistent projection to the source geometry.
- The projected curve agrees with the volume's sections instead of floating over them.
- Added sections appear only where they increase confidence in the final curve.
- A cut or surface detail still reads correctly when the construction lines are removed.

## Notes
The temporary-plane move is especially valuable in extreme foreshortening: **move the design problem to a plane you can see, then project the answer back**. This keeps the user's runtime task geometric and visual rather than algebraic.
