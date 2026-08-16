---
object_id: PAT_use_traits_classes_for_type_info
object_type: pattern
name: Use Traits Classes for Compile-Time Type Information
library_path:
- software-engineering
- languages
- cpp
- traits
stage_binding: 2 block
lane_fit: both
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
  target_object_id: PAT_use_template_metaprogramming
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Use Traits Classes for Compile-Time Type Information

## Pattern Rule
**IF** you need behavior that depends on properties of a type, and it must work for built-in types too
**THEN** put the information in a traits class — a template with specializations, including one for pointers — and dispatch on it with overloaded worker functions, giving a compile-time if/else on types.

## Do
- Define a traits template exposing the information (an iterator's category), supplied by a nested typedef for user-defined types and by a pointer specialization for built-ins.
- Dispatch by writing overloaded worker functions that each take a different traits tag, plus a master function that passes the trait so overload resolution picks the right worker during compilation.

## Don't
- Don't branch on the type at runtime with a typeid if/else; it wastes runtime, bloats the executable, and can force code that is invalid for some types to be compiled.
- Don't nest the information only inside the type; that fails for built-ins like pointers, so keep the traits external to the type.

## Checklist
- Is the type information exposed by a traits template with a specialization for pointers?
- Is dispatch done by overloaded workers selected by a traits tag rather than a runtime typeid test?
- Does the design work for built-in types as well as user-defined ones?

## Notes
advance wants iterator arithmetic for random-access iterators and stepping otherwise — a decision about a type. Traits make that decision at compile time: iterator_traits exposes an iterator_category (via a nested typedef, and a pointer specialization for built-ins), and overloaded doAdvance workers tagged by category let overload resolution choose. The tag structs inherit (forward is-a input), so a worker written for the base tag also serves the derived category. This is the compile-time if/else that runtime typeid cannot match.
