---
object_id: PAT_budget_per_thread_resources_against_residency
object_type: pattern
name: Budget Per-Thread Resources Against Residency
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
- gpu
- performance
- memory
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_keep_a_lockstep_group_on_one_path
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
- rel: related_to
  target_object_id: PAT_name_the_performance_metric_before_you_optimize
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Budget Per-Thread Resources Against Residency

## Pattern Rule
**IF** you are writing for hardware that hides memory latency by keeping many threads resident and switching between them, and those threads divide a fixed pool of on-chip storage
**THEN** treat every per-thread resource you consume as a purchase of latency exposure, because the pool is fixed and using more of it per thread means fewer threads resident and less stall coverage available
**ELSE** where the hardware covers latency by other means — deep caches, speculation, out-of-order execution — per-thread resource use does not limit how many threads can run, and this tension does not exist.

## Do
- Hold the causal chain in one piece, because each link is unremarkable and the conclusion is not. A fixed pool of on-chip storage divides among resident threads. More storage per thread means fewer threads fit. Fewer resident threads means fewer are ready to run when one stalls on memory. Fewer ready threads means the stall is exposed rather than covered. So a change that makes each thread faster in isolation can make the machine slower overall.
- Compute what your consumption actually permits rather than estimating it. Storage per thread times threads per group gives storage per group; the pool size divided by that gives how many groups can be resident; and that against the hardware's maximum gives the fraction of the machine's latency-hiding capacity you have retained. The arithmetic is simple, the inputs are all available before running anything, and the answer is frequently much worse than expected.
- Watch for the cliff, because this quantity is not continuous. Resident groups is a whole number, so consumption can rise a long way with no effect and then one unit more halves it. A kernel that is fine at some resource level and suddenly much worse a small change later has crossed a boundary, not hit a gradual decline.
- Ask the toolchain what it actually allocated instead of counting declarations. The compiler decides which values live in fast storage, and it will quietly move some to slow memory when the budget is exceeded — with the result that a kernel using more values than fit does not fail, it just gets slower in a way nothing in the source reveals. Every serious toolchain for this hardware will report the allocation on request.
- Treat spilling as the thing to detect rather than the thing to fear. Values pushed out of fast storage land somewhere much slower that happens to be named as though it were local; sometimes a cache absorbs it and the cost is small, sometimes it is not. Either way the first step is knowing it happened.
- Trade back deliberately when the budget binds: use fewer values per thread, shrink the group so fewer threads compete for the same pool, or recompute something instead of holding it. Each buys residency with work, and which one wins is a measurement rather than a rule.
- Query the device and derive the launch geometry from what it reports, rather than embedding constants. The number of processors, the pool sizes, the group size, and the per-thread limits are all readable at run time, and a front end that computes its configuration from them adapts to hardware it was never tested on. Constants tuned on a development machine are a portability bug that presents as ordinary underperformance.
- Size the launch from the totals rather than the shape. How many dimensions a launch is expressed in has no bearing on efficiency; the total threads per group and total groups do, and those are the two numbers worth reasoning about. Dimensions are for expressing the data mapping conveniently, and it is easy to mistake a tidy shape for a tuned one.
- Stop pursuing residency once the stalls are covered. Full occupancy is not the goal — covering the latency is, and a kernel that reaches that with half the machine's resident capacity has nothing further to gain from this dimension. Chasing the ratio past the point where it buys coverage optimizes a proxy.

## Don't
- Don't carry over the assumption that using more registers is free. On hardware that covers latency with speculation and caches, a routine holding more values in fast storage is simply faster. Here it is faster per thread and can be slower per machine, and nothing in the source distinguishes the two cases.
- Don't read low residency as automatically bad. It is only a problem if memory stalls are actually exposed; a kernel that is compute-bound with few memory accesses does not need many resident threads, and improving the ratio there buys nothing.
- Don't tune this before establishing that memory latency is the constraint. It is the third question, after whether control flow diverges and whether memory is being accessed in a pattern the hardware can serve efficiently — and it is usually the smallest of the three.
- Don't size the group without checking what it does to the pool. Group size and per-thread consumption multiply, so a change to either moves residency, and a group size chosen for a clean data mapping can quietly halve the machine's stall coverage.
- Don't assume the numbers transfer between devices. Pool sizes, maxima, and the per-thread limits all vary by generation, so a configuration tuned to fill one device can be well off on the next — which makes this a parameter to derive at build or run time rather than a constant to embed.

## Checklist
- How much on-chip storage does one thread consume, and how much does the group therefore need?
- How many groups can be resident given the pool, and what fraction of the maximum is that?
- Does the toolchain report anything spilling to slow memory?
- Is this kernel actually limited by memory stalls, or by something else?
- Would a smaller group, or fewer held values, buy back residency worth having?
- Are these figures derived from the target device, or assumed from the one you developed on?

## Notes
The reason this is worth stating explicitly is that it inverts a habit rather than adding to one. Keeping values in fast storage is, everywhere else, unambiguously good — it is what optimization *means* at this level. Here the fast storage is a shared pool rather than a private allowance, so consuming it is a decision about the whole machine rather than about one thread. The two situations look identical in source code and behave oppositely.

The discreteness is the practical trap. Because residency is counted in whole groups, the relationship between resource use and performance is a staircase, not a slope. That produces two confusing experiences: adding work that consumes more storage and observing no cost at all, and then adding a very small amount more and watching throughput fall sharply. Both are the same mechanism, and neither is interpretable without knowing where the steps are.

Worth keeping in view: this is one of three limits on this hardware and usually the least of them. Divergent control flow within a lockstep group and memory access patterns the hardware cannot coalesce both cost more and are more often the actual constraint. Residency matters when the kernel is waiting on memory and has too few threads ready to fill the gap — which is a specific situation worth confirming before restructuring a kernel to save storage that was never the problem.
