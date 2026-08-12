---
schema_version: vNext-draft.1
object_id: PAT_control_perspective_distortion_with_vanishing_spacing
object_type: pattern
name: Control Perspective Distortion With Vanishing Spacing
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- distortion
- cone_of_vision
- viewpoint
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
  - art.drawing.perspective.control_distortion_with_vanishing_spacing
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 86
  load_when:
  - the task needs control perspective distortion with vanishing spacing
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p58_60
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 58-60
    evidence_type: mixed
    note: D'Amelio relates excessive edge distortion to working beyond a useful cone of vision and to vanishing points placed too close together; he recommends greater viewing distance/VP separation or cropping to the undistorted center, while noting that excessive separation can make the view too flat.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Control Perspective Distortion With Vanishing Spacing

## Pattern Rule
**IF** perspective near the edges feels unnaturally stretched, pinched, or violently convergent, **THEN** treat the vanishing-point spacing and usable cone of vision as the first suspects; spread the vanishing points farther apart or keep the composition within the less-distorted central region.

## Do
- Compare central forms with forms near the outer limits of the view.
- Increase vanishing-point separation when convergence becomes excessive.
- Crop away extreme outer construction when only the center reads naturally.
- If the scene becomes too flat and scarcely converges, test somewhat closer vanishing points or a view that shows more surrounding depth.

## Don't
- Repair edge distortion by locally bending individual objects away from the shared perspective field.
- Assume stronger convergence is automatically more dramatic or more correct.
- Push useful construction far outside the view merely because the vanishing point is mathematically available there.

## Checklist
- Repeated forms remain plausible near the frame edges.
- Parallel families still converge consistently after correction.
- The center does not look flat while the edges look torn open.
- Cropping or changing vanishing spacing fixes the field globally instead of object by object.

## Boundaries
This is a practical distortion-control rule from D'Amelio's cone-of-vision discussion. It is not a lens model and does not introduce focal-length mathematics.

## Notes
The book's remedy is visual and constructive: alter the viewing relationship/vanishing-point spacing or restrict the usable field.
