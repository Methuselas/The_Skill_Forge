---
object_id: PAT_name_the_allocation_pattern_before_choosing_a_strategy
object_type: pattern
name: Name the Reuse Order Before Choosing a Pool Strategy
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
- allocation
- pooling
- caching
- workload_characterization
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
- rel: related_to
  target_object_id: PAT_keep_a_spare_before_releasing_capacity
- rel: related_to
  target_object_id: PAT_check_the_last_used_slot_before_searching
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Name the Reuse Order Before Choosing a Pool Strategy

## Pattern Rule
**IF** you are deciding how a pool, cache, or free list should hand back the units returned to it
**THEN** first name the order in which the program actually takes and returns them, because every reuse strategy is fast for some orders and bad for others, and the choice is only decidable against a named one.

## Do
- Sort the workload into the orders that behave differently: many taken at once, returned in the order taken, returned in the reverse of the order taken, or taken and returned with no relation between them.
- Expect more than one. Most programs show several orders in different phases, so the question is which one dominates the part you are making faster, not which one occurs.
- Get the order from the code that will actually use the pool. Building a collection produces one order, unwinding nested calls produces the reverse, and incidental use through a long-running program produces neither.
- State the order you designed for where the strategy is written down, so the next person can tell a wrong workload from a wrong implementation.

## Don't
- Don't reach for a most-recently-freed cache reflexively. It is excellent when take and return are unrelated, and it is a loss when they are ordered, because the bookkeeping runs on every return and the ordering was already doing the work for free.
- Don't tune against a benchmark that exercises one order. A pool that looks good taking and returning in a tight alternating loop can be the worst choice for a program that fills a collection and empties it.
- Don't assume a strategy that wins on average wins anywhere. Averaging over orders that behave differently describes no real workload, and the result is usually beaten on each individual order by something simpler.
- Don't keep looking for the strategy with no bad case. There is not one; every arrangement has an order that defeats it, and the useful goal is knowing which order defeats yours.

## Checklist
- Which of the orders dominates the code this pool is for, and how do I know rather than assume?
- What order would make my chosen strategy behave worst, and can that order occur here?
- Is the strategy's assumed order recorded next to the strategy?
- Am I measuring against the order I designed for, or against whichever one was easiest to write a loop for?

## Notes
The reason this comes before the implementation is that the orders are not variations in degree, they conflict. Handing back the most recently returned unit serves unordered use well because the returned unit is the one most likely still resident; the same rule applied to a workload that returns everything in the order it took it does bookkeeping on every operation and gains nothing, because the units were already coming back in a usable sequence.

Attempts to serve every order with one arrangement tend not to survive contact with the second order. Improving the same-order case by keeping returned units in a list makes the reverse-order case worse, and the fix for that makes the first worse again; there is no arrangement in the middle that is better than either, only one that is worse than both.

The honest end state is a strategy chosen for a named order with its weakness written down. That is a stronger position than an arrangement claiming to be generally good, because it converts a future slowdown from a mystery into a check: someone reads the recorded assumption, compares it against what their code does, and either finds the mismatch or rules it out.
