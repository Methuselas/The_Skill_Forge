---
object_id: PAT_return_by_value_when_returning_new_object
object_type: pattern
name: Return by Value When You Must Return a New Object
library_path:
- software-engineering
- languages
- cpp
- parameter-passing
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- parameter_passing
- return_values
- undefined_behavior
cross_links:
- rel: related_to
  target_object_id: PAT_return_by_const_value_to_block_assignment
- rel: related_to
  target_object_id: PAT_replace_nonlocal_statics_with_local_statics
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u04, pp. 90-94
  evidence_type: text
confidence: high
references: []
variants: []
---

# Return by Value When You Must Return a New Object

## Pattern Rule
**IF** a function must produce a brand-new object that did not exist before the call, such as operator*
**THEN** return it by value; never return a reference or pointer to a local object, a heap object, or a shared function-static.

## Do
- Return the new object by value and let the compiler's return-value optimization remove the copy where it can.
- Construct the result directly in the return statement, giving that optimization the best chance to apply.

## Don't
- Don't return a reference or pointer to a local object — it is destroyed when the function exits, leaving a dangling reference.
- Don't return a reference to a heap object — callers cannot delete what they cannot reach through the reference, so it leaks.
- Don't return a reference to a function-static — every call shares one object, making comparisons of two results always equal.

## Checklist
- Does this function create a new object that no existing reference could already name?
- Am I about to return a reference or pointer to a local, heap, or static object?
- Have I returned by value and left the efficiency to the compiler?

## Notes
Chasing pass-by-reference too far leads to returning references to objects that do not exist. For operator*, the local version dangles, the heap version leaks (no one can reach the pointer to delete it), and the single-static version makes `(a*b) == (c*d)` always true because both sides name the same static. The correct answer is to return a new object by value; return-value optimization often erases the cost, so correctness need not be sacrificed for speed.
