---
object_id: PAT_allocate_simulation_detail_by_expected_persistence
object_type: pattern
name: Allocate Simulation Detail by Expected Persistence
library_path:
- game-design
- foundations
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- simulation
- persistence
- representation
- complexity
- progressive-detail
cross_links:
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: PAT_scale_npc_and_adversary_detail_to_their_role_in_play
- rel: related_to
  target_object_id: DRILL_audit_specialist_subsystem_participation
reference:
  source_title: "Twilight: 2000 (1st Edition) and Twilight: 2000 Version 2.2"
  author: "Frank Chadwick; David Nilsen, Loren Wiseman, and Lester Smith"
confidence: high
references: []
variants: []
---

# Allocate Simulation Detail by Expected Persistence

## Pattern Rule
**IF** an entity, relationship, injury, asset, or condition may persist long enough for differentiated state to affect future play
**THEN** allocate detail in proportion to the expected persistence and elaborate lightweight state only when continued relevance makes the extra information useful
**ELSE** use a compressed representation that still answers the questions current play is likely to ask.

## Do
- Give persistent player characters, recurring contacts, owned vehicles, long-term injuries, and similar state enough detail to support their future consequences.
- Use cheap lightweight records for contacts, stock NPCs, temporary opponents, or other entities whose later importance is not yet known.
- Promote an entity to a richer representation when play makes it recurring or consequential rather than front-loading every possible field.
- Keep the expanded representation compatible with the same underlying resolution grammar when possible.
- Test whether the added fields are likely to be queried after the current scene or session.
- Budget specialist-system depth by expected persistence, activation cadence, and participation coverage as well as entity importance; rare vehicle detail and prolonged single-player subsystem detail do not have the same table cost.

## Don't
- Give every transient NPC, temporary injury, or one-scene object the same state depth as a campaign-persistent entity solely for symmetry.
- Force exhaustive preparation before relevance is known.
- Remove detailed persistent consequences merely because an equivalent level of detail would be excessive for disposable entities.
- Equate narrative importance, mechanical power, and representation depth; they are separate decisions.

## Checklist
- Expected persistence is identified before representation depth is selected.
- Every high-detail field can affect a plausible later interaction, consequence, recovery, repair, or decision.
- At least one lightweight representation can be expanded without retconning prior play.
- Temporary entities can resolve their current role without carrying unused campaign-grade state.
- Detail increases when persistence increases rather than merely when raw power increases.
- A campaign-defining persistent asset can gain richer state than an incidental object without forcing that richer model onto every instance.

## Notes
Uniform rules do not require uniform state depth. A player character's wound may need body location, functional impairment, healing time, medical demands, and infection because those consequences can shape weeks of play. A disposable opponent may need only enough state to resolve the current encounter. The same principle applies to contacts, equipment, settlements, and other campaign objects: instantiate deeper state when persistence makes that state decision-bearing.
