---
object_id: PAT_put_the_thread_safety_guarantee_at_the_transaction_boundary
object_type: pattern
name: Put the Thread-Safety Guarantee at the Transaction Boundary
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
- design
- api_design
- threading
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_atomic_steps_do_not_compose_into_a_safe_whole
- rel: related_to
  target_object_id: PAT_keep_thread_aware_code_away_from_thread_ignorant_code
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_define_your_code_contract_explicitly
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Put the Thread-Safety Guarantee at the Transaction Boundary

## Pattern Rule
**IF** you are deciding which components of a design must be thread-safe
**THEN** find the level at which a change is a single logical transaction from the program's point of view, and put the guarantee there rather than on the pieces the transaction happens to touch
**ELSE** where a component *is* the transaction — a counter that only counts, a queue whose operations are the unit of work — the guarantee belongs on it and there is no gap to close.

## Do
- State which of three guarantees each type offers, since "thread-safe" alone does not distinguish them. A strong guarantee means concurrent use from multiple threads is safe and invariants hold throughout. A weak guarantee — often called thread-compatible, and what most standard containers give — means concurrent read-only use is safe, and a thread with exclusive access may do anything otherwise valid. Anything offering neither is thread-hostile and cannot be used in a threaded program at all, shared or not.
- Test the design by asking what a reader could observe mid-change. Two independently thread-safe containers, one holding unit names and one holding unit strengths, still let a second thread see a unit that exists in the first and not yet in the second — each operation was safe and the transaction was not.
- Own the transaction in one component and let it choose its own internals. A database object that guards adding a unit across both containers gives the guarantee that callers need; whether the containers underneath are individually thread-safe becomes an implementation question, and often the answer is that they need not be.
- Decide it during design rather than afterwards. Which operations are transactions determines the interfaces, the module boundaries, and where data lives, and none of those can be retrofitted by adding guards later.
- Check for sharing the interface does not reveal before assuming an unshared object is safe. Static members and class-specific allocators are shared by every instance, so an object used by exactly one thread can still race with another thread's object of the same type.
- Distrust a read-only interface as evidence of read-only behaviour. Copying a reference-counted pointer takes its source by const reference and still modifies the count — safe here because it was designed to be, at a real cost, but the const alone did not establish it.
- Ship both forms where a component is used two ways. Anything that is both a client-visible component and a building block for a larger transaction needs a guarded variant and an unguarded one — otherwise every use inside a larger transaction pays for a lock the enclosing guard has already made redundant. A construction-time flag with a conditional guard, a locking policy chosen at compile time, or a thin decorator that wraps each operation in a guard all work; which fits depends on whether the choice is known when the code is built.
- Classify every piece of data during design as exclusive to one thread, read-only, or shared for writing, and record where it changes category. Data produced by one thread and later read by many is a common and useful shape, and it is the classification — not the code — that says which components need which guarantee.

## Don't
- Don't make everything strongly thread-safe by default. It costs on every operation, most objects in a threaded program are used by one thread, and the guarantee is frequently useless at the level where it was applied.
- Don't compose a transaction out of individually safe calls. Safety does not compose across operations, so a sequence of guaranteed-atomic steps is not itself atomic — which is the same failure whether the steps are container calls or atomic variables.
- Don't guard the pieces and the whole. Once one component holds a lock across the transaction, the internal guarantees of what it wraps are usually paid for and unused.
- Don't leave the guarantee undocumented. What a type promises under concurrency is part of its contract, and a caller cannot derive it from the interface — which is exactly how the two mistakes above get made.

## Checklist
- What is the smallest change that must appear to other threads as all-or-nothing?
- Which component owns that change, and does it hold the guarantee?
- For each type in this design: strong, weak, or none — and is it written down?
- Does any object here share state through statics or an allocator?
- Are you paying for a strong guarantee anywhere the object is never shared?

## Notes
The reason this decision cannot be deferred is that concurrency is not a property that can be added to a finished design. Where the transaction boundaries fall determines what has to be shared, which determines what has to be synchronized, which is most of what makes a concurrent program fast or slow. A design drawn without that question and guarded afterwards ends up guarding at whatever level the existing decomposition happens to offer.

Sorting types into the three levels is more useful than the binary it replaces. The weak guarantee describes the majority of well-written library code: private to a thread, do as you like; shared, read only. Recognizing that as a real and sufficient guarantee stops it being read as a deficiency, and stops the reflex to wrap such types in locks they do not need.

There is a cost argument as well as a correctness one, and they point the same way. A strong guarantee taken by default is overhead on every operation, on objects that are usually not shared, in service of atomicity at a level nothing depends on — three ways of paying for nothing at once.

Providing both a guarded and an unguarded form of the same component resolves what otherwise
looks like a contradiction in this card. Interfaces meant for concurrent use should be
transactional and safe; interfaces meant as building blocks should carry no synchronization,
because the component assembling them will guard the whole transaction and any inner lock is
then pure cost. Both are true, of the same component, in different roles — so the answer is
two forms rather than a compromise between them. There is a second reason to avoid the
gratuitous inner lock beyond its run-time cost: every lock enlarges the body of code that has
to be examined for deadlock.

Doing the data classification during design rather than discovering it later is what makes the
rest of this affordable. Retrofitting thread safety onto a component built on the assumption of
exclusive access is difficult and tends to produce something slow, because the safe version
wants different boundaries than the exclusive one had. Knowing which data is exclusive,
which is read-only, and which is written by several threads tells you where the transactional
components belong before those boundaries are set.
