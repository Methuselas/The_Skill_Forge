---
object_id: PAT_match_the_problem_to_a_known_coordination_shape
object_type: pattern
name: Match the Problem to a Known Coordination Shape
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
- threading
- design
- patterns
- starvation
cross_links:
- rel: related_to
  target_object_id: PAT_break_one_of_deadlocks_four_conditions
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
- rel: related_to
  target_object_id: PAT_assume_calls_can_overlap_and_arrive_in_any_order
reference:
  source_title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
  author: Robert C. Martin, with Brett L. Schuchert
confidence: high
references: []
variants: []
---

# Match the Problem to a Known Coordination Shape

## Pattern Rule
**IF** you are about to design how threads in your system will hand work to each other or share access to something
**THEN** check whether the arrangement is one of the small number of classic shapes before inventing a scheme, because the known ones come with known failure modes and worked solutions
**ELSE** where the arrangement genuinely matches none of them, describe it in the same vocabulary — what is limited, who waits, who can be starved — so the failure modes remain nameable.

## Do
- Learn the vocabulary first, because it is what makes the failures discussable. Something limited in number that cannot be used simultaneously; the guarantee that only one thread is inside a region; a thread prevented from progressing for an unreasonably long time or forever; threads each holding what another needs; and threads that keep moving but keep finding each other in the way and never finish.
- Recognise the shape where work is produced and consumed. One or more threads generate items into a bounded buffer while others take them out, and both sides can block — producers waiting for space, consumers waiting for content — with each side signalling the other that its wait is over.
- Recognise the shape where many read and a few write. Emphasising reader throughput lets writers wait indefinitely and lets readers see stale data; giving writers priority stalls the readers. The design work is choosing where between those to sit, and knowing that both extremes are failure modes rather than one being the safe choice.
- Recognise the shape where each participant needs several resources held at once. Threads competing for overlapping sets of limited things is the arrangement that seizes up, and identifying it is what tells you that resource ordering is the question to answer.
- Work through the standard solutions once, ahead of needing them. These arrangements arrive in the middle of building something else, and recognising one from having implemented it is a different experience from meeting it cold.
- Price the mechanisms separately for a one-shot notification, where one task tells another that something has happened exactly once. A condition variable needs a mutex that protects nothing, constrains which task may reach the meeting point first, and obliges the waiter to re-check that the event really occurred. A shared flag avoids all of that and polls rather than blocks, burning a core while it waits. Combining the two works and reads awkwardly. A one-shot promise-and-future pair expresses the notification directly, at the cost of an allocation for the shared state and of being usable only once.
- Recognize the rendezvous, where neither side can proceed alone and each must meet the other. Whichever party arrives first has nothing to do but wait, and the arrangement that scales is to let it *leave a request inside the structure* rather than wait outside it: the early arrival posts a reservation and watches its own slot, and the late arrival fulfils that reservation directly instead of announcing to everyone. This inverts the usual asymmetry — the structure holds either supply or demand, never both — and it buys local waiting and arrival-order fairness at once.
- Say which shape you have when you write it down. It tells the next reader which failures to watch for without their having to derive that from the code.

## Don't
- Don't invent a coordination scheme before checking whether the problem is a known one. Bespoke schemes carry failure modes nobody has enumerated, and the enumeration is most of the value.
- Don't treat one of these as solved because you named it. Naming tells you which trade-offs you face; it does not choose among them, and the choice is where the design work is.
- Don't design the reader-and-writer arrangement for throughput alone. Optimising that one dimension is how writers end up never running, which reads as a hang rather than as slowness.
- Don't assume the shape is absent because your threads are not obviously queuing or reading. A connection pool, a rate limiter, and a cache with a refresh are all these arrangements wearing other names.

## Checklist
- Which of the classic shapes is this, or which is it closest to?
- What here is limited in number, and what happens to a thread that cannot get it?
- Who can be starved in this design, and how would you notice if they were?
- If several resources are held at once, in what order are they taken?
- Would a reader of this code be able to name the arrangement from what is written?

## Notes
The reason to reach for a catalogue rather than reason from first principles is that these arrangements have been studied to exhaustion and their failure modes are already enumerated. Deriving them independently means rediscovering, under deadline, that prioritising readers starves writers or that competing for overlapping resources can seize up entirely. Recognising the shape gives you the enumeration immediately, and the enumeration is the part that is hard to produce and easy to consume.

The vocabulary carries more weight than it appears to, because it is what makes these failures reportable. A system where one thread never progresses while everything else looks healthy is close to undiagnosable without a word for that condition — nothing has errored, no exception was raised, throughput may look fine in aggregate. Distinguishing a thread that is blocked forever from a set of threads that are busy accomplishing nothing determines which measurements are worth taking, and neither is visible to anything watching for failures.

Recognition is also what keeps the scope of the design honest. Each of these shapes is a balancing problem rather than a puzzle with a right answer: how much staleness against how much writer delay, how much buffering against how much blocking, how much ordering discipline against how long resources stay held. Knowing which one you are in tells you which dial you are actually turning, which is far more useful than a scheme that appears to work in the arrangement you happened to test.
