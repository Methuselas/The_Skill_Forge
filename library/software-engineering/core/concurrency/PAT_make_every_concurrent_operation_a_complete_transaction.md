---
object_id: PAT_make_every_concurrent_operation_a_complete_transaction
object_type: pattern
name: Make Every Concurrent Operation a Complete Transaction
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- api_design
- threading
- interfaces
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_put_the_thread_safety_guarantee_at_the_transaction_boundary
- rel: related_to
  target_object_id: PAT_atomic_steps_do_not_compose_into_a_safe_whole
- rel: related_to
  target_object_id: PAT_define_your_code_contract_explicitly
- rel: related_to
  target_object_id: PAT_expose_clean_api_hide_implementation
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Make Every Concurrent Operation a Complete Transaction

## Pattern Rule
**IF** you are designing the operations of a type that several threads will use at once
**THEN** make each operation take the object from one fully defined state to another, with behaviour defined for every state it could be called in, so no caller ever has to hold a result across two calls
**ELSE** where the caller genuinely needs several operations to be one unit, give it a way to express that unit — and then that combination, not its parts, is the operation to make safe.

## Do
- Test each operation by asking what the caller must assume between calls. A container offering emptiness, inspection, and removal as three calls is individually safe and jointly useless: another thread can empty it between the check and the read, so the guarantee that made the sequence valid in single-threaded code has no concurrent equivalent.
- Fold the query and the action into one call. Removing an element becomes a single operation that either yields the element or reports that there was none — the check, the read, and the removal happen inside one guarded region where nothing can intervene.
- Decide what happens if handing the result back fails, once the query and the action are one call. The element has already been removed by the time it is being returned, so a copy that throws on the way out loses it — there is no longer a separate inspect step to retry. Returning something that cannot fail to be handed over, or removing only after the result is safely constructed, are the two ways out; the standard containers avoid the question entirely by keeping inspection and removal separate, which is exactly the split concurrency forbids.
- Give the return type room to express absence. An optional value fits naturally; a boolean result with the value passed by reference, or a value-and-flag pair, do the same job. What matters is that "there was nothing" is an ordinary outcome rather than a precondition the caller had to establish beforehand.
- Hide any state that is not fully defined. Where an operation must pass through an intermediate arrangement — an element reserved but not yet built, a count advanced ahead of the data — that state exists only inside the operation and is never observable through the interface.
- Wrap by composition rather than inheritance when you are adding safety to an existing type. Public inheritance exposes every inherited operation, so anything you forget to wrap compiles and runs unguarded; and constructors need writing by hand anyway, since a move constructor has to guard the object it moves from.
- Mark the lock as mutable so that inspecting operations can stay const, and keep that the only thing you do with it. The convention that const operations are safe to call concurrently rests on their not modifying the object, so a mutable member must be implementation detail rather than logical state.

## Don't
- Don't offer an operation whose validity depends on a state the caller checked earlier. That is precisely the contract that cannot be maintained under concurrency, and it is usually inherited unexamined from a single-threaded design.
- Don't expect a caller to combine operations correctly with its own locking. It can be made to work, and it means the object's safety is now a rule enforced everywhere it is used rather than a property it has.
- Don't add thread safety to a finished interface. Which sequences are transactions determines what the operations are, so the interface either had that question asked of it or it needs redesigning rather than guarding.
- Don't preserve an interface out of familiarity when you are writing the wrapper anyway. Matching a standard container's operation set exactly is a choice, and here it is the choice that produces the unusable version.

## Checklist
- For each operation: is its behaviour defined for every state the object could be in when it is called?
- Does any operation require the caller to have established something by a previous call?
- Can a caller observe a state in which the object's invariants do not hold?
- Does every operation that might find nothing have a way to say so in its result?
- If this wraps an existing type, is any inherited operation reachable unguarded?

## Notes
The failure this prevents is not a race inside any one operation — each of the three calls in the classic sequence is properly guarded. It is that the caller's reasoning spans the calls, and nothing protects the interval between them. Guarding smaller and smaller pieces cannot fix that, because the thing that needed to be atomic was never inside any of them.

This is the same non-composability that appears with atomic variables, arriving one level up. Two atomic steps are not an atomic pair; two thread-safe calls are not a thread-safe sequence. Recognizing the pattern once makes it visible in both places, and the answer is the same in both: move the boundary out to whatever the caller actually needs to be indivisible.

It follows that the operation set of a concurrent type is usually smaller and coarser than its single-threaded equivalent, and that this is a feature. Each operation does more, there are fewer of them, and the states between them do not exist as far as any caller can tell.
