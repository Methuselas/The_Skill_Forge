---
object_id: DRILL_write_a_conforming_operator_new
object_type: drill
name: Write a Conforming Class-Specific operator new and delete
target_skill: Following the new/delete conventions — new-handler loop, zero-byte, wrong-size forwarding
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 3 rough
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- allocation
- conventions
cross_links:
- rel: related_to
  target_object_id: PAT_follow_new_delete_conventions
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u08, pp. 252-256
  evidence_type: text
confidence: high
references: []
variants: []
---

# Write a Conforming Class-Specific operator new and delete

## Practice Task
Write a class-specific operator new and operator delete that follow the required conventions.

## Target Skill
Implementing the new-handler loop, zero-byte handling, and wrong-size forwarding.

## Setup
No special setup required.

## Instructions
- In operator new, loop: attempt allocation, call the current new-handler on failure, and throw bad_alloc only when the handler pointer is null.
- Handle a zero-byte request, and forward any request whose size is not the class size to the global operator new.
- In operator delete, return immediately on a null pointer and forward wrong-sized blocks to the global operator delete.
- Give the class (used as a base) a virtual destructor so operator delete receives the correct size.

## Success Check
- operator new never returns without allocating, throwing, or looping via the handler; zero-byte and wrong-size requests are handled.
- operator delete is null-safe and forwards wrong-sized blocks to the global version.

## Common Failures
- Omitting the new-handler loop or the zero-byte handling.
- Forgetting that inheritance can call the base operator new with a derived object's larger size.

## Notes
This drills Item 51: the size test that forwards wrong-sized requests also subsumes the zero-byte case, since a class size is never zero, and a virtual destructor keeps the delete size correct.
