---
object_id: PAT_price_communication_by_transfer_count_and_volume_separately
object_type: pattern
name: Price Communication by Transfer Count and Volume Separately
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- decomposition
- communication
- granularity
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
- rel: related_to
  target_object_id: PAT_place_cooperating_work_at_the_narrowest_scope_that_holds_it
- rel: related_to
  target_object_id: PAT_lay_data_out_for_the_group_that_reads_it_together
- rel: related_to
  target_object_id: PAT_ask_whether_the_problem_grows_with_the_machine
- rel: prerequisite_for
  target_object_id: AP_design_a_parallel_decomposition
- rel: prerequisite_for
  target_object_id: DRILL_run_the_decomposition_procedure_on_a_problem
confidence: high
references: []
variants: []
---

# Price Communication by Transfer Count and Volume Separately

## Pattern Rule
**IF** you are choosing how to group work whose pieces must exchange data — how many groups there are, and what shape each one has
**THEN** price the exchange as two independent terms, a fixed cost charged per transfer and a cost charged per unit moved, and pick the grouping from the ratio between them rather than from either term alone
**ELSE** where one term is negligible against the other at every grouping you would seriously consider, say which one and design against it, because the comparison is already decided and re-deriving it each time buys nothing.

## Do
- Collect two numbers for every grouping, not one. How much crosses, and how many separate transfers carry it. They answer different questions and they frequently move in opposite directions, so a grouping recorded only by volume cannot be compared with one recorded only by count.
- Derive the ratio at which the answer flips instead of picking a winner. With costs `n·s + V·w` — `n` transfers at fixed cost `s`, volume `V` at cost `w` per unit — two groupings tie when `s/w` equals `(V₁ − V₂) / (n₂ − n₁)`. That single number, compared against the machine, replaces an argument about which grouping is better with a fact about where the boundary sits.
- Reduce the volume term by making groups compact, and know why it works. For a fixed amount of work per group, what must cross is the group's boundary and what stays inside is its interior; as a group is made more compact its boundary grows more slowly than its interior does. That is the whole reason a squarer grouping moves less data than a long thin one holding the same number of elements.
- Expect the compact grouping to lose on the other term. Cutting a domain into compact blocks gives each group more neighbours than cutting it into slabs does, so the same restructuring that reduces volume raises the transfer count. Which effect wins is exactly what the ratio decides.
- Measure `s` and `w` rather than reasoning about them. Between shared memory and a network the fixed cost varies by orders of magnitude while the per-unit cost varies far less, which is why one decomposition can be correct on a single machine and wrong on a cluster with nothing about the algorithm having changed.
- Recognise the same trade wherever small operations are combined into large ones. Batching many small transfers into one, buffering writes before issuing them, and choosing a block size for input and output are all this decision with different names: they spend nothing on volume to buy a reduction in count.
- Charge the local consequences of a shape to the per-unit term. A compact group often reaches its data through strided rather than contiguous access, and the resulting cost belongs in `w` for that grouping rather than in the crossing total, where it would silently go missing.

## Don't
- Don't compare two groupings that hold different amounts of work. The comparison is only about communication when computation is equal on both sides; otherwise the numbers confound the two and the winner is whichever grouping happened to be coarser.
- Don't treat less data moved as the objective. Volume is one term of two, and a grouping chosen to minimise it alone will lose wherever transfers are expensive to initiate — which is most distributed hardware.
- Don't price a transfer by its payload. The fixed cost covers latency, startup, and whatever synchronisation the exchange requires, and it is paid once per transfer whether that transfer carries one value or ten thousand.
- Don't assume both sides of the threshold are inhabited. For some problems the volume advantage is large enough that no machine anyone would build sits on the other side. That is a stronger and more useful answer than a balanced one, and it is worth stating rather than treating as a failure to find the interesting case.
- Don't carry a threshold from one problem size to another. It commonly depends on the dimensions of the problem rather than on how finely the problem was divided, which means it survives a change in the number of groups and does not survive a change in the input.

## Checklist
- For each grouping under consideration, how much crosses and how many transfers carry it?
- Do the groupings being compared hold equal work, so that only the communication differs?
- At what ratio of fixed cost to per-unit cost does the answer flip, and was that derived rather than assumed?
- What are those two costs on the target machine, and were they measured or guessed?
- Is the threshold a property of the problem or of the number of groups?
- Does a realizable machine sit on each side of it, and if not, which side is empty?

## Notes
The reason to hold two terms rather than one is that the single-number view is not merely less precise, it recommends the wrong grouping. Summarised as "moving data is the expensive part," communication cost makes the volume-minimising decomposition look unconditionally correct — and on hardware where initiating a transfer is expensive relative to filling it, the decomposition that moves the least data is beaten by one that moves several times more in far fewer messages. The single number cannot express that, so a design derived from it has no way to discover it is wrong beyond measuring the finished system.

The two-dimensional case is worth carrying because it comes out clean and shows the structure. Take a square domain of side `N` divided into `G` groups of equal area. Cut into slabs, the interfaces are `G − 1` of them and each carries `N` values in each direction. Cut into square tiles, there are roughly `2√G(√G − 1)` interfaces each carrying about `N/√G` in each direction. The tiles move a factor of about `√G / 2` less data and need about twice as many transfers, and the two arrangements cost the same when the fixed cost equals `N` times the per-unit cost. That threshold is a property of the domain, not of how many groups it was cut into — the same number appears at every `G` — which is the sort of result worth deriving once and keeping.

What makes this hard to see in practice is that the two terms are collected at different moments and by different people. Volume falls out of the data dependencies and is usually known while the algorithm is still being designed; transfer count falls out of how the exchange is finally implemented and is often not decided until much later. A design that never writes them side by side has not chosen between them, and will discover which one mattered only after the arrangement is expensive to change.
