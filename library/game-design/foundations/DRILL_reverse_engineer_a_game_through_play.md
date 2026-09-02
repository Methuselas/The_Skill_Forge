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
- rel: supports
  target_object_id: PAT_make_the_game_operable_without_hidden_designer_knowledge
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
7. Run a rulebook-interface pass. Map the chapter and section hierarchy, note the recurring visual signals for rules, examples, tables, warnings, and reference material, and record where actual execution required page flipping, searching, index use, cross-references, or interpretation. Distinguish retrieval usability from whether you personally like the visual style.
8. When multiple editions, revisions, or system-changing supplements of the same RPG are available, compare at least one equivalent information domain and one equivalent play procedure. Record the defining affordances that are preserved, the affordances that are added, the dependencies that are replaced, any migration required for existing characters or content, and the resulting change in play identity. Classify the major change as primarily additive, evolutionary, or replacement/reinterpretive without assuming that any category is inherently better.
9. Separate architectural improvement from experiential repositioning. Ask both whether the later version implements the same experience more cleanly and whether it materially changes decision density, pacing, operating burden, or intended audience; a cleaner implementation does not by itself establish a lighter or broader experience.
10. Evaluate mature revisions through both a veteran-reference lens and a novice-facilitator lens. Record whether established users gain retrieval, consolidation, or compatibility benefits, and whether a new facilitator receives a known-good playable configuration, safe omissions, and expansion triggers without first mastering the full rules surface.
11. For the same comparison, record what the later interface preserves, removes, relocates, or visually reframes, and evaluate the resulting usability change without assuming that newer presentation is automatically better.

## Success Check
- At least one resolution procedure was actually played or executed, and the teardown records an observed decision, behavior, pacing cost, lookup cost, or interaction effect from that run rather than only predicting what the rules should do.
- The tested resolution procedure is mapped from trigger to termination with enough detail that another reader can identify its component mechanics, branch conditions, state changes, and outputs separately from the complete procedure that composes them.
- The teardown names at least one plausible near-miss interpretation that the observation rules out or qualifies—for example, “this rule exists only for realism”—and states what the observed play evidence demonstrates instead.
- The borrowed principle includes the reason it transfers to the destination design and one context in which the source implementation would be a poor fit; naming a favorite mechanic without that reasoning does not pass.
- The teardown records the rules artifact as an operating interface: it identifies the information hierarchy and at least one observed retrieval cost or retrieval aid encountered while executing play.
- Any edition or revision comparison records at least one preserved affordance, one added or removed affordance when present, one replaced dependency when present, and any migration burden imposed on existing play; calling the later version simply cleaner, modern, or different does not pass.
- Any edition comparison separates visual-style preference from operational evidence such as legibility, navigation, lookup speed, table usability, cross-reference burden, or prerequisite ordering.
- Any edition comparison distinguishes cleaner architecture from changed experience by recording whether decision density, pacing, operating burden, or audience fit materially moved.
- A mature-edition comparison evaluates both established-user reference value and new-facilitator learning/curation value rather than assuming one interface serves both equally well.

## Common Failures
- Reviewing the game as entertainment instead of analyzing how it works.
- Listing rules without identifying the decisions or behaviors those rules create.
- Calling complexity good or bad without explaining what it buys in play.
- Copying a favorite mechanic without checking whether the destination design has the same constraints and goals.
- Treating attractive, ugly, old, modern, sparse, or ornate presentation as proof of usability without observing how the interface supports actual rule retrieval.
- Treating one edition’s visual language as the canonical form of the game instead of analyzing what changed and what those changes did to use.
- Treating convertibility as compatibility without checking whether characters, capabilities, power relationships, procedures, and play identity survive the migration.

## Notes
Repeated comparison builds a designer’s vocabulary of solutions. Reading can reveal procedures, but actual play or equivalent execution exposes pacing, lookup cost, interaction effects, and player adaptation that are easy to miss on paper. Distinguishing a component mechanic from the larger resolution procedure prevents a teardown from treating one roll, modifier, or damage operation as if it were the entire action protocol. The exercise is most valuable when contrasting different implementations of the same broad problem. Chapter 19 adds the published artifact itself to that teardown. RPGs repeatedly use similar information grammar — chapter, section, subsection, procedure, example, table, reference — while expressing it through very different visual identities, and the same game can substantially change that identity between editions. Comparative review should therefore test whether a particular interface makes the game easier or harder to operate, while treating visual style as a separate preference and art direction as a distinct but interacting layer that can strengthen or weaken immersion without replacing usability. Edition comparison also needs a mechanical migration pass: a later version can preserve names and setting while replacing dependencies important enough to alter learned procedures, character behavior, content compatibility, or the game's practical identity. Additive, evolutionary, and replacement approaches can all be valid; the drill records what changed and what that change cost before judging fit. A revision can also become substantially cleaner without repositioning the experience at all, so implementation quality and experiential profile must be scored separately. Mature products further need two interface passes: established users may benefit from consolidation and fast reference while newcomers need an executable route into competent facilitation. Reference completeness, learning architecture, and curation support are related but distinct qualities.
