---
object_id: PAT_dont_call_unknown_code_while_holding_a_lock
object_type: pattern
name: Don't Call Unknown Code While Holding a Lock
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- locking
- deadlock
- dependencies
cross_links:
- rel: related_to
  target_object_id: PAT_break_one_of_deadlocks_four_conditions
- rel: related_to
  target_object_id: PAT_take_the_simplest_lock_type_that_does_the_job
- rel: related_to
  target_object_id: PAT_lock_the_smallest_region_that_must_be_atomic
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Don't Call Unknown Code While Holding a Lock

## Pattern Rule
**IF** a critical section is about to call out to something you did not write and do not control — a library entry point, a virtual function, a callback, a comparison or hash supplied by the caller
**THEN** get the value you need before taking the lock, or release it before the call, because you cannot know whether that code takes locks of its own and you are staking the program's liveness on it never doing so
**ELSE** where the called code is yours, in the same component, and its locking is something you can see and keep seeing, the call is as safe as the rest of the section.

## Do
- Restructure so the unknown call happens outside the guarded region. Fetching the value first and then locking only to store it turns an unbounded dependency into a bounded one, and usually shortens the critical section as a side effect.
- Treat the danger as growing over time rather than as a property of today's code. The library you call may be fine now; the next version may not be, and nothing about your code will change when it stops being fine.
- Remember that ordinary mutexes are not re-entrant. If the called code reaches back into the same object and takes the same mutex, the behaviour is undefined and what you will usually see is the thread waiting for a lock it is itself holding.
- Count callbacks, comparators, and virtual functions as unknown code. They are supplied by the caller by design, which means their contents are exactly what the component cannot know.
- Watch what the called code is given as well as what it does, where it is invoked on your internals. Anything handed a reference to guarded state can return it, store it, or capture it, and the caller then holds a way into the protected data that outlives the lock. This defeats a self-guarding type completely, and unlike the liveness failures it announces nothing — the interface still looks closed, because the escape route is supplied by the caller and appears nowhere in the type.

## Don't
- Don't switch to a recursive mutex to make the re-entrant case work. It resolves the immediate stall and leaves you holding a lock across code that may take other locks, which is the condition that produces the cycles — and it makes the critical section's real extent much harder to see.
- Don't assume a call is safe because it looks pure. A logging call, an allocation, or a formatting operation can all take locks internally, and none of them announces it in its signature.
- Don't rely on the exception path being handled by care. A throw from the called function leaves the mutex locked forever unless the lock is scope-bound — which is one more reason the release should belong to a destructor rather than to a statement.

## Checklist
- Which calls inside this critical section leave the component?
- For each, could that code acquire a lock, now or in a future version?
- Could any of them re-enter this object and take this same mutex?
- Could the needed value be computed before the lock is taken?
- Is the lock scope-bound, so that a throw from the call releases it?

## Notes
This is a specific instance of removing the hold-and-wait condition, and it is worth stating separately because it does not look like a locking decision. The code reads as a call to a function that happens to sit between a lock and an unlock; nothing at that line suggests that the callee's internals are now part of your program's deadlock analysis.

The three failure modes are distinct and it helps to keep them apart. The exception case is a lost unlock and is fixed entirely by scope-bound locks. The re-entrancy case is undefined behaviour arising from the same thread taking a non-recursive mutex twice. The third has no local fix at all: the called code takes some other lock, someone else's code takes them in the other order, and the cycle exists across components that never knew about each other.

That third case is why the rule is stated as prohibition rather than as caution. Auditing the current version of a dependency establishes nothing durable, because the property you need is about all its future versions.
