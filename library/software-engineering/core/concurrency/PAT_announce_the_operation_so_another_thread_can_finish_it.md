---
object_id: PAT_announce_the_operation_so_another_thread_can_finish_it
object_type: pattern
name: Announce the Operation So Another Thread Can Finish It
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
- starvation
- design
- latency
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_give_every_operation_one_instant_where_it_takes_effect
- rel: related_to
  target_object_id: PAT_take_a_consistent_view_by_collecting_twice
- rel: related_to
  target_object_id: PAT_check_a_primitives_coordination_power_before_designing_on_it
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Announce the Operation So Another Thread Can Finish It

## Pattern Rule
**IF** a nonblocking design guarantees only that *some* thread makes progress, and you need the guarantee that *every* thread completes — a latency bound, a real-time deadline, a caller that cannot be starved
**THEN** have each thread publish a description of the operation it is about to attempt before attempting it, and have every thread look for a pending announcement and complete it on its owner's behalf
**ELSE** where an occasional unlucky thread being delayed is tolerable, do not build this: it roughly doubles the work every operation performs and adds substantial state and subtlety, to buy a guarantee most systems never collect on.

## Do
- Establish first that the operation can be written down as data, because that is the precondition and it is not always met. If a thread cannot describe what it is trying to do in a form another thread can pick up and execute, nobody can help it. This constrains the interface itself, which is why helping is designed in from the start rather than retrofitted.
- Announce before attempting, never after failing. The interval between deciding to act and publishing the announcement is one in which no one can help, so a design that announces only once it has struggled has left the starvation window open exactly where it matters.
- Have helpers finish the announced operation, not merely clear the way for it. A helper that removes an obstacle and leaves the owner to try again has changed the odds without changing the guarantee, and the owner can lose the next race too.
- Make double execution harmless, because it will happen. The owner and one or more helpers may all execute the same announcement concurrently, so each must be able to detect that the work is already done — normally by making the committing step a conditional update that exactly one of them can win, with the losers treating their failure as success.
- Have the owner read its result from where the operation was completed, not from its own execution path. If a helper committed the operation, the owner never ran the step that produced the answer, and code that returns what its own attempt computed will return the wrong thing or nothing.
- Accept that the operation's committing instant now belongs to whoever won it. An operation finished by a helper took effect at the helper's step, inside the helper's execution — which is the case that most often defeats a reviewer looking for where an operation takes effect.
- Bound whose work each thread takes on. Helping everyone on every operation is the straightforward version and the most expensive; helping only the one participant whose turn it is, selected by a rotating index, spreads the cost while still guaranteeing every announcement is eventually picked up.
- Recognize the construction when you meet it elsewhere. A wait-free snapshot where writers publish a view for stalled readers, a wait-free queue, and the general result that any sequential object can be made wait-free given a strong enough primitive are all this technique. It is effectively the only route from "the system progresses" to "every thread progresses."

## Don't
- Don't adopt helping for throughput. It reduces throughput — every operation now performs work on behalf of others — and buys a guarantee about the worst case instead. Choosing it for speed is choosing it for the one thing it does not provide.
- Don't leave an announcement standing after its operation completes. A stale announcement is indistinguishable from a live one and will be executed again by the next helper that finds it, which is the failure this design produces most reliably.
- Don't assume the announcing thread observes its own completion. It may be descheduled throughout, and the entire operation may occur while it is not running; everything it needs must be recoverable from shared state afterwards.
- Don't reach for the stronger guarantee by default. A design in which the system always advances and an unlucky thread occasionally stalls is sufficient nearly everywhere, and the cases that genuinely need more — hard deadlines, bounded response times, a thread whose delay is externally visible — are identifiable in advance rather than discovered.
- Don't underestimate what this costs to verify. Every operation now has a path where another thread executes it, so the number of interleavings to reason about multiplies, and the reasoning cannot be confined to the operation's own code.

## Checklist
- Can this operation be described as data another thread could execute?
- Is the announcement published before the first attempt, or after the first failure?
- What happens if the owner and two helpers all execute the same announcement?
- Where does the owner read its result from if a helper committed the operation?
- What removes an announcement once its operation is done?
- Is the extra work on every operation acceptable, and what is it buying?

## Notes
The reason this is the standard route to the stronger guarantee is that the weaker one fails for a specific reason: a thread loses a race, retries, and can lose again, indefinitely. Nothing about retrying harder fixes that, because the thread's fate is decided by other threads' timing. The only structural escape is to stop requiring the thread to win at all — and once its work can be completed by someone else, whether it personally wins becomes irrelevant to whether it finishes.

The cost is best understood as moving work from the unlucky case to every case. Without helping, the common path is cheap and a rare thread pays an unbounded price; with helping, every path is more expensive and no thread pays an unbounded price. That is a good trade only when the unbounded price is genuinely unacceptable, which is a smaller set of systems than the appeal of the guarantee suggests. Latency-bounded work, real-time paths, and anything where one stalled participant blocks something outside the program are where it earns out.

Two consequences ripple outward and are worth expecting rather than discovering. The first is that the operation stops being confined to its own code: its effect can occur in another thread's execution, at another thread's step, which changes how the design must be reviewed and where its committing instant is found. The second is that the operation must be reified as data, and that requirement reaches all the way up into the interface — a design that cannot name its own operations concretely cannot use this technique at all, and finding that out late is expensive.
