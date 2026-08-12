---
schema_version: vNext-draft.1
object_id: PAT_construct_inclined_planes_from_base_vanishing_directions
object_type: pattern
name: Construct Inclined Planes From Base Vanishing Directions
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- inclined_plane
- slope
- vanishing_line
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
  - art.drawing.perspective.construct_inclined_planes
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 84
  load_when:
  - the task needs construct inclined planes from base vanishing directions
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p77_80
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 77-80
    evidence_type: mixed
    note: For repeated lines on an inclined plane, the inclined vanishing point lies directly above or below the corresponding horizontal-direction vanishing point on a vertical vanishing line; planes of the same slope share an inclined vanishing line.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Construct Inclined Planes From Base Vanishing Directions

## Pattern Rule
**IF** a road, roof, stair run, ramp, or other plane rises or falls while keeping a known horizontal direction, **THEN** locate the inclined direction's vanishing point directly above or below the matching horizontal-direction vanishing point and use that relationship to build the slope.

## Do
- Solve the horizontal direction first.
- Raise the inclined vanishing point above the horizon for an upward run or lower it for a downward run as the view requires.
- Keep corresponding horizontal and inclined vanishing points aligned on the same vertical vanishing line.
- Reuse one inclined vanishing line for parallel planes sharing the same slope.
- When the plane changes compass direction, move the base horizontal vanishing point and its inclined partner together.

## Don't
- Invent the sloping convergence independently of the scene's horizontal direction.
- Treat an inclined plane as a flat ground plane with objects merely rotated on top.
- Assume every roof or ramp in a scene shares one slope vanishing point if their slopes differ.

## Checklist
- The slope direction and its horizontal counterpart remain vertically related.
- Parallel inclined edges agree on one inclined vanishing point.
- Repeated slope planes remain consistent as they move through the scene.
- Objects placed on the slope can still inherit the scene's scale logic.

## Boundaries
This Pattern handles straight inclined planes. Curved terrain and irregular surfaces require additional construction beyond this source's plane method.

## Notes
D'Amelio treats the horizontal vanishing line and inclined vanishing lines as members of the same general family: vanishing loci for parallel directions contained in parallel planes.
