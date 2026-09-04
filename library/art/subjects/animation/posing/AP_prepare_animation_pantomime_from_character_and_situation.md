---
object_id: AP_prepare_animation_pantomime_from_character_and_situation
object_type: ap
name: Prepare Animation Pantomime From Character and Situation
library_path:
- art
- subjects
- animation
- posing
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: AP_resolve_temporal_movement_for_pose_or_sequence
tags:
- animation
- acting
- pantomime
- posing
- characterization
- staging
- story
- performance
cross_links:
- rel: supports
  target_object_id: PAT_characterize_story_figures_through_specific_behavior_and_evidence
- rel: supports
  target_object_id: PAT_design_animation_extreme_as_storytelling_pose
- rel: supports
  target_object_id: PAT_phrase_animation_timing_around_story_accents_and_action_beats
- rel: supports
  target_object_id: PAT_track_force_continuity_through_action
- rel: related_to
  target_object_id: DRILL_test_animation_acting_as_pantomime_without_supporting_channels
- rel: supports
  target_object_id: PAT_scale_visual_information_to_viewing_time_and_display_context
reference:
  source_title: Drawn to Life, Volume Two
  author: Walt Stanchfield
confidence: high
references: []
variants: []
---

# Prepare Animation Pantomime From Character and Situation

## Objective
Build a readable animated acting performance from the character's identity and present situation before polishing isolated poses, so each gesture has a reason, the action develops through meaningful states, and the performance can communicate without explanatory dialogue.

## Steps / Flow
1. **Define the character before inventing the performance.** Use `PAT_characterize_story_figures_through_specific_behavior_and_evidence` to establish the traits that materially affect acting: temperament, age, physical characteristics, habitual expression or movement, present mood, and distinguishing behavior. Use only traits that matter to the scene rather than loading the performance with biography that has no visible consequence.
2. **Define the acting situation.** Establish the necessary setting, prop relationships, clothing constraints, audience-facing staging, and what the character believes is happening. The situation must explain why the character is about to act.
3. **Choose an initial state and a change.** Give the character something to notice, want, fear, discover, resist, protect, pursue, or otherwise experience so the performance has a causal turn instead of becoming a string of unrelated gestures.
4. **Design one clear action or gesture at a time.** Use `PAT_design_animation_extreme_as_storytelling_pose` to make the decisive state communicate the current story idea, and use `PAT_track_force_continuity_through_action` to coordinate the whole body around it. Keep the primary statement simple and let secondary actions support the current idea rather than compete with it.
5. **Motivate the reaction sequence.** For cognitively driven reactions, let the internal decision precede the visible response; the eyes or gaze may lead the face and head before the larger body follows. Do not force this ordering onto reflexive, simultaneous, or deliberately abrupt actions.
6. **Give every movement a reason.** Ask whether each gesture clarifies who the character is, what they feel, what they want, or why they are acting. Remove motion that is merely decorative or generic.
7. **Stage the acting for the audience.** Keep important expressions, contacts, and actions visible. When shot scale or viewing distance may erase subtle acting, use `VAR_stanchfield_scale_animation_acting_to_final_viewing_distance` under `PAT_scale_visual_information_to_viewing_time_and_display_context` to calibrate the breadth of the performance.
8. **Phrase the performance.** Organize the acting into a beginning, progression or mood change, meaningful accent or climax, and conclusion. Use `PAT_phrase_animation_timing_around_story_accents_and_action_beats` when timing and temporal emphasis need explicit control.
9. **Preserve character through the ending.** Resolve the immediate acting problem without losing the character's established physical and behavioral identity. The final state should feel caused by the scene and performed by the same character who began it.
10. **Run the pantomime gate.** Use `DRILL_test_animation_acting_as_pantomime_without_supporting_channels` to remove dialogue and supporting channels temporarily. Repair pose, gaze, weight, silhouette, or phrasing if the body no longer communicates the intended performance.

## Notes
This AP constructs a pantomime performance; it is not the same as the pantomime Drill, which tests an already designed result. Stanchfield's source includes human acting and rehearsal advice, but the durable model-executable layer is the causal organization of character, situation, action, staging, and temporal phrasing. Dialogue may later enrich the performance, but it should not be required to explain basic body-language intent that the pose sequence is supposed to carry.

- Before choosing gestures, state what the character wants, why they want it, what they are doing to get it, and the single clear acting idea of the current beat. Technique serves that performance objective.
- Do one acting thing at a time clearly enough to read. Let thought, gaze, posture, task, and relationship progress through dialogue instead of freezing the body and animating only the mouth.
- Stage changes of thought where they can be read—before broad movement when thought should cause action, or just after when motion would otherwise hide the face. The mind is the pilot.
- Offset meaningful gesture from the matching spoken word when that separation gives each event more force. Symmetry may be useful for authority, order, or rhetorical certainty; break it when the acting needs asymmetry.
- Use gaze direction, small eye shifts, eyelids, and blinks as explicit evidence of changing attention rather than random “keep alive” motion.
