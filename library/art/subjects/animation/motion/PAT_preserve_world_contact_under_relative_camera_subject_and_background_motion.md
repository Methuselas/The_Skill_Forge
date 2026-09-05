---
object_id: PAT_preserve_world_contact_under_relative_camera_subject_and_background_motion
object_type: pattern
name: Preserve World Contact Under Relative Camera Subject And Background Motion
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
foundation_object_id: PAT_track_weight_support_and_transfer_through_every_pose
tags:
- animation
- camera_motion
- relative_motion
- world_contact
- planted_feet
- background_motion
- locomotion
cross_links:
- rel: related_to
  target_object_id: PAT_preserve_readable_composition_through_camera_motion
- rel: related_to
  target_object_id: AP_construct_walk_from_contact_down_passing_up_phases
reference:
  source_title: Timing for Animation
  author: Harold Whitaker and John Halas
confidence: high
references: []
variants:
- variant_id: VAR_byrne_hold_subject_while_environment_moves_in_perspective
  variant_name: Hold the Subject While the Environment Moves in Perspective
  variant_basis: method_sequence
  difference_from_foundation: Adds a hand-drawn animation-layout implementation in which a character or vehicle animates essentially
    in place while simplified environment elements move back toward the horizon in coherent perspective to create travel.
  when_to_use: Use for relatively short travel shots where moving the perspective environment is cheaper or clearer than translating
    the subject through a large world.
  when_not_to_use: Do not use when the resulting environment motion, duration, or complexity makes the cheat more visible
    than direct subject travel would be.
  absorbed_from_object_id: none
---

# Preserve World Contact Under Relative Camera Subject And Background Motion

## Pattern Rule
**IF** a foot, wheel, prop, or other point is supposed to remain attached to the world while the subject, camera, or background layers move independently
**THEN** solve the screen motion from the shared world contact and derive the relative layer compensation from that relationship
**ELSE** animate the layers independently only when no persistent world attachment needs to be preserved.

## Do
- Identify the contact point and the world-space travel it represents before assigning screen-space motion to subject, camera, or background.
- Derive background or camera-relative compensation from the subject's actual travel so planted contacts remain planted.
- Recompute the relative motion when the camera changes speed, pans ahead, tracks back, or otherwise alters the apparent screen displacement.
- In 3D, prefer genuine world positions for character, environment, and camera so projection creates the relative screen motion automatically.
- Check contact frames in playback for sliding even when every individual layer appears smooth by itself.
- Apply the same logic to wheels, carried objects touching surfaces, or any other element whose contact should remain fixed in the world.

## Don't
- Do not animate a walk cycle and a scrolling background as unrelated loops and hope their speeds happen to match.
- Do not preserve smooth camera motion at the cost of slipping feet, drifting wheels, or other broken world contacts.
- Do not hard-code historical peg-bar distances or one studio's camera measurements as universal rules.
- Do not compensate every layer mechanically when the scene already exists coherently in world space.

## Checklist
- Every intended planted contact is stable in the world rather than merely plausible in one still frame.
- Subject travel, camera motion, and background displacement agree on the same underlying movement.
- A camera speed change does not introduce foot slide or contact drift.
- Playback confirms the contact remains credible through the full shot.

## Notes
Whitaker and Halas show that a character cycle, background translation, and camera move cannot be timed as unrelated screen-space motions when the feet are meant to remain planted. The durable operation is to preserve the world relationship and derive the relative image motion from it. Their peg-bar arithmetic is one historical implementation of that relationship, not the rule itself.

`VAR_byrne_hold_subject_while_environment_moves_in_perspective` is a hand-drawn production implementation for short travel shots: keep the subject essentially in place while simple environmental elements move back toward the horizon in perspective. Use it only when the cheat remains clearer and cheaper than translating the subject through a larger world.
