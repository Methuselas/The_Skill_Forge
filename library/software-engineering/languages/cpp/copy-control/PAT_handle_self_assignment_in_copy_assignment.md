---
object_id: PAT_handle_self_assignment_in_copy_assignment
object_type: pattern
name: Make Copy Assignment Safe Under Self-Assignment
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
- self_assignment
- exception_safety
cross_links:
- rel: related_to
  target_object_id: PAT_return_reference_to_this_from_assignment
- rel: related_to
  target_object_id: AP_write_copy_control_for_a_resource_owning_class
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Make Copy Assignment Safe Under Self-Assignment

## Pattern Rule
**IF** you write a copy assignment operator that frees a resource before acquiring the new one
**THEN** make it safe when the source and target are the same object, because aliasing — `a[i] = a[j]`, `*px = *py`, a base reference bound to a derived object — means self-assignment really happens.

## Do
- Order the statements so the new resource is acquired before the old one is freed: remember the original pointer, point to a fresh copy of the source's resource, then delete the original.
- Add an identity test (return early when this equals the source's address) only when you expect self-assignment often enough to justify the branch, or use copy-and-swap.

## Don't
- Don't delete the current resource and then copy from the source; if the source is the same object, you have destroyed the very thing you were about to copy, leaving a pointer to freed memory.

## Checklist
- Called with the same object as source and target, does the object survive intact?
- Is the new resource acquired before the old one is released?
- Is the operator exception-safe, which usually makes it self-assignment-safe too?

## Notes
The classic bug (a `Widget` owning a `Bitmap*`) deletes `pb` and then copies from the source — fatal when they are the same object. The identity test at the top fixes self-assignment but not exception safety; reordering to copy-before-delete fixes both, and copy-and-swap is the idiomatic third option. Aiming for exception safety usually yields self-assignment safety for free, so it is increasingly common to solve the exception problem and let self-assignment fall out.
