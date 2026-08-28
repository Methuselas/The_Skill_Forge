---
object_id: PAT_create_motion_parallax_by_separating_panning_layers_by_depth_and_speed
object_type: pattern
name: Create Motion Parallax By Separating Panning Layers By Depth And Speed
library_path:
- art
- layout
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- layout
- animation
- parallax
- background
- panning
- depth
cross_links:
- rel: related_to
  target_object_id: PAT_design_depth_by_coordinating_spatial_cues
- rel: related_to
  target_object_id: PAT_preserve_world_contact_under_relative_camera_subject_and_background_motion
- rel: related_to
  target_object_id: PAT_build_repeat_pan_from_seamless_cycle_and_nonrevealing_landmarks
reference:
  source_title: The Art of Layout and Storyboarding
  author: Mark T. Byrne
confidence: high
references: []
variants:
- variant_id: VAR_byrne_plan_multiplane_motion_from_master_action_level
  variant_name: Plan Multiplane Motion From A Master Action Level
  variant_basis: method_sequence
  difference_from_foundation: "Adds Byrne's control for multiplane scenes: choose the depth plane containing the principal action as the master spatial reference, then derive other layers' relative displacement, scale behavior, and when relevant focus relationship from their depth relative to that plane instead of assigning arbitrary independent speeds."
  when_to_use: "Use when several depth layers pan or move around a principal animated action and the scene needs one coherent relational motion reference."
  when_not_to_use: "Do not canonize Byrne's example percentages as universal values or force the action plane to be the only possible focus plane when story emphasis requires another choice."
  absorbed_from_object_id: none
---

# Create Motion Parallax By Separating Panning Layers By Depth And Speed

## Pattern Rule
**IF** a moving layout needs stronger depth than one flat translated background can provide
**THEN** separate usable environment elements by depth and move nearer layers farther or faster across the screen than deeper layers while preserving one coherent underlying camera/subject motion.

## Do
- Decide which environment layers are nearer and farther before assigning their screen displacement.
- Let nearer elements traverse more screen distance while distant elements drift less for the same underlying travel.
- Design overlaps so the separate layers recombine as one environment rather than looking like independent sliding cards.
- Keep character, wheel, or prop contacts tied to the same world travel so the parallax does not introduce foot slide or drift.
- When layers repeat, stagger or design their cycles so multiple seams and landmark recurrences do not synchronize conspicuously.
- Judge the parallax in playback and reduce the differential motion when it becomes more noticeable than the scene itself.

## Don't
- Do not assign unrelated layer speeds simply to create visual activity.
- Do not move a distant background more aggressively than a near overlay unless the camera/world motion specifically requires it.
- Do not let separated levels contradict the scene's established spatial order.
- Do not use parallax as a substitute for coherent perspective, scale, and contact relationships.

## Checklist
- Near/far layer speeds agree with the intended depth order.
- All layers feel driven by one camera/world movement.
- Overlaps preserve a unified environment.
- World contacts remain stable.
- Repeating layers do not expose synchronized seams or cycles.

## Notes
Byrne's panning overlays show the animation-layout mechanism directly: a nearer overlay travels faster than the background and thereby increases the depth impression. His later multiplane example adds a useful control: use the principal action depth as a master reference and derive surrounding layer motion relationally from it rather than assigning every level an isolated speed. The durable operation is temporal parallax rather than any one cel or camera setup.

Retained bounded variant: `VAR_byrne_plan_multiplane_motion_from_master_action_level`.
