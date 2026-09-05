---
object_id: AP_make_a_function_exception_safe
object_type: ap
name: Make a Function Exception-Safe
library_path:
- software-engineering
- languages
- cpp
- exception-safety
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: AP_decide_how_to_signal_and_handle_an_error
tags:
- cpp
- exception_safety
- guarantees
- raii
- copy_and_swap
cross_links:
- rel: supports
  target_object_id: PAT_offer_an_exception_safety_guarantee
- rel: supports
  target_object_id: PAT_give_every_constructor_resource_a_self_releasing_owner
- rel: supports
  target_object_id: PAT_use_copy_and_swap_for_strong_guarantee
- rel: supports
  target_object_id: PAT_catch_exceptions_by_reference_and_rethrow_bare
- rel: supports
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: AP_decide_how_to_signal_and_handle_an_error
- rel: supports
  target_object_id: PAT_support_nonthrowing_swap
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted C++ sources
confidence: high
references: []
variants: []
---

# Make a Function Exception-Safe

## Objective
Take a function that can throw, or that calls something that can, and bring it to a stated guarantee — leaking nothing, corrupting nothing, and either leaving the program in a valid state or leaving it exactly as it was. Success is that the guarantee is one you chose and can name, rather than whatever the current arrangement of statements happens to deliver.

## Steps / Flow

1. **Find every point the function can leave from.** Not just the `throw` statements: every call that might throw is an exit, and in most functions those outnumber the visible returns. This inventory is the entry state for everything below.

2. **Close the leaks first, before considering guarantees.** A function that leaks cannot offer any guarantee at all, so resource ownership is the prerequisite rather than a parallel concern. `PAT_manage_resources_with_raii_objects` owns handing each acquisition to something that releases itself, and `AP_give_an_acquired_resource_an_owner` owns the full flow when the resource needs a bespoke manager.

3. **Close the constructor case separately.** A constructor that throws part-way leaves an object whose destructor never runs, so anything it already acquired is stranded. `PAT_give_every_constructor_resource_a_self_releasing_owner` owns this; the class destructor cannot.

4. *Gate.* **Choose the guarantee deliberately, and choose it against what your callees offer.** `PAT_offer_an_exception_safety_guarantee` owns the choice among basic, strong, and nothrow. The constraint that decides it: a function cannot offer the strong guarantee if it must commit to something whose own guarantee is only basic. Discover that here rather than after building the machinery.

5. **Branch — for the strong guarantee, restructure rather than patch.** `PAT_use_copy_and_swap_for_strong_guarantee` owns the construction: change a copy, then exchange it in with an operation that cannot fail. Bolting rollback code onto the existing statement order is the alternative, and it is the one that leaves a partially-applied state on the path nobody tested.

6. **Provide the non-throwing exchange the previous step assumes.** The swap has to actually not throw, or the all-or-nothing property is a claim rather than a fact. `PAT_support_nonthrowing_swap` owns the pieces.

7. **Branch — for the basic guarantee, define what "valid" means here.** Name the invariant the object still satisfies after a failure. Basic is a real guarantee, not the absence of one, and it is often the right answer where the strong guarantee would cost a copy of something large.

8. **Fix how the handlers take and re-emit the exception.** `PAT_catch_exceptions_by_reference_and_rethrow_bare` owns both halves — taking by reference to avoid slicing the exception object, and re-emitting without naming it so the original dynamic type survives.

9. **Completion check.** Every exit path releases what the function acquired; the guarantee is stated where callers can see it; nothing in the function silently weakens that guarantee by calling something that offers less; and a failure part-way through leaves a state you can describe in one sentence.

## Notes
The ordering that matters most is steps 2 and 4. Leak-freedom is a precondition of every guarantee, so it is not negotiable and not a trade-off; the guarantee level, by contrast, is a genuine trade-off against copying cost and is chosen per function. Reversing them produces the common failure of building elaborate rollback machinery around a function that was leaking the whole time.

The gate in step 4 is where most attempts at the strong guarantee actually die, and finding out there is cheap. A function is only as strong as the weakest guarantee among the operations it must commit to, which frequently means the honest answer is basic plus a clearly stated invariant.

The generic version of the signalling decision — recoverable or not, explicit or implicit, and what the caller is told — belongs to the core protocol this one specializes and is not repeated here.
