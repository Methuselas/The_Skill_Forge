---
object_id: PAT_decide_if_the_problem_is_worth_parallelizing
object_type: pattern
name: Establish That the Work Divides Before Dividing It
library_path:
- software-engineering
- core
- performance
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- parallelism
- concurrency
- tuning
- trade_offs
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_level_before_tuning_the_code
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_estimate_the_order_before_you_run_it
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
reference:
  source_title: 'Implementing Effective Code Reviews: How to Build and Maintain Clean Code'
  author: Giuliana Carullo
confidence: high
references: []
variants: []
---

# Establish That the Work Divides Before Dividing It

## Pattern Rule
**IF** you are considering spreading a computation across more cores, processes, or machines to make it faster
**THEN** first establish what fraction of the work can genuinely proceed independently, then price the coordination that dividing it will cost, and only commit if the first survives the second
**ELSE** where the slow part turns out to be inherently sequential, the remedy is a different algorithm or a different level of the system, and dividing it will make it slower rather than faster.

## Do
- Sort the problem before designing anything. Some work splits so cleanly that the parts never need to speak — each unit takes a slice, produces a partial answer, and the answers are combined at the end. Other work is known to resist division, and a chain where each step consumes the previous step's output is the shape to recognise.
- Find out whether your specific problem has a reputation. Several well-known computations are notoriously hard to divide, and discovering that after building the infrastructure is an expensive way to learn it.
- Price the coordination explicitly and put it against the saving. Work done before the split, moving data to where it will be processed, units sitting idle waiting for their neighbours, and the abstraction layers of whatever framework you adopt are all charged whether or not the division pays.
- Choose the size of each piece deliberately. Too small and coordination dominates the useful work; too large and the units finish at wildly different times leaving capacity idle. The right size depends on how much data each piece carries and how heavy the computation on it is, and neither is guessable from the code alone.
- Ask what data each unit needs close to it, what genuinely must be shared, and what has to move between units mid-computation. That inventory determines the cost more than the arithmetic does, since moving data is usually the expensive part.
- Treat whatever distributes the work as a component with its own cost and its own failure modes. It is a layer that everything passes through, which makes it a candidate bottleneck and something to watch rather than assume.
- Hold the ceiling in mind before promising anything. Whatever fraction of the work stays sequential sets a hard limit on the total speedup, and that limit applies no matter how many units are added — doubling the resources on a computation that is a third sequential does not come close to doubling the speed.

## Don't
- Don't expect the speedup to track the resources. The relationship is capped by the sequential remainder, and the gap between the naive expectation and the achievable result is where most disappointment with this approach comes from.
- Don't assume more cores means faster. Adding computational units changes nothing on its own; something has to be able to use them, and plenty of code cannot.
- Don't judge the result from a single run. Vary the number of units and the size of the problem separately, because a division that pays at one combination frequently loses at another, and one measurement cannot distinguish the two.
- Don't reach for this before the cheaper levels have been considered. Restructuring the work, choosing a better algorithm, or fixing how data is accessed are all available first and none of them add coordination cost.

## Checklist
- What fraction of this work can proceed without waiting on another part?
- Is this a computation already known to resist division?
- What does the split cost — before, during, and in the framework you would adopt?
- How big is each piece, and what happens to the total if you halve or double that?
- Which data must be shared, and which can sit next to the unit that needs it?
- What is the ceiling implied by the sequential remainder, and does the plan respect it?
- Has this been measured across several unit counts and several problem sizes?

## Notes
The seductive error is treating computational resources as though they were interchangeable with speed. They are not related that directly: resources create the *opportunity* for the work to proceed in parallel, and whether any of that opportunity is taken depends entirely on the structure of the computation. Code with a long chain of dependent steps runs at the same speed on sixty-four cores as on one, and the sixty-three idle ones are not a configuration problem to be solved.

The ceiling set by the sequential fraction is the single most useful thing to internalise, because it is both severe and easy to compute roughly. Whatever proportion of the work cannot be divided is paid in full regardless of resources, so it becomes the floor on total runtime and therefore the cap on speedup. A computation that is ninety percent divisible cannot exceed a tenfold improvement with infinite hardware, and most real work is far less divisible than that. Estimating the fraction before starting takes an afternoon and routinely shows that the achievable gain does not justify the complexity being contemplated.

The cost side gets underestimated because it is distributed across places nobody looks at together. Preparing the split, moving data to the units, waiting for the slowest one, combining the results, and the overhead of the framework that manages all of it are each individually modest and collectively frequently larger than the saving — which is the mechanism behind the common experience of a multi-threaded version running slower than the straightforward one. That outcome is not a sign of poor implementation; it is the expected result when the coordination exceeds the parallelism available, and the point of pricing it beforehand is to find out which side of that line the problem sits on while it is still cheap to walk away.
