---
object_id: PAT_generate_sandbox_situations_from_world_state_and_player_needs
object_type: pattern
name: Generate Sandbox Situations from World State and Player Needs
library_path:
- game-design
- adventures
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- sandbox
- encounters
- situations
- resources
- world-state
- agency
cross_links:
- rel: related_to
  target_object_id: PAT_structure_adventure_narratives_with_milestones_plot_beats_and_player_agency
- rel: related_to
  target_object_id: PAT_layer_adventure_information_by_how_players_can_access_it
reference:
  source_title: "Twilight: 2000 (1st Edition) and Twilight: 2000 Version 2.2"
  author: "Frank Chadwick; David Nilsen, Loren Wiseman, and Lester Smith"
confidence: high
references: []
variants: []
---

# Generate Sandbox Situations from World State and Player Needs

## Pattern Rule
**IF** an open campaign needs recurring direction without prescribing a plot
**THEN** generate actors, places, pressures, resources, and local problems whose significance changes when they intersect with persistent player needs and current world state
**ELSE** use a more directed adventure structure when the campaign does not rely on open-ended prioritization.

## Do
- Store contextual world variables such as territory condition, settlement attitude, local scarcity, faction presence, or crisis when one value can alter many later encounter results.
- Generate needs and pressures rather than predetermined solutions.
- Let persistent shortages, injuries, damaged equipment, relationships, or goals make ordinary generated locations strategically important.
- Reveal referee-facing world state through observable fictional consequences rather than simply naming the hidden category to players.
- Reuse the same generated element differently when the party arrives with different needs.

## Don't
- Treat a random encounter table as a sandbox engine when its results have no durable relationship to party state.
- Generate a mandatory quest response when a settlement problem, resource opportunity, or actor with a motive would create sufficient pressure.
- Expose every internal territory or faction category as a player-facing label when discovery is part of play.
- Assume survival pressure alone supplies long-term direction when players have no meaningful reasons to care about generated opportunities.

## Checklist
- At least one persistent player need can make the generated element matter differently from another party state.
- The generated result creates a situation with multiple plausible responses rather than a scripted solution.
- A stored world-state variable changes more than one later output or interpretation.
- Players can infer changing conditions from fictional evidence.
- The procedure produces usable pressure without requiring the referee to invent the entire situation from scratch.

## Notes
A sandbox can generate situations without generating stories. A repair yard means little to a well-supplied group and can become the most important location on the map after a vehicle loses a critical component. A field hospital, farm, roadblock, trader, or damaged settlement changes meaning according to the party's current injuries, shortages, relationships, and goals. The useful procedural loop is generated world state multiplied by persistent player need.
