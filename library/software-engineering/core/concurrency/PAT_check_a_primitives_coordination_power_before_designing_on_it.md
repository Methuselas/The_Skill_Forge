---
object_id: PAT_check_a_primitives_coordination_power_before_designing_on_it
object_type: pattern
name: Check a Primitive's Coordination Power Before Designing on It
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
- lock_free
- atomics
- design
- hardware
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_split_acquisition_into_a_bounded_doorway_and_a_wait
- rel: related_to
  target_object_id: PAT_keep_memory_alive_until_the_compare_and_swap_completes
- rel: related_to
  target_object_id: PAT_estimate_a_concurrent_designs_ceiling_before_building_it
- rel: related_to
  target_object_id: PAT_announce_the_operation_so_another_thread_can_finish_it
- rel: prerequisite_for
  target_object_id: DRILL_decide_whether_a_primitive_can_coordinate_the_design
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Check a Primitive's Coordination Power Before Designing on It

## Pattern Rule
**IF** you are designing something that must complete without depending on any thread being scheduled — a nonblocking object, or any protocol where several threads must settle on one outcome
**THEN** check what the primitive you intend to build on can actually coordinate, because each one has a fixed ceiling on how many threads it can bring to agreement, and no quantity of those primitives, no amount of additional ordinary memory, and no cleverness raises it
**ELSE** where a lock is acceptable, this does not arise: a lock lets any primitive coordinate any number of threads, and the cost is the blocking you have chosen to accept.

## Do
- Take the ceiling as a property of the operation, not of your use of it. The limit is not about performance or contention; it says that above a certain number of threads, no correct protocol exists at all. A design that needs more than the primitive offers is not slow or delicate — it is impossible, and no review of the code will show that.
- Learn the three tiers, because the practical distinctions are coarse. **Plain reads and writes coordinate one thread** — that is, none: no protocol built from ordinary loads and stores lets even two threads agree on an outcome without blocking. **Operations that unconditionally modify — exchange, test-and-set, fetch-and-add — coordinate exactly two**, no matter how many you use. **Compare-and-set has no ceiling**, and neither does its load-linked/store-conditional equivalent.
- Notice why the boundary falls where it does, because the reason generalizes. An unconditional write destroys what was there, so the thread that arrives second erases the evidence that anyone arrived first, and nobody can reconstruct the order afterwards. A conditional update *fails* instead of overwriting, so the loser learns that it lost — and that is the entire difference between a primitive that can decide an order and one that cannot.
- Read this as the reason your hardware has the instructions it has. Compare-and-set exists because a machine offering only loads, stores, and unconditional read-modify-write operations cannot support nonblocking data structures for more than two threads; it is not an optimization, it is what makes the category possible.
- Apply the same test to the objects you already have, not just to instructions. Anything whose operations return different results depending on the order they are applied — a queue, a stack, a set, a counter that reports what it replaced — coordinates two threads and no more. A concurrent queue is therefore not available as a wait-free construction over plain registers, and that follows without examining any particular attempt.
- Collect the positive half of the result, since it is what changes your next move. A primitive at or above the thread count you need is *universal*: given it and ordinary memory, every concurrent object has a wait-free implementation, and there are no further impossibility results waiting to be discovered. So when a nonblocking design built on compare-and-set keeps failing, the obstacle is engineering rather than possibility — which is exactly the opposite conclusion from the same symptom below the ceiling, and the reason to check the ceiling first.
- Use it as a stopping rule. When a nonblocking design keeps failing in a way that feels like a missing trick, check whether the primitives in it are above the thread count you need. If they are not, stop looking for the trick.
- Let it decide the fallback honestly. Below the ceiling the choices are to move to a stronger primitive or to accept a blocking design — and a well-built blocking design is very often the right answer, since it is simpler, easier to verify, and indistinguishable in practice where descheduling inside a critical section is rare.

## Don't
- Don't try to compensate with more memory. Additional ordinary read-write storage is already assumed to be freely available in the statement of the limit, so adding bookkeeping cannot raise it; a design that appears to have escaped is one whose failing schedule has not been found yet.
- Don't combine weak primitives and expect to climb. Several operations that each coordinate two threads still coordinate two; power is a ceiling on the construction, not a resource to accumulate.
- Don't confuse an operation being atomic with it being able to coordinate. An atomic add is genuinely indivisible and genuinely useful, and it still cannot make three threads agree on anything — atomicity and coordination power are separate properties, and the first is the one that gets checked.
- Don't take a passing test as evidence the ceiling was cleared. What the limit forbids is a protocol correct under every schedule; a protocol that is wrong under one schedule in ten thousand passes everything you will run.
- Don't overread the result as an argument for compare-and-set everywhere. It says what is possible, not what is advisable — an unconditional atomic operation is cheaper and entirely correct where two threads are all that must agree, and a lock is correct where blocking is acceptable.

## Checklist
- How many threads must agree on a single outcome here?
- What is the strongest primitive this design uses, and what does it coordinate?
- Is the design nonblocking by requirement, or would a lock be acceptable?
- If it relies on an object rather than an instruction, is that object's coordination power above what is needed?
- Has anyone assumed extra bookkeeping state raises the ceiling?

## Notes
The value of this result to a practitioner is almost entirely negative, and that is what makes it worth carrying. It rarely tells you how to build something; it tells you when to stop trying, which is knowledge that is otherwise purchased with weeks. Nonblocking designs fail in ways that look like insufficient ingenuity — the race is always narrower after each fix, never absent — so a designer without this has no way to distinguish a problem that is hard from one that has no solution.

The reason behind the hierarchy is more portable than the hierarchy itself. A primitive can order threads only if a thread can leave a mark that a later thread cannot erase. Loads and stores fail this completely: writing destroys the previous value and every trace of who wrote it. This is the same observation that forces a read-write mutual exclusion algorithm to consume storage proportional to the thread count, and it is why conditional update is the pivotal operation — its failure is information, and information is what the losing thread needs in order to defer.

Where this changes a design in practice is at the moment of choosing the fallback. Knowing the ceiling converts an open-ended search into a decision with two branches: strengthen the primitive, or accept blocking. Both are respectable, and the second is chosen more often than the literature's enthusiasm for nonblocking constructions suggests — the guarantee is worth its considerable cost only when a thread being descheduled at the wrong moment is a real and consequential event.
