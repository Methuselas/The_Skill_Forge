---
object_id: AP_resolve_temporal_movement_for_pose_or_sequence
object_type: ap
name: Resolve Temporal Movement for a Pose or Sequence
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
- movement
- pose
- action_analysis
- key_pose
- sequential_art
- storyboards
- animation
cross_links:
- rel: supports
  target_object_id: PAT_use_frame_sequence_reference_to_study_fast_action
- rel: supports
  target_object_id: PAT_track_force_continuity_through_action
- rel: supports
  target_object_id: PAT_synthesize_temporal_movement_into_rhythmic_visual_pattern
reference:
  source_title: PASS Art canonical synthesis
  author: Multiple accepted sources
confidence: high
references: []
variants: []
---

# Resolve Temporal Movement for a Pose or Sequence

## Objective
Understand an action as an event unfolding through time, then resolve only the temporal information the current task needs: a strong single pose/key pose, a short readable sequence, or an analysis that can be handed back to another Art workflow.

## Steps / Flow
1. **Enter only when time changes the drawing problem.** Use this AP when the action cannot be solved honestly as one static structural state because phase, anticipation, support transfer, reversal, impact, recovery, or overlapping motion matters. If the task is genuinely static, return to the caller without adding temporal machinery.
2. **Choose the required temporal resolution.** Decide whether the caller needs one pose/key instant, several ordered poses or panels, or only enough action analysis to support another workflow. Do not expand a single-image task into a sequence, and do not collapse a sequence into one attractive pose when the changing states are the point.
3. **Recover the event when ordinary observation is insufficient.** Apply `PAT_use_frame_sequence_reference_to_study_fast_action` when fast or fleeting action cannot be understood reliably from one observation, one frozen image, or memory. Compare adjacent states and reconstruct what materially changes before choosing the useful phase or phases.
4. **Establish physical continuity through the event.** Apply `PAT_track_force_continuity_through_action` at this decision. Identify what action is coming from, what support/contact/resistance redirects it, and where the event continues next. When an applicable subject-specific temporal specialization exists, follow that specialization only after this general event is understood.
5. **Branch by deliverable.** For a single still or key pose, apply `PAT_synthesize_temporal_movement_into_rhythmic_visual_pattern` so the chosen instant carries evidence of the action before and after it without becoming a collage of contradictory phases. For an ordered sequence, preserve distinct phase states and their causal order; do not average them into similar poses merely for visual smoothness.
6. **Keep connected parts temporally coherent.** Different body parts or attached structures may lead, lag, reverse, overlap, or recover at different times, but each state must remain traceable to the same articulated event rather than behaving as an unrelated decorative arc.
7. **Check the requested level, not the maximum possible level.** A pose/illustration caller may need only the strongest readable instant. A comic or storyboard caller may need selected beats. Animation may later require deeper timing, spacing, breakdown, and in-between decisions that this AP does not invent when those owners are absent.
8. **Return the temporal solution to the caller.** Hand back the selected pose, ordered phase logic, or action analysis while preserving the caller's own stage, medium, composition, character, and finish ceilings. This AP resolves motion timing/phase relationships; it does not take ownership of the entire artwork.

## Notes
Temporal movement is intentionally shared knowledge. Illustration and pose work may call this AP to select or strengthen one instant; comics and storyboards may call it to preserve meaningful state changes across panels or shots; animation may use the same foundation before deeper animation-specific timing and in-between workflows. Sharing this AP does not collapse those categories into one workflow. The caller determines how much temporal resolution is needed and what happens after the motion decision returns.
