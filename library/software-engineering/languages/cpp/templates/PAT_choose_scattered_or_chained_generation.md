---
object_id: PAT_choose_scattered_or_chained_generation
object_type: pattern
name: Choose Scattered or Chained Generation From a Type List
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- code_generation
- object_layout
- inheritance
cross_links:
- rel: related_to
  target_object_id: PAT_use_multiple_inheritance_judiciously
- rel: related_to
  target_object_id: PAT_lift_each_varying_design_decision_to_a_parameter
- rel: related_to
  target_object_id: PAT_keep_a_generic_accessor_out_of_the_type
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Choose Scattered or Chained Generation From a Type List

## Pattern Rule
**IF** you are generating one piece of a class per type in a list — a stored member, an interface function, an implementation of one
**THEN** decide between inheriting every generated piece independently and threading them into a single-inheritance chain, on whether callers must reach each piece directly or the object must stay small.

## Do
- Scatter — one base per type — when callers need to name a single generated piece and get at it. Every piece is then a base of the whole, so the conversion that reaches it is one the compiler already performs, and no lookup code is needed.
- Chain — each generated piece deriving from the next — when size is what matters. The whole object then carries one vtable pointer instead of one per polymorphic piece, and the difference grows with the list.
- Where you chain, require each generated unit to take its base as a parameter and derive from it. That requirement is what threads the chain, and it is the price the unit's author pays for the generation.
- Offer access by position, not only by the type. A list may legitimately name the same type twice, and every by-type route into the result is ambiguous the moment it does.

## Don't
- Don't treat the two layouts as an implementation detail to settle later. They differ in what a caller can convert to, so the choice is visible in the interface and changing it later breaks callers rather than just recompiling them.
- Don't offer only by-type access and assume duplicates are pathological. Three coordinates of the same numeric type is the ordinary case, not the corner one.
- Don't write the whole thing out by hand to control the layout. That recovers the size and loses the reason for generating it, which was that the list is the single place the set of types is stated.
- Don't assume the sizes are close. Every independently inherited piece that has a virtual function adds its own pointer, so the scattered form of a list of ten is measurably fatter than the chained form.

## Checklist
- Does any caller need to convert the whole to one generated piece by naming it?
- How many pointers does the resulting object carry, and did I count rather than assume?
- Can the same type appear twice in a legitimate list, and does access still work when it does?
- If I later change which layout is used, what breaks — a recompile, or callers?

## Notes
The trade is accessibility against size, and it is not a close call in either direction once the requirement is known. Independent bases make every generated piece a base of the result, so reaching one costs nothing at all; threading them makes the result a chain where only the outermost is directly a base, and the object shrinks to a single dispatch pointer.

The two combine well, and the combination is the usual answer for anything with an interface and an implementation: generate the abstract interface with independent bases so callers can convert to any single one, and generate the implementation as a chain so the concrete object stays small.

The idiom that builds an overload set by inheriting from a pack of callables is the scattered form, and its behavior follows from that directly — each callable is a base, so all of them contribute to one overload set. The positional-access problem is equally live: asking a standard tuple for the element of a given type is ill-formed when two elements share that type, which is exactly this constraint surfacing in the standard library.
