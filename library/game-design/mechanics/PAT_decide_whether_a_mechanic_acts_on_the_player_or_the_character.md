---
object_id: PAT_decide_whether_a_mechanic_acts_on_the_player_or_the_character
object_type: pattern
name: Decide Whether a Mechanic Acts on the Player or the Character
library_path:
- game-design
- mechanics
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- mechanics
- player-facing
- character-capability
- embodiment
cross_links:
- rel: related_to
  target_object_id: PAT_derive_character_capabilities_from_expected_play
- rel: related_to
  target_object_id: PAT_define_the_intended_player_before_designing_for_them
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: PAT_calibrate_encounters_to_their_purpose_challenge_and_response_space
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Decide Whether a Mechanic Acts on the Player or the Character

## Pattern Rule
**IF** a mechanic uses a player's real-world ability, physical performance, knowledge, memory, verbal skill, or real-time pressure to influence a fictional outcome
**THEN** deliberately decide whether the challenge belongs to the player, the character, or a designed combination of both, and make that relationship support the intended experience
**ELSE** resolve represented character competence primarily through the game's character-facing mechanics.

## Do
- Name where competence resides for the activity: player, character, or hybrid.
- Preserve the ability to portray characters whose represented competence exceeds the player's real-world competence when that is part of the game's promise.
- When player performance is intentional, define what character traits, resources, or permissions can still mediate the result if the design is hybrid rather than purely player-facing.
- For riddles, logic puzzles, deduction scenes, and similar encounters that deliberately test player reasoning, decide whether represented character expertise can supply clues, partial information, retries, leverage, or a bypass, or whether the intended experience explicitly makes the challenge player-facing.
- Distinguish fictional pressure from player pressure; a countdown in the fiction and a real timer at the table create different decision environments.
- Test whether the player-facing demand produces the intended emotion or behavior rather than merely adding novelty.
- Account for accessibility, physical ability, available space, online play, and other environmental constraints when real-world performance matters.

## Don't
- Accidentally require the player to personally possess an ability the character sheet claims belongs to the character.
- Let trivia, puzzles, dexterity tasks, acting skill, or other player-facing challenges silently override character investment unless that transfer is deliberate.
- Require an unassisted player-only solution when the game otherwise promises that the character's represented expertise should matter, unless excluding that expertise is an explicit part of the challenge.
- Assume a physical or real-time mechanic is automatically more immersive because it resembles the fictional pressure.
- Use real-time pressure when the intended experience depends on careful deliberation, table conversation, or accessibility that the timer suppresses.
- Treat a hybrid challenge as fair merely because both player skill and character statistics appear somewhere in the procedure; inspect which one actually controls the outcome.

## Checklist
- The design explicitly identifies whether the activity tests the player, the character, or both.
- A player can understand what their character investment contributes even when real-world performance also matters.
- Player-facing puzzles state whether and how character expertise can provide leverage, and that choice matches the intended experience.
- The mechanic does not unintentionally prevent players from portraying competencies they do not personally possess.
- Any real-time or physical pressure produces behavior appropriate to the intended tone and audience.
- Accessibility and play-environment costs of the player-facing demand have been considered.
- Hybrid mechanics have been tested to confirm that neither player skill nor character capability unintentionally erases the other.

## Notes
Alternative mechanics can move part of resolution out of the character sheet and into the player's body, knowledge, attention, or available real time. That transfer can be the point: a falling block tower can make players physically feel mounting tension, and a real timer can change how a table deliberates. The design question is not whether such mechanics are legitimate, but whether the game intentionally wants player capability to determine fictional capability and how that choice interacts with the character the player was invited to portray.

Chapter 17 makes the player/character boundary especially visible in puzzles. A riddle can intentionally test the people at the table, but the design should still decide what a brilliant scholar, expert investigator, or otherwise competent character contributes. The answer may be clues, partial solutions, retries, alternate access, or nothing at all when pure player reasoning is the promised challenge; the failure is leaving that relationship accidental.
