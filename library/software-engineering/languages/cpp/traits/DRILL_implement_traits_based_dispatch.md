---
object_id: DRILL_implement_traits_based_dispatch
object_type: drill
name: Implement Traits-Based Compile-Time Dispatch
target_skill: Selecting an implementation at compile time with traits and overloaded workers
library_path:
- software-engineering
- languages
- cpp
- traits
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- traits
- templates
- compile_time
cross_links:
- rel: related_to
  target_object_id: PAT_use_traits_classes_for_type_info
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Implement Traits-Based Compile-Time Dispatch

## Practice Task
Implement an advance(iter, d) that uses iterator arithmetic for random-access iterators and iterative stepping for others, choosing the implementation at compile time.

## Target Skill
Dispatching on a type's traits via overloaded worker functions instead of a runtime type test.

## Setup
No special setup required.

## Instructions
- Read the iterator's category from iterator_traits (its iterator_category), which is available during compilation.
- Write overloaded doAdvance workers, one per iterator category tag, each using only the operations valid for that category (+= for random access, stepping for bidirectional and input).
- Write the master advance that constructs the category tag from the traits and passes it, letting overload resolution pick the worker.
- Confirm a bidirectional iterator compiles because its worker never uses +=.

## Success Check
- The random-access path uses += and the others step, with the choice made during compilation.
- Calling advance on a bidirectional iterator compiles, unlike a runtime typeid version.

## Common Failures
- Branching at runtime with typeid, which both wastes runtime and forces the invalid += branch to compile.
- Forgetting that the input-iterator worker also serves forward iterators through tag inheritance.

## Notes
This drills Items 47 and 48: the traits-plus-overloading dispatch is template metaprogramming — a compile-time if/else that keeps each type's code in a function using only that type's valid operations.
