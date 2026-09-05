---
object_id: PAT_choose_cast_shadow_ray_model_from_light_geometry
object_type: pattern
name: Choose Cast-Shadow Ray Model From Light Geometry
library_path:
- art
- perspective
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- perspective
- cast_shadow
- light_geometry
- projection
cross_links:
- rel: related_to
  target_object_id: PAT_project_cast_shadow_points_from_shade_boundary_to_receiver
reference:
  source_title: Perspective Made Easy
  author: Ernest R. Norling
confidence: high
references: []
variants: []
---

# Choose Cast-Shadow Ray Model From Light Geometry

## Pattern Rule
**IF** a cast shadow must be constructed from an explicit light source, **THEN** choose the ray model from the light geometry before projecting the shadow: treat effectively distant directional light as parallel rays, and treat a nearby point light as rays diverging from the source.

## Do
- Identify whether the light behaves as effectively directional/distant or local/point-like for the construction.
- Keep directional-light rays parallel in space even when their projected lines converge in the picture.
- For a local point light, originate each construction ray at the actual source position.
- Preserve one light model throughout a single shadow construction unless multiple real sources are intentionally present.

## Don't
- Let directional sunlight fan outward merely because the drawing is in perspective.
- Force a local point source into a parallel-ray construction.
- Change ray models locally to make an inconvenient shadow contour fit.

## Checklist
- The light type is classified before shadow points are projected.
- All construction rays obey the chosen light model.
- The chosen model remains consistent with the scene's established light position/direction.

## Notes
The decision is geometric rather than stylistic: parallel versus divergent rays determines which projection construction is valid. Perspective may change how those rays appear on the page without changing their spatial relationship.
