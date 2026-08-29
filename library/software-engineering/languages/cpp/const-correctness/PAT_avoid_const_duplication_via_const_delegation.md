---
object_id: PAT_avoid_const_duplication_via_const_delegation
object_type: pattern
name: Implement the Non-const Overload in Terms of the const One
library_path:
- software-engineering
- languages
- cpp
- const-correctness
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- const
- member_functions
- casting
cross_links:
- rel: related_to
  target_object_id: PAT_use_logical_constness_with_mutable
- rel: related_to
  target_object_id: AP_make_a_class_const_correct
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Implement the Non-const Overload in Terms of the const One

## Pattern Rule
**IF** a `const` and a non-const member function would have essentially identical bodies (bounds check, logging, then a return)
**THEN** have the non-const version call the const version — adding `const` to `*this` with `static_cast`, then stripping it from the result with `const_cast` — and never the other way around.

## Do
- In the non-const accessor, `static_cast` `*this` to a const reference, index it with the const overload, and `const_cast` the `const` off the returned reference — so the real work lives once, in the const overload.
- Use `static_cast` for the safe non-const-to-const conversion that selects the const overload, and `const_cast` only to remove `const` from the returned reference.

## Don't
- Don't let the const version call the non-const one: a const method promises not to change the object, and this direction risks exactly that, forcing a `const_cast` on `*this` that signals the danger.
- Don't call the accessor plainly from inside itself hoping to reach the other overload — you recurse forever; you must cast `*this` to pick the const version.

## Checklist
- Does the shared logic exist in exactly one place, the const overload?
- Does the non-const overload delegate via `static_cast`-then-`const_cast`, not the reverse?
- Did casting `*this` to const prevent accidental infinite recursion?

## Notes
Duplicating bounds checks, logging, and validation across both overloads invites bloat and drift. The safe cure is one-directional: the non-const overload delegates to the const one. It is safe because whoever called the non-const version already held a non-const object, so re-adding then removing `const` changes nothing they were promised. The reverse — const calling non-const — could mutate an object the const contract said it would not, so it is never the move.
