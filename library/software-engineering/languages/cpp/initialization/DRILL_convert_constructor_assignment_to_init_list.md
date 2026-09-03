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
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
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
- Order the list to match the order the members are declared in the class, checking it against the class declaration rather than against itself.
- Name concretely, for at least one member, the redundant work the body-assignment form did — default-constructed and then assigned, so two operations run where one would serve — and identify the members that gain nothing.
- Check any member whose initializer reads another member against the declaration order.
- Add a `const` or reference member to the class, compile the body-assignment form, and record the error; then confirm it compiles when initialized through the list.

## Success Check
- The redundant work is named concretely for at least one member — default-constructed and then assigned, so two operations run where one would serve. Asserting that the list is more efficient, without saying what is avoided, restates what everyone already believes.
- The list order is checked against the class declaration rather than against itself. Members initialize in declaration order whatever the list says, so a reordered list is a statement that is not true and may draw no warning.
- A const or reference member is actually added and the body-assignment form shown failing to compile, with the error recorded. This is the case that turns a preference into a rule.
- The members that gain nothing are identified as well, so the run separates what this fixes from what it merely tidies.
- Any member whose initializer reads another member is checked against the declaration order, because that is where a correct-looking list quietly produces a garbage value.

## Common Failures
- Leaving a built-in member such as `numTimesConsulted` off the list and then reading it while uninitialized.
- Assuming the order written in the list, rather than the declaration order, drives initialization.

## Notes
This makes the assignment-versus-initialization distinction concrete: the body-assignment version default-constructs the string and list members before overwriting them, work the initialization list skips. The added `const`/reference member shows the case where the list is not merely better but mandatory.
