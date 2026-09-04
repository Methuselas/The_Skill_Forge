---
object_id: AP_construct_animation_with_keys_extremes_breakdowns_and_inbetweens
object_type: ap
name: Construct Animation With Keys Extremes Breakdowns And Inbetweens
library_path:
- art
- subjects
- animation
- inbetweening
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- planning
- keys
- breakdowns
- inbetweens
cross_links:
- rel: supports
  target_object_id: PAT_separate_story_keys_from_motion_extremes
- rel: supports
  target_object_id: PAT_design_animation_extreme_as_storytelling_pose
- rel: supports
  target_object_id: PAT_design_breakdowns_as_authored_motion_decisions
- rel: supports
  target_object_id: PAT_inbetween_motion_along_arcs_revealed_by_neighboring_frames
- rel: supports
  target_object_id: PAT_construct_difficult_inbetween_from_basic_shapes_before_details
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Construct Animation With Keys Extremes Breakdowns And Inbetweens

## Objective
Build animation hierarchically so storytelling and motion decisions are solved before interpolation fills the remaining frames.

## Steps / Flow
1. Apply `PAT_separate_story_keys_from_motion_extremes` to establish only the storytelling keys needed for the event to remain intelligible.
2. Continue `PAT_separate_story_keys_from_motion_extremes`, then apply `PAT_design_animation_extreme_as_storytelling_pose` to add the motion extremes required by the physical and expressive transition without confusing their role with story keys.
3. Apply `PAT_design_breakdowns_as_authored_motion_decisions` to place breakdowns or passing positions that choose the path, attitude, overlap, and spacing bias rather than defaulting to arithmetic midpoints.
4. Test the structure in motion.
5. Add only the remaining inbetweens after the action is already designed. Apply `PAT_inbetween_motion_along_arcs_revealed_by_neighboring_frames` where the wider sequence determines the path; when finished contours make an intermediate form ambiguous, apply `PAT_construct_difficult_inbetween_from_basic_shapes_before_details` before restoring detail.

**Completion check**
- Inbetweens finish an already understandable action rather than inventing it.
- The hierarchy can be revised at the cheapest responsible level.

## Notes

Temporarily hide the ordinary inbetweens to diagnose the hierarchy. If the remaining keys, extremes, and breakdowns no longer communicate the action, restore the missing decision at the appropriate structural level instead of adding denser interpolation.
