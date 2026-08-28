---
object_id: PAT_use_frame_sequence_reference_to_study_fast_action
object_type: pattern
name: Use Frame-Sequence Reference to Study Fast Action
library_path:
- art
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
  source_title: The Art of Animal Drawing
  author: Ken Hultgren
confidence: high
references: []
variants:
- variant_id: VAR_hultgren_find_extreme_animal_action_phases_in_slow_motion
  variant_name: Find Extreme Animal Action Phases in Slow Motion
  variant_basis: context
  difference_from_foundation: Applies frame-sequence study to animal locomotion, with special attention to support, extension,
    compression, reversal, and changing head-neck relationships that are difficult to isolate at normal speed.
  when_to_use: Use when fast animal action is being guessed from memory, reduced to a generic pose, or missing the extreme
    phase relationships that make the movement read.
  when_not_to_use: Do not turn one species, gait, lead, terrain, or speed sequence into a universal locomotion chart.
  absorbed_from_object_id: PAT_use_slow_motion_reference_to_find_extreme_animal_action_phases
- variant_id: VAR_dodson_use_freeze_frame_sequence_to_study_fleeting_human_action
  variant_name: Use Freeze-Frame Sequence to Study Fleeting Human Action
  variant_basis: context
  difference_from_foundation: Applies successive-frame study to human action captured through television, film, or comparable
    frame-based reference so brief movement states can be compared and reconstructed rather than guessed from ordinary observation.
  when_to_use: Use when a human action changes too quickly for reliable direct observation or memory and adjacent phases reveal
    informative differences in support, reach, timing, or silhouette.
  when_not_to_use: Do not copy one accidental frozen frame without checking the neighboring phases or rebuilding the pose
    through coherent anatomy and perspective.
  absorbed_from_object_id: none
- variant_id: VAR_webster_match_recording_rate_to_action_speed_and_analysis_question
  variant_name: Match Recording Rate to Action Speed and the Analysis Question
  variant_basis: method_sequence
  difference_from_foundation: Extends frame-sequence analysis upstream into capture by choosing temporal sampling dense enough
    to reveal the event being studied while preserving real-time playback as the authority for the action's actual timing and dynamic.
  when_to_use: Use when you control the recording and a fast, brief, or complex event would lose critical phases at an ordinary
    sampling rate.
  when_not_to_use: Do not assume a higher recording rate is automatically better; oversampled slow playback can obscure the
    overall dynamic, and real-time viewing remains necessary to judge the action's true speed.
  absorbed_from_object_id: none
- variant_id: VAR_webster_register_successive_states_in_shared_frame_to_expose_displacement
  variant_name: Register Successive States in a Shared Frame to Expose Displacement
  variant_basis: method_sequence
  difference_from_foundation: Places successive captured states into one stable coordinate frame so spacing, direction, path,
    and landmark displacement can be compared directly instead of mentally registered across separate images.
  when_to_use: Use when trajectories, spacing, or relative landmark displacement remain difficult to compare across separate
    frames and a registered composite or chronophotographic view would make the motion clearer.
  when_not_to_use: Do not treat the composite as a final animation drawing or allow overlapping states to replace anatomical,
    timing, or perspective analysis of the individual phases.
  absorbed_from_object_id: none
- variant_id: VAR_webster_analyze_recorded_action_from_whole_to_parts_to_whole
  variant_name: Analyze Recorded Action From Whole to Parts to Whole
  variant_basis: method_sequence
  difference_from_foundation: "Extends frame-sequence study into a full analysis cycle: define the action span, establish the real-time whole, isolate timing and causal layers frame by frame, then return to normal-speed playback to judge how the parts recombine."
  when_to_use: Use when recorded action is complex enough that isolated frames or one analytical pass do not reveal how timing, primary action, subordinate motion, and phase changes work together.
  when_not_to_use: Do not stay trapped in frame-by-frame dissection; the analysis is incomplete until the reconstructed understanding survives a return to the whole action at real speed.
  absorbed_from_object_id: none
---

# Use Frame-Sequence Reference to Study Fast Action

## Pattern Rule
**IF** a fast action cannot be reliably understood from ordinary observation or memory
**THEN** inspect a short run of successive frames around the event, compare how the structure changes from phase to phase, and reconstruct the informative states before inventing or polishing the final pose
**ELSE** use ordinary direct reference when the action is slow, stable, or already sufficiently understood.

## Do
- Inspect adjacent frames rather than choosing one attractive silhouette in isolation.
- Begin with the action at normal speed to understand the whole event, then slow or single-frame it and isolate individual components while continually relating them back to the complete movement.
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

- Before stylizing reference, extract the motion invariants that repeat beneath surface variation: contact order, support, high/low phases, weight transfer, stride timing, characteristic delays, and changing masses. Adapt those invariants to the design rather than copying every frame literally.
`VAR_webster_match_recording_rate_to_action_speed_and_analysis_question` adds the capture-side sampling decision. Record densely enough to expose fleeting phases when needed, but return to real-time playback to preserve the action's actual rhythm and timing authority.

`VAR_webster_register_successive_states_in_shared_frame_to_expose_displacement` adds a registered-comparison route: successive states can be overlaid or captured into a shared frame to make spacing, trajectory, and landmark displacement directly visible.

`VAR_webster_analyze_recorded_action_from_whole_to_parts_to_whole` adds Webster's complete deconstruction/reassembly pass: start from the whole event at normal speed, isolate timing, phases, and causal motion hierarchies only as needed, then return to real-time playback so local findings are judged inside the original dynamic.
