---
object_id: PAT_rotate_perspective_grids_without_changing_unit_scale
object_type: pattern
name: Rotate Perspective Grids Without Changing Unit Scale
library_path:
- art
- perspective
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- perspective
- grid
- rotation
- scale
cross_links:
- rel: supports
  target_object_id: AP_construct_a_shared_scene_perspective_field
reference:
  source_title: 'How to Draw: Drawing and Sketching Objects and Environments from Your Imagination'
  author: Scott Robertson with Thomas Bertling
confidence: high
references: []
variants: []
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
The useful invariant is not “same screen-size square”; it is **same real square under a changed direction family**. The ellipse-overlay method preserves that invariant without recomputing the entire camera mathematically.
