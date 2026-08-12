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
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u09, pp. 246-252
  evidence_type: text
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
2. Show the interference: two features both adding to the basket see each other's items, making safe reuse impossible.
3. Convert the class to be instantiable, giving each instance its own distinct state.
4. Inject an instance into each class that needs it, choosing deliberately which classes share one instance and which get their own.
5. Create two independent instances (say, a normal-products basket and a fresh-products basket) and confirm each consumer sees only its own.

## Success Check
- No static state remains; each instance holds its own copy.
- Consumers receive the instance by injection rather than reaching a global.
- Two independent instances operate without interfering.

## Common Failures
- Making the class instantiable but still reaching a single shared instance through a global accessor.
- Injecting the same instance everywhere out of habit, recreating the shared-state problem.

## Notes
This drills Long's `ShoppingBasket` conversion from static global state to injected instances. The reflex it builds is to treat static mutable state as a reuse hazard, and to replace it with instances whose sharing you control explicitly through injection.
