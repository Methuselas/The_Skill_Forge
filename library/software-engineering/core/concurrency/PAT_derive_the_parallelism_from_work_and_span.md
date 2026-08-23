---
object_id: PAT_derive_the_parallelism_from_work_and_span
object_type: pattern
name: Derive the Parallelism From Work and Span
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
- scalability
- design
- estimation
- scheduling
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
- rel: related_to
  target_object_id: PAT_estimate_a_concurrent_designs_ceiling_before_building_it
- rel: related_to
  target_object_id: PAT_model_the_design_before_there_is_code_to_measure
- rel: related_to
  target_object_id: PAT_let_idle_workers_take_work_rather_than_busy_ones_hand_it_out
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Derive the Parallelism From Work and Span

## Pattern Rule
**IF** you need to know how much a computation can gain from more processors — before committing to a parallel design, or before sizing the machine you will run it on
**THEN** treat it as a graph of steps with dependency edges and take two numbers from its structure: the total number of steps, and the length of the longest chain that must run in order — their ratio is the maximum speedup available, and therefore the largest processor count worth paying for
**ELSE** where the work is a fixed set of independent items with no dependencies at all, the longest chain is one step, the parallelism is simply the item count, and there is nothing to derive.

## Do
- Take both numbers from the algorithm rather than from a profile, because both are structural and available before any code exists. The total step count is what one processor would execute. The longest dependent chain is what unlimited processors could not shorten. For a recursively defined algorithm both fall directly out of its recurrences, which is why this is a design-time instrument rather than a measurement.
- Read the ratio as the processor count worth having. It is the average amount of work available at each point along the critical path, so it estimates how many processors could be kept busy — and it says plainly that using substantially more than that buys nothing at all.
- Hold the two floors and notice which one binds. Execution time cannot beat the total work divided by the processors, and it cannot beat the longest chain. When the first is larger, more processors help; when the second is larger, they do not, and the only remedy is restructuring the algorithm to shorten the chain.
- Prefer this to reasoning about a sequential fraction wherever the algorithm's structure is known. Asking what proportion of a program must run serially is hard to answer honestly and easy to guess wrong; asking how long the longest dependency chain is has a structural answer you can derive.
- Recompute the chain when you restructure, not the total work. The work usually stays roughly the same — the same operations still have to happen — while the chain is exactly what a restructuring moves, so it is the number that tells you whether the restructuring achieved anything.
- Stop looking for a clever scheduler once you have a greedy one. Any schedule that never leaves a processor idle while some task is ready finishes within the total work divided by the processors, plus the longest chain — which is within a factor of two of the best schedule that exists, while computing that optimal schedule is intractable. That factor of two is the entire prize for arbitrarily sophisticated scheduling, and it is almost never worth chasing.
- Expect near-linear speedup exactly when the parallelism greatly exceeds the processor count, and check that condition in advance. It is the situation in which a greedy schedule is not merely within a constant factor but close to perfect, and it is knowable before anything is built.

## Don't
- Don't read the parallelism figure as a prediction of speedup. It assumes every step costs the same, that any ready task can be placed on any idle processor instantly, and that nothing else constrains the machine — so it is an upper bound on what the algorithm permits, not a forecast of what the program will do.
- Don't add processors when the chain is what binds. Past the point where the ratio is exhausted, additional processors have nothing to run, and the money buys idle hardware while the finish time stays exactly where it was.
- Don't confuse the total work with elapsed time. A design that lowers the total work while lengthening the chain can be slower on a large machine and faster on a small one, and only separating the two numbers makes that visible.
- Don't let a design with less parallelism lose on that basis alone. One that uses far less memory can beat a more parallel rival that thrashes, and the model deliberately ignores memory entirely.
- Don't skip the analysis because the answer looks obviously large. Knowing that a computation could keep millions of processors busy is what tells you the algorithm is not the constraint — which redirects the effort to where the constraint actually is.

## Checklist
- What is the total number of steps, and what is the longest chain of dependent ones?
- What is their ratio, and how does it compare to the processors you actually have?
- Which of the two floors binds at that processor count?
- Does the scheduler ever leave a processor idle while a task is ready?
- If the chain binds, what restructuring would shorten it?
- What does the model ignore that this deployment cannot?

## Notes
The reason to prefer these two numbers over the sequential-fraction framing is that they are derivable rather than estimated. Asking what proportion of a program is inherently serial requires a judgment about code that has usually not been written; asking how long the critical path is requires only the algorithm's dependency structure, which is present as soon as the algorithm is. Two questions that answer the same design concern, and only one of them has a method.

The greedy scheduling result is the most immediately useful thing here and the least celebrated. It says that the enormous design space of scheduling policies is worth at most a factor of two, and that any policy which simply refuses to idle a processor while work is ready collects most of what is available. That converts scheduling from an open research problem into a solved engineering one for nearly every application — and it means effort spent on scheduling sophistication is nearly always effort that belonged on shortening the critical path instead.

The instrument's honesty about its own idealization is worth preserving when the numbers get quoted. It assumes uniform step cost, free task placement, and unlimited memory, none of which hold. What it produces is a ceiling: a statement about what the algorithm cannot exceed, which is exactly the right thing to know before choosing a machine or committing to a parallel design, and exactly the wrong thing to promise anyone as a result.
