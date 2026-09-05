---
object_id: PAT_scale_npc_and_adversary_detail_to_their_role_in_play
object_type: pattern
name: Scale NPC and Adversary Detail to Their Role in Play
library_path:
- game-design
- adversaries
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- adversaries
- npcs
- representation
- complexity
cross_links:
- rel: related_to
  target_object_id: PAT_make_the_game_operable_without_hidden_designer_knowledge
- rel: related_to
  target_object_id: PAT_derive_character_capabilities_from_expected_play
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Scale NPC and Adversary Detail to Their Role in Play

## Pattern Rule
**IF** an NPC or adversary is being represented mechanically
**THEN** include the information required to support the interactions and decisions that entity is expected to make in play, and add further detail when its role expands
**ELSE** do not construct a full player-character-equivalent record merely because the system is capable of doing so.

## Do
- Classify the entity by what play is likely to ask of it: incidental contact, recurring social role, ordinary combatant, companion, specialist, major adversary, or another concrete function.
- Store the statistics, abilities, equipment, motives, and other data needed to answer those likely questions at the table.
- Use compressed representations for minor entities when they can still resolve actions through the game's established mechanical grammar.
- When many similar minor actors appear together, compress not only stat blocks but repeat state such as initiative, luck/resources, damage conventions, and morale where doing so preserves the decisions that matter.
- Apply the same representation test to player-owned or player-commanded subordinate actors when they are numerous and individually low-decision. Controller identity does not by itself justify full fidelity for every drone, summon, pet, hireling, or helper.
- Use one behavioral abstraction—discipline, professionalism, morale, doctrine, or mission commitment—when it can answer recurring referee questions such as when ordinary opposition panics, retreats, bargains, or fights to completion.
- Add detail when play promotes an incidental character into a recurring or consequential role; the entity did not suddenly become more capable merely because more of its information is now instantiated.
- Give major NPCs and adversaries enough detail to support the tactical, social, defensive, and narrative decisions they are expected to make.

## Don't
- Build every shopkeeper, guard, or disposable opponent with the same construction depth as a player character solely for symmetry.
- Invent a second resolution system merely to make minor NPCs easier to run when a compressed representation can use the existing rules.
- Equate a lightly represented NPC with a weak NPC; narrative importance and mechanical power are separate decisions.
- Track fields that are unlikely to be queried in play and do not change how the entity behaves or resolves actions.
- Preserve full player-character-equivalent turns for every minor subordinate solely because a player owns it when group or aggregate handling would preserve the important commands and consequences.

## Checklist
- Every stored field supports a likely interaction, decision, or consequence in play.
- Minor representations still plug into the same underlying resolution grammar used elsewhere in the game.
- A lightly represented entity can be expanded later without requiring its previous play to be retconned.
- Major adversaries contain enough information to express the capabilities that make their role consequential.
- Representation depth can increase independently of raw power or difficulty.
- A group abstraction reduces repeated operator state without erasing distinctions that change positioning, target choice, or other consequential behavior.
- High-count subordinate actors are tested under the same fidelity criteria regardless of whether the facilitator or a player controls them.

## Notes
Uniform mechanics do not require uniform representation, and ownership does not require uniform fidelity. A bartender can be represented by a name, identity, and one broad competence value while a recurring villain receives a full mechanical profile, provided both remain inside the same game engine. Simplify the entity record before simplifying the fundamental rules: scale information to expected use, then instantiate more when play creates demand for it.
