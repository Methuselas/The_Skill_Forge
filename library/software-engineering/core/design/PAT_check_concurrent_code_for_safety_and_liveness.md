---
object_id: PAT_check_concurrent_code_for_safety_and_liveness
object_type: pattern
name: Ask Both What Must Never Happen and What Must Eventually Happen
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- correctness
- deadlock
- threading
- review
cross_links:
- rel: related_to
  target_object_id: PAT_assume_calls_can_overlap_and_arrive_in_any_order
- rel: related_to
  target_object_id: PAT_atomic_steps_do_not_compose_into_a_safe_whole
- rel: related_to
  target_object_id: PAT_verify_an_object_is_as_immutable_as_you_think
reference:
  source_title: 'Implementing Effective Code Reviews: How to Build and Maintain Clean Code'
  author: Giuliana Carullo
confidence: high
references: []
variants: []
---

# Ask Both What Must Never Happen and What Must Eventually Happen

## Pattern Rule
**IF** you are judging whether code that runs more than one thread of execution is correct
**THEN** check it against two separate questions — whether anything bad can occur, and whether the good outcome is guaranteed to arrive — because code can be flawless on the first and still hang forever on the second
**ELSE** where the code has no shared mutable state and no shared resource to contend for, neither question has anything to bite on and the ordinary correctness argument is the whole of it.

## Do
- Take the first question as two specific checks. Can two threads be inside the same critical region at once, and can a set of threads end up mutually blocked, each holding something another needs. Both are answerable by reading the code and reasoning about the resources it holds.
- Take the second question as two more. Can a thread be passed over indefinitely while others keep proceeding, and does the order in which waiting requests get served follow any defined rule at all. A program where every thread could in principle run, but one never does, is broken in a way that no correctness proof about mutual exclusion will detect.
- Expect the second question to be the harder one and budget for it accordingly. Whether something eventually happens depends on the scheduler, so it cannot be settled by reading the source the way the first question can — it needs reasoning about interleavings, or a test that runs long enough under contention to expose starvation.
- Treat correct locking as the beginning rather than the end. Mutual exclusion is the property locks provide; it is entirely possible for every critical region to be properly guarded and for the program to stop dead because two of those guards are acquired in opposite orders.
- Look for the failure where every participant is waiting on something another participant holds and will not release until it finishes. Five diners, four forks, nobody willing to put one down — the shape is the same whether the resources are files, connections, or rows.
- Name the condition where a result depends on which thread happens to get there first. That dependence on timing is the thing to hunt, and it is present whether or not the wrong outcome has been observed yet.

## Don't
- Don't accept the absence of observed failure as evidence. Both classes of fault depend on interleavings that may occur rarely, and a suite that passes a thousand times has sampled a tiny share of the possible orderings.
- Don't assume that adding a lock makes a region correct. A lock introduces the possibility of the second failure while removing the first, so every one you add is a trade rather than a gain.
- Don't confine the check to the code you wrote. A library call, a connection pool, or a framework holding something on your behalf can supply the other half of a mutual block.
- Don't treat serving order as beneath attention because it is not a correctness bug in the usual sense. A request that waits forever is indistinguishable from a request that failed, and it is worse, because nothing reports it.

## Checklist
- Which regions must never be entered by two threads at once, and what enforces that?
- Are locks acquired in a consistent order everywhere, including inside called libraries?
- Can any thread here be passed over indefinitely while the system as a whole makes progress?
- Is there a defined rule for who gets served next, or does it fall out of the scheduler?
- Which outcomes here would change if two operations happened to interleave differently?
- Has anything been tested under sustained contention, or only under load light enough to hide it?

## Notes
The split matters because the two halves fail in ways that look nothing alike and are found by different means. The bad-thing-happening class produces wrong answers — corrupted state, a value read mid-update, two writers clobbering each other — and it is the one people think of first because it resembles ordinary bugs. The good-thing-never-arriving class produces no wrong answers at all. The program simply stops, or one participant waits forever while everything else appears healthy, and a monitoring system watching for errors sees nothing because nothing errored.

The asymmetry in how they are established is what makes the second class expensive. Whether two threads can occupy a region simultaneously is a question about the code, and a careful reader with the source can answer it. Whether a waiting thread eventually runs is a question about the scheduler, which is outside the code and free to behave differently on another machine, under another load, or on a day when a neighbouring service is slow. That is why reading is enough for one and not for the other, and why the reviewer who has checked every lock has done perhaps half the job.

The relationship between the two is genuinely adversarial, which is the point most easily missed. The obvious remedy for the first class is to add locking, and every lock added creates a new opportunity for the second. A system with one enormous lock around everything is trivially free of the first problem and maximally exposed to contention and starvation; a system with no locks has the opposite profile. Correctness lives in between, which means neither question can be optimised alone — a change that improves one should be examined for what it did to the other.
