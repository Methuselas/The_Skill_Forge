---
object_id: PAT_construct_pacing_gait_from_alternating_same_side_limb_pairs
object_type: pattern
name: Construct a Pacing Gait From Alternating Same Side Limb Pairs
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
- pace
- gait
- lateral_support
- camel
- giraffe
- animation
cross_links: []
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Construct a Pacing Gait From Alternating Same Side Limb Pairs
## Pattern Rule
**IF** a quadruped is using a pacing gait
**THEN** coordinate the forelimb and hindlimb on the same side as a lateral pair, then alternate to the pair on the opposite side, instead of using the diagonal pairing of a trot

## Do
- Keep right fore and right hind mechanically related as one lateral pair, then left fore and left hind as the other.
- Let whole-body balance and side-to-side support respond to the same-side pairing.
- Treat pacing as a gait choice that may appear at particular speeds or in particular species rather than as a universal walk pattern.
- Verify whether the target species actually paces and how its timing changes with speed.

## Don't
- Do not mistake a pace for a trot; the pair relationship is different.
- Do not force same-side pairing onto species or speeds that use another gait.
- Do not isolate the legs from the trunk balance changes created by lateral support.

## Checklist
- Same-side fore and hind limbs move as identifiable pairs.
- The two lateral pairs alternate.
- Body balance agrees with the lateral support strategy.
- Species and speed applicability have been checked against reference.

## Notes
Pacing is mechanically distinctive because it groups limbs laterally rather than diagonally. Camel locomotion makes the contrast especially readable, and related same-side pairing can occur in other species such as giraffes. The exact timing remains reference-dependent.
