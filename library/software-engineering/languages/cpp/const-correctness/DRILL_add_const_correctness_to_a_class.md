---
object_id: DRILL_add_const_correctness_to_a_class
object_type: drill
name: Make a C++ Class Fully const-Correct
target_skill: Applying const across a C++ class interface, including const/non-const overloads and mutable
library_path:
- software-engineering
- languages
- cpp
- const-correctness
stage_binding: 3 rough
lane_fit: skill
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
  target_object_id: PAT_use_logical_constness_with_mutable
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Make a C++ Class Fully const-Correct

## Practice Task
Take a small mutable class — a `TextBlock` holding a `std::string`, with an `operator[]` and a `length()` — and make it const-correct.

## Target Skill
Applying const to member functions and return types, overloading on constness, using `mutable`, and delegating the non-const overload to the const one.

## Setup
No special setup required.

## Instructions
- Add a `const` overload of `operator[]` returning `const char&` and a non-const overload returning `char&`.
- Implement the non-const overload in terms of the const one: `static_cast` `*this` to `const`, call the const overload, then `const_cast` the const off the returned reference.
- Add a `length() const` that caches its result, and make the cache members `mutable` so it compiles.
- Mark every parameter and local that never changes `const`.

## Success Check
- A `const TextBlock` can call the read-only members, while writing through it fails to compile.
- No bounds-check or return logic is duplicated between the two `operator[]` overloads.
- `length()` compiles as `const` while updating its cache.

## Common Failures
- Casting in the wrong direction — the const overload calling the non-const one.
- Using a const iterator where a `const_iterator` was needed.
- Leaving a cache member non-const and then const-casting to update it, instead of declaring it `mutable`.

## Notes
This exercises the const member-function techniques from Item 3 together: overloading on constness, `mutable` for logical constness, and the one-directional delegation that removes duplication. If the const version ever needs a cast on `*this` to reach the non-const one, the delegation is backwards.
