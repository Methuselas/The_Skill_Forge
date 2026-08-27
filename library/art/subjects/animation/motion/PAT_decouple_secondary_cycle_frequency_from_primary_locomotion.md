---
object_id: PAT_decouple_secondary_cycle_frequency_from_primary_locomotion
object_type: pattern
name: Decouple Secondary Cycle Frequency From Primary Locomotion
library_path:
- art
- subjects
- animation
- motion
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- cycle
- frequency
- locomotion
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants:
- variant_id: VAR_williams_layer_secondary_bounce_frequency_over_step_cycle
  variant_name: Layer Secondary Bounce Frequency Over the Step Cycle
  variant_basis: context
  difference_from_foundation: Specializes the general frequency-decoupling rule to a walk or run by keeping foot support and step timing readable while giving the torso, pelvis, head, or another body mass an additional rise-and-fall rhythm inside the same locomotion cycle; this preserves Williams's double-bounce / differing-body-timings idea without treating it as an independent owner.
  when_to_use: Use when the locomotion needs extra buoyancy, comic energy, weight character, or a deliberately more complex vertical rhythm while the step cycle itself remains the primary support structure.
  when_not_to_use: Do not add extra bounce merely to decorate a walk, and do not let the added rises and falls obscure contacts, weight transfer, or the intended gait.
  absorbed_from_object_id: PAT_layer_secondary_bounce_frequency_over_step_cycle
---

# Decouple Secondary Cycle Frequency From Primary Locomotion

## Pattern Rule
**IF** a secondary oscillation rides on locomotion but should not repeat at exactly the same frequency as the steps
**THEN** Let arms, head, or another secondary cyclic action repeat at a different frequency ratio from the primary leg cycle

## Do
- Define the primary locomotion period.
- Choose a secondary ratio such as faster, slower, or multi-beat.
- Test whether the combined cycles create the intended character without confusing support.

## Don't
- Do not assume every body cycle must repeat once per step.

## Checklist
- Primary and secondary rhythms remain legible and coordinated.

## Notes
`VAR_williams_layer_secondary_bounce_frequency_over_step_cycle` is the walk-specific specialization of this rule. Keep the support cycle authoritative, then let selected body masses rise and fall at an additional rhythm when that change serves the gait's character; it should never make the contact pattern or weight transfer ambiguous.
