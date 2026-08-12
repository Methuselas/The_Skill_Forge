---
object_id: DRILL_make_copy_assignment_self_and_exception_safe
object_type: drill
name: Make a Copy Assignment Operator Self- and Exception-Safe
target_skill: Writing a resource-owning copy assignment operator that survives self-assignment and allocation failure
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
- self_assignment
- exception_safety
cross_links:
- rel: related_to
  target_object_id: PAT_handle_self_assignment_in_copy_assignment
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u02, pp. 53-56
  evidence_type: text
confidence: high
references: []
variants: []
---

# Make a Copy Assignment Operator Self- and Exception-Safe

## Practice Task
Start from a `Widget` owning a raw `Bitmap` pointer whose assignment operator does `delete pb; pb = new Bitmap(*rhs.pb); return *this;`, and make it safe under self-assignment and allocation failure.

## Target Skill
Statement ordering and copy-and-swap for a safe resource-owning copy assignment operator.

## Setup
No special setup required.

## Instructions
- Reproduce the naive version and trace what happens when the same object is assigned to itself.
- Rewrite it to copy first: save the original pointer, allocate the new copy, then delete the original; return a reference to *this.
- Rewrite it a second time using copy-and-swap, and compare readability and efficiency.

## Success Check
- Assigning the object to itself leaves it holding a valid resource.
- If the allocation throws, the original object is unchanged.
- The operator returns *this and chaining works.

## Common Failures
- Deleting the current resource before copying the new one.
- Adding an identity test but leaving the exception-unsafe ordering underneath it.

## Notes
This drills Item 11: the delete-before-copy bug is fatal only under aliasing, and the copy-before-delete ordering fixes both self-assignment and exception safety at once. The identity test is an optional efficiency tweak, not the fix.
