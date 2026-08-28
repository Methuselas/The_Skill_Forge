---
object_id: PAT_stabilize_head_through_compensating_neck_motion_during_locomotion
object_type: pattern
name: Stabilize the Head Through Compensating Neck Motion During Locomotion
library_path:
- art
- subjects
- animals
- gesture-locomotion
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_track_animal_motion_through_moving_pivots_and_overlapping_arcs
tags:
- animal_drawing
- locomotion
- head
- neck
- stabilization
- counter_motion
- animation
cross_links: []
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Stabilize the Head Through Compensating Neck Motion During Locomotion
## Pattern Rule
**IF** trunk motion during animal locomotion would make the head bob or pitch more than the observed action requires
**THEN** animate compensating motion through the neck so the head follows a comparatively stable trajectory while the body oscillates beneath it

## Do
- Track the head trajectory separately from the chest, back, and pelvis.
- Use neck flexion, extension, and counterrotation to absorb part of the body's rise, fall, pitch, or fore-aft rocking.
- Scale the compensation to neck length, gait, speed, and species rather than applying one fixed amount.
- Allow deliberate looking, feeding, striking, or other behavioral head actions to override stabilization when required.

## Don't
- Do not freeze the head absolutely in world space.
- Do not copy trunk oscillation directly into the skull when reference shows the neck compensating for it.
- Do not erase purposeful head movement in the name of stabilization.

## Checklist
- The head path is less erratic than the trunk path when the action calls for stabilization.
- Neck motion visibly accounts for the difference.
- The compensation preserves plausible articulation and range.
- Intentional head actions remain readable.

## Notes
Long-necked animals make the effect conspicuous, but the same principle can appear across many species: the body may rise, fall, pitch, or rock while the neck counteracts part of that movement. The useful target is relative head stability, not immobility.
