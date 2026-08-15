---
object_id: PAT_use_frame_sequence_reference_to_study_fast_action
object_type: pattern
name: Use Frame-Sequence Reference to Study Fast Action
library_path:
- art
- drawing
- foundations
- temporal-movement
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- motion_reference
- frame_sequence
- slow_motion
- animation
- action_analysis
cross_links:
- rel: related_to
  target_object_id: PAT_synthesize_temporal_movement_into_rhythmic_visual_pattern
- rel: related_to
  target_object_id: PAT_track_force_continuity_through_action
reference:
  source_id: ken_hultgren_art_of_animal_drawing
  source_title: The Art of Animal Drawing
  author: Ken Hultgren
  publish_date: Unknown
  media_type: book
  locator: u07, physical pp. 53-54; printed pp. 51-52
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_hultgren_find_extreme_animal_action_phases_in_slow_motion
  variant_name: Find Extreme Animal Action Phases in Slow Motion
  variant_basis: context
  source_id: ken_hultgren_art_of_animal_drawing
  source_title: The Art of Animal Drawing
  locator: u07, physical pp. 53-54; printed pp. 51-52
  difference_from_foundation: Applies frame-sequence study to animal locomotion, with special attention to support, extension, compression, reversal, and changing head-neck relationships that are difficult to isolate at normal speed.
  when_to_use: Use when fast animal action is being guessed from memory, reduced to a generic pose, or missing the extreme phase relationships that make the movement read.
  when_not_to_use: Do not turn one species, gait, lead, terrain, or speed sequence into a universal locomotion chart.
  absorbed_from_object_id: PAT_use_slow_motion_reference_to_find_extreme_animal_action_phases
- variant_id: VAR_dodson_use_freeze_frame_sequence_to_study_fleeting_human_action
  variant_name: Use Freeze-Frame Sequence to Study Fleeting Human Action
  variant_basis: context
  source_id: bert_dodson_keys_to_drawing
  source_title: Keys to Drawing
  locator: u08, physical pp. 216-217
  difference_from_foundation: Applies successive-frame study to human action captured through television, film, or comparable frame-based reference so brief movement states can be compared and reconstructed rather than guessed from ordinary observation.
  when_to_use: Use when a human action changes too quickly for reliable direct observation or memory and adjacent phases reveal informative differences in support, reach, timing, or silhouette.
  when_not_to_use: Do not copy one accidental frozen frame without checking the neighboring phases or rebuilding the pose through coherent anatomy and perspective.
  absorbed_from_object_id: none
---

# Use Frame-Sequence Reference to Study Fast Action

## Pattern Rule
**IF** a fast action cannot be reliably understood from ordinary observation or memory
**THEN** inspect a short run of successive frames around the event, compare how the structure changes from phase to phase, and reconstruct the informative states before inventing or polishing the final pose
**ELSE** use ordinary direct reference when the action is slow, stable, or already sufficiently understood.

## Do
- Inspect adjacent frames rather than choosing one attractive silhouette in isolation.
- Compare what changes: support, balance, compression, extension, joint position, body trajectory, head direction, limb reach, and overlap.
- Identify phases where a transition, extreme, reversal, impact, or support handoff becomes especially legible.
- Reconstruct the chosen phase through the relevant anatomy, construction, perspective, and FORCE foundations.
- Use the sequence to understand what came before and what follows the selected pose.
- Keep exact timing and species/action particulars bounded to appropriate reference.

## Don't
- Average two distant frames into a vague in-between pose and call that motion study.
- Treat one frozen frame as the entire truth of the action.
- Let frame capture replace structural validation.
- Generalize one person's or animal's exact timing into a universal rule without supporting evidence.

## Checklist
- The action was compared across successive frames.
- At least one meaningful phase change can be described.
- The selected pose is structurally coherent when reconstructed.
- Neighboring frames support the interpretation of the chosen phase.

## Notes
Hultgren first supplied the animal-motion owner through slow-motion deer sequences. Dodson independently demonstrates the same learner decision with fleeting human action captured across successive television/freezing states. That cross-subject evidence promotes the Pattern into shared temporal-movement foundations. The important method is not a particular medium: it is using a sequence of temporal samples to understand action that normal perception cannot isolate reliably.

`VAR_hultgren_find_extreme_animal_action_phases_in_slow_motion` preserves the animal-specific slow-motion route while keeping exact species and gait timing bounded to source evidence.

`VAR_dodson_use_freeze_frame_sequence_to_study_fleeting_human_action` supplies the human-action route and requires neighboring-frame comparison plus anatomical reconstruction rather than literal worship of a single frozen instant.
