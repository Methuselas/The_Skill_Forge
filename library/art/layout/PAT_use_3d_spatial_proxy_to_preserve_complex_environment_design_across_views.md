---
object_id: PAT_use_3d_spatial_proxy_to_preserve_complex_environment_design_across_views
object_type: pattern
name: Use 3D Spatial Proxy To Preserve Complex Environment Design Across Views
library_path:
- art
- layout
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- layout
- 3d
- environment
- continuity
- camera
- spatial_proxy
cross_links:
- rel: related_to
  target_object_id: PAT_preserve_established_scene_geography_while_cheating_minor_details_for_clarity
- rel: related_to
  target_object_id: AP_construct_a_shared_scene_perspective_field
reference:
  source_title: The Art of Layout and Storyboarding
  author: Mark T. Byrne
confidence: high
references: []
variants: []
---

# Use 3D Spatial Proxy To Preserve Complex Environment Design Across Views

## Pattern Rule
**IF** a complex designed environment or structure must remain consistent across many difficult viewpoints
**THEN** build or use a simplified 3D spatial proxy from the approved design and derive new views from that shared model while keeping the approved visual design authoritative.

## Do
- Establish the environment's design in drawings or another approved visual source before treating the 3D model as production authority.
- Build only enough model structure to preserve the spatial relationships, proportions, and camera-dependent geometry that are difficult to redraw consistently.
- Generate or inspect the required camera views from the same proxy, then develop the surrounding layout around those views.
- When an approved layout already defines the final shot, make the 3D construction conform to that layout rather than quietly redesigning the shot because the model prefers another solution.
- Use the proxy as a repeatable spatial reference for architecture, streets, rooms, vehicles, or other complex forms that recur across views.
- Translate the proxy through the project's final shape language and rendering rather than treating a raw model render as finished art by default.

## Don't
- Do not spend hours or days modeling an unapproved design that could have been rejected in cheap thumbnails.
- Do not let the 3D proxy override approved proportions, camera, or stylization merely because it is geometrically convenient.
- Do not build production detail that is irrelevant to the required views.
- Do not use independent models for different shots when one shared proxy is needed to preserve continuity.

## Checklist
- The proxy is derived from an approved environment/design authority.
- Repeated views preserve the same structure and proportions.
- Camera views can be changed without rebuilding the environment from scratch.
- The model serves the approved layout when the shot is already fixed.
- Final art remains consistent with project style rather than looking like an unintegrated model render.

## Notes
Byrne describes both directions of the layout/CG handoff: a 3D department may be required to match an approved layout, while Layout may use a computer model of a complex building to generate consistent views and draw the rest of the scene around them. The durable pattern is one approved spatial proxy serving continuity across viewpoints, not the era-specific print-and-paste method.
