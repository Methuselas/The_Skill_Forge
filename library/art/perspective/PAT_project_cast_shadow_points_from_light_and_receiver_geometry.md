---
object_id: PAT_project_cast_shadow_points_from_light_and_receiver_geometry
object_type: pattern
name: Project Cast-Shadow Points From Light and Receiver Geometry
library_path:
- art
- perspective
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- perspective
- cast_shadow
- light_ray
- projection
- receiver
cross_links: []
reference:
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants: []
---

# Project Cast-Shadow Points From Light and Receiver Geometry

## Pattern Rule
**IF** a cast-shadow boundary must be located constructively on a known receiving surface
**THEN** project rays from the light through points on the caster's shade boundary, intersect those rays with the receiver, and reconnect the resulting points in casting-boundary order

## Do
- Identify the shade-boundary points that actually block the light before projecting the shadow.
- Treat distant directional light as parallel rays and a nearby compact light as rays diverging from the source.
- Establish the receiver's plane or surface geometry before locating ray intersections on it.
- For a planar receiver, use the perspective direction shared by the light-ray family and the receiver-plane shadow traces.
- For a local point light and upright caster, use the light source and its projection onto the receiver to coordinate ray and shadow directions.
- Reconstruct intersections whenever the shadow crosses to another plane, incline, or curved surface; preserve the light ray while changing the receiving geometry.
- Connect projected points in the same order as their casting points so the shadow boundary does not fold arbitrarily.

## Don't
- Do not extend a screen-space silhouette across a receiver without ray/surface intersections.
- Do not let directional-light rays diverge or local-light rays become parallel merely to improve the shape.
- Do not project from arbitrary object corners when those points do not belong to the shade boundary.
- Do not carry one flat contour unchanged across a turn in the receiving surface.

## Checklist
- Every decisive shadow point traces back to a shade-boundary point, a valid light ray, and a receiver intersection.
- The ray family matches the light type.
- The shadow lies on the receiver and changes construction when the receiver changes.
- Boundary order remains coherent from caster to projected shadow.

## Notes
This Pattern owns the local geometric decision that turns caster, light, and receiver information into projected shadow points. It does not choose the scene lighting, establish the whole perspective field, or sequence a complete cast-shadow workflow.
