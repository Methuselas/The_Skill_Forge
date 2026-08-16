---
object_id: PAT_avoid_global_state_inject_shared_state
object_type: pattern
name: Avoid Global State; Dependency-Inject Shared State
library_path:
- software-engineering
- core
- reusability
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- global_state
- reusability
- dependency_injection
- encapsulation
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_reusable_and_generalizable
- rel: related_to
  target_object_id: PAT_use_dependency_injection
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Avoid Global State; Dependency-Inject Shared State

## Pattern Rule
**IF** several parts of a program need to share some state
**THEN** hold that state in instances of a class and dependency-inject the instance where needed, rather than storing it in global (static) state that every part of the program shares.

## Do
- Make the state instance-scoped: change a `ShoppingBasket` from static variables and functions to an instantiable class where each instance has its own distinct contents.
- Inject the instance into exactly the classes meant to share it, so you control which code shares one basket and which uses a separate one.
- Use separate instances to make reuse safe: one basket for normal products and one for fresh products never interfere, and each view widget shows only its own basket.

## Don't
- Don't put shared state in a global variable to make it convenient to reach; two features using the same global basket silently pollute each other's contents.
- Don't assume "only one of these will ever exist at a time"; that assumption is exactly what breaks when the code is reused, making global-state code essentially impossible to reuse safely.

## Checklist
- Is the shared state static/global, so every caller sees the same single copy?
- Can two independent uses of this code run without interfering through shared state?
- Is the state injected so you control precisely which code shares which instance?

## Notes
Global state encodes a particularly costly assumption — that a single shared copy is always what everyone wants — and Long's `ShoppingBasket` shows it collapsing the moment two parts of the app need independent baskets. Converting the static class to instance state plus dependency injection makes each basket self-contained and reuse safe. This is why the chapter treats global state as best avoided in most scenarios, and it leans directly on the dependency-injection technique from chapter 8.
