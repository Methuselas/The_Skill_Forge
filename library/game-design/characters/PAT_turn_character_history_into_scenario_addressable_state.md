---
object_id: PAT_turn_character_history_into_scenario_addressable_state
object_type: pattern
name: Turn Character History into Scenario-Addressable State
library_path:
- game-design
- characters
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- characters
- lifepath
- backstory
- campaign-state
- hooks
cross_links:
- rel: related_to
  target_object_id: PAT_generate_sandbox_situations_from_world_state_and_player_needs
- rel: related_to
  target_object_id: PAT_express_faction_power_as_deployable_response_capacity
- rel: related_to
  target_object_id: PAT_derive_character_capabilities_from_expected_play
reference:
  source_title: Cyberpunk 2020 (2.0.2.0 Version)
  author: Mike Pondsmith and R. Talsorian Games contributors
confidence: high
references: []
variants: []
---

# Turn Character History into Scenario-Addressable State

## Pattern Rule
**IF** character generation spends procedure on history, relationships, victories, disasters, enemies, debts, or obligations
**THEN** let those outputs survive creation as unresolved state the campaign can later activate
**ELSE** keep biography generation lightweight when the result will not affect future play.

## Do
- Record the smallest useful handle for a future situation: who or what is involved, what remains unresolved, what the other side wants, and what resources or leverage can be brought to bear.
- Let history leave present residue such as debt, injury, institutional attention, a loyal contact, an enemy, an unresolved relationship, a reputation, or an obligation.
- Preserve open loops rather than resolving every generated event into closed prose.
- Let players adapt or reject random prompts that fundamentally contradict the intended character; randomness should create discovery, not confiscate authorship.
- Promote a lightweight relationship or antagonist to richer state only after play makes it recurring or important.

## Don't
- Spend several tables generating facts that the referee has no practical way to reactivate.
- Treat an enemy as useful campaign state without knowing at least what it wants or what it can plausibly do.
- Require full NPC construction for every generated relationship before that relationship enters active play.
- Confuse a long biography with a large number of playable hooks.

## Checklist
- At least one background result can create a future scene without inventing a new reason for it to matter.
- Enemies and institutions have enough response capacity to act when activated.
- Friends and relationships can be contacted, threatened, owed, or otherwise interacted with.
- Random generation produces editable prompts rather than immutable character facts.
- The campaign has a way to remember dormant state until it becomes relevant.

## Notes
Backstory earns its operating cost when the past leaves state in the present. An unresolved lover, corporate enemy, debt, injury, mentor, or obligation is not merely characterization; it is an address the campaign can call later. This trades blank-page scenario invention for continuity management, which is often worthwhile because the stored pressure is already connected to player investment.
