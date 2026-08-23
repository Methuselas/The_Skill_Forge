---
object_id: PAT_choose_lazy_or_eager_by_how_often_the_result_is_needed
object_type: pattern
name: Choose Lazy or Eager by How Often the Result Is Actually Needed
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
- optimization
- design
- caching
- trade_offs
cross_links:
- rel: related_to
  target_object_id: PAT_ask_whether_the_hot_code_can_run_less_often
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Choose Lazy or Eager by How Often the Result Is Actually Needed

## Pattern Rule
**IF** you are designing something whose results are expensive to produce and are deciding when the production should happen relative to the request
**THEN** answer one question first — is this result usually wanted, or usually not? — and let it pick the strategy: put the work off when many results are never demanded, and do it ahead of the demand when results are nearly always demanded or demanded repeatedly
**ELSE** where every result computed is used exactly once, straightforward evaluation on request is correct, and both alternatives charge you their bookkeeping while saving you nothing.

## Do
- Recognize deferral when you see it, because it wears several costumes: sharing one representation among holders until somebody writes; retrieving only the fields a caller touches rather than the whole record; recording a description of a pending operation and computing only the portion later asked for.
- Recognize anticipation the same way: maintaining running answers as the data changes so queries need no work; keeping what was expensive to obtain in case it is asked for again; fetching neighbors along with the item requested because whoever wanted one usually wants the others.
- Aim deferral at the case where partial results are enough. The technique pays best where callers routinely need a slice of a large result rather than all of it, since then the work skipped is most of the work.
- Keep the strategy out of the interface. When the choice is invisible to callers, you can implement the obvious version first, measure, and switch later without touching a line of client code — which is what makes this a decision you are allowed to revisit rather than commit to up front.

- Separate a third reason for deferring from the two this rule weighs, because it answers a different question. Deferring because a result may never be wanted is avoidance. Deferring so that the *whole chain* of intended operations is known before any of it runs is composition: nothing is skipped, but the implementation gets to see every step at once and can fuse them into a single pass over the data instead of one pass per step. That is why a chain of transformations expressed as a pipeline can beat the same steps written as successive loops, and it has nothing to do with how often the result is demanded.
- Separate building the plan from running it when the same plan runs repeatedly. Describing the work once, paying the analysis and setup once, and then replaying the prepared form many times amortizes a cost that the deferred-composition argument otherwise pays on every execution. This is what a prepared statement, a compiled expression, and a pre-built graph of operations all are — and it only pays where the shape is stable and the repetitions are many, since a plan built for one execution is pure overhead.
- Price what deferred composition costs in exchange. Errors surface at the point the chain is finally run rather than where the offending step was written, a stack trace shows the machinery instead of the intent, and the accumulated plan is a second thing to reason about that does not appear in the source. Those costs are real and are paid by whoever debugs it, not by whoever wrote it.
- Consider the third option where the work is bulky and the pause is what hurts: spread it across the operations that follow, doing a fixed slice of it on each. A structure that must be enlarged can migrate a few entries on every subsequent insertion rather than migrating everything at once, so no single call pays the whole cost and no thread has to stop the world. What you buy is a flat response time; what you pay is that the structure is in a partly-converted state for a while, and every operation must be written to work correctly in that state.
- Recognize when incremental conversion is not available. It requires that a half-converted structure still answer every question correctly, which is a real design constraint rather than a detail — if operations cannot be written to consult both the old arrangement and the new one during the transition, the work has to happen all at once and the pause has to be scheduled instead.

## Don't
- Don't adopt either strategy where all the computed results are genuinely required. Deferral then performs the entire original workload *and* maintains the structures that track what has not been done yet, so it is both slower and larger than doing the work when asked.
- Don't treat trading memory for time as a trade that always wins when memory is available. Larger objects mean fewer of them fit per cache line or page, so an anticipatory scheme can lose more to increased paging and reduced hit rates than it gains, and the only way to find out is to measure.
- Don't let anticipated state drift from the data it summarizes. Every path that changes the underlying values has to update or invalidate what was computed ahead, and the paths that get missed are the ones added later by somebody who did not know the summary existed.
- Don't leave deferred work depending on inputs that can change underneath it. If a pending computation refers to values that are later assigned to, either the result must be forced before the change or the old inputs preserved, and neither happens by itself.

## Checklist
- Of the results this produces, what fraction is never looked at?
- When a result is looked at, is the whole of it needed or a part?
- Are the same results requested more than once?
- What does the deferral or anticipation machinery itself cost in space and in code?
- Which code paths invalidate what has been computed ahead, and do all of them know about it?

## Notes
The two directions look contradictory and are not, because they answer different questions about the same design. Deferral is for operations whose results are frequently not needed; anticipation is for operations whose results are nearly always needed, or needed more than once. What they share is the recognition that the moment a computation is requested need not be the moment it is performed.

The strongest historical case for deferral is also the clearest statement of when it pays. APL ran matrix arithmetic interactively on hardware nowhere near adequate for it, because its users almost always wanted a small part of a large result — so the system deferred until it knew which part, and computed only that.

Both strategies cost more to write, test, and maintain than plain evaluation, and both add structures whose sole purpose is tracking what has or has not been done. That cost is real and paid whether or not the strategy turns out to pay off, which is the reason for settling the frequency question with evidence rather than intuition before adopting either.
