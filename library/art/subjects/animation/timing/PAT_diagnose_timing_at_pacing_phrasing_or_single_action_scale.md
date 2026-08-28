---
object_id: PAT_diagnose_timing_at_pacing_phrasing_or_single_action_scale
object_type: pattern
name: Diagnose Timing at Pacing Phrasing or Single Action Scale
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
foundation_object_id: PAT_phrase_animation_timing_around_story_accents_and_action_beats
tags:
- animation
- timing
- pacing
- phrasing
- sequence
- performance
- diagnosis
cross_links:
- rel: related_to
  target_object_id: PAT_separate_timing_from_spacing_when_designing_motion
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Diagnose Timing at Pacing Phrasing or Single Action Scale
## Pattern Rule
**IF** a sequence feels too slow, too even, poorly accented, or mechanically mistimed
**THEN** locate the problem at the correct scale—pacing, phrasing, or single-action timing—before changing frames or spacing

## Do
- Diagnose **pacing** at the narrative or sequence scale: how faster and slower passages shape tension, mood, action, intimacy, and overall progression.
- Diagnose **phrasing** across a short series of related actions: how fast, medium, slow, pause, change of thought, and behavioral shift combine into performance.
- After identifying the actions in a phrase, inspect **how they connect**: gradual transition, abrupt switch, or a distinct linking action. Treat quieter intervals as active timing when they contain balance shifts, preparation, thought, or low-energy motion, and track where emphasis migrates across the sequence.
- Diagnose **single-action timing** at the level of one movement: its duration, acceleration, deceleration, and local temporal behavior.
- Fix the smallest scale that actually owns the failure, then recheck the larger scales for knock-on effects.

## Don't
- Do not repair a sluggish sequence only by changing the spacing of one gesture.
- Do not globally shorten a scene when the real problem is monotonous phrasing among its actions.
- Do not use a universal frame count as a substitute for context-appropriate timing.

## Checklist
- The timing failure has been assigned to one of the three scales.
- The proposed edit operates at that same scale.
- Phrasing contains meaningful variation when performance requires it.
- Transitions and low-energy intervals have been judged rather than ignored as empty gaps.
- Local timing changes still support the sequence's larger pacing.

## Notes
Timing problems look similar from the audience side but occur at different structural levels. Separating narrative pacing, action phrasing, and the timing of a single movement turns "the timing feels wrong" into a more precise repair decision.

Webster's systematic-analysis pass adds a useful phrasing diagnostic: once the major actions are named, the animator should also inspect the transitions and quieter intervals between them. Those regions often carry preparation, balance, thought, or shifting emphasis and therefore need timing decisions of their own.
