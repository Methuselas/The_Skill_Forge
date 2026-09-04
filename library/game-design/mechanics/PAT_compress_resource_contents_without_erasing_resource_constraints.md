---
object_id: PAT_compress_resource_contents_without_erasing_resource_constraints
object_type: pattern
name: Compress Resource Contents Without Erasing Resource Constraints
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
- resource-management
- abstraction
- scarcity
- inventory
- logistics
- operator-cost
- decisions
cross_links:
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
reference:
  source_title: FrontierSpace Player's Handbook
  author: Bill Logan
confidence: high
references: []
variants: []
---

# Compress Resource Contents Without Erasing Resource Constraints

## Pattern Rule
**IF** a resource matters because depletion changes player choices
**THEN** preserve the fictionally meaningful constraint while aggregating interchangeable low-value component detail into a small, trackable resource pool
**ELSE** remove or simplify the tracking when depletion does not create a meaningful decision.

## Do
- Identify the decision the resource is supposed to create before selecting its unit of tracking.
- Keep fictionally distinct pools separate when their depletion changes behavior differently.
- Aggregate interchangeable low-value components into provisions, charges, uses, loads, person-days, or another decision-bearing unit.
- Make depletion change available actions, risk, route, timing, opportunity cost, or another consequential choice.
- Give players a low-friction interface for updating the resource state at the cadence where it is consumed.
- Test whether recovery or resupply can generate route, time, money, risk, scavenging, exploration, or specialist decisions rather than merely resetting a meter.
- Revisit the abstraction level when players spend more attention maintaining the resource record than deciding how to use it.

- Couple distinct resources through shared bottlenecks such as time, labor, cargo capacity, mobility, money, or future risk when those interactions create planning.
- Preserve substitution and conversion where one physical resource can answer different needs, because the choice between uses may be more important than the resource's internal composition.
- Treat routine execution as compressible once the constraint is established and repeating the underlying accounting no longer changes a decision.

## Don't
- Track individual components merely because they exist in the fiction.
- Collapse every resource into one universal supply pool when ammunition, medicine, food, power, repair material, or fuel produce meaningfully different choices.
- Use scarcity that creates clerical work without changing player behavior.
- Hide essential depletion state from players when the intended tension depends on planning around it.
- Treat all bookkeeping as automatically harmful; compare maintenance cost with the decisions the maintained state repeatedly creates.

- Track separate resources as isolated meters when the intended play depends on them competing for the same time, labor, capacity, or risk budget.

## Checklist
- The decision created by depletion can be named.
- The resource's current state is visible and cheap to update.
- Low-value components have been aggregated as far as possible without erasing a meaningful choice.
- Separate pools remain separate because they change behavior differently, not merely because the fiction names different objects.
- Resupply or recovery creates at least one meaningful route, time, money, risk, scavenging, exploration, or specialist tradeoff when appropriate to the game.
- Tracking cadence matches the frequency with which the resource is consumed.
- Removing the bookkeeping would remove a meaningful pressure rather than merely remove clerical work.

## Notes
Resource simulation is most useful at the boundary where remaining supply changes decisions. A medical kit may fictionally contain many drugs, tools, and disposables while the game tracks only a provision pool; an energy system may hide electrical detail while preserving a finite shared capacity. The useful abstraction is therefore not the smallest number of resource categories possible, but the coarsest representation that still preserves behaviorally distinct constraints. Compress the contents beneath that boundary, not the scarcity that makes players choose.
