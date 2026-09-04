---
object_id: DRILL_audit_resource_detail_by_decision_effect
object_type: drill
name: Audit Resource Detail by Decision Effect
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
- resources
- simulation
- abstraction
- playtesting
- decisions
cross_links:
- rel: teaches
  target_object_id: PAT_compress_resource_contents_without_erasing_resource_constraints
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
reference:
  source_title: "Twilight: 2000 (1st Edition) and Twilight: 2000 Version 2.2"
  author: "Frank Chadwick; David Nilsen, Loren Wiseman, and Lester Smith"
confidence: high
target_skill: Determine which tracked resource distinctions create actual planning and which only create clerical state.
references: []
variants: []
---

# Audit Resource Detail by Decision Effect

## Practice Task
Audit one resource-heavy subsystem by tracing every tracked distinction into an actual player choice, then rerun a representative scenario after compressing one low-value distinction.

## Target Skill
Determine which tracked resource distinctions create actual planning and which only create clerical state.

## Setup
Choose a subsystem with at least three resource distinctions and a representative scenario in which some of those resources can be depleted, substituted, converted, or resupplied.

## Instructions
1. List every resource field the table must track and the cadence at which it changes.
2. For each field, name the decision it can change: route, timing, load, equipment, staffing, risk, social need, mission priority, or another concrete choice.
3. Mark the shared bottlenecks that connect resources, such as time, labor, cargo, mobility, money, or future risk.
4. Execute the scenario once with the full resource model and record the decisions that actually occur.
5. Select one distinction that produced bookkeeping but no observed decision, compress or remove it, and rerun the same scenario.
6. Compare the two runs. Keep the compression only if the same meaningful constraints and tradeoffs remain legible.

## Success Check
- Every retained resource distinction is tied to at least one observed decision in the full-detail run.
- At least one resource interaction through a shared bottleneck was actually exercised rather than merely predicted.
- The compressed rerun was executed and preserved the named decision-bearing constraints.
- A named near-miss is excluded: replacing all resources with one universal supply meter does not pass if ammunition, medicine, fuel, food, or parts changed behavior differently in the full run.
- The final keep/compress decision states which choice would be lost or preserved, not merely that the detail feels realistic.

## Common Failures
- Keeping a field because it corresponds to a real object without identifying any decision it changes.
- Removing a distinction after observing only a scenario in which the resource never became scarce.
- Comparing bookkeeping quantity without testing substitution, conversion, or shared bottlenecks.
- Calling two resources interchangeable when their depletion changes different capabilities.

## Notes
Resource detail earns its cost at the boundary where remaining supply changes planning. The audit therefore tests resources under pressure rather than judging their names or realism in isolation.
