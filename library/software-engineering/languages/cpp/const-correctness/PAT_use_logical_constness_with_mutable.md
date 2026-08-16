---
object_id: PAT_use_logical_constness_with_mutable
object_type: pattern
name: Make Member Functions const for Logical, Not Bitwise, Constness
library_path:
- software-engineering
- languages
- cpp
- const-correctness
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- const
- member_functions
- mutable
cross_links:
- rel: related_to
  target_object_id: PAT_apply_const_to_lock_invariants
- rel: related_to
  target_object_id: PAT_avoid_const_duplication_via_const_delegation
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Make Member Functions const for Logical, Not Bitwise, Constness

## Pattern Rule
**IF** a member function does not change anything a client can observe about the object
**THEN** declare it `const`, and mark any internal-only members it must update — caches, validity flags — as `mutable`, so `const` means logically unchanged rather than bitwise-frozen.

## Do
- Overload accessors on constness: give a class both `const char& operator[](std::size_t) const` and `char& operator[](std::size_t)` so const and non-const objects are served correctly.
- Declare cached members such as `textLength` and `lengthIsValid` as `mutable`, so a `length() const` method can memoize its result without a cast.

## Don't
- Don't accept bitwise constness as your design standard: a member that only changes what a pointer points to passes the compiler's check yet can turn a const object's `"Hello"` into `"Jello"`.
- Don't cast away `const` to sneak in an internal modification; declare the member `mutable` instead.

## Checklist
- Does this const method change anything a client can detect? If not, is it declared const?
- Are internal-only members it updates declared `mutable` rather than const-cast?
- Where const and non-const callers need different results, have I overloaded on constness?

## Notes
C++ enforces bitwise constness — a const member function may not assign to non-static data members — but that is too crude: a function can be bitwise const and still change observable state through a pointer, or need to update a private cache while staying observably const. Meyers' rule is to design for logical constness and use `mutable` to free the genuinely internal members from the bitwise rule. The `CTextBlock` length cache is the anchor: it must update `textLength` and `lengthIsValid` inside a const method, which only compiles once those members are `mutable`.
