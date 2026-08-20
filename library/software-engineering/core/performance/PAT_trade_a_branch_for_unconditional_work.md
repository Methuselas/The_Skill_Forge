---
object_id: PAT_trade_a_branch_for_unconditional_work
object_type: pattern
name: Trade a Branch for Unconditional Work
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
- branches
- hardware
- optimization
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_confirm_a_branch_is_mispredicted_before_optimizing_it
- rel: related_to
  target_object_id: PAT_count_the_dependency_chain_not_the_operations
- rel: related_to
  target_object_id: PAT_treat_a_compound_condition_as_several_branches
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Trade a Branch for Unconditional Work

## Pattern Rule
**IF** measurement has shown a hot loop losing time to a genuinely unpredictable branch
**THEN** consider computing every alternative unconditionally and selecting the result by indexing, spending spare execution capacity to buy back the pipeline flushes
**ELSE** where the branch is well predicted, or the loop body is expensive relative to a flush, leave the conditional alone — the trade runs the wrong way.

## Do
- Make the selection an index rather than a jump. A loop that adds into one of two accumulators according to an unpredictable flag becomes an array of two pointers indexed by the flag, so every iteration executes identical straight-line code; that transformation measured three and a half times faster than the branching original.
- Extend the same move to the computation, not just the destination. Where the two paths compute different expressions, evaluate both into a two-element array and index it with the condition alongside indexing the destination — more arithmetic, no jumps, and it still wins.
- Rely on the boolean converting to zero or one, and make sure it really does. The index arithmetic depends on `true` being exactly 1; a non-boolean type where any non-zero value counts as true will index out of range or silently pick the wrong slot.
- Accept doing both sides' work as the price of the technique. The reserve it spends is real — the gap between a perfectly predicted branch and a branchless version of the same loop is small, which says the processor had capacity sitting idle — but it is finite, and there is no rule of thumb for where it runs out.
- Try the simpler spelling first and check what it compiles to. Some compilers implement a conditional expression with a lookup rather than a jump, in which case writing the selection as `(b ? a1 : a2) += x` gets the same benefit with none of the damage to readability.
- Re-measure after every variant. Two branchless formulations of the same loop — one indexing the destination, one adding a zero into both accumulators — performed identically despite one doing considerably more work, which is not something to predict.

## Don't
- Don't apply it to a predictable branch. With a well-behaved condition the ordinary conditional code beats the branchless version, because the flushes it was buying back barely happen.
- Don't assume the compiler needs your help. A clamp loop rewritten around a 256-entry lookup table is usually slower than the straightforward conditional, which a modern compiler vectorizes into branch-free code that handles several elements at once — and profiling the original would have shown no misprediction problem to begin with.
- Don't convert a branch into an indirect call. Replacing a two-way `if` between function calls with an array of function pointers prevents inlining, and an unindirected call already disrupts the pipeline by itself; you give up a major optimization to remove a comparatively cheap event. The table starts to pay only when there are many alternatives — at which point a polymorphic design is worth considering, since that is exactly how virtual dispatch is implemented.
- Don't treat manual loop unrolling as this technique's simple case. Removing the loop-end check is real branch elimination in principle and almost never helps in practice: that branch is predicted nearly perfectly, and the compiler has usually unrolled or vectorized the loop already.
- Don't leave the readability cost unaccounted. A table of function pointers or a pair of index arrays is harder to read and considerably harder to debug than the `if` it replaced, and that cost is paid by everyone who touches the code afterwards.

## Checklist
- Has the branch been measured as unpredictable, rather than assumed to be?
- How much extra work does the branchless version do per iteration, and did it still win?
- Is the selector guaranteed to be exactly 0 or 1?
- Does the compiler already produce branch-free code for the original?
- Is the loop body cheap enough that a pipeline flush is a large fraction of it?
- Is the speedup worth what the rewritten code costs the next reader?

## Notes
The technique is one idea with many spellings: stop choosing which code to execute, execute the same code always, and move the conditional logic into an index. Everything else — pointer arrays, value arrays, lookup tables, adding zero — is a variation on where the index is applied.

Its economics rest on two facts that pull in opposite directions. A mispredicted branch is expensive, worth ten or more arithmetic instructions, and processors have idle execution capacity that unconditional work can occupy for close to free. But the capacity is bounded and the extra work is unconditional, so the return falls as the branch becomes more predictable and as the per-iteration work grows. Both quantities are properties of the data as much as the code, which is why this cannot be settled by inspection.

The prerequisite is not optional and is the most common way this goes wrong. The transformations here are only ever worth their cost against a branch that has been shown to mispredict; applied on the theory that branches are bad, they produce slower, less readable code.
