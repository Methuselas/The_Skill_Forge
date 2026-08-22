---
object_id: PAT_give_a_shared_object_its_own_thread_instead_of_a_lock
object_type: pattern
name: Give a Shared Object Its Own Thread Instead of a Lock
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
- design
- patterns
- threading
- latency
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_put_the_thread_safety_guarantee_at_the_transaction_boundary
- rel: related_to
  target_object_id: PAT_keep_thread_aware_code_away_from_thread_ignorant_code
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
- rel: related_to
  target_object_id: PAT_lock_at_the_public_boundary_and_nowhere_inside
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Give a Shared Object Its Own Thread Instead of a Lock

## Pattern Rule
**IF** an object must serve many threads and you have decided the guarantee belongs on this object
**THEN** choose deliberately between serializing by exclusion — callers run the object's code one at a time under its lock — and serializing by ownership, where callers enqueue a request and the object executes it on its own thread while the caller carries on holding a handle to the eventual result
**ELSE** where the operations are short and the caller has nothing to do until the answer arrives, exclusion is the smaller construction and ownership only adds a queue, a thread, and a scheduler between the call and the work.

## Do
- Decide on the caller's blocking, since that is what actually differs. Under exclusion the caller's thread executes the operation and waits out everyone ahead of it; under ownership the caller's thread returns as soon as the request is queued and blocks only if and when it asks for the result. A processing-intensive operation is the case where that difference dominates.
- Read the two arrangements as the same decision made in different places. Both give the object one-at-a-time access to its own state. Exclusion enforces it with a lock that every calling thread contends for; ownership enforces it by having exactly one thread ever touch the state, so nothing inside the object needs guarding at all.
- Put the guard where the queue is, and nowhere else, when you choose ownership. Enqueueing happens on caller threads and so must be serialized; everything behind the queue runs on one thread and is single-threaded code that anyone can read.
- Hand back a handle to the result at the moment of the call. Without it, ownership has only deferred the work and given the caller no way to collect it, and callers will invent their own signalling to compensate.
- Separate submission from execution in time on purpose, and exploit it. Because requests sit in a list before they run, the object may run them in an order other than arrival, refuse to run one until its precondition holds, or coalesce them — none of which an exclusion-based design can express, because there the operation begins the moment the lock is taken.
- Weigh the cost against the size of one request. The queue, the handle, the scheduler, and the handoff are paid per request regardless of how small it is, so ownership pays for itself on coarse operations and loses on fine ones.
- Keep the interface the callers see identical either way. Which serialization you chose is an implementation decision, and callers who can tell the difference will build on it.

## Don't
- Don't reach for ownership to fix a lock you have not measured. It is a larger structure with more moving parts, and its advantage is caller latency rather than throughput — a design that was slow because the critical section was too big stays slow with a queue in front of it.
- Don't give an object its own thread and then also lock its internals. The single owner thread is the guarantee; the lock is then protecting state that nothing else reaches, and its presence tells the next reader the opposite of the truth.
- Don't let requests be so fine-grained that the handoff exceeds the work. Enqueueing, waking the owner, dispatching, and delivering a result is a fixed cost per request, and at small enough grain it is the entire cost.
- Don't assume a queued design is easier to debug because nothing deadlocks. It is generally harder: the call site and the execution site are separated in time, the order of execution need not match the order of submission, and a stack trace at the point of failure no longer shows who asked for the work.
- Don't let requests accumulate without deciding what happens when they arrive faster than one thread can drain them. An unbounded activation list turns a throughput problem into a memory problem, which surfaces much later and much further away.

## Checklist
- Which serialization does this object use, and is that written down anywhere a reader will find it?
- What does the caller's thread do between the call and the result?
- If it uses ownership, is the queue the only place a lock appears?
- How long does one request take, relative to enqueueing and dispatching it?
- What limits the number of pending requests, and what happens at that limit?
- Could the object's state be reached by any thread other than its own?

## Notes
The reason this reads as one decision rather than two techniques is that both answer the same question — how does this object come to be touched by one thread at a time — and they answer it at opposite ends. Exclusion admits every thread into the object and stops them at the door; ownership admits none of them and moves the data to the one thread that is already inside. Everything else about the two designs follows from that, including which one leaves the internals free of guards and which one leaves callers waiting.

The exchange being made is a real one and worth naming: caller latency and scheduling freedom are bought with structure and with the loss of a straight-line call. In an exclusion design the call stack tells the whole story — who called, what ran, what it returned. In an ownership design that stack is cut in half, and the two halves execute on different threads at different times, possibly in a different order than they were written. This is what makes the design harder to debug, and it is not a defect of any particular implementation; it is what decoupling invocation from execution means.

The scheduling freedom is easy to undervalue at design time and is often the reason to accept the cost. Once requests exist as objects in a list before they run, an object can ask whether a request is ready before dispatching it, prefer one kind of work over another, or drop work that has been superseded. None of those is available where the operation and the lock acquisition are the same event, and retrofitting them later means moving to ownership anyway, at a point when callers already depend on the synchronous shape.
