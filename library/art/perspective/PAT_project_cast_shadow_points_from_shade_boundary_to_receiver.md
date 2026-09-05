---
object_id: PAT_project_cast_shadow_points_from_shade_boundary_to_receiver
object_type: pattern
name: Project Cast-Shadow Points From Shade Boundary to Receiver
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
- shade_boundary
- receiving_plane
- projection
cross_links:
- rel: related_to
  target_object_id: PAT_choose_cast_shadow_ray_model_from_light_geometry
reference:
  source_title: Perspective Made Easy
  author: Ernest R. Norling
confidence: high
references: []
variants: []
---

# Project Cast-Shadow Points From Shade Boundary to Receiver

## Pattern Rule
**IF** exact cast-shadow placement is needed on a known receiving surface, **THEN** project rays from valid points on the casting form's shade boundary and intersect those rays with the receiving plane to locate the shadow, preserving the receiver's perspective geometry.

## Do
- Establish the receiving plane before solving the shadow contour.
- Use points on the shade boundary as the casting points; the cast shadow begins from geometry that actually separates light-facing from unlit form.
- Project each casting point along the accepted light-ray model until it meets the receiver.
- Connect projected shadow points in the order implied by the casting boundary.
- Validate that the resulting contour lies on the receiver rather than floating through space.

## Don't
- Guess the shadow silhouette first and retrofit rays afterward.
- Project from arbitrary silhouette points that are not part of the relevant shade boundary.
- Let the shadow violate the receiver's perspective simply to improve a local shape.

## Checklist
- Each important shadow point traces back to a valid casting point.
- Each construction follows the accepted light model.
- Each projected point terminates on the receiving surface.
- The connected contour remains coherent with the receiver's perspective.

## Notes
This Pattern owns the local projection decision. Sequence-level setup, branch choice, rollback, and completion remain AP responsibilities.
