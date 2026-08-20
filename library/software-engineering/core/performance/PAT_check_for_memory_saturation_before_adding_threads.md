---
object_id: PAT_check_for_memory_saturation_before_adding_threads
object_type: pattern
name: Check for Memory Saturation Before Adding Threads
library_path:
- software-engineering
- core
- performance
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- concurrency
- memory
- scalability
- hardware
cross_links:
- rel: related_to
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
- rel: related_to
  target_object_id: PAT_spend_computation_to_buy_sequential_access
- rel: related_to
  target_object_id: PAT_separate_per_thread_data_by_a_cache_line
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Check for Memory Saturation Before Adding Threads

## Pattern Rule
**IF** you are deciding how many threads to run, or explaining why more threads stopped helping
**THEN** find out whether the single-threaded version was already limited by memory traffic, because threads share the bus and the last-level cache no matter how independent their work is
**ELSE** where each thread's working set fits its own private cache, scaling is close to linear and the thread count can be set by core count alone.

## Do
- Test the ceiling directly by running the same memory benchmark at one, two, four, and more threads across a range of working-set sizes. Per-thread throughput holds nearly flat while the data fits per-core caches — sixteen threads each still running at about eighty percent of single-thread speed — and falls away sharply once the data spills into the shared last level or main memory.
- Expect the knee to arrive early and to move with the machine. On a sixteen-core processor, aggregate throughput stopped improving somewhere past four threads and barely moved between six and sixteen. On a machine two years older, two threads saturated the bus. A cheaper four-core part comes with a cheaper bus, so having fewer cores is no protection.
- Shrink the working set per thread as the first remedy, since it converts the problem into the case that scales. Splitting the computation so each thread works within a private cache level restores near-linear behaviour, and this is where blocking a computation pays twice.
- Reconsider the access pattern before concluding the bus is full. Sequential traffic reaches far higher aggregate bandwidth than scattered traffic, so the same program can be memory-bound with random access and not memory-limited at all with the same data touched in order.
- Trade computation for traffic more aggressively than you would in a single-threaded program. Recomputing a value instead of fetching it removes load from a resource every thread is queuing for, so the arithmetic budget that made it worthwhile alone is multiplied by the thread count.
- Change the algorithm when the implementation techniques run out. A problem often has one algorithm that is fastest on one thread and another that moves less data; the second can win outright once the first stops scaling, buying back with parallel throughput what it gives up in single-threaded speed.

## Don't
- Don't read poor scaling as a work-division problem without checking the bus. Threads that share nothing, coordinate through nothing, and touch only their own memory will still stop scaling, and the code contains no evidence of why.
- Don't set the thread count from the core count alone. Whether more threads help is a property of the working set as much as of the hardware, and the only way to know is to measure the program at several thread counts.
- Don't expect the read and write cases to behave identically. Aggregate read bandwidth commonly scales somewhat better than write bandwidth on the same machine, so a write-heavy phase can hit the ceiling while a read-heavy one is still improving.
- Don't assume symmetric multi-threading adds capacity here. Two logical threads on one core share the same path to memory, so where the bus is the constraint the extra thread has nothing to contribute — its gains, typically a quarter to a half of a core when they appear at all, come from filling idle execution units.

## Checklist
- Was the single-threaded version limited by memory traffic or by computation?
- How large is each thread's working set, and which cache level does it fit?
- Does measured throughput still rise between four threads and eight on this machine?
- Would blocking the computation bring each thread's data inside a private cache?
- Is the traffic sequential or scattered, and how much of the ceiling is that costing?

## Notes
The reason this constraint is invisible in the source is that it is a property of the hardware the threads happen to share rather than of anything they do to each other. Per-core L1 and L2 caches mean genuinely independent threads are genuinely independent while their data stays small. A shared last-level cache and a single path to main memory mean the same threads are competing for one resource as soon as it does not.

The consequence for design is that memory efficiency matters more in a concurrent program than in a sequential one, not less. A single-threaded program wastes bandwidth it was not going to use anyway; a program with sixteen threads is dividing a fixed budget, so every avoidable access is taken from another thread.

Both charts behind these numbers were current hardware when measured, and the older one saturating at two threads is the more useful of the two. It shows the ceiling is not a fixed property to be learned once — it moves with each generation of processor and memory, in both directions, which is why the measurement has to be repeated on the machine that will run the program.
