---
object_id: DRILL_profile_serial_resolution_latency
object_type: drill
name: Profile Serial Resolution Latency
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
- complexity
- pacing
- playtesting
- throughput
cross_links:
- rel: teaches
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: supports
  target_object_id: PAT_account_for_the_intended_play_environment_before_freezing_the_design
- rel: related_to
  target_object_id: DRILL_stress_test_concurrent_rule_activation
- rel: related_to
  target_object_id: DRILL_reverse_engineer_a_game_through_play
reference:
  source_title: Rolemaster Standard Rules and Rolemaster Fantasy Role Playing Core Rules
  author: Coleman Charlton, John Curtis, Pete Fenlon, and Steve Marvin
confidence: high
target_skill: Detect when tolerable per-action operating cost multiplies across sequential actors into long player downtime or poor table throughput.
references: []
variants: []
---

# Profile Serial Resolution Latency

## Practice Task
Execute one representative full round or other repeated multi-actor cycle, time it, and record how long each participant waits between meaningful decisions as the same resolution work repeats across actors.

## Target Skill
Detect when tolerable per-action operating cost multiplies across sequential actors into long player downtime or poor table throughput.

## Setup
Choose a subsystem in which several actors resolve in sequence. Use a representative party or team size plus opposing or facilitator-controlled entities. Prepare the normal reference surfaces, sheets, tables, or digital tools the intended play environment provides. Select one participant as the observation anchor.

## Instructions
1. Execute the anchor participant's first ordinary action and count the human-facing operations required: meaningful decisions, rolls, arithmetic steps, lookups, reference transitions, branch checks, state writes, and reminders. Record this as the baseline Human Operations Per Resolution (HOPR); do not count a software-internal operation unless a human must inspect or act on it.
2. Continue through one complete representative round or cycle without skipping other actors' ordinary procedures. Time each actor's resolution and record any facilitator-only work inserted between player actions.
3. Measure the Time Between Meaningful Decisions (TBMD) for the anchor participant: start when the anchor finishes a decision-bearing action and stop when that participant next receives a decision that can materially change play. Distinguish active reaction or defense decisions from passive waiting.
4. Separate decision time from operator-service time. Mark arithmetic, table retrieval, cross-book or cross-screen navigation, state maintenance, interpretation, and repeated setup that can consume time without creating a new choice.
5. Identify serial multipliers. Record which costs recur once per actor, once per attack, once per target, once per persistent condition, or once per facilitator-controlled entity rather than assuming one resolution represents the whole round.
6. Rerun the same round with one plausible interface or procedure change such as a consolidated reference page, a shared table, precomputed invariant arithmetic, a coarser state representation, parallel resolution, or transparent automation. Keep the player-facing choices as constant as possible.
7. Compare the two runs and decide whether the bottleneck is primarily decision density, procedure length, retrieval distance, state maintenance, actor count, facilitator concentration, or a combination. Record which play value would be lost by any proposed simplification.

8. For any action that resolves several simulated units inside one declaration, such as bullets, missiles, targets, subcomponents, summons, or damage packets, record whether operator work grows per unit while player decision count remains mostly fixed. Treat this as a serial multiplier even when it occurs inside one actor's turn.

## Success Check
- A complete representative multi-actor round or cycle was actually executed and timed; timing one isolated action and multiplying by actor count does not pass.
- Baseline HOPR separates meaningful decisions from arithmetic, lookup, translation, branching, state writes, and reminders.
- TBMD is measured for at least one participant and excludes periods in which that participant is making consequential reactions or defenses.
- At least one serial multiplier is observed directly, such as a lookup or state update repeated for every actor, attack, target, or condition.
- A named near-miss is included where one actor's resolution is individually tolerable but the full cycle produces substantial waiting; the record explains why single-resolution usability would have missed the table-level burden.
- The rerun changes one interface or procedure factor while preserving the intended decisions closely enough to identify whether the observed latency came from retrieval, calculation, state maintenance, or the decision structure itself.
- Any recommendation states both the measured throughput gain and the meaningful decision, consequence, simulation distinction, or genre effect that must remain intact.

- At least one within-action scaling factor is checked when the system contains multi-unit resolution; a test that times one bullet or one component while the normal action can require many does not pass.

## Common Failures
- Measuring only the GM's total combat duration without locating where individual participants lose decision access.
- Treating every second between turns as dead time even when the player is making defenses, reactions, bids, interrupts, or other meaningful choices.
- Assuming a fast expert group proves novice throughput when veterans have memorized table locations, shortcuts, or dependency paths.
- Automating the whole procedure and concluding the design is efficient without identifying which human operations were removed.
- Reducing actor count during the optimized rerun and attributing the improvement to the rule or interface change.

## Notes
A resolution can be acceptable in isolation and still produce poor table flow when its operating cost repeats serially across every participant and every facilitator-controlled actor. Detailed table-driven systems make this especially visible, but the problem is general: attacks, reactions, upkeep steps, bidding, initiative, status decay, and other repeated procedures can multiply small local friction into long waits. HOPR provides a rough count of human operations; TBMD captures the player's experiential consequence. Neither metric is a universal target. A tactical game may intentionally support long intervals filled with reactions and planning, while a fast action game may require very short gaps. The exercise asks whether the waiting is intended play or merely the time humans spend servicing the rules.
