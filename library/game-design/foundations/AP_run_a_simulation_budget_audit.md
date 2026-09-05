---
object_id: AP_run_a_simulation_budget_audit
object_type: ap
name: Run a Simulation Budget Audit
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
- simulation
- complexity
- HOPR
- TBMD
- resources
- cadence
cross_links:
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: PAT_preserve_decision_relevant_state_while_compressing_resolution_procedure
- rel: related_to
  target_object_id: DRILL_profile_serial_resolution_latency
reference:
  source_title: "Twilight: 2000 (1st Edition) and Twilight: 2000 Version 2.2"
  author: "Frank Chadwick; David Nilsen, Loren Wiseman, and Lester Smith"
confidence: high
references: []
variants: []
---

# Run a Simulation Budget Audit

## Objective
Determine which simulation detail should remain explicit, which procedure should be compressed, and where complexity is affordable based on decision value, persistence, and activation cadence.

## Steps / Flow
1. State the player-facing pressure or behavior the subsystem is intended to create.
2. List the persistent state distinctions required for that pressure to alter later choices.
3. Trace the most common resolution path and count human-facing decisions, rolls, arithmetic, lookups, branches, and state writes.
4. Measure where the cost is paid: common runtime, conditional runtime, character creation, downtime, preparation, construction, or another cadence.
5. Separate character-facing friction from operator-facing servicing work.
6. Identify shared bottlenecks that couple any resources involved, such as time, labor, cargo, mobility, money, or future risk.
7. Test whether categorical compression, precomputation, better reference locality, or a coarser intermediate model can preserve the required final states.
8. Stress-test any genre-common special mode at its real activation frequency rather than treating it as rare because it has a separate rule section.
9. Sum the **aggregate operating budget** across simultaneously relevant domains. Individually justified rules can still exceed a human table's usable complexity when combat, gear, magic, hacking, vehicles, economy, and referee state all become active in the same session.
10. Separate player specialization from facilitator integration cost. A table may distribute domain mastery across players while one facilitator still has to understand, schedule, and arbitrate every interface.
11. Separate **local operating cost** from **global integration cost**. Cleaner individual subsystems can still raise total facilitator work when their states interact more frequently across physical, social, technical, magical, economic, or other domains.
12. Count total event/actor throughput in addition to rule complexity. A simple per-actor procedure can still dominate the session when initiative passes, minions, drones, summons, agents, or other independent actors multiply the number of resolutions.
13. Re-run the affected procedure and verify that the intended decisions, consequences, and causal feedback remain available.
14. Keep complexity whose decision or consequence value survives both the local and aggregate audit; redesign or remove operator work that does not.

## Notes
A simulation budget is not a target rule count. A once-per-character lifepath, a weekly recovery procedure, and an every-attack branch can tolerate very different operating costs. The audit therefore protects purposeful friction while locating the human servicing work that can be compressed without flattening the game. **Locally justified complexity still accumulates globally**: a design can contain few pointless rules and nevertheless exceed its usable human-operating budget when several deep domains converge on one session or one facilitator. Interoperability can improve the game while also creating integration work; measure both the cost of each subsystem and the cost of keeping their shared state coherent.
