---
object_id: PAT_match_action_state_across_shot_boundaries
object_type: pattern
name: Match Action State Across Shot Boundaries
library_path:
- art
- subjects
- animation
- posing
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- continuity
- hookup
- editing
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants:
- variant_id: VAR_whitaker_bridge_reusable_animation_states_for_interactive_transitions
  variant_name: Bridge Reusable Animation States For Interactive Transitions
  variant_basis: context
  difference_from_foundation: Applies action-state continuity to modular or interactive animation libraries by adding explicit transition clips between reachable reusable states when a direct switch would visibly reset direction, support, prop state, or body phase.
  when_to_use: Use when reusable actions such as run, jump, fire, land, or gesture can connect dynamically and some legal state changes need a dedicated bridge to preserve motion continuity.
  when_not_to_use: Do not author bridges for unreachable state pairs, and do not invent a full game-state architecture when the task only requires continuity between known reusable actions.
  absorbed_from_object_id: none
---

# Match Action State Across Shot Boundaries

## Pattern Rule
**IF** a continuing action crosses a cut and the incoming shot must preserve the relevant phase, direction, gaze, and prop state
**THEN** Match the relevant character and object state across a cut so position, pose phase, gaze, prop relation, direction, and continuing motion connect cleanly between shots

## Do
- Compare the outgoing final action state with the incoming first readable state.
- Preserve the action phase or intentionally bridge the phase change.
- Check gaze, held objects, screen direction, and body configuration.

## Don't
- Do not let adjacent shots silently reset the character or prop to a different state.

## Checklist
- The cut preserves both spatial and animation-state continuity.

## Notes
`VAR_whitaker_bridge_reusable_animation_states_for_interactive_transitions` extends the same continuity decision to modular animation sets. Identify the reusable states that can actually follow one another, add a bridge where a hard switch would pop or reset the figure, inherit the outgoing direction/support/prop/body state, and arrive cleanly into the incoming action. Test the bridge from both neighbors in playback rather than judging it as an isolated clip.
