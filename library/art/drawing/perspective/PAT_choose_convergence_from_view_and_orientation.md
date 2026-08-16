---
object_id: PAT_choose_convergence_from_view_and_orientation
object_type: pattern
name: Choose Convergence From View and Object Orientation
library_path:
- art
- drawing
- perspective
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- perspective
- convergence
- one_point
- two_point
cross_links:
- rel: supports
  target_object_id: PAT_establish_eye_level_and_vanishing_directions
reference:
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants:
- variant_id: VAR_derive_coupled_vps_with_visual_rays
  variant_name: Derive Coupled Vanishing Points With Visual Rays
  variant_basis: method_sequence
  difference_from_foundation: 'Finalizes Norling''s coupled-VP intuition and Robertson''s visual-ray method: each vanishing point is the picture-plane intersection of a sight ray from the station point parallel to that world direction.'
  when_to_use: Use when exact horizontal direction families or rotated perpendicular grids must stay camera-consistent.
  when_not_to_use: Do not treat two vanishing points as independently draggable style handles in an exact perspective setup.
  absorbed_from_object_id: none
---

# Choose Convergence From View and Object Orientation

## Pattern Rule
**IF** you must decide whether an edge family stays parallel in the picture or converges, **THEN** decide from that family's orientation to the picture plane and central viewing direction rather than choosing a named one-, two-, or three-direction setup by habit.

## Do
- Treat a rectangular object as three families of mutually different parallel directions.
- Keep a family parallel in the drawing when it is parallel to the picture plane.
- Converge a family when it recedes through depth.
- Let a horizontal family point to the central vanishing point when it runs directly away from the observer.
- When looking materially up or down, allow vertical-world lines to converge toward their own upper or lower vanishing point.

## Don't
- Move the main vanishing point off center while mechanically keeping the perpendicular horizontal family parallel if the view no longer supports that condition.
- Force all verticals to remain vertical when the chosen view is clearly pitched up or down.
- Choose “one-point” or “two-point” first and bend the subject to the label afterward.

## Checklist
- Each line family behaves consistently with one three-dimensional direction.
- A face nearly parallel to the picture plane shows less convergence than a face turned away.
- The chosen convergence explains the view rather than decorating it.
- Up/down views are not flattened by an automatic vertical-line rule.

## Notes
D'Amelio's cube sequence is the practical carrier for this rule: named systems are consequences of view and orientation.

**Boundaries**
This Pattern selects convergence topology. It does not determine exact spacing or correct excessive distortion.

Variants retained in this canonical object: `VAR_derive_coupled_vps_with_visual_rays`.
