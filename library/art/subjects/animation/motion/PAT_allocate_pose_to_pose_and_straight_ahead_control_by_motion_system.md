---
object_id: PAT_allocate_pose_to_pose_and_straight_ahead_control_by_motion_system
object_type: pattern
name: Allocate Pose-to-Pose and Straight-Ahead Control by Motion System
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
- pose_to_pose
- straight_ahead
- workflow
- motion_systems
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Allocate Pose-to-Pose and Straight-Ahead Control by Motion System

## Pattern Rule
**IF** one animated action needs both dependable structural control and motion that would become lifeless or cumbersome if fully predetermined
**THEN** assign pose-to-pose control to the story-, timing-, staging-, and scale-critical systems while reserving straight-ahead treatment for systems whose vitality depends on freer continuity, overlap, or independent timing

## Do
- Identify the primary action and the poses or events that must remain fixed for story, staging, contact, timing, or scale.
- Divide the subject into motion systems by causal role rather than by arbitrary body-part lists.
- Use pose-to-pose anchors for systems whose relationships must coordinate exactly across the shot.
- Use straight-ahead treatment for fast, chaotic, flexible, or independently timed systems when predetermined matching would suppress their motion logic.
- State which systems are locked and which are free before animating the hybrid passage.
- Let the locked primary system constrain subordinate motion without forcing every subordinate state to share its keys.

## Don't
- Do not choose one method for the entire shot merely from habit.
- Do not use straight-ahead freedom to redesign required story poses, contacts, or staging.
- Do not over-key loose secondary systems until their overlap becomes mechanical.
- Do not leave method allocation implicit when several animators or passes must share the shot.

## Checklist
- Every important motion system has a stated control method and reason.
- Story, timing, staging, contact, and scale anchors remain authoritative where required.
- Freer systems retain causal connection to the primary action while developing their own continuity.
- The hybrid allocation reduces either rigidity or drift without creating conflicting authorities.

## Notes
This Pattern owns the choice of control method per motion system. It does not sequence the full hybrid workflow or perform the later drift and playback gates.
