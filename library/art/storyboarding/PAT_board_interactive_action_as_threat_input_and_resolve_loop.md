---
object_id: PAT_board_interactive_action_as_threat_input_and_resolve_loop
object_type: pattern
name: Board Interactive Action as a Threat, Input, and Resolve Loop
library_path:
- art
- storyboarding
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
- storyboarding
- interactive
- gameplay
- threat
- response
- resolution
- continuity
cross_links:
- rel: supports
  target_object_id: AP_develop_storyboard_sequence_in_progressive_directing_passes
- rel: related_to
  target_object_id: PAT_hook_storyboard_shots_through_continuing_action_and_camera_state
- rel: related_to
  target_object_id: PAT_control_story_information_with_conceal_and_reveal
reference:
  source_title: The Art of Storyboard
  author: Don Bluth
confidence: high
references: []
variants:
- variant_id: VAR_byrne_map_each_interactive_option_to_its_resulting_board_state
  variant_name: Map Each Interactive Option To Its Resulting Board State
  variant_basis: context
  difference_from_foundation: "Extends the linear threat-input-resolve loop to explicit branching: for each player choice or answer that can change progression, board the resulting state or route so success, failure, restart, alternate level, or other consequence is visible and traceable rather than implied from one preferred path."
  when_to_use: "Use when a game or interactive sequence has more than one valid outcome from the same decision point and the storyboard must communicate all production-relevant branches."
  when_not_to_use: "Do not invent branches that the design does not contain or explode the board into every theoretical input when only a bounded set of meaningful outcomes affects production."
  absorbed_from_object_id: none
---

# Board Interactive Action as a Threat, Input, and Resolve Loop

## Pattern Rule
**IF** a storyboarded action sequence requires the viewer or player to make a timely input that changes the next visible state
**THEN** organize each playable beat as a readable threat, a clear actionable response moment, and a visible resolution that proves the result before handing into the next threat
**ELSE** use ordinary linear action-board structure when no participant input determines the next state.

## Do
- Establish a visually recognizable problem or threat state before the response is required.
- Make the actionable moment legible enough that spectacle does not obscure what the participant must react to.
- Show a distinct consequence or resolve state after successful input so the result is visible rather than merely implied by an unrelated later event.
- Let the resolution of one beat hand coherently into the next threat so the interactive sequence still feels like continuous action.
- Keep gameplay information and visual entertainment working together rather than reducing the boards to functional prompts alone.
- Check each loop for a readable change of state: problem -> response opportunity -> result -> next problem.

## Don't
- Do not make the threat and successful resolution so visually similar that the state change is ambiguous.
- Do not let decorative action hide the moment when input matters.
- Do not introduce the next threat before the previous successful action has been visibly acknowledged.
- Do not treat every playable beat as an isolated vignette with no continuity into the next state.
- Do not infer a complete branching, failure-state, or game-design architecture when the source sequence only establishes a successful threat-and-resolve progression.
- Do not canonize source-specific prompt flashes, input symbols, or fixed timing values as universal interactive-board rules.

## Checklist
- The current threat is recognizable before input is expected.
- The response opportunity is visually legible.
- Successful input produces a distinct visible resolution.
- The resolve state leads coherently into the next threat.
- Spectacle supports rather than obscures interactive readability.

## Notes
Bluth's *Dragon's Lair* boards repeatedly pair a threat with an input opportunity and a visible successful resolve before introducing the next threat. The durable storyboard mechanism is the state loop, not the production's particular sword flashes, directional indicators, or timing notation. Byrne's computer-game material extends the same owner from a single successful loop to branching production states: when a choice changes what happens next, each meaningful option must map to its resulting board state. The example also treats entertainment and gameplay as simultaneous visual concerns: the participant must be able to read the interactive problem while the sequence remains engaging as animated action.

Retained bounded variant: `VAR_byrne_map_each_interactive_option_to_its_resulting_board_state`.
