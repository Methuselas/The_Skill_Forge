---
object_id: AP_design_a_customization_point
object_type: ap
name: Design a Customization Point
library_path:
- software-engineering
- languages
- cpp
- virtual-functions
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- virtual_functions
- polymorphism
- nvi
- strategy
cross_links:
- rel: supports
  target_object_id: PAT_match_virtualness_to_inherited_interface
- rel: supports
  target_object_id: PAT_externalize_varying_behavior_with_strategy
- rel: supports
  target_object_id: PAT_wrap_virtuals_with_nvi_idiom
- rel: supports
  target_object_id: PAT_never_redefine_inherited_non_virtual
- rel: supports
  target_object_id: PAT_never_redefine_inherited_default_parameter
- rel: supports
  target_object_id: PAT_give_a_polymorphic_class_a_virtual_clone
- rel: supports
  target_object_id: PAT_redesign_away_from_multiple_dispatch
- rel: supports
  target_object_id: PAT_price_virtual_dispatch_against_the_real_alternative
- rel: related_to
  target_object_id: AP_choose_the_relationship_between_two_types
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted C++ sources
confidence: high
references: []
variants: []
---

# Design a Customization Point

## Objective
Decide how a behavior that varies should be allowed to vary — which mechanism carries it, what a derived type may and may not change, and what surrounding context the base keeps control of. Success is that every extension point is deliberate, every non-extension point is closed, and a derived author cannot alter something the base was relying on.

## Steps / Flow

1. **Separate what varies from what does not.** Name the behavior that differs across types, and name the surrounding work that must happen identically every time — locking, logging, validation, before-and-after invariants. That second list is what decides between the mechanisms below.

2. *Gate.* **Ask whether the variation needs the object's type at all.** Where the behavior varies but need not be tied to the type, `PAT_externalize_varying_behavior_with_strategy` owns moving it out to a separate object. This exit is cheaper than everything below and is skipped far too often, because inheritance is the more familiar tool rather than the more suitable one.

3. **Decide what each declaration commits derived classes to.** `PAT_match_virtualness_to_inherited_interface` owns the mapping: a pure virtual commits derived types to supplying their own, a plain virtual supplies a default they may replace, and a non-virtual commits them to inheriting both the interface and the implementation unchanged.

4. **Branch — where the base must retain control of the context, wrap it.** `PAT_wrap_virtuals_with_nvi_idiom` owns the construction: a public non-virtual entry point that performs the invariant work and calls a non-public virtual for the varying part. This is the mechanism that makes step 1's second list enforceable rather than documented.

5. *Gate.* **Close the things that must not be redefined.** `PAT_never_redefine_inherited_non_virtual` owns why a non-virtual is a statement about invariant behavior that a derived redefinition silently breaks depending on the static type of the pointer used. `PAT_never_redefine_inherited_default_parameter` owns the related trap, where the default is resolved statically while the function is resolved dynamically, producing a call no author intended.

6. **Branch — where callers need a copy without knowing the real type, add the virtual that produces one.** `PAT_give_a_polymorphic_class_a_virtual_clone` owns it, and this is also the route for creating an object whose type is decided by input data.

7. *Recovery.* **Where behavior turns out to depend on the dynamic types of two operands, stop and redesign.** `PAT_redesign_away_from_multiple_dispatch` owns the alternatives. Every mechanism above dispatches on one type, so this is a signal that the shape is wrong rather than a case for a more elaborate hierarchy.

8. **Price the dispatch only when someone objects to it.** `PAT_price_virtual_dispatch_against_the_real_alternative` owns the comparison, and the alternative it must be priced against is the real one — a switch, a branch, a function pointer — rather than against nothing.

9. **Completion check.** Every varying behavior has exactly one mechanism; the invariant work runs on every path a derived type can reach; nothing non-virtual is redefined anywhere in the hierarchy; no virtual carries a default argument; and the extension points are the ones a derived author would guess.

## Notes
The two gates carry most of the value. Step 2 removes whole hierarchies that were never needed, and step 5 closes the two traps that are invisible at the call site and produce behavior that changes with the static type of a pointer — among the hardest defects in this area to diagnose from a symptom.

Step 4 is what turns step 1's separation into something the compiler helps enforce. Without it, "the derived class must call the base version first" is a comment, and comments are not a mechanism.

Choosing the relationship between the types comes before any of this. Where the hierarchy itself is in question rather than the extension points within it, that decision has its own protocol and should be settled first.
