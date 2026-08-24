---
object_id: AP_make_a_class_const_correct
object_type: ap
name: Make a Class const-Correct
library_path:
- software-engineering
- languages
- cpp
- const-correctness
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- const_correctness
- interface_design
- thread_safety
- mutable
cross_links:
- rel: supports
  target_object_id: PAT_apply_const_to_lock_invariants
- rel: supports
  target_object_id: PAT_use_logical_constness_with_mutable
- rel: supports
  target_object_id: PAT_make_const_member_functions_thread_safe
- rel: supports
  target_object_id: PAT_avoid_const_duplication_via_const_delegation
- rel: supports
  target_object_id: PAT_return_by_const_value_to_block_assignment
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted C++ sources
confidence: high
references: []
variants: []
---

# Make a Class const-Correct

## Objective
Take a class whose interface does not distinguish between operations that observe and operations that change, and produce one where that distinction is carried by the type system — so that callers holding a read-only reference can use everything they are entitled to, and nothing else. Success is that the compiler enforces the read/write split the design intended, and that no member function is const merely because it happened to compile.

## Steps / Flow

1. **Mark everything that should not change.** `PAT_apply_const_to_lock_invariants` owns the sweep across parameters, return values, locals, and pointer targets. Do this first and broadly: the compiler errors it produces are the inventory for everything below, and they are cheaper to read than a manual audit.

2. *Gate.* **Decide constness by what a client can observe, not by what the bits do.** A member that touches a cache, a memoized result, or a validity flag while changing nothing a caller can see is conceptually an observer. `PAT_use_logical_constness_with_mutable` owns that judgement and the mechanism for expressing it. Taking this decision per member is what stops the sweep in step 1 from being reverted one function at a time.

3. **Branch — where a const member does modify internal state, make it safe to call concurrently.** Two threads may hold const references to the same object and both call it, which the language permits and the class must survive. `PAT_make_const_member_functions_thread_safe` owns this, and it is the obligation that the previous step creates rather than an unrelated concern.

4. **Provide both overloads where callers need read and write access to the same thing.** Element access, and anything returning a reference into the object, typically needs one of each.

5. *Recovery.* **When the two overloads have the same body, remove the duplication in one direction only.** `PAT_avoid_const_duplication_via_const_delegation` owns it: the non-const version calls the const one and casts the constness off the result. The reverse direction casts away a guarantee the caller relied on, and is not the same trade.

6. **Decide what the return values permit.** `PAT_return_by_const_value_to_block_assignment` owns the case where a returned value has no business being assigned into, which closes a class of mistake at compile time rather than in review.

7. **Completion check.** Every observer is const; every const member is const for a reason you can state in terms of what a client sees; a const object supports everything a caller should be able to do with one; no pair of overloads duplicates a body; and two threads calling the same const member cannot corrupt each other.

## Notes
The order matters more than it looks. Running the sweep in step 1 before making the per-member judgement in step 2 is deliberate — the sweep generates the list of decisions to make, whereas deciding first and marking afterwards means auditing every member by hand and missing the ones that were already fine.

Step 3 exists because step 2 creates the obligation. A class that uses the mechanism for logical constness has taken on a concurrency responsibility whether or not it was thinking about threads, and that connection is easy to miss when the two rules are met separately.

The direction in step 5 is not symmetric and the asymmetry is the whole content of the step; the readable-looking alternative removes a guarantee instead of adding one.
