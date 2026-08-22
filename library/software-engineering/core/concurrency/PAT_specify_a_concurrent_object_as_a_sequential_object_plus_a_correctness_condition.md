---
object_id: PAT_specify_a_concurrent_object_as_a_sequential_object_plus_a_correctness_condition
object_type: pattern
name: Specify a Concurrent Object as a Sequential Object Plus a Correctness Condition
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- concurrency
- correctness
- contracts
- design
- composition
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_make_every_concurrent_operation_a_complete_transaction
- rel: related_to
  target_object_id: PAT_put_the_thread_safety_guarantee_at_the_transaction_boundary
- rel: related_to
  target_object_id: PAT_give_every_operation_one_instant_where_it_takes_effect
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Specify a Concurrent Object as a Sequential Object Plus a Correctness Condition

## Pattern Rule
**IF** you must say what a shared object guarantees to the threads using it, and "it is thread-safe" is not enough to settle what callers may conclude
**THEN** write the ordinary sequential specification — what each operation does to the state, one call at a time — and then state separately which condition maps concurrent executions back onto it: that some sequential order explains them, that the order respects real time, or that order is guaranteed only across periods when the object is idle
**ELSE** where the object is used by one thread at a time under an external guard, the sequential specification is the whole contract and no condition is needed, because there are no overlapping calls to explain.

## Do
- Keep the sequential specification exactly as you would write it single-threaded, because that economy is the point. Each operation described by what it requires and what it leaves behind, in isolation, gives a document that grows with the number of operations rather than with the number of ways they could interleave — and the interleavings are unbounded.
- Add the correctness condition as a separate clause rather than folding it into each operation. The specification says what the operations mean; the condition says which concurrent executions count as explained by them. Merging the two is what produces documentation nobody can finish writing.
- Reach for real-time order as the default condition, and understand what it buys. Requiring that each call appears to take effect at one instant between its invocation and its return means that if one call finishes before another starts, everyone agrees on their order — including observers outside the object.
- Know the weaker condition and when it is honest. Requiring only that some sequential order explains the execution, consistent with each thread's own program order, permits calls that did not overlap to be reordered: one thread's completed enqueue may be ordered after a later thread's, because nothing relates them but wall-clock time. That is often fine and occasionally indefensible — a deposit reordered after a withdrawal is the shape of the complaint.
- Consider the weakest condition where you are buying throughput deliberately. Guaranteeing order only across periods when the object has no operation in flight yields something genuinely useful — a counter that issues every index exactly once, in no particular order — and it is the right contract for a work distributor where only the set of values matters, not their sequence.
- **Choose on composition, because that is the property that decides system-level correctness.** Real-time order composes: assemble a system from objects that each satisfy it and the system satisfies it. Program-order consistency does not — two objects can each individually satisfy it while their combined execution satisfies nothing, and the counterexample needs only two threads and two queues. A component built to the weaker condition cannot be reasoned about from its interface alone, which defeats the purpose of having an interface.
- Connect the implementation back to the specification with two statements, once you are building rather than specifying. The first says which concrete arrangements of your data are meaningful at all — sorted, no duplicates, every live element reachable — and every operation must both preserve it and be entitled to assume it. The second says what a valid arrangement *means* as a value of the specified object, which is rarely the identity: a structure holding elements flagged as removed maps to the set of elements that are reachable and unflagged.
- Prove an invariant the cheap way rather than by considering interleavings. Show it holds when the object is created, then show that no single operation can take a step that falsifies it. That discharges every schedule at once, and it works only because the invariant is a contract each operation may assume while being obliged to restore — which is what lets you reason about one operation at a time.
- Establish that nothing outside the implementation can touch the representation, since the whole argument rests on it. If the elements are internal and callers can only reach them through the operations, the invariant is preserved by construction; a design that hands out references to its own internals has no such guarantee and cannot use this reasoning at all.
- State the condition in the interface where callers can see it. A caller cannot infer it from the operations, cannot test for it, and will assume the strongest one — so an object offering less needs to say so as plainly as it states what it returns.
- Notice that memory itself is one of these objects. All of a program's shared locations, taken together, form a shared object whose correctness condition is the memory model; the platform's guarantee is exactly a statement in this vocabulary, which is why the same words appear in both places.

## Don't
- Don't describe a concurrent object by enumerating interactions. There are unboundedly many ways calls can overlap, the enumeration is never finished, and every operation added invalidates it.
- Don't assume "thread-safe" names a condition. It says operations may be called concurrently without corruption and says nothing about what order callers may conclude, which is the part that determines whether their code is correct.
- Don't expect these conditions to sit on one scale. Real-time order is stronger than both of the others, but program-order consistency and quiescent ordering are incomparable — each permits executions the other forbids — so "weaker" is not a single axis to slide along.
- Don't assume a condition constrains how much concurrency you can have. All three permit any pending call to be given some correct answer immediately, so none of them forces one call to wait for another; what makes an implementation block is the implementation, not the contract it is meeting.
- Don't reason about an object's state between operations the way you would single-threaded. A shared object may never be between calls at all — there can be an operation in flight at every instant — so every operation has to be written to encounter state reflecting other calls that have started and not finished.

## Checklist
- Is there a sequential specification for this object written down anywhere?
- Which condition does it claim, and is that claim visible to callers?
- Does anything outside the object observe the order of two non-overlapping calls?
- Will this object be composed with others under one correctness argument?
- Is the representation invariant written down, and does every operation preserve it?
- What does a valid representation mean as a value of the specified object?
- If the condition is not the real-time one, what breaks when two of these objects are used together?
- Is any operation written assuming the object is idle when it is called?

## Notes
The move that makes all of this work is refusing to specify concurrent behaviour directly. Concurrent executions are unbounded in a way that defeats enumeration, so the framework sidesteps them: describe the object as if calls happened one at a time, then state a rule for mapping real executions onto that description. Everything else — which condition, how to prove it, what composes — follows from that one decision, and a team that has not made it usually ends up trying to document interactions instead, which does not terminate.

Compositionality is the reason to care about which condition, and it is easy to underrate because it is invisible until the second object arrives. An object satisfying only the weaker condition is perfectly usable on its own; the failure appears when two such objects are used by the same threads and each becomes an external observer of the other, at which point their individually valid explanations cannot be reconciled into one. This is precisely the situation every real system is in, and it is why the stronger condition is worth its cost almost everywhere.

The relationship to guarding is worth stating because the two are often conflated. A lock gives you a correctness condition almost by accident — with each operation inside a critical section, the sequential order is the order the lock granted, and real time is respected. That is why lock-based objects rarely prompt anyone to think about this at all. The moment locking gets finer, or disappears, the condition stops being automatic and has to be chosen, stated, and argued — and the argument is exactly what the condition was defined to make possible.
