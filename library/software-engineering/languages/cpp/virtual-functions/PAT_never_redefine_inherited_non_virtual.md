---
object_id: PAT_never_redefine_inherited_non_virtual
object_type: pattern
name: Never Redefine an Inherited Non-Virtual Function
library_path:
- software-engineering
- languages
- cpp
- virtual-functions
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- virtual_functions
- static_binding
- inheritance
cross_links:
- rel: related_to
  target_object_id: PAT_match_virtualness_to_inherited_interface
- rel: related_to
  target_object_id: PAT_give_polymorphic_base_a_virtual_destructor
- rel: related_to
  target_object_id: AP_design_a_customization_point
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Never Redefine an Inherited Non-Virtual Function

## Pattern Rule
**IF** you are tempted to give a derived class its own version of a non-virtual function it inherits
**THEN** don't — non-virtual functions are statically bound, so the same object behaves differently depending on the static type of the pointer or reference used to call it.

## Do
- Leave inherited non-virtual functions alone; if a derived class must behave differently, make the function virtual in the base instead.
- Reconsider the design when you feel the urge: either the relationship is not really is-a, or the function is not really an invariant over specialization.

## Don't
- Don't redefine a non-virtual `mf` in the derived class; calling through a base pointer runs `Base::mf` and through a derived pointer runs `Derived::mf`, on the very same object.
- Don't declare a non-virtual destructor in a polymorphic base — a derived destructor then redefines an inherited non-virtual function, which is the same error in a particularly damaging form.

## Checklist
- Does a derived class redefine any function that is non-virtual in the base?
- If different behavior is needed, should the base function be virtual, or is the is-a relationship itself wrong?
- Is every polymorphic base's destructor virtual, so it is not silently redefined?

## Notes
Non-virtual means statically bound, so `pB->mf()` and `pD->mf()` invoke different functions for one object depending only on the pointer's declared type — inconsistent and surprising. There is also a theory argument: a non-virtual function is an invariant over specialization, and public inheritance is is-a, so redefining it means either the function should have been virtual or the class should not inherit publicly. Item 7's virtual-destructor rule is a special case of this one.
