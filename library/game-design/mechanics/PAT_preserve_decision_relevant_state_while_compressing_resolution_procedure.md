---
object_id: PAT_preserve_decision_relevant_state_while_compressing_resolution_procedure
object_type: pattern
name: Preserve Decision-Relevant State While Compressing Resolution Procedure
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
- simulation
- state
- resolution
- abstraction
- operator-cost
- consequences
cross_links:
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: PAT_build_complete_resolution_procedures_incrementally
- rel: related_to
  target_object_id: PAT_expand_resolution_detail_only_after_consequential_state_change
reference:
  source_title: "Twilight: 2000 (1st Edition) and Twilight: 2000 Version 2.2"
  author: "Frank Chadwick; David Nilsen, Loren Wiseman, and Lester Smith"
confidence: high
references: []
variants: []
---

# Preserve Decision-Relevant State While Compressing Resolution Procedure

## Pattern Rule
**IF** several possible end states change later tactics, logistics, recovery, ownership, or other meaningful decisions
**THEN** preserve those differentiated end states while compressing intermediate causal resolution that is not needed after the state is known
**ELSE** simplify both the state and its derivation when the distinctions do not change future play.

## Do
- List the final states that produce different player choices before deciding how literally to simulate the process that creates them.
- Prefer categorical severity, lookup compression, precomputed mappings, or another bounded transformation when it can reach the same decision-relevant states with fewer human operations.
- Preserve component-specific or location-specific state when engine failure, fuel loss, limb loss, communications failure, weapon loss, or another result changes play differently.
- Trace what state survives the resolution and ask whether each intermediate calculation is ever consulted again.
- Compare the high-detail and compressed procedures by HOPR, TBMD, retrieval distance, and the decisions their outputs enable.
- When one declaration represents many simulated units, compress projectile, packet, target, or component generation separately from the consequence model; then test the maximum number of consequential results the second stage may still invoke.
- Prefer compressing **process before consequence** when the consequence state drives later play. A burst, chase, intrusion, injury, credential check, or identity verification can use a compact cause-resolution step while still preserving armor effects, damage type, wounds, evidence, positioning, recovery, burned access, or other downstream state.
- For paperwork- or data-heavy fictional systems, consider compressing the hidden supporting detail into a quality/rating while preserving meaningful failure state such as exposure, revocation, burned credentials, frozen access, or future investigation.

## Don't
- Collapse every differentiated failure into generic hit points solely because the original derivation is expensive.
- Assume a detailed fictional result requires a physically continuous step-by-step simulation of how it happened.
- Preserve intermediate quantities after they have served their only purpose of selecting a final state.
- Call a compressed procedure less simulationist when it preserves the state distinctions that drive later play.

## Checklist
- The final states that must remain distinct are named.
- Each retained state changes at least one later decision, capability, route, repair, recovery, or risk calculation.
- At least one intermediate operation can be removed or compressed without erasing a decision-relevant state.
- The compressed procedure has a bounded endpoint and does not simply relocate equivalent work into another high-frequency branch.
- The resulting state remains understandable enough that players can plan around it.
- A multi-hit or multi-packet branch has been stress-tested for whether consequence processing still scales faster than meaningful decisions after cause generation is compressed.

## Notes
The useful granularity of a simulation can live in its persistent output rather than in every causal step. A penetrating vehicle hit may need to leave a vehicle immobilized, disarmed, blind, low on fuel, or crew-degraded because those states create different future decisions. It does not follow that the table must trace the projectile through every internal component to obtain those outcomes. Treat output granularity and process granularity as separate design dimensions. A design can become substantially easier to operate by simplifying how an outcome is reached while leaving the decision-relevant aftermath intact. The same principle applies outside physical simulation: a forged identity can compress years of supporting records into one credibility rating if failure still burns the identity, invalidates linked permissions, or creates investigation state that changes later play.
