---
object_id: PAT_match_virtualness_to_inherited_interface
object_type: pattern
name: Match a Function's Virtual-ness to What Derived Classes Must Inherit
library_path:
- software-engineering
- languages
- cpp
- virtual-functions
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- virtual_functions
- interface_design
- inheritance
cross_links:
- rel: related_to
  target_object_id: PAT_never_redefine_inherited_non_virtual
- rel: related_to
  target_object_id: PAT_wrap_virtuals_with_nvi_idiom
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Match a Function's Virtual-ness to What Derived Classes Must Inherit

## Pattern Rule
**IF** you declare a member function in a base class
**THEN** choose pure virtual, simple virtual, or non-virtual to say exactly what derived classes inherit — interface only, interface plus an overridable default, or interface plus a mandatory implementation.

## Do
- Declare a pure virtual function when derived classes must supply their own implementation and the base has no sensible default (Shape::draw).
- Declare a simple virtual function when there is a reasonable default derived classes may override (Shape::error).
- Declare a non-virtual function when the behavior is an invariant over specialization that no derived class should change (Shape::objectID).
- Mark every function you intend as an override with the `override` keyword, and let the compiler check that it is one. Overriding requires the base function to be virtual and the names, parameter types, constness, return types, exception specifications, and — since C++11 — reference qualifiers all to match. Miss any one and you have silently declared a new function that the base interface will never call; the keyword turns that into a compile error.

## Don't
- Don't give a simple virtual both an interface and a silently-inherited default when forgetting to override is dangerous; sever them — make it pure virtual and offer the default as a separate protected `defaultFly`, or as a definition of the pure virtual that derived classes call explicitly — so a new ModelC cannot inherit the wrong behavior by accident.
- Don't reflexively make everything non-virtual (no room to specialize) or everything virtual (no invariants); each extreme is a common beginner mistake.

## Checklist
- For each base function, have I decided: interface only, interface plus default, or interface plus mandatory implementation?
- Where a default exists, must derived classes opt in explicitly rather than inherit it silently?
- Are functions that represent an invariant over specialization non-virtual, and customization points virtual?

## Notes
Public inheritance always inherits the interface; the declaration kind decides what else. The Airplane fly() trap is the key lesson: a simple virtual with a default let ModelC silently fly like a ModelA. Severing interface from default — pure virtual `fly` plus protected `defaultFly`, or a defined pure virtual called explicitly — forces each derived class to opt in. Choosing deliberately among pure/simple/non-virtual is how you state precisely what you want inherited.
