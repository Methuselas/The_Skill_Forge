---
object_id: PAT_copy_all_members_and_base_parts
object_type: pattern
name: Copy Every Member and Base Part in Copying Functions
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
- inheritance
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_know_compiler_generated_special_members
- rel: related_to
  target_object_id: PAT_dont_implement_one_copying_function_via_the_other
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Copy Every Member and Base Part in Copying Functions

## Pattern Rule
**IF** you write your own copy constructor or copy assignment operator
**THEN** copy every data member and explicitly invoke the base class's copying function, and revisit them whenever you add a member or a base — the compiler will not warn you about a partial copy.

## Do
- In a derived copy constructor, name the base in the member initialization list, `Base(rhs)`; in a derived copy assignment, call `Base::operator=(rhs)` before copying the derived members.
- When you add a data member or a base class, update every copying function (and constructor) to include it.

## Don't
- Don't count on the compiler to flag a partial copy; once you write your own copying functions it stays silent even at maximum warnings, so a forgotten member or base is copied wrong.

## Checklist
- Does each copying function copy every data member this class declares?
- Does each derived copying function invoke the corresponding base copying function?
- After adding a member or base, did I update all copying functions?

## Notes
When you hand-write copying functions the compiler stops helping — the `Customer` example silently drops `lastTransaction` after it is added. Inheritance is the insidious case: `PriorityCustomer` copying functions that mention only `priority` leave the base `Customer` part default-initialized (copy constructor) or unchanged (assignment), because a derived copying function does not automatically copy base members. "Copy all parts" means all local members plus an explicit call to each base's copying function.
