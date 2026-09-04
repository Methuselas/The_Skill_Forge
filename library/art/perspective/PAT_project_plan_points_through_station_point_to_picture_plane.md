---
object_id: PAT_project_plan_points_through_station_point_to_picture_plane
object_type: pattern
name: Project Plan Points Through the Station Point to the Picture Plane
library_path:
- art
- perspective
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: PAT_establish_eye_level_and_vanishing_directions
tags:
- perspective
- plan
- station_point
- picture_plane
- projection
cross_links: []
reference:
  source_title: Perspective Made Easy
  author: Ernest R. Norling
confidence: high
references: []
variants: []
---

# Project Plan Points Through the Station Point to the Picture Plane

## Pattern Rule
**IF** known plan locations must be transferred into an exact perspective view
**THEN** draw visual rays from the station point through the controlling plan points and use their picture-plane intersections to establish the corresponding projected horizontal locations

## Do
- Register the plan, station point, picture plane, and perspective view before drawing visual rays.
- Select only the plan corners, contacts, or direction controls needed to define the projected footprint.
- Draw each visual ray from the station point through its plan point and continue it to the picture plane.
- Transfer each picture-plane intersection into the registered perspective view without changing its horizontal identity.
- Use station-point lines parallel to principal plan directions when exact vanishing directions must be derived from the same setup.
- Keep each projected vertical attached to the plan point that generated it so later height transfer has an unambiguous destination.

## Don't
- Do not project plan points from a convenient page location that is not the chosen station point.
- Do not move picture-plane intersections by eye after the visual rays establish them.
- Do not infer exact projected heights from the plan; the plan owns horizontal location, not elevation.
- Do not crowd the construction with plan points that add no controlling information.

## Checklist
- Every important projected footprint point traces to one plan point and one station-point visual ray.
- Picture-plane intersections remain registered to the perspective view.
- Derived direction families agree with the established station point and picture plane.
- The result fixes horizontal locations without inventing vertical dimensions.

## Notes
This Pattern owns plan-to-picture-plane projection. It does not choose the camera, supply elevation heights, or orchestrate completion of the projected object.
