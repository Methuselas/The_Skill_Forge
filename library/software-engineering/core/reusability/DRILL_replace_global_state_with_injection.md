---
object_id: DRILL_replace_global_state_with_injection
object_type: drill
name: Replace Global State With Injected Instance State
library_path:
- software-engineering
- core
- reusability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- global_state
- reusability
- dependency_injection
- refactoring
cross_links:
- rel: teaches
  target_object_id: PAT_avoid_global_state_inject_shared_state
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: converting global static state into injected instance state so reuse is safe
references: []
variants: []
---

# Replace Global State With Injected Instance State

## Practice Task
Take a class holding global static state, convert it to instance state, inject it, and prove two independent uses no longer interfere.

## Target Skill
Turning global shared state into instance state controlled by dependency injection.

## Setup
No special setup required.

## Instructions
1. Start from a class with a static variable and static functions — a shopping basket where all code shares one set of items.
2. Demonstrate the interference: exercise both features that add to the basket and record the wrong result each sees.
3. Convert the class to be instantiable, giving each instance its own distinct state.
4. Search the codebase for the old static accessor and state the result, naming any consumer still reaching a shared accessor.
5. Inject an instance into each class that needs it through its constructor or parameters, recording per consumer whether it shares an instance and the reason.
6. Create two independent instances (say, a normal-products basket and a fresh-products basket), exercise them together, and write down each consumer's view.

## Success Check
- The interference is demonstrated before the change, with both features exercised and the wrong result recorded. An account of how the interference would arise is the thing being fixed, not evidence that it was there.
- No static state remains, and the search establishing that is stated — a search for the old accessor across the codebase rather than a reading of the one class.
- Every consumer receives the instance through its constructor or parameters, and any consumer still reaching a shared accessor is named. Making the class instantiable while leaving one global getter satisfies the conversion and preserves the defect intact.
- The sharing decision is recorded per consumer with the reason it shares or does not. A run where every consumer got its own, or all got the same, skipped the decision the drill is about.
- The two independent instances are exercised together and each consumer's view is written down. What passes is the recorded contents, not the absence of a crash.

## Common Failures
- Making the class instantiable but still reaching a single shared instance through a global accessor.
- Injecting the same instance everywhere out of habit, recreating the shared-state problem.

## Notes
This drills Long's `ShoppingBasket` conversion from static global state to injected instances. The reflex it builds is to treat static mutable state as a reuse hazard, and to replace it with instances whose sharing you control explicitly through injection.
