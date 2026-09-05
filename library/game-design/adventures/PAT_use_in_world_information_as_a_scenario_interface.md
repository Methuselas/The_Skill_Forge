---
object_id: PAT_use_in_world_information_as_a_scenario_interface
object_type: pattern
name: Use In-World Information as a Scenario Interface
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
- adventures
- information
- hooks
- factions
- uncertainty
cross_links:
- rel: related_to
  target_object_id: PAT_layer_adventure_information_by_how_players_can_access_it
- rel: related_to
  target_object_id: PAT_generate_sandbox_situations_from_world_state_and_player_needs
- rel: related_to
  target_object_id: PAT_design_shared_problems_with_multiple_solution_interfaces
- rel: related_to
  target_object_id: PAT_make_preparation_change_problem_topology
reference:
  source_title: Cyberpunk 2020 (2.0.2.0 Version)
  author: Mike Pondsmith and R. Talsorian Games contributors
confidence: high
references: []
variants: []
---

# Use In-World Information as a Scenario Interface

## Pattern Rule
**IF** the setting contains media, rumors, reports, notices, dispatches, broadcasts, social feeds, prophecies, or other information channels
**THEN** use them to present active situations, competing perspectives, uncertainty, and actionable leads in a form characters can investigate or exploit
**ELSE** keep exposition direct when no player decision depends on interpreting the information.

## Do
- Present a current event or dispute rather than only background history.
- Let different sources frame the same event differently when motives, propaganda, incomplete knowledge, or uncertainty are meaningful.
- Give the information at least one actionable handle: a person, place, need, claim, deadline, anomaly, resource, or contradiction.
- Let information skills and social relationships change what players can verify, contextualize, conceal, publicize, or weaponize.
- When preparation matters, let actionable information change the later problem topology: bypass a checkpoint, identify a dependency, reveal an alternate route, invalidate an assumption, or eliminate a roll whose uncertainty has genuinely been resolved.
- Use the artifact itself as part of the setting so exposition also demonstrates how the world communicates.

## Don't
- Bury the actual hook under lore that players cannot act on.
- Present contradictory accounts when no investigation or choice can distinguish or exploit them.
- Treat an in-world handout as automatically interactive simply because it is flavorful.

## Checklist
- The information describes something happening now or about to matter.
- At least one uncertainty, conflict of interest, or missing fact can motivate player inquiry.
- The artifact points toward concrete people, places, resources, or actions.
- Different character specialties can interact with the information in different ways when appropriate.
- Removing the in-world framing would lose setting or decision value, not merely decoration.

## Notes
Information can be both exposition and interface. A news report, rumor sheet, police bulletin, corporate statement, or guild notice can teach the setting while also presenting incomplete, biased, or contested state. The strongest versions create a question players can act on rather than a paragraph they merely consume.
