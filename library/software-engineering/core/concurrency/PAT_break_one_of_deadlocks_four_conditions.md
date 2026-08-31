---
object_id: PAT_break_one_of_deadlocks_four_conditions
object_type: pattern
name: Break One of Deadlock's Four Conditions
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- deadlock
- locking
- threading
- resources
cross_links:
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
- rel: related_to
  target_object_id: PAT_lock_the_smallest_region_that_must_be_atomic
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
reference:
  source_title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
  author: Robert C. Martin, with Brett L. Schuchert
confidence: high
references: []
variants: []
---

# Break One of Deadlock's Four Conditions

## Pattern Rule
**IF** threads in your design contend for more than one limited resource and you need them not to seize up
**THEN** identify which of the four necessary conditions you can remove — exclusive use, holding while waiting, inability to reclaim, and cyclic waiting — and remove one deliberately, since all four must hold simultaneously for the seizure to be possible
**ELSE** where you cannot remove any of them, say so explicitly and design for detection and recovery instead, because you have chosen to accept the risk rather than eliminated it.

## Do
- Attack the exclusivity first where the resource allows it. Something that supports simultaneous use removes the condition outright, as does having at least as many instances as there are contenders, or checking that everything you need is free before taking any of it.
- Attack the holding-while-waiting condition by refusing to wait: test each resource before seizing it, and if any is busy, release everything you hold and begin again. It is crude and it can almost always be implemented, which makes it the fallback when nothing else is available.
- Know what refusing to wait costs you. One thread needing an unusual combination may never find all of it free, and several threads can fall into lockstep — each taking one and releasing one, repeatedly. The first wastes the thread and leaves the processor idle; the second consumes the processor entirely while accomplishing nothing.
- Attack the no-reclaiming condition with a request mechanism: a thread finding a resource busy asks its holder to give it up, and a holder that is itself waiting releases everything and restarts. It permits waiting, so it restarts less often than the previous strategy, at the cost of tracking all those requests.
- Attack the cycle by agreeing an order. If every thread acquires resources in one globally agreed sequence, a cycle cannot form. This is the usual answer and it is usually just a convention rather than a mechanism.
- Put that convention where an acquisition site will hit it, since it is a convention and nothing enforces it. A rule in a design note constrains whoever reads the design note; the same rule written on the declaration of the lock that must be taken *second* is met by every future caller inside the definition they already have to read to use it. It costs one comment, it survives the departure of everyone who agreed to it, and it is the difference between an ordering that holds and one that held when it was written.
- Weigh what ordering costs before adopting it. The acquisition order rarely matches the order of use, so something taken early may sit held until the end; and where the identity of the second resource depends on what you did with the first, no ordering is possible at all.
- Check whether every contender is yours to instruct before choosing among the four. Three of them assume it: release-and-retry needs a contender that will release, the request mechanism needs a holder that will answer, and an agreed order needs every party to have agreed. All three become unavailable the moment one contender is a separate process, a device, or a peer across a socket — and what remains is the exclusivity attack, applied entirely on your own side.
- Treat the buffer behind any stream you hold open as a contended resource, since that is the ordinary case where the other party cannot be instructed. A parent reading one pipe to completion while a child writes to a second deadlocks as soon as the child outruns the unread pipe's buffer: the child blocks writing, so it never finishes the stream the parent is reading, so the parent never returns. The move is to give every stream you hold open its own consumer — a thread, a poll loop, an event-loop registration — so you are never blocked on one while withholding another.
- Expect that particular one to pass every test you have. The buffer is tens of kilobytes, so a child that writes a little to the unread stream works perfectly and one that writes a lot hangs forever, with no error, no timeout and no partial output. The threshold belongs to the platform rather than to your code, which is why it survives review and testing and then appears in the field.
- Isolate the coordinating part of the design so you can change strategy and measure the result. Which of these is right is not decidable on paper, and the ability to swap one for another is what lets you find out.

## Don't
- Don't reach for a strategy before naming which condition it removes. Locking practices adopted by reflex frequently leave all four intact, and the resulting code looks careful while guaranteeing nothing.
- Don't assume ordering is always available. It is the cheapest strategy and it fails precisely in the case where one resource is discovered by using another.
- Don't treat a strategy as free. Every one of these trades the seizure for something else — wasted threads, wasted processor, longer holds, or bookkeeping — and the trade is the decision.
- Don't count only the resources you named. A connection pool, an open file, a record lock, or a semaphore all qualify, and so does anything else limited in number that cannot be shared.
- Don't assume the other party can be talked to. Every strategy here except attacking exclusivity is a rule the contenders follow, and a rule only binds parties you wrote. A subprocess, a driver, or a service on the far end of a connection will not release on request, will not restart, and has never heard of your acquisition order.

## Checklist
- Which of the four conditions does your design actually remove, stated plainly?
- Is every contended resource here genuinely exclusive and genuinely limited?
- Is every contender something you can instruct, or is one of them a process, device, or peer that will not cooperate?
- For each stream you are holding open: who is draining it while you are blocked on another?
- If threads release and retry, what stops one of them from never succeeding?
- Is there a global acquisition order, and does every path obey it?
- Where is that order written down, and would someone adding an acquisition site read it there?
- Does any resource's identity depend on the result of using another one?
- What is the chosen strategy costing, and where would you observe that cost?

## Notes
The reason to learn the four conditions rather than a list of practices is that they turn an open-ended problem into a closed one. Faced with threads that hang, the instinctive response is to add or rearrange locking until the symptom stops, which is unfalsifiable — nothing tells you whether the problem is gone or merely rarer. Knowing that all four must hold converts it into a question with four answers: which one are you removing? A design that cannot answer has not addressed the problem, whatever care went into it.

The ranking below assumes something the four conditions do not require, and it is worth making explicit because it silently narrows the advice: three of the four strategies are rules the contending parties follow, so they are available only where you wrote every contender. Across a process boundary that assumption fails completely — a subprocess has not agreed to your acquisition order and will not release on request — and the whole apparatus collapses to the one strategy that acts on your own side alone. That is not a rare corner. Reading a child's output, talking to a device, and calling a service are all cases where one contender is beyond instruction, and in every one of them the resource being contended is usually buffer space in a stream rather than anything that looks like a lock.

The strategies are genuinely ranked by practicality, and the ranking is worth carrying. Removing exclusivity is best and rarely available, because most contended things are limited in number and cannot be used simultaneously. Ordering is the common answer because it usually costs nothing but agreement — and its failure case is specific and recognisable, namely that you cannot order what you have not discovered yet. Release-and-retry is the one that always works and is worst, which is exactly why it is worth knowing: it is the floor beneath the others.

What makes the retry strategies subtle is that they exchange one liveness failure for another rather than eliminating the class. Threads that release and restart never seize up permanently, but a thread can still fail to make progress forever, and a group of them can still consume a processor without accomplishing anything. Those look completely different from the outside — one shows an idle machine and a stalled task, the other shows a busy machine and a stalled task — and neither is detected by anything watching for errors, because nothing has failed.
