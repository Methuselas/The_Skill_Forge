---
object_id: PAT_use_multiple_inheritance_judiciously
object_type: pattern
name: Use Multiple Inheritance Judiciously
library_path:
- software-engineering
- languages
- cpp
- inheritance
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- multiple_inheritance
- virtual_inheritance
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_use_private_inheritance_judiciously
- rel: related_to
  target_object_id: PAT_minimize_compilation_dependencies
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Use Multiple Inheritance Judiciously

## Pattern Rule
**IF** you are considering inheriting from more than one base class
**THEN** prefer an equivalent single-inheritance design, and use multiple inheritance only for genuinely clean cases such as combining public inheritance of an interface with private inheritance of an implementation.

## Do
- Reach for MI in its legitimate form: publicly inherit an abstract Interface class to get the interface, and privately inherit a helper class to reuse its implementation (CPerson from IPerson and PersonInfo).
- Disambiguate a name inherited from two bases by qualifying the call with the base class name.
- When a diamond forms and the shared base's data should exist once, make it a virtual base class by having the intermediate classes inherit virtually.

## Don't
- Don't accept virtual inheritance's costs without need; it enlarges objects, slows access to virtual-base data, and complicates initialization — so avoid virtual bases unless required, and keep data out of them.
- Don't default to MI when a single-inheritance design is roughly equivalent; SI is simpler to use and understand, so push harder for it first.

## Checklist
- Is there an equivalent single-inheritance design I should prefer?
- If MI is used, is it the interface-plus-implementation combination rather than an accident?
- If a diamond exists, is the shared base virtual, and is it free of data?

## Notes
MI adds ambiguity (a name in two bases, resolved by qualifying) and the diamond problem, where a shared base is replicated unless made a virtual base — and virtual bases cost size, speed, and initialization complexity, so keep them dataless. Its clearest legitimate use is combining public inheritance of an Interface class (the interface to implement) with private inheritance of a class that helps implement it, as CPerson does with IPerson and PersonInfo. Prefer single inheritance when it is roughly equivalent; use MI only when it is genuinely the clearest design.
