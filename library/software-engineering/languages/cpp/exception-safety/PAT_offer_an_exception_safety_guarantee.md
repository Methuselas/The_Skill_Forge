---
object_id: PAT_offer_an_exception_safety_guarantee
object_type: pattern
name: Offer a Definite Exception-Safety Guarantee
library_path:
- software-engineering
- languages
- cpp
- exception-safety
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- exception_safety
- resource_management
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: PAT_use_copy_and_swap_for_strong_guarantee
- rel: related_to
  target_object_id: AP_make_a_function_exception_safe
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Offer a Definite Exception-Safety Guarantee

## Pattern Rule
**IF** you write a function that could throw or that calls something that throws
**THEN** make it leak no resources and corrupt no data, and offer one of the three guarantees on purpose — basic (a valid state), strong (state unchanged on failure), or nothrow — choosing the strongest that is practical.

## Do
- Use RAII objects — a lock guard, a smart pointer — so resources are released even when an exception is thrown.
- Reorder so you do not record that something happened until it actually has, such as incrementing a change counter only after the change succeeds.
- Document the guarantee each function offers; it is part of the function's interface, chosen as deliberately as any other part.

## Don't
- Don't offer a guarantee stronger than the weakest guarantee of the functions you call — a function is only as exception-safe as its callees.
- Don't assume an empty exception specification means nothrow; the guarantee comes from the implementation, not the declaration.

## Checklist
- On a thrown exception, does this function leak a resource or leave data corrupted?
- Which guarantee — basic, strong, or nothrow — does it offer, and is it the strongest practical one?
- Is that guarantee no stronger than the weakest callee's, and is it documented?

## Notes
The naive `changeBackground` fails both requirements: if constructing the new image throws, the manually locked mutex leaks and `bgImage` is left dangling with the counter already bumped. RAII (a Lock) removes the leak; reordering removes the corruption. Then choose a guarantee deliberately — nothrow where you can, otherwise strong, otherwise basic — remembering that a function can be no stronger than its weakest callee, and that an exception specification says nothing about which guarantee holds.
