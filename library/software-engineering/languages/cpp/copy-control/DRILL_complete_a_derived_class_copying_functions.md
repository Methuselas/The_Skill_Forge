---
object_id: DRILL_complete_a_derived_class_copying_functions
object_type: drill
name: Complete a Derived Class's Copying Functions
target_skill: Writing derived-class copying functions that copy base parts and every member
library_path:
- software-engineering
- languages
- cpp
- copy-control
stage_binding: 3 rough
lane_fit: skill
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
  target_object_id: PAT_copy_all_members_and_base_parts
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Complete a Derived Class's Copying Functions

## Practice Task
Given a base `Customer` (a name and a last-transaction date) and a derived `PriorityCustomer` (a priority) whose copying functions copy only `priority`, fix them so nothing is dropped.

## Target Skill
Copying every local member and invoking the base class's copying function from a derived class.

## Setup
No special setup required.

## Instructions
- Read the class declaration and list which members and base parts the current copying functions fail to copy.
- Copy an object and show the inherited parts default-initialized rather than copied.
- In the copy constructor, invoke the base copy constructor in the member initialization list.
- In the copy assignment operator, call the base class operator= before copying the derived members.
- State what happens instead when each of those two is omitted.
- State the relationship between the two copying functions, and why neither should be implemented by calling the other.
- Add a new member to the base class, name every copying function that must now change before consulting the compiler, then consult the compiler and compare the two lists.

## Success Check
- The members and base parts the original copying functions miss are listed before the fix, produced by reading the class declaration rather than by reading the copying functions, which is what omitted them in the first place.
- The failure is demonstrated: an object is copied and the inherited parts are shown default-initialized rather than copied. The compiler produces this silently, which is why an inspection is not enough.
- The base copy constructor is invoked in the member initialization list and the base assignment operator is called explicitly, and the run states what happens instead when each is omitted. The two omissions have different symptoms and only one of them is easy to see.
- A base member is actually added; every copying function needing a change is named before the compiler is consulted, and then the compiler is consulted. The gap between those two lists is the finding, because the compiler reports none of them.
- The run states the relationship between the two copying functions — why neither should be implemented by calling the other — rather than leaving them as parallel hand-written bodies whose agreement is a coincidence.

## Common Failures
- Omitting the base call, so base parts are default-initialized (copy constructor) or left unchanged (assignment).
- Copying only the newly declared derived members and forgetting the inherited ones.

## Notes
This drills Item 12. The derived copying functions look complete but silently skip the base part, because a derived copying function never copies base members for you — you must call the base copying function explicitly.
