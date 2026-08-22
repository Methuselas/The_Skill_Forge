---
object_id: PAT_split_acquisition_into_a_bounded_doorway_and_a_wait
object_type: pattern
name: Split Acquisition Into a Bounded Doorway and a Wait
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
- fairness
- starvation
- locking
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
- rel: related_to
  target_object_id: PAT_check_a_primitives_coordination_power_before_designing_on_it
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Split Acquisition Into a Bounded Doorway and a Wait

## Pattern Rule
**IF** threads contending for something must not merely get it eventually, but get it in a defined order — or with a bound on how often one can be overtaken by another
**THEN** split acquisition into a doorway that completes in a fixed number of steps and fixes the thread's position, followed by a wait that defers only to positions already fixed
**ELSE** where eventual service is genuinely enough, do not build this: the ordering costs storage and read traffic proportional to the number of participants, and that is the whole reason ordinary locks do not provide it.

## Do
- Separate the two guarantees, because the weaker one is what nearly every lock actually offers and it is routinely mistaken for the stronger. Eventual service says every waiting thread gets in at some point. Ordered service says a thread that asked first gets in first. A lock can satisfy the first while letting one thread be overtaken any number of times, and nothing about it looks unfair while you are watching it.
- Make the doorway bounded in *steps*, not merely quick. What matters is that it finishes within a fixed number of operations no matter what other threads are doing, which in practice means it contains no loop that another thread can extend. That is what converts "A arrived before B" from a race into a fact you can build on.
- Take a number in the doorway and wait on it afterwards. Publish your intent, read every participant's current number, choose one greater than all of them, and publish it — then wait until no thread that wants in holds an earlier one.
- Break ties with a fixed total order on the participants themselves. Threads whose doorways overlap can read the same numbers and choose the same one, so the number alone does not order them; pairing it with the participant's identity and comparing the pairs does, at no extra cost.
- Announce intent before taking the number, and keep the announcement standing until you leave. Without it, a thread that has decided to enter but has not yet published its number is invisible, and a later arrival can order itself ahead of it.
- Collect the liveness property rather than proving it separately. Ordered service plus freedom from deadlock gives freedom from starvation for nothing — once the order is real and the system always makes progress, waiting behind a finite number of predecessors is the whole argument.
- Decide what happens when the numbers run out. They are never reset, so they grow without bound; at the moment a counter rolls over, the ordering property silently stops holding while everything continues to appear to work. A counter wide enough to outlast the system is the usual answer, and it is a decision to make rather than an implementation detail to inherit.
- Price the construction before adopting it. Every acquisition reads every participant's state, so both storage and traffic scale with how many threads could contend — which is what makes this a technique for small, known participant sets rather than a general-purpose lock.

## Don't
- Don't read freedom from starvation as fairness. It is the weakest of the useful liveness guarantees: it promises arrival with no bound on the wait and no constraint on the order, so a thread can be passed over an unlimited number of times without the property ever being violated.
- Don't put an unbounded wait inside the doorway. A doorway that can be delayed by another thread no longer establishes who arrived first, and the ordering it appears to give is then decided by scheduling.
- Don't expect to escape the cost by being clever with ordinary loads and stores. Any deadlock-free mutual exclusion built from reads and writes alone provably needs storage proportional to the number of threads, for a reason that generalizes well beyond locks: a value one thread writes can be overwritten by another before anybody reads it, so a thread cannot reliably leave evidence of its presence. Hardware read-modify-write instructions exist precisely to escape that bound, and reaching for one is the practical answer.
- Don't accept a definition of deadlock-freedom that only rules out everyone stopping. Threads that keep taking steps while systematically undoing each other's progress satisfy that definition and accomplish nothing; the definition worth holding is that some thread must actually complete.
- Don't build this where a queue would do. If the participants can simply be put in a line — each waiting on the one ahead of it — the ordering is structural, and that is a smaller and faster construction than having everyone read everyone.

## Checklist
- Does this design need ordered service, or only eventual service?
- Can the doorway be delayed by another thread, or does it always finish in a fixed number of steps?
- What breaks a tie between two threads whose doorways overlapped?
- Is a thread visible to later arrivals between deciding to enter and publishing its position?
- What is the participant count, and is reading all of them on every acquisition acceptable?
- What happens when the ordering counter wraps?

## Notes
The doorway is the whole idea, and it is worth stating why it has to be bounded rather than merely fast. Ordering threads requires a moment at which their relative order becomes a fact, and that moment can only exist if reaching it does not depend on what other threads do. A doorway containing a loop that another thread can extend has no such moment: two threads' positions would then be decided by the scheduler, which is exactly the thing the construction exists to take the decision away from.

The reason this is a specialist technique rather than how locks are normally built is the cost, and the cost is not an artifact of any particular algorithm. Reading and writing are weak coordination primitives in a specific way — a write can be erased before it is observed — and that weakness is what forces a thread to occupy its own location if it wants its presence to be reliably detectable. The result is a lower bound proportional to the participant count that no cleverness removes. Every practical lock avoids it by using an instruction that reads and writes indivisibly, which is a good illustration of what those instructions are actually for: not speed, but a coordination power that loads and stores do not have.

Where this does earn its place is anywhere the ordering is part of the contract rather than a nicety — request handling that must not starve a client, resource grants that have to be auditable, real-time work with a bound on how long anything waits. In those settings the question is not whether threads eventually proceed but whether you can say anything about the order, and a lock chosen for throughput will usually have no answer.
