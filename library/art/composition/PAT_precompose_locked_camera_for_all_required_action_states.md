---
object_id: PAT_precompose_locked_camera_for_all_required_action_states
object_type: pattern
name: Precompose Locked Camera For All Required Action States
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
- locked_camera
- blocking
- storyboarding
- composition
cross_links:
- rel: related_to
  target_object_id: PAT_preserve_readable_composition_through_camera_motion
reference:
  source_title: 'Framed Ink: Drawing & Composition for Visual Storytellers'
  author: Marcos Mateu-Mestre
confidence: high
references: []
variants:
- variant_id: VAR_bluth_cover_dialogue_acting_beat_with_one_readable_view_before_multiplying_cuts
  variant_name: Cover a Dialogue or Acting Beat With One Readable View Before Multiplying Cuts
  variant_basis: context
  difference_from_foundation: >-
    Extends locked-camera precomposition into storyboard coverage: search first for a viewpoint that keeps the important faces and reactions visible, separates character silhouettes, preserves the spatial relationship, and lets the acting exchange play clearly from one setup. Add reaction cuts only when they create stronger emotional or informational emphasis rather than compensating for a weak base angle.
  when_to_use: >-
    Use when a two-character or small-group dialogue/acting beat is becoming needlessly cutty, especially when the important reactions could potentially coexist in one clear setup.
  when_not_to_use: >-
    Do not force one shot to carry a beat when a dedicated close-up, reaction, reveal, or point-of-view change genuinely adds necessary information or emotional emphasis.
  absorbed_from_object_id: none
---

# Precompose Locked Camera For All Required Action States

## Pattern Rule
**IF** one fixed camera must contain several required action states without losing readability at any point
**THEN** When the camera stays fixed, choose a framing that keeps every required entrance, exit, overlap, pose, and interaction readable across the full action

## Do
- List the important action states before locking the frame.
- Test each state inside the same camera.
- Adjust blocking or framing until no required beat falls outside the readable composition.

## Don't
- Do not compose only the opening pose of a locked shot.

## Checklist
- All required action states read from the same viewpoint.

## Notes
`VAR_bluth_cover_dialogue_acting_beat_with_one_readable_view_before_multiplying_cuts` applies the locked-camera test specifically to storyboard coverage of dialogue or acting beats: find a base view that keeps the necessary reactions readable and silhouettes separated before multiplying reaction cuts. Use separate shots when they genuinely add emphasis or information rather than merely repairing a weak base setup.
