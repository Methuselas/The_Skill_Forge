---
object_id: PAT_use_public_inheritance_only_for_is_a
object_type: pattern
name: Use Public Inheritance Only for an Is-A Relationship
library_path:
- software-engineering
- languages
- cpp
- inheritance
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- inheritance
- is_a
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_composition_over_inheritance
- rel: related_to
  target_object_id: PAT_model_has_a_with_composition
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Use Public Inheritance Only for an Is-A Relationship

## Pattern Rule
**IF** you are considering deriving one class publicly from another
**THEN** do it only when every derived object truly is-a base object and is substitutable for one everywhere a base is expected, because public inheritance asserts that everything true of the base is true of the derived.

## Do
- Confirm the substitutability before deriving: anywhere a base reference or pointer is accepted, a derived object must work correctly.
- When a real-world "is-a" has exceptions, restructure the hierarchy to model reality — split a non-flying Penguin off from a FlyingBird rather than inheriting a fly() it cannot honor.
- Prefer a design that rejects invalid use at compile time (no fly() for Penguin) over one that only reports it at runtime.

## Don't
- Don't force an is-a that breaks base invariants: a Square is-a Rectangle mathematically, but `makeBigger` changing width independent of height is valid for a rectangle and invalid for a square, so the inheritance is wrong.
- Don't override an inherited operation to throw a runtime error to "remove" it — that says the operation is allowed but erroneous, not that it is disallowed.

## Checklist
- Is every derived object usable wherever a base object is expected?
- Does any operation valid on the base violate an invariant of the derived (Square/Rectangle)?
- Is an invalid use rejected at compile time rather than only at runtime?

## Notes
Public inheritance means is-a — the single most important rule in C++ OOP. The Penguin/Bird and Square/Rectangle examples show the two failure modes: a derived class that cannot honor an inherited operation, and one where a base invariant does not hold for the derived. When the relationship is really has-a or is-implemented-in-terms-of, use composition or private inheritance instead; forcing is-a compiles but does not work.
