---
object_id: DRILL_compare_state_detail_to_resolution_cost
object_type: drill
name: Compare State Detail to Resolution Cost
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
- simulation
- state
- resolution
- HOPR
- TBMD
- testing
cross_links:
- rel: teaches
  target_object_id: PAT_preserve_decision_relevant_state_while_compressing_resolution_procedure
- rel: related_to
  target_object_id: DRILL_profile_serial_resolution_latency
reference:
  source_title: "Twilight: 2000 (1st Edition) and Twilight: 2000 Version 2.2"
  author: "Frank Chadwick; David Nilsen, Loren Wiseman, and Lester Smith"
confidence: high
target_skill: Preserve differentiated consequences while reducing unnecessary causal-resolution work.
references: []
variants: []
---

# Compare State Detail to Resolution Cost

## Practice Task
Resolve the same consequence-producing event once with a physically literal procedure and once with a categorical or compressed procedure designed to preserve the same final state distinctions.

## Target Skill
Preserve differentiated consequences while reducing unnecessary causal-resolution work.

## Setup
Choose a subsystem with at least three possible persistent failure states, such as vehicle components, injuries, equipment systems, infrastructure, or another stateful object.

## Instructions
1. Write the minimum list of final states that must remain distinct because each changes later play differently.
2. Execute the existing or most literal causal procedure once and count human-facing operations, lookups, branch transitions, arithmetic, and state writes.
3. Build a bounded alternative that maps severity, margin, or another compact input directly into the same final-state vocabulary.
4. Execute the same event with the compressed procedure.
5. Compare HOPR, approximate TBMD, retrieval distance, and final state.
6. Identify every intermediate quantity from the literal procedure that disappears after the event and ask whether retaining it changed any later decision.

## Success Check
- Both procedures were actually executed and ended in final states drawn from the same decision-relevant state list.
- The comparison records HOPR or equivalent human operations for both runs rather than merely predicting that one is faster.
- At least one intermediate causal value is shown to be unnecessary after state selection, or the drill records that none could safely be removed.
- A named near-miss is excluded: replacing component states with a single hit-point total does not pass when the listed component failures produce different later decisions.
- The selected procedure is justified by preserved consequences and measured operating cost, not by a general preference for realism or simplicity.

## Common Failures
- Comparing two procedures that produce materially different final-state vocabularies.
- Treating a table lookup as automatically cheaper than arithmetic without measuring retrieval and branch cost.
- Compressing away the state that made repair, recovery, routing, or tactical choice different.
- Preserving a causal quantity solely because it makes the simulation easier to narrate after the fact.

## Notes
Detailed output and detailed derivation are separate design dimensions. This drill forces the designer to hold consequence granularity constant while changing only the route used to reach it.
