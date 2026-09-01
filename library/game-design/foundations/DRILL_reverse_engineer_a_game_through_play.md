---
object_id: DRILL_reverse_engineer_a_game_through_play
object_type: drill
name: Reverse-Engineer a Game Through Play
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
- analysis
- reverse-engineering
- play
- mechanics
cross_links:
- rel: teaches
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: supports
  target_object_id: PAT_use_the_defining_affordances_of_an_adopted_game_system
- rel: teaches
  target_object_id: PAT_build_complete_resolution_procedures_incrementally
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
target_skill: Analyze how a game turns design goals into player behavior, component mechanics, complete resolution procedures, and tradeoffs rather than stopping at preference judgments.
references: []
variants: []
---

# Reverse-Engineer a Game Through Play

## Practice Task
Play or closely execute an unfamiliar or instructive game, then produce a compact design teardown of one major system and its relationship to the rest of play.

## Target Skill
Analyze how a game turns design goals into player behavior, component mechanics, complete resolution procedures, and tradeoffs rather than stopping at preference judgments.

## Setup
Choose a game that is unfamiliar, structurally different from your current project, or especially relevant to a design problem you are studying. Have access to the rules while the game is being played or reconstructed.

## Instructions
1. Record the intended audience and experience the game appears to promise, then list the recurring actions that actually consume player time and attention.
2. Mark where outcomes are controlled by player decision, skill, chance, facilitator judgment, or automated procedure.
3. Execute one important resolution procedure from trigger to termination. Map its inputs, component mechanics, decision points, conditional branches, state changes, outputs, and costs in time, attention, tracking, or reference work.
4. Identify one deliberate tradeoff the mechanic makes and what benefit that cost appears to purchase.
5. Extract one principle worth borrowing and name the design problem it solves rather than copying its surface implementation.
6. Name one audience, medium, genre, or intended experience for which the source implementation would be a poor fit.

## Success Check
- At least one resolution procedure was actually played or executed, and the teardown records an observed decision, behavior, pacing cost, lookup cost, or interaction effect from that run rather than only predicting what the rules should do.
- The tested resolution procedure is mapped from trigger to termination with enough detail that another reader can identify its component mechanics, branch conditions, state changes, and outputs separately from the complete procedure that composes them.
- The teardown names at least one plausible near-miss interpretation that the observation rules out or qualifies—for example, “this rule exists only for realism”—and states what the observed play evidence demonstrates instead.
- The borrowed principle includes the reason it transfers to the destination design and one context in which the source implementation would be a poor fit; naming a favorite mechanic without that reasoning does not pass.

## Common Failures
- Reviewing the game as entertainment instead of analyzing how it works.
- Listing rules without identifying the decisions or behaviors those rules create.
- Calling complexity good or bad without explaining what it buys in play.
- Copying a favorite mechanic without checking whether the destination design has the same constraints and goals.

## Notes
Repeated comparison builds a designer’s vocabulary of solutions. Reading can reveal procedures, but actual play or equivalent execution exposes pacing, lookup cost, interaction effects, and player adaptation that are easy to miss on paper. Distinguishing a component mechanic from the larger resolution procedure prevents a teardown from treating one roll, modifier, or damage operation as if it were the entire action protocol. The exercise is most valuable when contrasting different implementations of the same broad problem.
