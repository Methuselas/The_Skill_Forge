---
object_id: PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation
object_type: pattern
name: Separate Ballistic Center Of Mass Path From Body Rotation And Deformation
library_path:
- art
- subjects
- animation
- motion
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- ballistic_motion
- center_of_mass
- trajectory
- rotation
cross_links:
- rel: related_to
  target_object_id: PAT_show_mass_through_resistance_to_acceleration_and_direction_change
reference:
  source_title: Timing for Animation
  author: Harold Whitaker and John Halas
confidence: high
references: []
variants: []
---

# Separate Ballistic Center Of Mass Path From Body Rotation And Deformation

## Pattern Rule
**IF** an object or character is unsupported in free flight and its shape, pose, or orientation changes while gravity governs the overall travel
**THEN** establish the center-of-mass trajectory first, then animate rotation, pose change, or deformation around that traveling center without letting local shape changes distort the ballistic path

## Do
- Track the center of mass as the stable reference for the airborne path, even when an irregular object spins or a character changes pose in flight.
- For angled flight, keep the forward component comparatively steady while vertical spacing closes toward the apex and opens again during the fall.
- Rotate irregular objects around their traveling center of mass rather than around a convenient visual corner or endpoint.
- Let a character articulate, tuck, stretch, or rotate during flight while preserving the already-established route of the body mass.
- Treat each airborne segment after a bounce as a new arc, and reduce successive heights when impact has removed energy.
- Simplify or exaggerate the natural path when the story needs it, but keep the gravitational cause legible.

## Don't
- Do not redraw the trajectory to follow whichever limb, edge, or silhouette feature happens to be easiest to track.
- Do not let internal pose changes make the whole body appear to steer arbitrarily while it is unsupported.
- Do not flatten an angled ballistic path into uniform spacing through the apex; the rise should decelerate before the fall accelerates.
- Do not repeat identical bounce heights when the intended material is losing energy on impact.

## Checklist
- The center of mass follows one coherent airborne arc independent of local rotation or deformation.
- Spacing closes into the apex and opens out of it in a way that makes gravity readable.
- Rotation or pose change appears to occur around the traveling mass rather than replacing its path.
- Successive bounce arcs diminish when the action is meant to dissipate energy.

## Notes
Free-flight animation becomes easier to reason about when the path of the mass and the changing shape of the body are solved as separate problems. A hammer can spin while its center of mass follows a clean arc; a jumping or diving character can change pose dramatically while the body mass still travels on the same ballistic route. This separation preserves physical causality without requiring literal numerical simulation.
