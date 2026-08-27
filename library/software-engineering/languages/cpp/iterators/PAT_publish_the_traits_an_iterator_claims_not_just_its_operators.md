---
object_id: PAT_publish_the_traits_an_iterator_claims_not_just_its_operators
object_type: pattern
name: Publish the Traits an Iterator Claims, Not Just Its Operators
library_path:
- software-engineering
- languages
- cpp
- iterators
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- iterators
- traits
- interface_design
cross_links:
- rel: related_to
  target_object_id: PAT_use_traits_classes_for_type_info
- rel: related_to
  target_object_id: PAT_program_to_a_templates_implicit_interface
- rel: related_to
  target_object_id: PAT_constrain_a_template_so_the_error_lands_at_the_call
- rel: related_to
  target_object_id: PAT_state_the_guarantees_a_function_can_honor
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Publish the Traits an Iterator Claims, Not Just Its Operators

## Pattern Rule
**IF** you are writing a type that other code will drive as an iterator
**THEN** publish the trait aliases that say what it is — what dereferencing yields, how distances between positions are spelled, which category of movement it supports — alongside the operators that make it work, because a range-based loop needs only the operators while every algorithm interrogates the traits
**ELSE** where the type will only ever be driven by a loop in the same file, the operators alone are sufficient and the aliases are ceremony.

## Do
- Know that there are two tiers and which one you have satisfied. A range-based loop expands to a begin, an end, a not-equal comparison, a prefix increment, and a dereference — five operations and no questions. An algorithm asks the type about itself before it does anything, and a type that answers nothing is not an iterator as far as the algorithm is concerned, however well it drives a loop.
- Expect the first tier to pass silently and the second to fail late. The type iterates correctly from the day it is written, so nothing suggests it is incomplete; the first algorithm call may come months later, and the diagnostic arrives as a cascade from inside the library naming instantiations rather than naming the omission.
- Treat variation between implementations as the hazard rather than an inconvenience. How much a library checks, and which aliases it consults, differs by implementation and by version — so the same iterator compiles under one toolchain and fails under another with nothing in your code having changed, and the toolchain that accepted it taught you the wrong lesson.
- Name the category honestly, because it is the one alias that is a claim rather than a formality. An algorithm selects its strategy from the category — stepping or jumping, one pass or several — so claiming a stronger category than the operators support yields code that compiles and then behaves wrongly, which is worse than the failure you were trying to fix.
- Put the aliases at the top of the public interface where they read as the type's declaration of what it is. Buried among the operators they are easy to omit, and an omission is invisible until something interrogates them.

## Don't
- Don't conclude from "the loop works" that the type is an iterator. The loop is the weakest consumer there is, and passing it is the least the type can do.
- Don't paste the alias block from another iterator without re-deciding the category. The other aliases follow from the value type; the category is a judgement about this type's operators, and copying it is how a false claim gets made silently.
- Don't add aliases to make an error go away. The error says the algorithm could not learn what it needed; the fix is to tell it the truth, and an alias chosen to satisfy the compiler is a claim nobody checked.

## Checklist
- Will anything other than a loop in this file drive this type?
- Are the value type, the difference type, and the category all published?
- Is the declared category one the operator set actually supports, or the one that made the error go away?
- Has this been compiled against more than one standard library implementation?

## Notes
The idea underneath this is that an iterator is a protocol rather than a kind of pointer. Nothing requires one to point at stored memory, which is precisely why an adapter can present the interface while inserting into a container, and why a generator can present it while computing values that were never stored anywhere. The syntax was modelled on pointers so that algorithms would work on raw buffers as well as containers, but the resemblance is a convenience and not a constraint.

That freedom is what makes the traits necessary. Where an iterator really is a pointer, everything an algorithm needs can be recovered from the pointer type itself. Once the type is free to be anything that supplies the operations, the operations alone stop carrying the information — nothing about having a dereference operator says what dereferencing yields, and nothing about having an increment says whether the type can also step backwards or jump. The aliases exist because the protocol has to be stated by types that are not pointers, and forgetting them produces a type that behaves like an iterator right up until something asks it what it is.
