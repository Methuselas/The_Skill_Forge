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
- Add a placement operator delete taking the same ostream parameter, and check that its parameters match the placement new's beyond the first.
- Run the exception path again and show the matching delete executing.
- Keep the normal operator delete for ordinary delete on the pointer, and exercise ordinary deletion separately.
- Re-expose the standard new forms hidden by the class new, using a base class of standard forms and using declarations, then compile a call to each — plain and nothrow both.

## Success Check
- The leak is reproduced by making the constructor throw, with the absent release observed rather than reasoned about.
- The placement delete's parameters are checked to match the placement new's beyond the first. A near-match is silently never called and reproduces the original leak exactly, with code that reads as correct.
- The exception path is run again after the addition and the matching delete is shown to execute.
- Ordinary deletion is exercised separately, because the placement pair and the normal path are different routes and repairing one routinely conceals the other.
- The standard forms hidden by the class's own declaration are re-exposed and each is compiled, plain and nothrow both. The check is a call that compiles, not the presence of a using declaration.

## Common Failures
- Declaring a placement new without its matching placement delete.
- Forgetting that the class operator new hides the normal and nothrow forms.

## Notes
This drills Item 52: the runtime undoes a failed placement new only via the placement delete with matching extra parameters, and any class operator new hides the standard forms until you bring them back.
