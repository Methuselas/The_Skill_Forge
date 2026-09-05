---
object_id: DRILL_audit_action_economy_multipliers
object_type: drill
name: Audit Action-Economy Multipliers
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
- action-economy
- initiative
- cadence
- feedback
- spotlight
cross_links:
- rel: related_to
  target_object_id: DRILL_profile_serial_resolution_latency
- rel: related_to
  target_object_id: DRILL_map_attribute_dependency_density
- rel: related_to
  target_object_id: DRILL_audit_specialist_subsystem_participation
- rel: supports
  target_object_id: AP_run_a_simulation_budget_audit
reference:
  source_title: Shadowrun, Third Edition
  author: FASA Corporation contributors
confidence: high
references: []
variants: []
target_skill: Detect when extra actions multiply downstream procedure, feedback, and spotlight strongly enough that a speed or command advantage becomes a structural dominance problem.
---

# Audit Action-Economy Multipliers

## Practice Task
Run the same representative conflict or repeated-action scene with an ordinary actor and with an actor who receives additional actions, passes, reactions, or subordinate turns, then compare both state impact and table-time share.

## Target Skill
Detect when extra actions multiply downstream procedure, feedback, and spotlight strongly enough that a speed or command advantage becomes a structural dominance problem.

## Setup
Choose a subsystem where a legal option can materially increase action count or generate additional acting entities. Use the normal attack, defense, damage, reaction, resource-refresh, and wound/state rules. Include at least one opposing actor whose future actions can be impaired or removed by early success.

## Instructions
1. Record the baseline actor's number of meaningful actions in one full cycle and the human-facing operations each action can invoke.
2. Apply the legal speed, initiative, command, summon, drone, pet, or other action-multiplying option and rerun the same cycle.
3. Count not only extra actions but every downstream procedure they can trigger: attack sequences, defensive rolls, damage processing, movement, resource allocation, status changes, or subordinate actions.
4. Measure each participant's share of meaningful decisions and TBMD across the cycle.
5. Trace feedback. Record whether early extra actions can wound, disable, reposition, suppress, or otherwise reduce an opponent's later action quantity or effectiveness.
6. Check the refresh cadence of shared resources and defensive state. Determine whether more actions also produce more resources, clear accumulated penalties sooner, reset per-action/per-turn counters more often, or instead force one fixed reserve to be spread across the enlarged action count.
7. Test at least one counterpressure such as escalating cost, resource dilution, exposure, recoil, fatigue, vulnerability, or opportunity loss.
8. Distinguish **control bandwidth** from **actor bandwidth**. If one command can activate several drones, pets, summons, agents, hirelings, or subordinate units, count every independent action cycle that still resolves after the command.
9. Test whether money, build points, spells, or other resources can purchase new independent actors; compare that growth curve with options that improve one existing actor.
10. If initiative or tempo can itself be spent on interrupts, defenses, reactions, or emergency actions, audit that value separately from acting earlier and acting more often; one speed statistic may be buying priority, quantity, and defensive flexibility simultaneously.
11. When a summon, service, charge, command point, or similar abstract resource purchases subordinate behavior, expand the cost into **resolved actor time**. A single service that covers an entire combat can buy many turns and many downstream procedures; compare resource consumption against actor cycles, not against the number of commands issued.
12. Compare the action-multiplier option with a same-cost option that improves one action rather than creating more actions.
13. If the system already compresses numerous minor GM-controlled actors through shared initiative, group resources, aggregated damage, or simplified morale, run the same fidelity test on numerous player-owned subordinates. Ownership does not change the table-time cost of an independent actor cycle.

## Success Check
- Baseline and multiplied runs were both executed through a complete comparable cycle.
- The audit reports downstream procedures per cycle, not only the nominal number of extra actions.
- At least one participant's TBMD or decision share is measured.
- Feedback into enemy future actions is either observed or explicitly shown absent.
- A named near-miss is excluded: an option does not pass merely because its numeric cost is high if the extra actions multiply several high-value downstream systems without comparable counterpressure.
- The final judgment states why the action multiplier is acceptable, constrained, or structurally dominant rather than merely labeling it fast or powerful.
- Command cost and total resolved actor cycles are reported separately when subordinates are involved.
- Any service/task/charge cost that spans multiple turns is normalized against the number of meaningful subordinate actor cycles it actually buys.
- Any action-triggered reset of defense penalties, reaction budgets, or other state is counted as part of the multiplier's leverage rather than treated as unrelated bookkeeping.
- Equivalent high-count GM-owned and player-owned actor sets have been compared for representation depth; any fidelity difference is justified by decision importance rather than ownership alone.

## Common Failures
- Comparing initiative bonuses while ignoring that higher initiative also changes action quantity.
- Counting extra attacks but ignoring the defensive and consequence procedure each attack forces other participants to execute.
- Ignoring subordinate actors because the controlling player's character technically took only one command action.
- Assuming a once-per-turn reserve fully balances extra actions without testing whether the base actions remain strong after the reserve is depleted.
- Calling an action multiplier balanced solely because it is expensive.
- Treating one summon service, pet command, or drone order as one unit of action value when that unit authorizes an autonomous actor for an entire encounter.
- Compressing GM-controlled grunts while preserving full independent turns for equally minor player-owned drones, pets, summons, or hirelings solely because a player owns them.

## Notes
Action economy is a multiplier, not an ordinary modifier. One additional action can invoke the full downstream machinery of the game and may also deny future opposition actions if early success causes wounds, control states, or removal. The dangerous form is positive feedback: the advantage acts first, acts more often, and uses those actions to reduce the opponent's opportunity to answer. Extra actions can also be defensive multipliers when acting clears accumulated attack pressure, refreshes reaction windows, or supplies a tempo pool that can be spent on interrupts. Counterpressure should be tested against that whole loop, not against the initiative number in isolation. Cheap group commands do not make a minion architecture cheap if each subordinate still receives its own meaningful turns; control compression and actor compression are separate design problems. Likewise, a service-based summon economy can look bounded while still purchasing disproportionate table bandwidth if one service authorizes many independent actions across an encounter. Price or constrain the generated actor stream, not only the trigger that created it. Apply actor-fidelity compression by decision importance and count, not by controller identity: a minor subordinate costs the table the same independent resolution cycle whether a player or the facilitator owns it.
