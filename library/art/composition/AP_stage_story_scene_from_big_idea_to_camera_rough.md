---
object_id: AP_stage_story_scene_from_big_idea_to_camera_rough
object_type: ap
name: Stage a Story Scene from Big Idea to Camera Rough
library_path:
- art
- composition
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- storytelling
- staging
- illustration
- thumbnailing
- camera
- action
- environment
cross_links:
- rel: supports
  target_object_id: PAT_define_image_story_job_before_visualizing
- rel: supports
  target_object_id: PAT_choose_viewpoint_to_strengthen_story_effect
- rel: supports
  target_object_id: PAT_design_whole_picture_as_interlocking_shape_pattern
- rel: supports
  target_object_id: PAT_route_group_composition_through_directional_paths_and_accents
- rel: related_to
  target_object_id: AP_project_plan_and_elevation_into_perspective
- rel: related_to
  target_object_id: PAT_synthesize_visual_concepts_from_diverse_source_types
- rel: supports
  target_object_id: PAT_enrich_story_moment_with_plausible_unstated_specifics
- rel: supports
  target_object_id: PAT_use_thirds_to_break_static_equal_divisions
- rel: supports
  target_object_id: PAT_characterize_story_figures_through_specific_behavior_and_evidence
- rel: supports
  target_object_id: PAT_direct_reference_subject_through_story_state_not_feature_pose
- rel: supports
  target_object_id: PAT_design_depth_by_coordinating_spatial_cues
- rel: supports
  target_object_id: PAT_choose_viewer_participation_through_character_address
- rel: supports
  target_object_id: PAT_choose_line_and_shape_character_to_support_emotional_intent
- rel: supports
  target_object_id: PAT_resolve_unintended_tangencies_with_overlap_or_separation
- rel: supports
  target_object_id: PAT_stage_animal_mood_through_whole_body_pose_and_behavioral_cues
- rel: related_to
  target_object_id: AP_resolve_temporal_movement_for_pose_or_sequence
reference:
  source_title: Creative Illustration
  author: Andrew Loomis
confidence: high
references: []
variants: []
---

# Stage a Story Scene from Big Idea to Camera Rough

## Objective
Turn story or brief material into a staged, drawable scene by solving the communication job, action, spatial arrangement, and camera while each decision is still cheap to change.

## Steps / Flow
**Entry Conditions**
- A story, brief, scene concept, or communication objective exists.
- The image's story job can be stated or discovered before final reference is acquired.

**Persistent Invariants**
- The picture must serve the big idea rather than merely inventory available facts.
- Action and arrangement are designed before pose reference is allowed to dictate them.
- Camera choice and spatial staging are tested as design decisions before detailed construction.
- Character, setting, costume, props, and reference are selected for specific story jobs rather than accumulated indiscriminately.

**Flow**
1. **Define the image's communication job.** Apply `PAT_define_image_story_job_before_visualizing` at this decision. Decide what the picture must reveal, reinforce, or withhold.
2. **Read for the big idea.** Identify the central event or emotional proposition, mood, characters, setting, period/costume needs, important accessories, and facts that materially affect the scene.
3. **Search for plausible unstated specifics.** Apply `PAT_enrich_story_moment_with_plausible_unstated_specifics` at this decision. Ask what secondary actions, reactions, object behavior, environmental consequences, or before-and-after clues would reasonably exist in that moment; keep only those that strengthen the beat without contradicting or spoiling the story.
4. **Choose the staging emphasis.** Decide whether the image needs environment-heavy staging, interaction between figures, or a tighter gesture/expression emphasis.
5. **Invent the action cheaply.** Sketch tiny gesture, skeleton, or mass poses until the interaction and story beat work without depending on a model or photograph. When the beat depends on choosing a readable instant from a continuing or fast action, delegate that bounded decision to `AP_resolve_temporal_movement_for_pose_or_sequence` in single-pose mode. When an animal subject must communicate a specific mood or attitude before detail, apply `PAT_stage_animal_mood_through_whole_body_pose_and_behavioral_cues` so large posture and behavior carry the emotional read. When gaze, gesture, pose, or expression can make the audience part of the event, apply `PAT_choose_viewer_participation_through_character_address` so that relationship is deliberate. When a figure reads as generic or merely posed, apply `PAT_characterize_story_figures_through_specific_behavior_and_evidence` so behavior and a few concrete story facts clarify who that figure is in the moment.
6. **Map the scene when space matters.** Make a simple ground plan for figures, furniture, doors, major props, or other anchors; rotate or rearrange it to test what different camera directions reveal.
7. **Audition camera and eye level.** Apply `PAT_choose_viewpoint_to_strengthen_story_effect` at this decision. Compare several small views from different positions or heights while holding the same story beat constant.
8. **Project only as much perspective as needed.** Convert the selected arrangement into a small perspective or camera rough so major relationships can be checked before enlargement. When near/middle/far structure needs stronger communication, apply `PAT_design_depth_by_coordinating_spatial_cues` while leaving exact geometry and later optical rendering to their proper owners.
9. **Iterate the arrangement.** Apply `PAT_design_whole_picture_as_interlocking_shape_pattern`, `PAT_route_group_composition_through_directional_paths_and_accents`, and `PAT_use_thirds_to_break_static_equal_divisions` at this decision. When the dominant line/shape language does not support the intended emotional effect, apply `PAT_choose_line_and_shape_character_to_support_emotional_intent`; when independent shapes create an accidental kiss, false attachment, or false depth event, apply `PAT_resolve_unintended_tangencies_with_overlap_or_separation`. Turn, regroup, enlarge, crop, subordinate, or separate elements to strengthen story concentration, directional flow, hierarchy, and the whole shape pattern.
10. **Acquire or build reference after the conception exists.** Use models, photographs, studies, or factual research to make the chosen staging convincing rather than allowing reference to originate the scene by accident. When live or photographic figure reference must carry a specific emotion, intention, relationship, or dramatic state, apply `PAT_direct_reference_subject_through_story_state_not_feature_pose`: direct the subject through the story circumstance rather than manufacturing isolated facial features. Follow narrower subject-specific specializations, such as child-rapport methods, only when their IF conditions match.
11. **Select the rough that best serves the story job.** Preserve the chosen action, camera, and hierarchy as the basis for the next construction stage.

**Failure / Rollback Rules**
- If the rough is attractive but tells the wrong part of the story, return to the communication job before changing camera or rendering.
- If poses become stiff after reference acquisition, return to the pre-reference action sketch and rebuild the reference around it.
- If the scene feels spatially arbitrary, return to the ground plan and camera audition instead of nudging figures in screen space.
- If every element competes equally, return to the big idea and staging emphasis and remove or subordinate information that does not serve them.

**Completion Criteria**
- The image's narrative job and central story beat are explicit.
- Major action reads in small rough form before detailed anatomy or rendering.
- Important scene elements have a coherent spatial relationship and chosen camera.
- More than one arrangement or viewpoint was considered when the solution was not obvious.
- Subsequent reference acquisition has clear jobs and does not replace the designed conception.

## Notes
Loomis's staging sequence moves from story understanding and plausible narrative inference to rough action, ground-plan arrangement, camera/eye-level testing, and small perspective studies before model photography or finish. His examples show that the first layout is temporary: figures are turned, regrouped, resized, and recomposed until the scene concentrates both story and design. The reusable procedure is to solve narrative, action, space, and camera in inexpensive representations before committing expensive reference and rendering work.
