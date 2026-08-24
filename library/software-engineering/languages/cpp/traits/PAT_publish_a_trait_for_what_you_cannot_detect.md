---
object_id: PAT_publish_a_trait_for_what_you_cannot_detect
object_type: pattern
name: Publish a Trait for the Property You Cannot Detect
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
- customization_point
- optimization
- generic_programming
cross_links:
- rel: related_to
  target_object_id: PAT_use_traits_classes_for_type_info
- rel: related_to
  target_object_id: PAT_use_template_metaprogramming
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Publish a Trait for the Property You Cannot Detect

## Pattern Rule
**IF** a generic routine could take a faster path when its argument type has some property, and no compile-time test can decide whether a given type has it
**THEN** define a trait that answers no by default, select the fast path from that trait, and document the trait as the place a user asserts the property for their own type.

## Do
- Default the trait to the conservative answer. An unfamiliar type must get the slow correct path without its author knowing this mechanism exists.
- Gate the fast path on the whole conjunction of what it requires, not on the trait alone — that every argument is the shape the fast path assumes, that the sizes agree, that the operation is meaningful — so a single true trait cannot enable it by itself.
- Route both paths through one entry point and select between separate implementations, so neither implementation contains code that is invalid for the other's types.
- Say in the trait's documentation what a user is promising by specializing it, in terms of the behavior that becomes legal rather than the optimization that becomes available.

## Don't
- Don't infer the property from something you can test that merely correlates with it. Being made only of fundamental members is not the same claim as being safe to copy bytewise, and the case where they diverge is the case that corrupts data.
- Don't make the fast path the default and ask users to opt out. Someone who never reads the documentation must land on correct behavior, and opting out is a decision nobody makes until after the bug.
- Don't let the trait be the only guard. A user asserting a property about their type has said nothing about whether the two types in this particular call are compatible with each other.

## Checklist
- Does an unknown type get the conservative path without anyone doing anything?
- Is every precondition of the fast path checked, or only the one the trait covers?
- Can a user turn the fast path on for their own type without editing this code?
- Does the trait's documentation state the promise being made rather than the speed being bought?

## Notes
This is the escape hatch for the gap between what a compiler can see and what a programmer knows. A routine can determine that a type is a pointer, that its target is fundamental, and that two sizes match; it cannot determine that a user's plain structure carries no invariant that a bytewise copy would violate. That knowledge exists, it is simply not in the type system, and the trait is where its owner deposits it.

The shape is worth recognizing because the standard library settled on the same one — the properties a library cannot deduce are exposed as traits with conservative defaults that a type's author specializes. A trait used this way is a customization point rather than a query, and the difference shows in who writes it: a query is answered by the library, and this is answered by whoever owns the type.

The conjunction matters as much as the trait. A fast path usually rests on several conditions at once, and the trait covers only the one that cannot be tested; leaving the others unchecked produces a routine that is correct for the types anyone tried and wrong for a combination nobody did.
