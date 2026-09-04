---
object_id: PAT_transfer_elevation_heights_from_true_measure_line
object_type: pattern
name: Transfer Elevation Heights From a True-Measure Line
library_path:
- art
- perspective
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: PAT_carry_scale_through_depth_with_height_and_width_guides
tags:
- perspective
- elevation
- true_measure
- height
- projection
cross_links: []
reference:
  source_title: Perspective Made Easy
  author: Ernest R. Norling
confidence: high
references: []
variants: []
---

# Transfer Elevation Heights From a True-Measure Line

## Pattern Rule
**IF** orthographic elevation heights must be introduced into a perspective construction
**THEN** place the true vertical intervals on a registered true-measure line and carry them through the established vanishing field to the plan-fixed verticals that need those heights

## Do
- Choose a vertical line whose relationship to the picture plane permits true height measurement.
- Register its base with the corresponding ground or plan-projected location before marking height.
- Transfer the required elevation intervals onto that line at true scale.
- Project each height mark toward the appropriate vanishing direction and intersect it with the vertical already fixed by the plan projection.
- Repeat the transfer from a new trustworthy measure location when a change of supporting elevation invalidates the first one.
- Trace important constructed corners back to both their plan-fixed vertical and their elevation-derived height.

## Don't
- Do not measure true height directly on a foreshortened distant vertical.
- Do not carry a height through a vanishing family unrelated to the supporting plane.
- Do not let a plan point silently supply a vertical dimension that only the elevation establishes.
- Do not reuse a level-ground transfer unchanged across a change in supporting elevation.

## Checklist
- Each true height originates on a registered true-measure line.
- Each destination vertical was already fixed by the plan or equivalent horizontal construction.
- Height guides converge through the same perspective field as the supporting geometry.
- A completed corner can be traced independently to horizontal location and vertical height evidence.

## Notes
This Pattern owns the elevation-to-perspective height transfer. It assumes the viewpoint, picture plane, plan locations, and relevant vanishing directions are already established.
