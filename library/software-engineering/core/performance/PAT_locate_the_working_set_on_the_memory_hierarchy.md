---
object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
object_type: pattern
name: Locate the Working Set on the Memory Hierarchy
library_path:
- software-engineering
- core
- performance
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- memory
- hardware
- measurement
- caching
cross_links:
- rel: related_to
  target_object_id: PAT_count_the_dependency_chain_not_the_operations
- rel: prerequisite_for
  target_object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
- rel: prerequisite_for
  target_object_id: PAT_spend_computation_to_buy_sequential_access
- rel: related_to
  target_object_id: PAT_reproduce_the_real_context_before_believing_a_microbenchmark
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Locate the Working Set on the Memory Hierarchy

## Pattern Rule
**IF** you are reasoning about what a data access costs, or measuring one
**THEN** answer two questions before any others — how much data is being touched, and in what address order — because the cost of a single read spans an order of magnitude between the answers
**ELSE** where the whole working set is a few kilobytes and stays resident, the access cost is effectively the register case and the questions are already answered.

## Do
- Carry the shape of the curve, not one number for "memory." Access time per value is flat while the data fits the innermost cache, steps up as it spills into each larger and slower level, and flattens again once the data exceeds the last level by several times. On one mid-range machine that meant 0.3 nanoseconds per random 64-bit read within 32 KB, rising to about 7 nanoseconds once past roughly 8 MB.
- Convert the cost into instructions to see what it buys. Seven nanoseconds is on the order of fifty arithmetic operations on the same processor, which is the budget available for any trick that removes one main-memory access. Very few computations do fifty operations per value, which is why a data-heavy program leaves the CPU idle.
- Separate latency-bound from bandwidth-bound by varying the word size. If reads per second stay constant as the word grows from 64 to 256 bits, you are paying per access and wider loads move four times the data for free. If bytes per second stay constant instead, the bus is saturated and wider words buy nothing.
- Mean address order when you say sequential. A linked list is traversed in sequence and touches memory at unrelated addresses; an array supports random indexing and is usually walked in address order. What the hardware responds to is the addresses, not the interface.
- Build the measurement so it measures memory. A single read reports as zero time — repeat it dozens of times per iteration and report items per second. For random access, precompute the index array, because `rand()` and even the modulo operator each cost far more than the read you are trying to time, and then remember you are timing two reads rather than one.
- Defeat the prefetcher deliberately when you need per-access numbers. Walking a range in order lets the hardware stream ahead and hides exactly what you were measuring, and adjacent values travel together anyway, so independent samples have to be far apart and visited in random order.

- Expect to place the working set yourself on hardware that gives you a scratchpad instead of a cache. Some accelerators expose a small, fast memory shared by a group of cooperating threads that nothing fills automatically — you copy the tile you are about to work on into it, operate there, and write the result back once. The reasoning is the same as reading the hierarchy anywhere else; what changes is that placement becomes an explicit step in the algorithm rather than a consequence of the access pattern.
- Budget that scratchpad as a shared allowance, not a free win. It is drawn from the same on-chip pool that limits how many thread groups can be resident, so a generous tile size buys locality and sells latency coverage — the two have to be priced against each other rather than maximized separately.
- Put a barrier between filling the scratchpad and reading it, and another before refilling it. The threads that cooperate to fill it are the threads that will read it, so the fill must be complete before any of them proceeds and the reads must be complete before any of them overwrites — two synchronization points that are easy to write once and easy to forget on the second iteration of a loop.

## Don't
- Don't quote a memory speed. There is no single one: the same machine varies by more than twenty times across working-set sizes and access orders, which is why the question is always where on the curve this code sits.
- Don't assume small data means free data. The first touch of any address goes to main memory regardless of how little you intend to read; the cache only pays off from the second access onward.
- Don't treat the cache sizes as portable constants. Thirty-two kilobytes of L1, a quarter megabyte of L2, and eight to twelve megabytes of shared L3 describe one class of machine, and the steps move with the processor model.
- Don't reason from a program's total data size. What matters is how much is live at once — a large array processed in cache-sized chunks behaves like small data, and a small structure chased through pointers behaves like large.

## Checklist
- How many bytes does this code touch between reuses of the same value?
- Which cache level does that fit in, on the machine this will run on?
- Are the addresses ascending, descending, strided, or unrelated?
- Does the per-value cost hold constant as the word size grows, or does the byte rate?
- Is the benchmark timing the access, or the index arithmetic that produced it?

## Notes
The gap this is all about is structural rather than incidental. Processors run at three to four gigahertz and can issue several operations per cycle; a DDR4 module's effective access time works out to something near ten nanoseconds once the column access latency is included. Nothing in the pipeline closes that difference — it can only be hidden, and the whole of memory optimization is about hiding it.

Two hardware mechanisms do the hiding, and both are pattern-matchers rather than oracles. The prefetcher watches the addresses being touched and, on detecting a regular pattern, starts moving the next data into the innermost cache before it is requested; it handles ascending and descending equally well, handles constant strides, and can track several strides at once, though reversing direction costs a brief re-adjustment. Pipelining overlaps the loads of later iterations with the computation of earlier ones. Between them, a sequential sweep can run near an order of magnitude faster than random access over the same bytes.

Specific claims about which access patterns the hardware handles well are exactly the kind of knowledge that expires. The advice that forward traversal beats backward was true once and has not been for years, and any list of prefetch-friendly patterns written today is on the same trajectory. What survives is the measurement: a benchmark shaped like the ones here, run on the machine in question, settles it in minutes and stays correct when the hardware changes.
