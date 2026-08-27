---
object_id: PAT_choose_ones_twos_or_mixed_exposure_by_motion_need
object_type: pattern
name: Choose Ones Twos Or Mixed Exposure By Motion Need
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
foundation_object_id: none
tags:
- animation
- ones
- twos
- exposure
- timing
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants:
- variant_id: VAR_whitaker_correct_ping_pong_cycle_endpoint_exposure_bias
  variant_name: Correct Ping Pong Cycle Endpoint Exposure Bias
  variant_basis: method_sequence
  difference_from_foundation: Audits reversible forward-then-back cycles for duplicated near-extreme exposures that can make intermediate states appear to hold longer than the actual reversal positions, then adjusts endpoint duration or removes redundant repeated exposures.
  when_to_use: Use when the same drawing sequence is played forward and backward and the reversal feels mushy, biased toward a near-extreme, or perceptually weighted to the wrong position.
  when_not_to_use: Do not force symmetric exposure when the opening and closing phases should intentionally use different spacing or when the action is better redrawn rather than mechanically reversed.
  absorbed_from_object_id: none
---

# Choose Ones Twos Or Mixed Exposure By Motion Need

## Pattern Rule
**IF** choosing drawing exposure for an action requires balancing smoothness, speed, strobing risk, and production economy
**THEN** Choose unique-drawing frequency according to speed, smoothness, spacing, silhouette change, and readability rather than as a global stylistic rule

## Do
- Use fewer unique drawings when ordinary motion remains readable.
- Increase sampling for very fast, unusually smooth, or strobing motion.
- Mix ones and twos when different parts of the action need different temporal density.
- When animated motion must synchronize with independently sampled live-action or another continuously changing layer, use a compatible single-frame sampling rate where coarser exposure would create visible skipping or strobing.
- Judge exposure partly by the projected screen-space gap between successive unique states: increase sampling when fast travel creates disconnected jumps the eye cannot bridge.
- For very slow motion, allow longer exposures only when adjacent states remain close and accurately registered enough to avoid visible stepping; close views reveal jitter and inconsistency sooner than distant ones.
- Verify borderline exposure choices in playback at the intended shot scale rather than assuming that a cadence which works in one view will work in another.

## Don't
- Do not force an entire scene onto ones or twos regardless of motion need.
- Do not judge exposure only from the animated layer in isolation when it must remain phase-locked to another moving source.
- Do not reduce the decision to a global rule such as fast action always on ones or slow action always on longer holds; screen displacement, shot scale, registration accuracy, and readability all matter.

## Checklist
- Sampling density fits the actual movement and avoids unnecessary work or visible strobe.
- Synchronized moving layers advance at compatible temporal sampling without visible skip against one another.
- Consecutive unique states are close enough in screen space for the eye to connect them at the chosen cadence.
- Slow exposed motion remains stable rather than jittering, especially in close view.

## Notes
Exposure choice is a sampling decision, not only a drawing-count decision. A cadence that reads well by itself can fail when composited against independently changing motion, because held drawings visibly lag or jump relative to the continuously sampled layer.

`VAR_whitaker_correct_ping_pong_cycle_endpoint_exposure_bias` treats a ping-pong loop as an exposure-count problem as well as a drawing-order problem. When the same sequence reverses, near-extreme drawings can be duplicated across the turnaround and visually outweigh the true extreme; audit the accumulated holds at the reversal and compensate rather than assuming a simple forward/backward playback is neutral.
