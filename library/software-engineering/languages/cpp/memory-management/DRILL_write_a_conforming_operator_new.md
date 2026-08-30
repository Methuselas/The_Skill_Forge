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
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
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
- The loop is checked for what ends it: allocation succeeding, the handler being null, or a throw. Each pass is accounted for, because a loop that spins forever once the handler stops freeing memory is the defect this shape is prone to.
- The zero-byte request is exercised and the run says what it was turned into, rather than recording that it was handled.
- A wrong-sized request is exercised and shown reaching the global version. This path appears only under inheritance, which is exactly why it goes untested.
- Deletion is called with a null pointer and with a wrong-sized block and both are shown safe. Null-safety concluded from reading the first line is how the wrong-size path gets skipped.
- The destructor is virtual, and the run states the consequence when it is not: the size handed to the delete is wrong, which routes a valid block to the global version and corrupts the accounting without any visible failure.

## Common Failures
- Omitting the new-handler loop or the zero-byte handling.
- Forgetting that inheritance can call the base operator new with a derived object's larger size.

## Notes
This drills Item 51: the size test that forwards wrong-sized requests also subsumes the zero-byte case, since a class size is never zero, and a virtual destructor keeps the delete size correct.
