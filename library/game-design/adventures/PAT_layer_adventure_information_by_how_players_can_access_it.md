---
object_id: PAT_layer_adventure_information_by_how_players_can_access_it
object_type: pattern
name: Layer Adventure Information by How Players Can Access It
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
- perception
- discovery
cross_links:
- rel: related_to
  target_object_id: PAT_structure_adventure_narratives_with_milestones_plot_beats_and_player_agency
- rel: related_to
  target_object_id: PAT_make_the_game_operable_without_hidden_designer_knowledge
- rel: related_to
  target_object_id: PAT_invoke_resolution_only_for_meaningful_uncertainty
- rel: related_to
  target_object_id: PAT_calibrate_encounters_to_their_purpose_challenge_and_response_space
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Layer Adventure Information by How Players Can Access It

## Pattern Rule
**IF** an adventure contains information that is not equally available to the referee, characters, and players
**THEN** partition that information by its actual route into play and reveal it when the characters have the perception, question, action, trigger, or meaningful resolution needed to gain access
**ELSE** present ordinary scene information directly instead of hiding it behind procedure merely because it was not included in the first description.

## Do
- Separate **referee truth** from player-facing information. Record hidden motives, actual causes, concealed hazards, secret identities, future triggers, and other underlying state where the referee can use them without accidentally presenting them as already known.
- Give **automatic perception** immediately when a character in the situation would plainly notice it or when it is necessary for ordinary orientation and a fair first decision.
- Treat **queryable information** as available when players ask a reasonable question, inspect an obvious feature, or focus attention on something that is plainly perceptible; do not invent a check solely because the detail was omitted from the initial read-aloud.
- Tie **discoverable information** to a concrete route of access such as searching, interacting, moving to a position, using a tool, questioning an NPC, examining evidence, making a deduction, or resolving genuine uncertainty.
- Use **triggered information** when knowledge becomes available only after a location, time, state change, plot beat, NPC interaction, event, or other identifiable condition occurs.
- Front-load enough scene information to establish the immediate decision surface: where the characters are, what obvious opportunities or dangers matter now, and what they can act on next.
- Let player questions refine the scene after the initial description rather than trying to preload every potentially relevant detail into boxed text.
- Make access conditions proportionate to the information. Obvious doors, fires, exits, and creatures should not require the same discovery procedure as concealed compartments, subtle tripwires, hidden allegiances, or forensic clues.
- When information is mechanically or tactically important, verify that the characters can obtain it early enough to make the decision it is supposed to inform.
- For severe risks, verify that players have a meaningful basis for informed caution. That basis can be distributed across premise-level warning, a learned challenge grammar, recurring patterns, environmental evidence, prior consequences, or immediate local clues; it does not have to be repeated as an isolated warning at every danger.
- Keep hidden information hidden because the fiction has not yet granted access, not because the adventure needs the players to make an uninformed choice.
- Match information precision to decision precision. Approximate language is sufficient when exact values do not change play; when movement, range, timing, capacity, cover, visibility, positioning, or another rule depends on a value, provide enough usable specificity for the player and referee to evaluate the choice.

## Don't
- Read referee-only truth aloud merely because it appears near descriptive text in the manuscript.
- Treat every omitted detail as concealed information.
- Require Perception, Search, Notice, or equivalent checks for plainly visible facts after a player asks about them.
- Hide a severe, automatically perceptible threat until after the players commit to a choice that reasonable characters would have recognized as dangerous.
- Assume every lethal or severe threat needs an explicit local warning when the adventure has already established a reliable risk grammar that attentive players can use; preserve some meaningful informational basis for caution either way.
- Put all available information in the opening description and monopolize synchronous table attention before players can act.
- Reveal secrets early merely because the referee knows them.
- Use a failed information check as a dead end when the adventure still requires that information to reach a mandatory milestone unless another access route or consequence is deliberately provided.
- Use vague descriptive terms such as “nearby,” “large,” or “far away” when the game asks players to make a mechanically consequential decision that depends on a more precise distance, size, duration, or quantity.

## Checklist
- Referee-only truth is visibly distinguishable from text or facts safe to present to players.
- The initial scene description gives enough information for a fair immediate decision without trying to exhaust the location.
- Plainly perceptible details are available without unnecessary resolution.
- Important hidden details have identifiable access conditions rather than depending on referee intuition.
- Player questions can obtain ordinary additional detail without converting every inquiry into a roll.
- Checks are reserved for information access that is meaningfully uncertain and where the result changes play.
- Tactical or consequential information becomes available before the decision it is meant to inform, unless uncertainty or surprise is itself the intended challenge.
- High-consequence risks have a meaningful informational basis somewhere in the adventure's premise, learned patterns, environment, prior play, or local presentation; the referee can identify where that basis comes from.
- Triggered and deferred information is recorded well enough that the referee knows when it becomes available.
- Concealed information needed for progress has either multiple access routes, a meaningful failure consequence that still moves play, or an explicit recovery path.
- Mechanically consequential dimensions, distances, durations, capacities, or similar facts are stated at enough precision for the decisions they are meant to support.

## Notes
Adventure description is an information interface as well as prose. The designer knows more than the characters, and the referee must be able to distinguish underlying truth from what the characters automatically perceive, what players can learn by asking, what requires deliberate discovery, and what becomes available only after a trigger. This preserves both fairness and mystery while keeping the table interactive.

Martin Buinicki's *Designing TTRPGs For Dummies*, Chapter 16, emphasizes concise read-aloud text, sensory orientation, and leaving room for the GM and players to contribute rather than scripting every reaction. Practitioner comparison with *The Keep on the Borderlands* and *Star Frontiers: Crash on Volturnus* sharpens the game-design owner. *Keep on the Borderlands* tells the referee to provide accurate information the characters can perceive while withholding secrets they have not discovered. *Crash on Volturnus* repeatedly separates brief player-facing descriptions from referee background, special rules, discoverable information, and planned-event logic. Together they establish a reusable information-access grammar: description establishes the decision surface, questions refine it, actions expose more, and mechanics resolve genuinely uncertain access.

Chapter 17 and the practitioner comparison with *Tomb of Horrors* refine the fairness boundary. High consequence increases the need for a meaningful basis for caution, but that basis can be distributed across the whole challenge grammar. *Tomb of Horrors* globally warns that the expedition is exceptionally lethal, teaches probing and careful examination early, repeats deceptive architectural patterns, and then relies on players learning from those patterns. Local telegraphing is one information channel among several, not a universal requirement.

Chapter 19 adds a precision boundary to the same information-interface model. Description does not need numerical specificity merely for realism, but it must become specific enough when the rules make the value decision-relevant. A “large hangar” can be perfectly adequate orientation until a player must decide whether a movement rate, weapon range, spell, flight distance, or line of sight reaches across it; at that point, missing scale becomes missing play information.
