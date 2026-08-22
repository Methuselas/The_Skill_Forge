---
object_id: PAT_construct_inclined_planes_from_base_vanishing_directions
object_type: pattern
name: Construct Inclined Planes From Base Vanishing Directions
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
- inclined_plane
- slope
- vanishing_line
cross_links: []
reference:
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants:
- variant_id: VAR_slope_auxiliary_false_eye_level
  variant_name: Use a Slope Auxiliary Vanishing Direction
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Norling''s useful hill/street mnemonic while preserving the true eye level: rising or
    falling directions get their own slope-aligned vanishing line/direction.'
  when_to_use: Use for roads, ramps, roofs, or repeated forms traveling along a shared incline.
  when_not_to_use: Do not interpret the auxiliary slope line as a second literal camera eye level.
  absorbed_from_object_id: none
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

## Notes
D'Amelio treats the horizontal vanishing line and inclined vanishing lines as members of the same general family: vanishing loci for parallel directions contained in parallel planes.

**Boundaries**
This Pattern handles straight inclined planes. Curved terrain and irregular surfaces require additional construction beyond this source's plane method.

Variants retained in this canonical object: `VAR_slope_auxiliary_false_eye_level`.
