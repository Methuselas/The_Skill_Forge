---
object_id: PAT_construct_trot_from_alternating_diagonal_limb_pairs_and_suspension
object_type: pattern
name: Construct a Trot From Alternating Diagonal Limb Pairs and Suspension
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
foundation_object_id: PAT_read_quadruped_locomotion_from_support_swing_and_suspension_phases
tags:
- animal_drawing
- quadruped
- trot
- gait
- diagonal_support
- suspension
- animation
cross_links: []
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Construct a Trot From Alternating Diagonal Limb Pairs and Suspension
## Pattern Rule
**IF** a quadruped movement is intended to read specifically as a trot
**THEN** organize support around alternating diagonal limb pairs, with one forelimb and the opposite hindlimb acting as a pair before the opposite diagonal pair takes over, and include suspension where the species and speed show it

## Do
- Track the right-fore/left-hind pair against the left-fore/right-hind pair rather than treating all four legs independently.
- Make the handoff between diagonal pairs readable through support, thrust, recovery, and any suspension phase.
- Preserve coherent chest and pelvis motion while the paired contacts alternate.
- Verify exact timing, suspension duration, and species-specific variation from reference.

## Don't
- Do not confuse the diagonal pairing of a trot with the same-side pairing of a pace.
- Do not impose one exact frame chart on every quadruped or speed.
- Do not add suspension as a decorative speed symbol when the actual gait does not show it.

## Checklist
- Opposite fore and hind limbs are paired diagonally.
- The diagonal pairs alternate coherently.
- Any suspension sits between plausible departure and reception phases.
- Torso and support changes agree with the limb pairing.

## Notes
The diagonal pair is the defining structural cue. Exact phase counts vary, so the durable animation rule is the relationship among paired support, thrust, suspension, and reception rather than a memorized timing chart.
