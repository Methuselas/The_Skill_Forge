---
object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
object_type: pattern
name: Choose the Data Structure for the Dominant Access Pattern
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
- memory
- data_structures
- design
- caching
cross_links:
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
- rel: related_to
  target_object_id: PAT_look_for_hot_data_when_there_is_no_hot_code
- rel: related_to
  target_object_id: PAT_estimate_the_order_before_you_run_it
- rel: related_to
  target_object_id: PAT_choose_the_control_construct_that_fits_the_data
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Choose the Data Structure for the Dominant Access Pattern

## Pattern Rule
**IF** you are choosing how to hold a body of data that the program will spend significant time traversing
**THEN** pick the arrangement that makes the access pattern you perform most optimal, and treat the operations you rarely perform as the ones to pay for
**ELSE** where the data is not accessed often enough to matter, take whichever structure is simplest — the layout cannot be a problem if the traffic is not there.

## Do
- Read the cost off the hierarchy rather than off the interface. A million 64-bit values in a vector occupy 8 MB accessed in address order; the same values in a linked list occupy 24 MB — value plus two pointers per node — at addresses scattered by separate allocations. That is the difference between roughly 0.6 and 5 nanoseconds per element, and it is predictable from the size and the pattern before any code is written.
- Ask what the node-based structure was actually bought for, because the answer usually has a cheaper alternative. Unknown final size is the common one, and a counting pass over the input to size the array exactly can be worth a second traversal.
- Reach for a block-allocated array when the size genuinely cannot be known. Fixed blocks small enough to sit in the innermost cache — commonly two to sixteen kilobytes — linked together, grow by allocating another block, cost one likely miss per block, and stream at array speed inside it. The standard double-ended queue is this structure, though implementations vary in how close to a vector they get.
- Migrate the data when the access pattern changes, instead of finding one structure that serves every phase. Build in a list while insertions are arbitrary, freeze into an array once the contents stop changing, or convert the settled part while leaving the mutable part where it is — the copy is often repaid by the first traversal afterwards.
- Separate the order from the storage when the data is needed in several orders. Keep the values contiguous and impose each order as an array of pointers over them. Every ordered traversal is then indirect, so this only pays when those traversals are the rare ones.
- Count what a traversal costs where the elements are small. A short record may be fetched in a single load, so a scattered layout pays full latency for every element; a long record pays it once and then streams, which makes the layout question much less urgent.

## Don't
- Don't choose a container from its interface guarantees alone. Constant-time insertion at an arbitrary position is a real property and it is bought with a pointer chase per element, which is the most expensive access pattern there is.
- Don't keep a structure past the phase that justified it. The insertion-heavy build and the traversal-heavy use are different problems, and holding one arrangement across both optimizes for whichever phase was written first.
- Don't pay for a conversion you cannot amortize. Rearranging data that is barely touched costs real time and buys nothing, and the fact that it is barely touched is already the answer.
- Don't treat this as an algorithmic-complexity question. The operation counts can be identical and the measured times an order of magnitude apart, because complexity does not model where the bytes are.

## Checklist
- Which traversal or lookup does this data see most, per unit of work?
- How many bytes does the arrangement occupy, including per-element overhead?
- Are those bytes visited in address order, or in an order the allocator determined?
- Which phase of the program is the current structure optimized for, and is it the expensive phase?
- If a cheaper structure loses one capability, how often is that capability actually used?

## Notes
The claim that data organization is the most consequential memory decision a programmer makes is not rhetorical. The hardware's behaviour is fixed and the curve of cost against size and pattern cannot be beaten; what a programmer chooses is *where on that curve the program sits*, and the structure is what places it there.

Per-element overhead deserves separate attention from access order because it moves the data along the size axis as well. Three times the bytes for the same values does not merely waste memory — it can push a working set out of a cache level it would otherwise have fitted, so the same traversal pattern lands on a slower part of the curve.

The migration answer is worth holding onto because it dissolves an argument that otherwise has no winner. Asking which single container is best assumes the program has one access pattern, and programs that build a collection and then process it repeatedly have at least two. Once the question becomes when to convert rather than what to choose, the phases can each get the arrangement they want.
