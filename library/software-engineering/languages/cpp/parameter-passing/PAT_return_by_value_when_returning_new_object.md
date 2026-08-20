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
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
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
- Construct the result directly in the return statement, giving that optimization the best chance to apply. Returning an unnamed temporary is more than a hint: since C++17 no copy or move is even *requested* in that form, so it is guaranteed rather than optimized away.
- Keep copy and move operations declared even when you expect every call to elide them. Elision happens after the code compiles, so a type with both deleted fails to compile at the return statement and never reaches the step that would have removed the calls.

## Don't
- Don't return a reference or pointer to a local object — it is destroyed when the function exits, leaving a dangling reference.
- Don't return a reference to a heap object — callers cannot delete what they cannot reach through the reference, so it leaks.
- Don't return a reference to a function-static — every call shares one object, making comparisons of two results always equal.
- Don't write `return std::move(local)` to guard against the optimization not happening. It defeats it: you asked for a move and you get one, where the optimization would have done no work at all. The guard is also unnecessary — where the optimization is possible and the compiler declines it, the language already requires it to look for a move constructor first and fall back to a copy.
- Don't count on copy or move constructors running just because the code appears to copy. Eliding them is the one case where a compiler may remove calls whose side effects are observable, so a constructor that logs or counts will under-report.

## Checklist
- Does this function create a new object that no existing reference could already name?
- Am I about to return a reference or pointer to a local, heap, or static object?
- Have I returned by value and left the efficiency to the compiler?

## Notes
Chasing pass-by-reference too far leads to returning references to objects that do not exist. For operator*, the local version dangles, the heap version leaks (no one can reach the pointer to delete it), and the single-static version makes `(a*b) == (c*d)` always true because both sides name the same static. The correct answer is to return a new object by value; return-value optimization often erases the cost, so correctness need not be sacrificed for speed.

How the optimization works explains the rules around it. The local variable, the unnamed
return value, and the caller's destination are three names for objects of one type that no
code can observe simultaneously, so the compiler builds all three in one place: the caller
allocates the storage, passes its address into the function, and the "local" is constructed
there. Nothing is returned because the result is already where it belongs. The function does
not need to be inlined or even in the same translation unit for this — the address travels
with the call.

Deleting a move constructor is not the same as never declaring one, and the difference bites
here. Overload resolution on return still finds a deleted move constructor, selects it as the
best match, and fails — so a type meant to be returned by value while copyable but not
movable must declare no move operations at all rather than deleted ones.
