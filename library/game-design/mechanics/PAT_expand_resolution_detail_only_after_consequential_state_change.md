---
object_id: PAT_expand_resolution_detail_only_after_consequential_state_change
object_type: pattern
name: Expand Resolution Detail Only After Consequential State Change
library_path:
- game-design
- mechanics
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- mechanics
- resolution
- complexity
- consequences
- operator-cost
cross_links:
- rel: related_to
  target_object_id: PAT_invoke_resolution_only_for_meaningful_uncertainty
- rel: related_to
  target_object_id: PAT_preserve_decision_relevant_state_while_compressing_resolution_procedure
- rel: related_to
  target_object_id: DRILL_profile_serial_resolution_latency
reference:
  source_title: Cyberpunk 2020 (2.0.2.0 Version)
  author: Mike Pondsmith and R. Talsorian Games contributors
confidence: high
references: []
variants: []
---

# Expand Resolution Detail Only After Consequential State Change

## Pattern Rule
**IF** an attempted action has a cheap branch where no consequential state changes and a richer branch where success or failure creates persistent effects
**THEN** keep the common attempt path shallow and invoke detailed consequence processing only after the state-changing branch is reached
**ELSE** use one bounded procedure when every outcome requires the same meaningful state update.

## Do
- Make misses, harmless failures, or other no-change outcomes terminate quickly.
- Put location, severity, equipment interaction, impairment, or other detailed processing behind the event that makes those distinctions relevant.
- Precompute high-frequency values that change slowly, such as resistance, armor coverage, derived modifiers, or thresholds, and surface them at the point of play.
- Stop resolving additional sub-events when they no longer change any decision-relevant final state, unless the remaining state is explicitly important to later recovery, ownership, or campaign consequences.
- When one declaration can generate many consequences, compress event generation separately from consequence resolution and measure the maximum consequential hit/packet count.

## Don't
- Pay full consequence-processing cost for every failed attempt merely because the successful branch is detailed.
- Assume a cheap single-event procedure remains cheap when another rule can invoke it ten times inside one action.
- Continue tracing intermediate quantities after they have ceased to alter final state.
- Hide frequently consulted stable values behind repeated recalculation or rulebook lookup.

## Checklist
- The cheapest ordinary no-change path has a clear early exit.
- Detailed resolution begins at a named state-changing trigger.
- Stable high-frequency values are precomputed or immediately accessible.
- Multi-event actions have been tested at realistic maximum output rather than one event at a time.
- The procedure terminates when further detail no longer changes future decisions or persistent consequences.

## Notes
Simulation detail can be asymmetric. An attack roll may be cheap while a successful hit opens location, protection, injury, shock, and recovery state. That is efficient when the detailed branch fires only when something changed. The same architecture becomes expensive when burst, area, or multi-target rules multiply the consequence branch, so success-triggered expansion must still be tested at real cadence.
