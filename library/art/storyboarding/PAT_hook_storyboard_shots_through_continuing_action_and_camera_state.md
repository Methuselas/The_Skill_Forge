---
object_id: PAT_hook_storyboard_shots_through_continuing_action_and_camera_state
object_type: pattern
name: Hook Storyboard Shots Through Continuing Action and Camera State
library_path:
- art
- storyboarding
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
- storyboarding
- continuity
- cutting
- camera
- action
- hookup
cross_links:
- rel: related_to
  target_object_id: PAT_match_action_state_across_shot_boundaries
- rel: related_to
  target_object_id: PAT_preserve_screen_geography_with_axis_of_action
- rel: related_to
  target_object_id: PAT_motivate_camera_movement_from_story_action_or_information
- rel: supports
  target_object_id: AP_develop_storyboard_sequence_in_progressive_directing_passes
reference:
  source_title: The Art of Storyboard
  author: Don Bluth
confidence: high
references: []
variants: []
---

# Hook Storyboard Shots Through Continuing Action and Camera State

## Pattern Rule
**IF** a storyboard cut occurs while character action, prop motion, or camera movement is still continuing
**THEN** design the outgoing and incoming shots as two views of one uninterrupted event by carrying forward the relevant action phase, apparent speed, direction, spatial state, and camera state instead of restarting or nearly duplicating the movement
**ELSE** allow a clean state change when the cut intentionally jumps time, location, or action.

## Do
- Compare the last readable state of the outgoing shot with the first readable state of the incoming shot before approving the cut.
- Advance continuing body and prop action across the cut rather than repeating the outgoing pose as the opening pose of the next shot.
- Preserve the apparent speed and phase of continuing action so a sword swing, run, reach, fall, or other movement does not visibly restart after the cut.
- Preserve intended screen direction and spatial relationships while changing viewpoint; use `PAT_preserve_screen_geography_with_axis_of_action` when the cut could reverse the interaction or travel direction.
- If a camera move is active at the cut, either continue that camera state coherently into the incoming shot or complete/bridge the move before changing camera behavior.
- Make a new viewpoint different enough to earn the cut. If two framings are nearly the same without a clear story reason, reconsider whether the change will read as an accidental jump.
- Flag unintended changes in background color, mood, lighting, or other environmental state when the location is meant to remain continuous and route them to the appropriate color/lighting owner.

## Don't
- Do not reset a continuing action merely because a new drawing or shot begins.
- Do not repeat the same body position on both sides of a cut when the event is supposed to be advancing continuously.
- Do not stop a camera move at the edit point and begin the next shot with an unrelated static camera unless the interruption is deliberate and readable.
- Do not use a tiny unexplained change in camera position as a substitute for a meaningful new shot.
- Do not preserve continuity mechanically when the story intentionally uses a discontinuity, time jump, or disorienting cut.

## Checklist
- The action reads as one event rather than two separately posed illustrations.
- Direction, phase, and apparent velocity remain believable across the boundary.
- The incoming shot advances the event or information instead of redundantly repeating the outgoing shot.
- Any continuing camera move has a coherent state across the cut or a readable completion before the new camera behavior begins.
- The new viewpoint is sufficiently motivated and distinct to read as an intentional cut.
- Environmental continuity does not jump accidentally when the location and time are meant to remain continuous.

## Notes
Bluth describes a storyboard "hook-up" as a shot transition that minimizes the audience's awareness of the camera change while the action itself continues. His Dirk examples preserve the sword swing and running speed through cuts, while his near-duplicate sneaking views demonstrate how a small unexplained camera shift can read as an accidental jump. This Pattern owns the storyboard-stage decision of where to cut and what continuing action and camera state the incoming board must inherit. It differs from `PAT_match_action_state_across_shot_boundaries`, which governs the animator's downstream character/prop continuity after shot design is established.
