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
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u02, pp. 57-60
  evidence_type: text
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
- Identify which members and base parts the current copying functions fail to copy.
- In the copy constructor, invoke the base copy constructor in the member initialization list.
- In the copy assignment operator, call the base class operator= before copying the derived members.
- Add a new member to the base class and list which copying functions must now change.

## Success Check
- A copied `PriorityCustomer` has its inherited name and date copied, not default-initialized.
- Adding a base member surfaces every copying function that needs updating.

## Common Failures
- Omitting the base call, so base parts are default-initialized (copy constructor) or left unchanged (assignment).
- Copying only the newly declared derived members and forgetting the inherited ones.

## Notes
This drills Item 12. The derived copying functions look complete but silently skip the base part, because a derived copying function never copies base members for you — you must call the base copying function explicitly.
