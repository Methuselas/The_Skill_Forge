---
object_id: PAT_give_polymorphic_base_a_virtual_destructor
object_type: pattern
name: Give Polymorphic Base Classes a Virtual Destructor
library_path:
- software-engineering
- languages
- cpp
- destructors
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- destructors
- inheritance
- polymorphism
cross_links:
- rel: related_to
  target_object_id: PAT_no_virtual_calls_in_constructors_or_destructors
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Give Polymorphic Base Classes a Virtual Destructor

## Pattern Rule
**IF** a class is a polymorphic base — clients delete or manipulate derived objects through base-class pointers or references, and it has virtual functions
**THEN** declare its destructor virtual, so deleting a derived object through a base pointer destroys the whole object instead of leaking the derived part.

## Do
- Add a virtual destructor to any class that has at least one virtual function.
- To make an abstract base that has no other pure virtual function, declare a pure virtual destructor and still provide its definition, since derived destructors call it.

## Don't
- Don't give a virtual destructor to a class that is not meant to be a polymorphic base; the added vptr enlarges every object and breaks layout compatibility with C.
- Don't inherit from a class whose destructor is non-virtual — including the standard string type and the STL containers — because deleting through a base pointer is undefined behavior.

## Checklist
- Does this class have any virtual function, and if so is its destructor virtual?
- Is this class genuinely a polymorphic base, or am I adding a vptr for nothing?
- Am I deriving from a type (string, a container) whose destructor is non-virtual?

## Notes
Deleting a derived object through a base pointer with a non-virtual destructor is undefined — typically the derived part is never destroyed, leaving a partially destroyed object that leaks. The rule of thumb is a virtual destructor if and only if the class has at least one virtual function; a gratuitous virtual destructor is as wrong as a missing one, because the vptr costs size and portability (the `TimeKeeper`/`Point` contrast). This applies only to *polymorphic* bases: non-polymorphic bases like `Uncopyable` need no virtual destructor.
