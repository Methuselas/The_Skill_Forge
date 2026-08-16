---
object_id: PAT_make_interfaces_hard_to_misuse
object_type: pattern
name: Make Interfaces Easy to Use Correctly and Hard to Use Incorrectly
library_path:
- software-engineering
- languages
- cpp
- interface-design
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: PAT_make_code_hard_to_misuse
tags:
- cpp
- interface_design
- type_safety
- hard_to_misuse
cross_links:
- rel: related_to
  target_object_id: PAT_convey_usage_through_names_and_types
- rel: related_to
  target_object_id: PAT_design_a_class_as_type
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Make Interfaces Easy to Use Correctly and Hard to Use Incorrectly

## Pattern Rule
**IF** you design a function, class, or template interface
**THEN** shape it so incorrect uses fail to compile and correct uses are the path of least resistance — because when a reasonable client misuses an interface, the interface is partly to blame.

## Do
- Introduce distinct types to bar wrong-order or wrong-kind arguments; wrapping day, month, and year in separate types stops a `Date(30, 3, 1995)` call from compiling.
- Restrict what a type permits: const-qualify returns and values, and constrain valid values (predefined Month objects rather than raw ints).
- Remove client bookkeeping: have a factory return a smart pointer so callers cannot forget to release, and bind a custom deleter to head off wrong-release and cross-DLL errors.
- Keep your types consistent with the built-ins and with one another — every STL container has a size() — because consistency is what makes an interface easy to use.

## Don't
- Don't require clients to remember to do something — call a specific delete, pass arguments in a special order — because whatever they must remember, they can forget.

## Checklist
- Can a plausible wrong use of this interface be made not to compile?
- Does the interface rely on the client remembering a step, an order, or a cleanup?
- Does this type behave like the built-in types the client already knows?

## Notes
This is the C++ realization of making code hard to misuse: the type system is your primary ally, so lean on it. The `Date` example turns a positional-argument trap into a compile error via wrapper types; constrained Month values stop out-of-range input; a factory returning a shared pointer with a bound deleter removes the whole class of release mistakes. Consistency matters as much as any single trick — inconsistency imposes mental friction no IDE removes.
