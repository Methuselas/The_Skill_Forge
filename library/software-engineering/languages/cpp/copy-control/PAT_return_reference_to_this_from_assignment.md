---
object_id: PAT_return_reference_to_this_from_assignment
object_type: pattern
name: Return a Reference to *this from Assignment Operators
library_path:
- software-engineering
- languages
- cpp
- copy-control
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- copy_control
- operators
- convention
cross_links:
- rel: related_to
  target_object_id: PAT_handle_self_assignment_in_copy_assignment
- rel: related_to
  target_object_id: AP_write_copy_control_for_a_resource_owning_class
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Return a Reference to *this from Assignment Operators

## Pattern Rule
**IF** you implement a copy assignment operator or a compound assignment such as `+=` or `*=`
**THEN** return a reference to *this, so assignments chain the way they do for built-in types and the standard library.

## Do
- End the operator with `return *this;` and declare its return type a reference to the class.
- Apply the same convention to every assignment form, including operators whose parameter is not the class type.

## Don't
- Don't return void or a copy from an assignment operator; it compiles, but chaining like `a = b = c` breaks and the type stops matching the convention every built-in and standard type follows.

## Checklist
- Does each assignment operator return a reference to *this?
- Does chaining (a = b = c) work on this type?

## Notes
Assignment is right-associative, so `x = y = z = 15` assigns 15 to z, then the updated z to y, then to x — which only works if each assignment yields a reference to its left-hand object. Every built-in type and every standard-library type (string, vector, shared_ptr) follows this, so a type that does not is gratuitously inconsistent. It is only a convention — code that breaks it compiles — but there is rarely a good reason to.
