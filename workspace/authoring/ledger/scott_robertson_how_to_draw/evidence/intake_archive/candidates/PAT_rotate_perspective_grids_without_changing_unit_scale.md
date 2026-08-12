---
schema_version: vNext-draft.1
object_id: PAT_rotate_perspective_grids_without_changing_unit_scale
object_type: pattern
name: Rotate Perspective Grids Without Changing Unit Scale
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- grid
- rotation
- scale
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
  - art.drawing.perspective.rotate_grids_preserve_unit_scale
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  - art.drawing.perspective.construct_projected_circles
  optional:
  - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
  excludes: []
context:
  residency: triggered
  priority: 84
  load_when:
  - multiple objects need different horizontal rotations on one ground plane while sharing the same real unit size
  unload_when:
  - the rotated grids are established and can be reused as underlays
relations:
- rel: supports
  target_object_id: AP_construct_a_shared_scene_perspective_field
grounding:
  mode: source_led
  evidence:
  - evidence_id: robertson_pp51_52_rotated_grids
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 51-52 (physical PDF pp. 49-50)
    evidence_type: mixed
    note: Robertson constructs a trusted square, inscribes its correct perspective circle, traces the circle/view field, and uses tangency to that same ellipse to derive differently rotated squares that preserve unit size on the same ground plane.
  derivations:
  - derivation_id: robertson_same_scale_rotation_synthesis
    kind: synthesis
    inputs:
    - robertson_pp51_52_rotated_grids
    note: Converts the overlay demonstration into a reusable decision rule for one-world multi-orientation scenes.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Rotate Perspective Grids Without Changing Unit Scale

## Pattern Rule
**IF** several horizontal grids or objects must rotate independently on the same ground plane **THEN** preserve one trusted square and its perspective circle as the scale invariant, derive each new rotated square as another tangent square around that same ellipse, and let the new square establish its own vanishing pair.

## Do
- Build one reliable square first and keep its horizon, view field, and unit size fixed.
- Inscribe the circle carefully enough that it genuinely belongs to the original square; the ellipse becomes the shared rotational reference.
- Trace or otherwise preserve the ellipse and camera/view guides before searching for another orientation.
- Choose the new orientation on the same plane, construct a square whose sides are tangent to the same ellipse, then extend those side directions to obtain the new vanishing pair.
- Recheck that the rotated square still reads as the same real unit before multiplying it into a larger grid.
- Reuse the finished rotated grids as underlays instead of reconstructing them every time.

## Don't
- Rotate a square by eye and then resize it until it looks plausible; that destroys the shared unit.
- Keep the original vanishing pair after the world direction has changed.
- Change the ellipse size or position between rotations unless the unit or depth position is intentionally changing.
- Use a rough freehand ellipse when exact shared scale is the reason for loading this construction.

## Checklist
- The original and rotated squares occupy the same ground plane and represent the same real dimensions.
- Each orientation owns a coherent horizontal vanishing pair on the same horizon.
- The same inscribed ellipse can be read inside every rotated unit square.
- Objects built on different grids can stand together without unexplained scale drift.

## Notes
The useful invariant is not “same screen-size square”; it is **same real square under a changed direction family**. Robertson's ellipse-overlay method gives a practical way to preserve that invariant without recomputing the entire camera mathematically.
