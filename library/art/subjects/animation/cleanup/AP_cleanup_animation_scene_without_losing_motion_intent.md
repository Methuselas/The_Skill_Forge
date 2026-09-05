---
object_id: AP_cleanup_animation_scene_without_losing_motion_intent
object_type: ap
name: Clean Up an Animation Scene Without Losing Motion Intent
library_path:
- art
- subjects
- animation
- cleanup
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: AP_resolve_temporal_movement_for_pose_or_sequence
tags:
- animation
- cleanup
- continuity
- extremes
- arcs
- model_consistency
- motion_intent
cross_links:
- rel: supports
  target_object_id: PAT_design_animation_extreme_as_storytelling_pose
- rel: supports
  target_object_id: PAT_deform_animated_form_with_squash_and_stretch_while_preserving_volume
- rel: supports
  target_object_id: PAT_carry_secondary_parts_through_overlap_follow_through_and_drag
- rel: supports
  target_object_id: PAT_construct_difficult_inbetween_from_basic_shapes_before_details
- rel: related_to
  target_object_id: PAT_phrase_animation_timing_around_story_accents_and_action_beats
reference:
  source_title: Drawn to Life, Volume One
  author: Walt Stanchfield
confidence: high
references: []
variants: []
---

# Clean Up an Animation Scene Without Losing Motion Intent

## Objective
Bring a rough animated scene to a clearer, more consistent final drawing state while preserving the original action, force, timing relationships, character identity, and subtle secondary motion that make the sequence work.

## Steps / Flow
1. **Enter by understanding the scene rather than the first drawing.** Review the character model or accepted design, the intended story action, and enough of the sequence to know what the scene is portraying. Resolve uncertainty about the action before committing to finished corrections.
2. **Survey the sequence for its controlling states.** Use `PAT_design_animation_extreme_as_storytelling_pose` when deciding which extreme carries the story beat. Compare several drawings across the action, identify the key extremes and high points, and note which poses carry the strongest drive or story emphasis. Do not assume chronological cleanup is the safest route when later extremes establish the size, force, or destination needed to judge earlier drawings.
3. **Establish continuity anchors before local finish.** Compare key extremes for character size, proportion, volume, perspective, and major shape relationships. When the character deliberately grows or diminishes through the scene, use the beginning and ending states as anchors so the change progresses coherently instead of drifting.
4. **Preserve the motion logic while correcting structure.** Use `PAT_deform_animated_form_with_squash_and_stretch_while_preserving_volume` for deformation decisions and `PAT_carry_secondary_parts_through_overlap_follow_through_and_drag` for connected secondary response. As each drawing is clarified, compare it with relevant preceding and following states. Keep arcs, overlaps, squash and stretch, directional changes, and connected secondary actions consistent with where each shape came from and where it is going.
5. **Protect subtle action when a drawing must be rebuilt.** Use `PAT_construct_difficult_inbetween_from_basic_shapes_before_details` when a difficult replacement/inbetween needs to be reconstructed rather than traced. If roughness or off-model construction requires a new drawing, carry over the action's force, accent, deformation, and secondary relationships before refining contour. A structurally cleaner replacement that weakens the action has failed the cleanup task.
6. **Use sequence-aware correction rather than isolated polishing.** When a shape, line ending, feature, or detail appears to travel mechanically, compare multiple neighboring states and repair the path or volume relationship across the sequence instead of fixing only the visibly bad frame.
7. **Allocate finish according to what the motion can show.** Slow movement, close views, and exposed acting may require tighter control; fast movement or distant action can often retain broader construction so long as the main line of action and character read remain clear. Do not spend finish effort where it cannot survive the motion while neglecting the decisive poses.
8. **Run a reverse or fresh continuity pass.** Reinspect the sequence in a way that breaks familiarity, checking for drifting size, lost arcs, weakened extremes, mechanical spots, broken overlaps, inconsistent perspective, or cleanup choices that flattened the rough animation's vitality.
9. **Stop only when clarity improved without loss of life.** The scene is complete when the drawings are coherent and usable as final animation art while the sequence still carries the intended force, timing, character, and connected motion of the accepted rough action.

## Notes
Cleanup is not tracing rough drawings more neatly. It is a sequence-level finishing action that may correct or improve individual drawings, but every correction is constrained by neighboring states and by the animator's intended action. Physical registration methods, paper handling, and legacy reproduction mechanics are implementation details; the durable control problem is preserving motion while increasing drawing clarity and consistency.
