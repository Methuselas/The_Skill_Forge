---
object_id: PAT_measure_subdivide_and_repeat_on_perspective_planes
object_type: pattern
name: Measure, Subdivide, and Repeat on Perspective Planes
library_path:
- art
- perspective
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- perspective
- measurement
- diagonal
- grid
cross_links: []
reference:
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants:
- variant_id: VAR_derive_arbitrary_measuring_point
  variant_name: Derive an Arbitrary Measuring Point
  variant_basis: method_sequence
  difference_from_foundation: Adds an exact trigger-only construction for deriving a measuring point from station/view geometry
    when arbitrary true-distance transfer is required.
  when_to_use: Use when diagonal-center subdivision and simpler proportion transfer are not exact enough.
  when_not_to_use: Do not load the full measuring-point derivation for ordinary subdivision tasks.
  absorbed_from_object_id: none
- variant_id: VAR_whitaker_project_locomotion_contact_intervals_through_depth
  variant_name: Project Locomotion Contact Intervals Through Depth
  variant_basis: context
  difference_from_foundation: Applies perspective-plane interval transfer to successive walk, run, or gallop contacts so equal real-space strides compress or expand correctly in image space as the subject recedes or approaches.
  when_to_use: Use when locomotion travels materially toward or away from the camera and equal screen-space contact gaps would flatten the depth or distort stride length.
  when_not_to_use: Do not add a perspective grid to side-on or shallow-depth locomotion when ordinary contact placement already preserves the intended travel.
  absorbed_from_object_id: none
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

## Notes
This Pattern intentionally consolidates several chapter techniques to keep the operational library smaller while retaining the exact-use cases that matter.

**Boundaries**
Use the simplest construction that proves the relationship. D'Amelio presents measuring lines as a precision aid, not as a reason to turn every sketch into a geometry exercise.

Variants retained in this canonical object: `VAR_derive_arbitrary_measuring_point`, `VAR_whitaker_project_locomotion_contact_intervals_through_depth`.

`VAR_whitaker_project_locomotion_contact_intervals_through_depth` specializes the same measurement logic for locomotion moving through depth. Treat successive ground contacts as equal real-space stride intervals on the solved perspective plane, then let their visible spacing compress or expand with recession/approach. Pair those contact anchors with the existing scale-through-depth construction so the whole figure changes apparent size coherently instead of merely shrinking the gaps between its feet.
