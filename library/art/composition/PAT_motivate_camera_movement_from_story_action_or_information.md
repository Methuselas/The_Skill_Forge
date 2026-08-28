---
object_id: PAT_motivate_camera_movement_from_story_action_or_information
object_type: pattern
name: Motivate Camera Movement From Story Action Or Information
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
- camera_move
- storytelling
- staging
- animation
cross_links:
- rel: related_to
  target_object_id: PAT_choose_viewpoint_to_strengthen_story_effect
reference:
  source_title: 'Framed Ink: Drawing & Composition for Visual Storytellers'
  author: Marcos Mateu-Mestre
confidence: high
references: []
variants:
- variant_id: VAR_byrne_use_camera_shake_as_brief_directional_impact_accent
  variant_name: Use Camera Shake As A Brief Directional Impact Accent
  variant_basis: context
  difference_from_foundation: "Adds Byrne's impact-specific camera behavior: when a collision, explosion, stampede, or other event genuinely transfers apparent force to the camera, derive the dominant shake axis from the event, allow smaller secondary-axis displacement, keep the disturbance brief unless the cause persists, and preserve enough scene margin that the move cannot expose the artwork boundary."
  when_to_use: "Use when a real story event justifies a momentary camera disturbance that should reinforce the direction and force of impact."
  when_not_to_use: "Do not add shake as generic excitement, do not let it obscure the story action, and do not preserve source-specific fielding values or rostrum-camera measurements as universal settings."
  absorbed_from_object_id: none
- variant_id: VAR_byrne_tune_camera_move_speed_to_emotional_beat
  variant_name: Tune Camera-Move Speed To The Emotional Beat
  variant_basis: context
  difference_from_foundation: "Adds Byrne's speed-as-story control after a move is already motivated: choose the move's duration and acceleration to reinforce the intended audience response. A slow move away can let reflection or release linger, a slow move toward can increase involvement or intimacy progressively, and a fast move toward can heighten urgency, danger, surprise, or excitement. The mapping is contextual rather than formulaic."
  when_to_use: "Use after the camera move has a legitimate story or information reason and its speed can materially reinforce the emotional beat."
  when_not_to_use: "Do not move the camera merely because an emotional beat exists, do not use fixed formulas such as 'slow equals sad' or 'fast equals exciting,' and do not let camera behavior substitute for weak staging or performance."
  absorbed_from_object_id: none
---

# Motivate Camera Movement From Story Action Or Information

## Pattern Rule
**IF** a camera move is being considered and needs a story, attention, or information reason to exist
**THEN** Move the camera because action, attention, information, or emotional emphasis requires the frame to change

## Do
- Let character travel, gaze, discovery, or a coming reveal pull the camera.
- Define what new information the move earns.
- Stop or redirect the move when the narrative reason ends.

## Don't
- Do not move the camera only to make a shot feel busy or expensive.

## Checklist
- The movement has a clear story trigger and payoff.

## Notes
Byrne's camera-shake diagrams are a bounded impact case of the same motivation rule: a vertical impact produces primarily vertical disturbance, a lateral collision primarily lateral disturbance, with smaller secondary displacement and sufficient overscan/safe margin to keep artwork edges out of frame. Preserve motivated directional disturbance, not historical fielding values. Byrne's timing examples add a second bounded control: once a move is justified, its speed can reinforce the emotional beat, but only as support for the story and performance rather than as a canned emotion effect.

Retained bounded variants: `VAR_byrne_use_camera_shake_as_brief_directional_impact_accent`; `VAR_byrne_tune_camera_move_speed_to_emotional_beat`.
