---
object_id: AP_combine_pose_to_pose_planning_with_straight_ahead_motion_passes
object_type: ap
name: Combine Pose To Pose Planning With Straight Ahead Motion Passes
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
cross_links:
- rel: supports
  target_object_id: PAT_allocate_pose_to_pose_and_straight_ahead_control_by_motion_system
- rel: supports
  target_object_id: PAT_separate_story_keys_from_motion_extremes
- rel: supports
  target_object_id: PAT_design_breakdowns_as_authored_motion_decisions
- rel: supports
  target_object_id: PAT_inbetween_motion_along_arcs_revealed_by_neighboring_frames
- rel: supports
  target_object_id: PAT_carry_secondary_parts_through_overlap_follow_through_and_drag
- rel: supports
  target_object_id: PAT_phase_offset_body_parts_to_break_mechanical_locomotion
- rel: supports
  target_object_id: PAT_reanchor_straight_ahead_animation_with_registration_drawings
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Combine Pose To Pose Planning With Straight Ahead Motion Passes

## Objective
Combine pose-to-pose control with straight-ahead vitality by planning the important structure first and then animating selected motion systems more freely between guides.

## Steps / Flow
1. **Choose the control problem before choosing the method.** Apply `PAT_allocate_pose_to_pose_and_straight_ahead_control_by_motion_system` to assign pose-to-pose control where story poses, exact timing, coordinated staging, contact, or scale must stay locked and straight-ahead treatment where freer continuity or independent timing serves the motion.
2. **Lock the primary anchors that truly need control.** Apply `PAT_separate_story_keys_from_motion_extremes` and `PAT_design_breakdowns_as_authored_motion_decisions` to establish keys, extremes, and crucial breakdowns for the main action without over-keying subordinate systems.
3. **Animate the primary action between the anchors.** Preserve planned timing and construction while applying `PAT_inbetween_motion_along_arcs_revealed_by_neighboring_frames` wherever the surrounding action reveals a non-mechanical path.
4. **Use straighter-ahead passes where vitality matters.** Continue the allocation established by `PAT_allocate_pose_to_pose_and_straight_ahead_control_by_motion_system`. Apply `PAT_carry_secondary_parts_through_overlap_follow_through_and_drag` to loose or inertial systems, and use `PAT_phase_offset_body_parts_to_break_mechanical_locomotion` when a locomotion system needs a causal phase offset.
5. **Check cumulative structural drift.** Apply `PAT_reanchor_straight_ahead_animation_with_registration_drawings` periodically, especially at changes of direction, force, contact, or staging, so successive local errors do not accumulate into visible shrinkage, growth, or attachment drift.
6. **Test after each pass.** Repair pose-to-pose woodenness, straight-ahead structural drift, timing conflicts, or subordinate motion that redesigns the primary action before continuing.

**Completion check**
- The action keeps story clarity without becoming mechanically interpolated.
- Fast or complex subordinate motion retains vitality without losing structural control.
- Character scale and construction remain stable across long straight-ahead passages.
- Secondary and tertiary motion support rather than redesign the primary action.

## Notes

Define which motion systems are locked and which are allowed to develop freely before starting the hybrid pass. Periodic registration drawings are most useful at changes of direction or force, where accumulated scale drift and a mistimed secondary system are easiest to detect before they spread.
