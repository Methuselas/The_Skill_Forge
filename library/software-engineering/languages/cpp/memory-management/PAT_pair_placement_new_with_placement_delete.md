---
object_id: PAT_pair_placement_new_with_placement_delete
object_type: pattern
name: Pair Every Placement new with a Matching Placement delete
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- placement_new
- exception_safety
cross_links:
- rel: related_to
  target_object_id: PAT_offer_an_exception_safety_guarantee
- rel: related_to
  target_object_id: AP_replace_new_and_delete_for_a_named_reason
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Pair Every Placement new with a Matching Placement delete

## Pattern Rule
**IF** you declare a placement operator new — one that takes extra parameters beyond the size
**THEN** also declare the matching placement operator delete with the same extra parameters, and keep the normal operator delete, or an exception from the constructor will leak the allocation.

## Do
- For a placement new taking extra arguments, write a placement delete with the identical extra arguments, so the runtime can undo the allocation when the constructor throws.
- Also provide the normal operator delete, because a later plain delete on the pointer always calls the normal version, never a placement one.

## Don't
- Don't declare a placement new without its matching placement delete; if the constructor throws, the runtime finds no delete to call and the memory leaks silently.

## Checklist
- Does each placement operator new have a placement operator delete with the same extra parameters?
- Is the normal operator delete also provided for ordinary delete calls?
- Have I confirmed that a throwing constructor triggers the placement delete?

## Notes
A new expression allocates, then constructs; if the constructor throws, the runtime must free the allocation, and it does so by calling the operator delete whose extra parameters match the operator new it used. A logging placement new taking an ostream needs an operator delete taking the same ostream, or a constructor exception leaks. The normal delete is still required, because applying plain delete to the pointer later never calls a placement delete — that path only fires on a constructor exception coupled to a placement new.
