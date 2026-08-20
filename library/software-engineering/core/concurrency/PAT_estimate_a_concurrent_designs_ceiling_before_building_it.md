---
object_id: PAT_estimate_a_concurrent_designs_ceiling_before_building_it
object_type: pattern
name: Estimate a Concurrent Design's Ceiling Before Building It
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
- measurement
- design
- benchmarking
- estimation
cross_links:
- rel: related_to
  target_object_id: PAT_prototype_to_answer_one_specific_design_question
- rel: related_to
  target_object_id: PAT_buy_concurrent_performance_with_restrictions
- rel: related_to
  target_object_id: PAT_reproduce_the_real_context_before_believing_a_microbenchmark
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Estimate a Concurrent Design's Ceiling Before Building It

## Pattern Rule
**IF** you are about to invest in a lock-free or otherwise elaborate concurrent implementation
**THEN** build a benchmark that stands in for it — a thread-local copy of the structure, plus the synchronization operations the real design would perform — and compare that upper bound against the simple guarded version before writing the design
**ELSE** where the simple version has already been measured as adequate, no estimate is needed and neither is the design.

## Do
- Compose the stand-in from two halves you can already measure. Give each thread its own non-thread-safe structure so there is no contention to model, and add the atomic operations the intended design would execute — one increment per push and pop, or one compare-and-exchange, whichever the scheme requires. Nothing thread-safe will beat that, so it bounds the design from above.
- Anchor it with the two numbers that bracket the question: the same structure with no synchronization at all, and the same structure under a good lock. On one machine those were about 485 million operations per second unguarded and 30 million down to 3 million mutex-guarded, which is what made the estimate interpretable.
- Compare against a well-implemented lock and not the default one. A spinlock-guarded version of the same structure reached around 70 million operations per second, above the estimated ceiling for the lock-free design — which settled the question in the opposite direction from the mutex comparison.
- Model the operation the design would actually use. Atomic increment and compare-and-exchange differ in cost, and differ differently across processors, so an estimate built on the wrong primitive answers a question you are not asking.
- Run the estimate on every architecture you target, and expect the answer to flip. The design that could not beat a spinlock on one processor family was clearly worth building for a many-core machine of another, where locks cost relatively more and the atomic increment in particular is inefficient.
- Benchmark a partial implementation by excluding what it does not handle yet. Restrict the workload so the structure never empties or never runs out of capacity, and you learn what the common path will cost while the corner cases are still unwritten.

## Don't
- Don't read the estimate as a prediction of the finished design. It omits the contention the real structure will have on its own shared state, so the real implementation lands below it — which is exactly why a design that loses to the simple version at its ceiling can be abandoned with confidence.
- Don't generalize a ranking of synchronization primitives from one machine. Which of spinlock, pointer-lock, retry loop, and native atomic wins varies across processor generations and families; the estimate is a measurement of your hardware, not a fact about the techniques.
- Don't estimate with unrepresentative elements. Small cheap elements make the synchronization dominate and show no scaling; large expensive ones show scaling that a real design would achieve — and if copying is that expensive, the better answer is usually a structure of pointers rather than a more concurrent structure.
- Don't skip this because the design is interesting. Elaborate concurrent implementations are expensive to write, far more expensive to verify, and the estimate costs an afternoon.

## Checklist
- What synchronization operations would the intended design perform per operation?
- What does the stand-in benchmark report, and what do the unguarded and well-locked baselines report?
- Is the estimated ceiling above the simple version by enough to be worth the complexity?
- Have you run it on each target architecture?
- Are the element size and access mix in the estimate representative of the application?

## Notes
The apparent circularity — needing a measurement of something not yet built — dissolves once the composition is seen. Performance of a concurrent structure is dominated by how many shared variables are touched concurrently and by what kind of operation, and both are known from the design sketch. Everything else in the structure can be measured today, without synchronization, on thread-local data.

This is a decision procedure rather than a benchmark, and its value is mostly in the outcomes where it says no. Building a genuinely lock-free stack is a substantial and error-prone project; discovering afterwards that a twenty-line spinlock beats it is an expensive lesson, and the estimate delivers the same conclusion before the work.

Two things that make estimates like this go wrong are worth naming together, because they push in the same direction: choosing a synchronization primitive the design would not use, and choosing data that makes synchronization look either dominant or irrelevant. Both produce a number that is technically correct about something nobody asked.
