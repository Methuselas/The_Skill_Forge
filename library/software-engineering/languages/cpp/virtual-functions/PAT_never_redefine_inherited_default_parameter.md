---
object_id: PAT_never_redefine_inherited_default_parameter
object_type: pattern
name: Never Redefine an Inherited Default Parameter Value
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
- default_parameters
- static_binding
cross_links:
- rel: related_to
  target_object_id: PAT_wrap_virtuals_with_nvi_idiom
- rel: related_to
  target_object_id: AP_design_a_customization_point
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Never Redefine an Inherited Default Parameter Value

## Pattern Rule
**IF** a derived class overrides a virtual function that carries a default parameter value
**THEN** do not change that default, because virtual functions are dynamically bound while default parameter values are statically bound.

## Do
- Keep the derived override's default identical to the base's, so a call through a base pointer or reference behaves consistently.
- When base and derived should share a default without duplicating it, use the NVI idiom: a non-virtual function supplies the default and calls a virtual with no default of its own.

## Don't
- Don't give the override a different default; calling the derived function through a base-typed pointer runs the derived body but uses the base's default, a combination almost no one intends.
- Don't duplicate the same default in every derived class as a workaround — a later change to the base default silently desynchronizes them.

## Checklist
- Does any virtual override change an inherited default parameter value?
- Would a call through a base pointer mix the derived body with the base default?
- Is a shared default expressed once (via NVI) rather than copied into every override?

## Notes
The object's dynamic type picks the function, but its static type picks the default argument — so a `Shape*` pointing to a Rectangle calls `Rectangle::draw` with Shape's default color, not Rectangle's. C++ binds defaults statically for runtime efficiency. Repeating the base default in each override "fixes" the mismatch but creates duplicated, drift-prone code; the clean solution is NVI, where a non-virtual function owns the default and forwards to a defaultless virtual.
