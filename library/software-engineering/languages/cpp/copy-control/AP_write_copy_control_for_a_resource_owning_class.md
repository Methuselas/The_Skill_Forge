---
object_id: AP_write_copy_control_for_a_resource_owning_class
object_type: ap
name: Write the Copy Control for a Resource-Owning Class
library_path:
- software-engineering
- languages
- cpp
- copy-control
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- copy_control
- special_members
- rule_of_five
- exception_safety
cross_links:
- rel: supports
  target_object_id: PAT_understand_special_member_generation
- rel: supports
  target_object_id: PAT_know_compiler_generated_special_members
- rel: supports
  target_object_id: PAT_delete_the_functions_you_want_to_forbid
- rel: supports
  target_object_id: PAT_copy_all_members_and_base_parts
- rel: supports
  target_object_id: PAT_handle_self_assignment_in_copy_assignment
- rel: supports
  target_object_id: PAT_dont_implement_one_copying_function_via_the_other
- rel: supports
  target_object_id: PAT_return_reference_to_this_from_assignment
- rel: supports
  target_object_id: PAT_use_copy_and_swap_for_strong_guarantee
- rel: supports
  target_object_id: PAT_support_nonthrowing_swap
- rel: supports
  target_object_id: PAT_share_a_representation_until_a_write_forces_a_copy
- rel: related_to
  target_object_id: AP_give_an_acquired_resource_an_owner
- rel: supports
  target_object_id: PAT_choose_raii_copying_behavior_deliberately
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted C++ sources
confidence: high
references: []
variants: []
---

# Write the Copy Control for a Resource-Owning Class

## Objective
Take a class that owns something — memory, a handle, a lock, anything with a release — and give it a complete, correct set of copying and destruction operations, so that copying it does what the design says it should and no combination of aliasing, exceptions, or later edits produces a double release or a half-copied object. Success is that every special member is either written deliberately, defaulted deliberately, or deleted deliberately, and none of them arrived by accident.

## Steps / Flow

1. **Settle what copying is supposed to mean before writing a line.** Prohibited, reference counted, deeply copied, or ownership transferred — the four are different classes with different clients, not implementation variants. `PAT_choose_raii_copying_behavior_deliberately` owns the decision, and the rest of this flow is different depending on which one it produced.

2. **Work out what the compiler is already giving you.** `PAT_know_compiler_generated_special_members` owns what appears on demand and the cases where the compiler refuses.

3. *Gate.* **Work out what your own declarations suppress.** Declaring a destructor, a copy operation, or a move operation silently stops other members from being generated, which is how a class acquires an expensive copy where a move was intended. `PAT_understand_special_member_generation` owns the table; run it before writing, not after a performance surprise.

4. **Branch — if copying should be prohibited, stop here.** `PAT_delete_the_functions_you_want_to_forbid` owns the mechanism, including the reason the deleted declaration is public rather than private. The class is finished, and steps 5 through 9 do not apply.

5. **Branch — if copies should share until written to, take the counted route.** `PAT_share_a_representation_until_a_write_forces_a_copy` owns that design, and it replaces the deep copy the remaining steps assume rather than layering on top of it.

6. **Copy every member and every base part.** `PAT_copy_all_members_and_base_parts` owns this, including the part that is easiest to lose: a derived class must invoke the base's copying function explicitly, and neither the compiler nor the tests will complain about a partial copy that silently drops a field added next quarter.

7. **Make assignment safe when the source and the target are the same object.** Aliasing makes self-assignment real even where no caller would write it deliberately, and a resource-owning assignment that releases before it acquires will destroy the thing it was about to copy. `PAT_handle_self_assignment_in_copy_assignment` owns the fix.

8. **Provide a non-throwing swap, then use it for the strong guarantee.** `PAT_support_nonthrowing_swap` owns the three pieces a swap needs, and `PAT_use_copy_and_swap_for_strong_guarantee` owns turning it into an assignment that either completes or leaves the original untouched. This step subsumes step 7 when taken — a copy-and-swap assignment is self-assignment-safe by construction.

9. **Return a reference to the assigned-to object.** `PAT_return_reference_to_this_from_assignment` owns the convention, which matters for chaining and for the compound operators alongside it.

10. *Recovery.* **If the two copying functions have grown similar bodies, factor, do not delegate.** `PAT_dont_implement_one_copying_function_via_the_other` owns why calling one from the other is the wrong repair even though it removes the duplication.

11. **Completion check.** Every special member is deliberate; a copy of an owner releases exactly once; assignment survives aliasing; the guarantee the class offers on a failed assignment is one you can name; and adding a member later has an obvious place to be added in each function.

## Notes
The order is the whole technique. Steps 1 through 3 are decisions, and taking them after the code exists is what produces the classic half-finished result — a working copy constructor, an assignment operator that leaks on self-assignment, and a move that never happens because a destructor declaration quietly suppressed it.

The two branches at steps 4 and 5 are genuine exits, not variations. A class that forbids copying is complete at step 4, and most classes should reach that exit: prohibiting copying is a legitimate final answer rather than a failure to implement it.

Step 8 is worth taking even where step 7 already passed. Self-assignment safety and the strong guarantee are different properties, and copy-and-swap is the one construction that delivers both without a special case for aliasing.
