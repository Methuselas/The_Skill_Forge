---
object_id: DRILL_convert_constructor_assignment_to_init_list
object_type: drill
name: Convert Constructor Body Assignments to an Initializer List
target_skill: Using the member initialization list in declaration order instead of body assignment
library_path:
- software-engineering
- languages
- cpp
- initialization
stage_binding: 3 rough
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- initialization
- constructors
- member_initialization
cross_links:
- rel: related_to
  target_object_id: PAT_initialize_members_with_init_list
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u01, pp. 27-30
  evidence_type: text
confidence: high
references: []
variants: []
---

# Convert Constructor Body Assignments to an Initializer List

## Practice Task
Start from an `ABEntry` constructor whose body assigns `theName`, `theAddress`, `thePhones`, and `numTimesConsulted`, and rewrite it to initialize those members properly.

## Target Skill
Moving member setup out of the constructor body and into the initialization list, in declaration order, including members that must be initialized there.

## Setup
No special setup required.

## Instructions
- Move each member from a body assignment into the member initialization list.
- Order the list to match the order the members are declared in the class.
- Add a `const` or reference member to the class and confirm it now compiles only when initialized through the list.
- Compare the two versions and note where the body-assignment form did redundant work.

## Success Check
- Class-type members are copy-constructed once rather than default-constructed and then assigned.
- The list order matches the declaration order.
- The `const`/reference member compiles only via the list, not by body assignment.

## Common Failures
- Leaving a built-in member such as `numTimesConsulted` off the list and then reading it while uninitialized.
- Assuming the order written in the list, rather than the declaration order, drives initialization.

## Notes
This makes the assignment-versus-initialization distinction concrete: the body-assignment version default-constructs the string and list members before overwriting them, work the initialization list skips. The added `const`/reference member shows the case where the list is not merely better but mandatory.
