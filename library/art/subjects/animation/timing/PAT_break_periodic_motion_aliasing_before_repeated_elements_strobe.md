---
object_id: PAT_break_periodic_motion_aliasing_before_repeated_elements_strobe
object_type: pattern
name: Break Periodic Motion Aliasing Before Repeated Elements Strobe
library_path:
- art
- subjects
- animation
- timing
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_choose_ones_twos_or_mixed_exposure_by_motion_need
tags:
- animation
- timing
- aliasing
- strobing
- repeated_elements
- sampling
- rotation
cross_links:
- rel: related_to
  target_object_id: PAT_use_elongated_inbetween_to_imply_fast_motion_blur
reference:
  source_title: Timing for Animation
  author: Harold Whitaker and John Halas
confidence: high
references: []
variants:
- variant_id: VAR_blair_break_fast_cycle_aliasing_with_distinct_successive_action_silhouettes
  variant_name: Break Fast Cycle Aliasing With Distinct Successive Action Silhouettes
  variant_basis: context
  difference_from_foundation: Extends periodic-aliasing control from repeated graphic motifs to fast character cycles, where neighboring locomotion or action states can become perceptually interchangeable if whole-body silhouettes or limb correspondences repeat too closely in time.
  when_to_use: Use in very fast locomotion or repeated character action when playback creates strobe, false reversal, or ambiguous limb correspondence even though each drawing is individually valid.
  when_not_to_use: Do not randomize limbs, violate support/contact order, or change a mechanically clear repeated silhouette merely for variety; preserve the actual gait and intervene only when temporal sampling creates perceptual ambiguity.
  absorbed_from_object_id: none
---

# Break Periodic Motion Aliasing Before Repeated Elements Strobe

## Pattern Rule
**IF** repeated similar elements such as spokes, rungs, stripes, fence posts, or background intervals advance by a screen-space amount that makes successive samples perceptually interchangeable
**THEN** compare per-frame displacement with the repeated motif spacing and change the sampling, speed, spacing, landmark design, or fast-motion treatment until playback preserves the intended direction and continuity
**ELSE** leave the repetition intact when successive states remain easy to correspond and no false reversal, flicker, or stationary pattern appears.

## Do
- Identify the repeated interval that the eye is likely to use for correspondence; judge the risk against that interval rather than against object speed alone.
- Test the motion in playback, because a mathematically consistent wheel or pan can still look reversed, frozen, or flickery after temporal sampling.
- Increase temporal sampling or alter speed when the repeated states are too ambiguous at the current cadence.
- Change motif spacing or introduce a distinctive irregular landmark when preserving the exact speed matters more than preserving perfectly uniform repetition.
- When individual repeated detail is moving too fast to track honestly, simplify it into a directional blur or other fast-motion treatment instead of insisting that every repeated element remain separately readable.
- Apply the same check to moving backgrounds and camera-relative translation, not only to rotating wheels.

## Don't
- Do not assume that correct frame-by-frame geometry guarantees correct perceived direction in playback.
- Do not preserve perfectly uniform repeated detail when that uniformity is what makes one sampled state indistinguishable from another.
- Do not memorize one fixed safe fraction of motif spacing as a universal threshold across frame rates, shot scales, speeds, and designs.
- Do not repair a false reversal by adding arbitrary jitter that introduces a different continuity error.

## Checklist
- Repeated elements have an unambiguous correspondence or are intentionally simplified when they move too fast to track.
- Playback does not create unintended reversal, stationary repetition, or rhythmic flicker.
- The chosen correction preserves the intended carrier motion and does not add a new distracting beat.
- Any landmark or spacing irregularity used to break aliasing still belongs to the design.

## Notes
Whitaker and Halas show the familiar backward-wheel problem as a temporal sampling failure: when similar repeated elements advance by an unfortunate fraction of their spacing, the eye can match each new sample to the wrong neighbor. The same ambiguity can make ladder rungs, fence posts, or regularly spaced background marks flicker or appear stationary during motion. The durable decision is therefore relational: compare displacement to repetition spacing, inspect the actual playback, and break the ambiguous correspondence before finalizing. Their numerical examples illustrate the phenomenon but are not universal production constants.

**Blair fast-cycle silhouette variant — `VAR_blair_break_fast_cycle_aliasing_with_distinct_successive_action_silhouettes`.** In fast locomotion or repeated action, inspect neighboring unique drawings for near-identical whole-body silhouettes or limb correspondences that let the eye match the wrong state across frames. Where the mechanics allow it, vary legitimate limb extension, recovery, grouping, or phase presentation enough to keep successive samples distinct while preserving the real support sequence. Judge the fix in playback; do not introduce arbitrary variation when the cycle already reads clearly.
