---
object_id: PAT_use_template_metaprogramming
object_type: pattern
name: Reach for Template Metaprogramming to Move Work to Compile Time
library_path:
- software-engineering
- languages
- cpp
- metaprogramming
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- metaprogramming
- compile_time
- templates
cross_links:
- rel: related_to
  target_object_id: PAT_use_traits_classes_for_type_info
- rel: related_to
  target_object_id: PAT_prefer_const_and_enum_to_define
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u07, pp. 233-238
  evidence_type: text
confidence: high
references: []
variants: []
---

# Reach for Template Metaprogramming to Move Work to Compile Time

## Pattern Rule
**IF** a computation or a type-dependent choice can be resolved during compilation
**THEN** consider template metaprogramming — traits plus overloading for compile-time branching, recursive template instantiation for loops — to shift work from runtime to compile time, gaining earlier error detection and efficiency.

## Do
- Prefer the traits-and-overloading dispatch over a runtime typeid test; it splits code per type, so each branch uses only operations valid for its type.
- Express a compile-time loop as recursive template instantiation with a specialization as the base case (a Factorial template holding its result in an enum-hack value).
- Reach for TMP where it pays: enforcing dimensional-unit correctness, expression templates that fuse matrix loops, and policy-based design that generates custom implementations.

## Don't
- Don't force a single runtime function to hold code invalid for some types (a += on a bidirectional iterator); the compiler must validate every branch, even unexecuted ones, so it fails to compile.
- Don't adopt TMP casually; the syntax is unintuitive, tool support is weak, and compile times grow.

## Checklist
- Can this type test or computation move to compile time via traits/overloading or recursive instantiation?
- Does splitting per type avoid emitting code that is invalid for some instantiations?
- Is the added complexity and compile-time cost justified by the benefit here?

## Notes
The runtime typeid version of advance both wastes runtime and fails to compile for a bidirectional iterator, because the compiler must validate the += branch it will never take; the traits-based version compiles because each type's code lives in a separate overload. TMP is Turing-complete: loops become recursive instantiations (Factorial referencing Factorial of n-1, terminating at a specialization), variables become enum-hack values. Its wins — dimensional units, expression templates, policy-based design — buy earlier errors and speed at the cost of compile time and difficulty.
