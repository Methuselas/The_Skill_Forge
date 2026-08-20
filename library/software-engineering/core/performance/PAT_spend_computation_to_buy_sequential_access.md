---
object_id: PAT_spend_computation_to_buy_sequential_access
object_type: pattern
name: Spend Computation to Buy Sequential Access
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
- algorithms
- caching
- trade_offs
cross_links:
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
- rel: related_to
  target_object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
- rel: related_to
  target_object_id: PAT_prototype_to_answer_one_specific_design_question
- rel: related_to
  target_object_id: PAT_trade_a_branch_for_unconditional_work
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Spend Computation to Buy Sequential Access

## Pattern Rule
**IF** an algorithm's cost is dominated by scattered memory accesses rather than by its arithmetic
**THEN** look for a reformulation that does more total work — recomputing values, or copying data that did not change — in exchange for touching memory in address order
**ELSE** where the per-element computation is already expensive relative to a memory access, the access pattern is not what limits the algorithm and rearranging it buys nothing.

## Do
- Price the trade before designing for it. One scattered main-memory access costs on the order of fifty arithmetic operations, and streaming the same bytes in order runs roughly an order of magnitude faster than fetching them at random, so the budget for extra work is unusually large.
- Consider recomputing a value instead of storing and fetching it. Where the retrieval would be a random access and the computation is cheaper than the access, the classic space-for-time trade runs backwards: keeping less data is faster as well as smaller.
- Shrink what is live at one moment, not only what is stored in total. Processing data in chunks sized to a cache level pays the misses once per chunk and then works at cache speed, which beats sweeping the whole set and missing on every element repeatedly.
- Take the counter-intuitive version seriously: move data that did not need moving. In a record-editing pass where an unpredictable subset of records changes size, copying every record into a fresh buffer — changed or not — replaces a scattered read-and-reallocate per record with one sequential read and one sequential write, and no per-record allocation.
- Recycle the freed block immediately rather than returning it. In a blocked version of that scheme the block released by the record just edited is the block needed for the next result, and it is the memory most recently touched, so it is still hot in cache.
- Settle it with a mock rather than two full implementations. The measurement needs only the approximate record size, the fraction that changes, and the real per-record work; a small prototype on simplified data answers the design question at a fraction of the cost.

## Don't
- Don't apply it without the fraction and the size in hand, because those two numbers decide it and they decide it sharply. For medium records with almost all of them changing, the sequential version ran about four times faster; at half changing, twelve percent, which is within the noise between machines; at one percent changing, the two tied — the copying was almost entirely wasted and the saved random reads still paid for it.
- Don't expect it to win on large records. Once a record is long enough that reading it streams regardless, both formulations access memory sequentially, the initial scattered touch is negligible, and the extra copying is pure loss.
- Don't ignore what the buffer costs. Rebuilding into a second buffer doubles peak memory and requires a pessimistic upper bound on total size, which is the reason to reach for fixed-size blocks instead of one contiguous allocation.
- Don't reason about this from operation counts. The reformulation deliberately performs more operations and more memory traffic, and is faster anyway; any analysis that scores it on work done will reject the winning design.

## Checklist
- What fraction of the data actually changes per pass, and how large is each element?
- Is the per-element computation cheap enough that memory access is the constraint?
- Does the reformulation turn scattered accesses into ascending ones, or merely fewer of them?
- What is the peak memory cost of the rearranged version?
- Has a prototype measured the crossover, or is the trade being assumed?

## Notes
The move behind all the variants is the same one: start from the constraint instead of the specification. Implementing the operation as stated — change these records, leave those alone — forces records to move individually and therefore to be scattered. Asking instead what algorithms are available *given* that everything must be touched in order produces a different program, and the extra work it does is the price of the constraint rather than an oversight.

The results are worth remembering for their shape rather than their numbers, because the shape is what generalizes: the sequential formulation's advantage grows with the fraction of data that changes and shrinks with element size, and the break-even sits far enough toward "almost nothing changes" that the intuition against wasteful copying is wrong across most of the range.

This is also a clean example of why the design has to be prototyped rather than argued. Both algorithms are obviously correct, both are easy to describe, and the better one depends on two properties of the data that no amount of reading the code will reveal.
