---
object_id: PAT_let_idle_workers_take_work_rather_than_busy_ones_hand_it_out
object_type: pattern
name: Let Idle Workers Take Work Rather Than Busy Ones Hand It Out
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
- scheduling
- load_balancing
- contention
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_derive_the_parallelism_from_work_and_span
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
- rel: related_to
  target_object_id: PAT_split_a_lock_only_where_the_structure_makes_the_regions_disjoint
- rel: related_to
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Let Idle Workers Take Work Rather Than Busy Ones Hand It Out

## Pattern Rule
**IF** work is created dynamically and unevenly across workers, so that some run dry while others still hold a backlog
**THEN** have the workers that run out go and take work from the ones that have it, rather than having loaded workers try to push work onto their neighbours
**ELSE** where the work is known up front and divides into equal-cost pieces, hand it out once at the start and skip the mechanism entirely.

## Do
- Put the coordination cost on whoever has spare capacity, because that is the entire argument and it decides the design. Under a push scheme, the moment when every worker is loaded — exactly when overhead is least affordable — is the moment when all of them are attempting handoffs that will be refused. Under a pull scheme, that same moment costs nothing at all, because nobody is idle and so nobody is searching. The overhead scales with idleness, which is when it is free.
- Give every worker its own queue and let it work one end exclusively. The owner adds and removes at one end; takers remove from the other. The owner's ordinary operations are then uncontended, takers contend only with each other, and the two sides can only collide when the queue is nearly empty — the same disjoint-ends construction that makes finer locking legal anywhere else, and it needs the same care about the empty case.
- Take the *oldest* task while the owner takes the newest. In a recursive decomposition the oldest pending task is the largest unexplored subtree, so a taker that takes it moves the most work per act of taking — and the owner working from the newest end keeps touching data it has just touched. One choice makes stealing rare and productive; the other makes local work fast.
- Choose the victim at random rather than by any scheme that inspects the others. Surveying who has the most work is itself coordination, and it concentrates several idle workers onto the same victim; independent random choice spreads takers without anyone consulting anyone.
- Give up the processor before attempting to take, where there can be more workers than processors. An idle worker searching for work is holding a processor that some worker *with* work could be using, which is the one way this mechanism can actively harm throughput.
- Decide how searching ends, and expect it to be harder than it looks. A worker that finds every queue empty will otherwise search forever, long after the work is done. The obvious answer — have each worker announce it has gone idle and count the announcements — is wrong, because an idle worker can be made active again by taking work from one that is not, so idleness is not a state that accumulates. What has to be established is that every worker was idle *at one instant*, which is a global-predicate problem rather than a counting problem and needs a construction built for it.
- Shrink the piece size as the work drains, where you control how much is handed out at a time. Large pieces early keep the per-request overhead low while there is plenty left; small pieces late let the finish times converge instead of leaving one worker holding a large final piece. Handing out a fixed fraction of what remains does both automatically — the pieces shrink on their own — with a floor to stop the requests becoming more expensive than the work.
- Reach for a computed static split rather than this mechanism when both the work and the workers are known and stable. Dynamic balancing earns its coordination overhead by discovering at run time what you could not know in advance; where the piece costs and the worker capabilities are both measurable beforehand, a split weighted to capability captures most of the same benefit and pays nothing while running. The mechanism here answers uncertainty, so the question to ask first is how much uncertainty there actually is.
- Read the fixed-size extremes as the ends of that same dial. Splitting everything up front costs nothing to coordinate and balances only if the pieces were equal; handing out one item at a time balances perfectly and pays a request per item. Neither end is usually right, and the choice is a position between them rather than between two schemes.
- Recognize the shape outside thread pools. Consumers pulling from a queue rather than producers pushing to them, workers claiming jobs rather than a dispatcher assigning them, and readers requesting rather than writers broadcasting are all this decision, made for the same reason.

## Don't
- Don't have loaded workers offload onto their neighbours. It is the intuitive design — the worker that knows it is overloaded takes the initiative — and it inverts the cost curve so the mechanism is most expensive exactly when the system is busiest and the handoffs are least likely to be accepted.
- Don't put all the work in one shared queue instead. It balances perfectly and serializes every worker through one point; the per-worker queues exist so that the common case, a worker taking its own work, touches nothing anyone else touches.
- Don't let takers repeatedly target the same victim. Whether by a deterministic rule or by everyone independently picking the fullest queue, converging on one worker turns its queue into the bottleneck the design was avoiding.
- Don't let idle workers search without yielding when workers outnumber processors. Searching looks like work to the scheduler, so a thief can hold a processor away from a worker that has real work, and the system does less than it would with fewer workers.
- Don't assume the queue can be simple because most operations are local. The two ends meeting at the empty case is a genuine race, and it is the case a nearly-drained system spends most of its time in.

## Checklist
- Who initiates a transfer — the worker with too much, or the one with none?
- What does the mechanism cost when every worker is busy?
- Does each worker have its own queue, and does it use an end the takers do not?
- Which end does a taker take from, and why that one?
- How is a victim chosen?
- What happens when a worker finds every queue empty?

## Notes
The asymmetry is the whole insight and it is easy to state backwards. Both schemes move work from where it is to where it is not, and they differ only in who initiates. That difference decides when the overhead is paid: initiating from the loaded side means paying most when the system is saturated, and initiating from the idle side means paying only when someone has nothing better to do. A mechanism whose cost is proportional to idleness is close to free precisely when it matters.

The queue geometry is worth understanding rather than copying, because it is doing two jobs at once. Separating the ends makes the owner's path uncontended, which matters because that path runs constantly while stealing is rare. Choosing which end each side uses is a separate decision about *what* gets taken — oldest work is the biggest remaining chunk in a divide-and-conquer computation, so a rare steal should take the most it can, and newest work is the warmest in cache, so the frequent local operation should take that. Getting the first right and the second wrong yields a correct design that steals constantly.

The failure mode to watch for is not incorrectness but a system that does less work as it is given more workers. Idle searchers consume processors, look busy to the operating system, and can crowd out the workers actually making progress. That is why yielding before a search and terminating the search properly are not refinements but parts of the design — without them the mechanism that exists to keep processors fed becomes the thing taking them away.
