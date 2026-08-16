---
object_id: DRILL_pair_a_placement_new_with_placement_delete
object_type: drill
name: Pair a Placement new with a Placement delete and Restore Hidden Forms
target_skill: Matching placement new/delete and re-exposing standard new forms
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- placement_new
- name_hiding
cross_links:
- rel: related_to
  target_object_id: PAT_pair_placement_new_with_placement_delete
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Pair a Placement new with a Placement delete and Restore Hidden Forms

## Practice Task
Given a class with a logging placement operator new (taking an ostream) but only a normal operator delete, fix the memory leak when the constructor throws, and restore the standard new forms the class new hid.

## Target Skill
Declaring a placement delete matching a placement new, and re-exposing the standard forms.

## Setup
No special setup required.

## Instructions
- Reproduce the leak: construct an object with the placement new and have its constructor throw; observe that no delete runs.
- Add a placement operator delete taking the same ostream parameter; confirm it now runs on a constructor exception.
- Keep the normal operator delete for ordinary delete on the pointer.
- Re-expose the standard new forms hidden by the class new, using a base class of standard forms and using declarations.

## Success Check
- A throwing constructor after the placement new invokes the matching placement delete, so no memory leaks.
- Plain new and nothrow new still compile for the class.

## Common Failures
- Declaring a placement new without its matching placement delete.
- Forgetting that the class operator new hides the normal and nothrow forms.

## Notes
This drills Item 52: the runtime undoes a failed placement new only via the placement delete with matching extra parameters, and any class operator new hides the standard forms until you bring them back.
