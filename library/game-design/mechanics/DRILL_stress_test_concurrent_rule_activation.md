---
object_id: DRILL_stress_test_concurrent_rule_activation
object_type: drill
name: Stress-Test Concurrent Rule Activation
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
- mechanics
- playtesting
- state
cross_links:
- rel: teaches
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: teaches
  target_object_id: PAT_build_complete_resolution_procedures_incrementally
- rel: related_to
  target_object_id: DRILL_stress_test_mechanical_constraints_under_composition
- rel: related_to
  target_object_id: PAT_account_for_the_intended_play_environment_before_freezing_the_design
reference:
  source_title: GURPS Basic Set, Fourth Edition
  author: Steve Jackson, David L. Pulver, and Sean M. Punch
confidence: high
target_skill: Detect when individually reasonable conditional mechanics create excessive operating load or cascades under realistic simultaneous activation.
references: []
variants: []
---

# Stress-Test Concurrent Rule Activation

## Practice Task
Construct one realistic scene that activates several conditional mechanics at the same time, execute the rules exactly enough to expose their interactions, and compare the stacked operating cost with the value each active layer contributes to player decisions and consequences.

## Target Skill
Detect when individually reasonable conditional mechanics create excessive operating load or cascades under realistic simultaneous activation.

## Setup
Choose a working subsystem with at least three conditional rules that can plausibly overlap. Include at least one shared resource, derived value, timer, status, or other state touched by more than one rule. Prepare a simple baseline scene in which only one of those rules is active and a stacked scene in which at least three are active together.

## Instructions
1. Execute the single-rule baseline and record the decisions made, rolls, arithmetic, lookups, state writes, reminders, and elapsed resolution time.
2. Execute the stacked scene without simplifying away the selected rules. Record the order in which they activate and every shared value or state each one reads or changes.
3. Trace downstream propagation after every shared-state change. If fatigue changes movement, defense, action permission, or another derived value, record those secondary changes rather than stopping at the resource deduction.
4. Separate work that creates a meaningful choice or consequence from work that only calculates, translates, retrieves, propagates, or maintains state.
5. Identify any branch that is cheap in isolation but expensive because another rule repeatedly reactivates it, changes its timing, or makes its state harder to remember.
6. Remove or collapse one active layer and rerun the stacked scene. Record the decision, consequence, simulation distinction, or genre effect that disappears with it.
7. If the intended medium can automate bookkeeping, simulate that automation and verify that the player can still inspect why the visible result changed.
8. Decide whether each tested layer should remain baseline, become opt-in, be collapsed into a broader approximation, be automated, or be redesigned, and record the observed reason for that choice.

## Success Check
- The stacked scene actually activated at least three selected mechanics simultaneously; listing three optional rules that never overlap does not pass.
- At least one shared resource, derived value, timer, or persistent state was modified by more than one active rule, and the downstream effects were traced rather than merely predicted.
- The record separates meaningful decisions/consequences from arithmetic, lookup, translation, propagation, and maintenance work.
- A named near-miss is included in which the subsystem contains many rules but the tested scene activates only one; the record explains why raw rule count alone would have overstated the observed operating burden.
- At least one active layer was removed or collapsed and the stacked scene was rerun, producing concrete evidence about what play value that layer actually contributed.
- Any keep, opt-in, collapse, automate, or redesign decision cites an observed contribution and an observed operating cost rather than a preference for realism or simplicity.

## Common Failures
- Testing every conditional rule separately and assuming their isolated costs simply add without interaction.
- Counting only additional rolls while ignoring reminders, cross-references, timers, derived-value changes, and the audit burden created by shared state.
- Declaring a stacked procedure bad because it is long without checking whether the campaign is specifically about the decisions that the detailed state creates.
- Simplifying the stacked scene during the test and then using the simplified execution as evidence that the written procedure is cheap.
- Treating automation as a cure when the hidden rules still make player-facing outcomes impossible to understand.

## Notes
Conditional depth can keep the common path efficient: a serious-wound check need not run when no serious wound occurred, and an environmental hazard need not matter when the character is safe. The harder case appears when fiction makes several conditions true at once. Shared resources and derived values can turn separate modules into a cascade, so operating cost must be measured under representative composition as well as one rule at a time. The goal is not to prohibit detailed simulation. A survival game may gain important decisions when injury, fatigue, cold, food, and movement interact. The drill asks whether the stacked state is itself the intended play or merely the bookkeeping required to reach it.
