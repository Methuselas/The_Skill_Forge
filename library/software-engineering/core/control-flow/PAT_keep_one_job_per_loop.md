---
object_id: PAT_keep_one_job_per_loop
object_type: pattern
name: Give Each Loop One Job, Even When Two Would Fit in One Pass
library_path:
- software-engineering
- core
- control-flow
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- loops
- control_flow
- premature_optimization
- maintainability
cross_links:
- rel: related_to
  target_object_id: PAT_keep_a_loops_control_outside_its_body
- rel: related_to
  target_object_id: PAT_write_functions_as_single_sentences
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Give Each Loop One Job, Even When Two Would Fit in One Pass

## Pattern Rule
**IF** you are about to do two pieces of work in one traversal because one pass looks cheaper than two
**THEN** write the loops separately, one job each, and record in a comment that they could be combined if performance ever demanded it
**ELSE** once a benchmark has identified that section as a real problem, merging is the right response and the comment is the instruction for how to do it.

## Do
- Name the reason you are merging. It is nearly always speed rather than clarity, and that is worth noticing because the read-aloud test that catches an overloaded routine does not fire on a loop — a loop doing two things per pass describes itself perfectly well.
- Treat "this loop could carry both" as insufficient. Being *able* to do a second job in the same traversal is not a reason to give it one.
- Write the comment. Without it the separation reads as something nobody considered; with it, the decision is recorded and the optimization stays available to whoever eventually needs it.
- Wait for a measurement. Leave the two loops alone until a benchmark says that section matters, at which point the comment already says what to do.
- Tell one job apart from two smuggled into one pass. Accumulating a count and a total over the same records is a single traversal doing a single thing, not a violation of this.

## Don't
- Don't accept an unmeasured efficiency argument for merging. The cost is paid immediately in a loop that now has two reasons to change, and the benefit is speculative until something measures it.
- Don't skip the comment on the grounds that the separation is obvious. It is obvious only to the person who just made the decision.
- Don't use this to argue against merging once a benchmark has spoken. A measured requirement outranks the default, and refusing it then is the same mistake in the other direction.

## Checklist
- Is the argument for combining these traversals clarity, or speed?
- If speed — has anything actually measured this section?
- Does a comment record that combining is available and that it was deliberately not done?
- Are these genuinely two jobs, or one job that happens to touch two variables?

## Notes
The one-job rule is familiar at the level of a routine, where an overloaded one is caught by trying to read it aloud as a single sentence and hearing the sentence go clunky. That detector does not transfer to loops, and the reason is worth holding onto: nobody merges two loops because the merged version reads better. They merge because one traversal looks cheaper than two. The merged loop then narrates itself without any strain — it does this and that, once per element — so the heuristic has nothing to catch.

What replaces the heuristic is a procedure rather than a diagnosis, and its centre of gravity is the comment. A pair of adjacent loops over the same data looks, to a later reader, like an oversight; the comment converts it into a recorded judgment and carries the intended optimization forward. That is the whole mechanism by which the decision survives contact with someone who did not make it.

The exception is not a loophole but a genuine limit. Two pieces of work that are really one job — a count and a total accumulated over the same records — belong in one loop, and separating them would be the error this card is guarding against in mirror image. Likewise a benchmark that identifies the traversal as a bottleneck settles the question in favour of merging, and the comment written earlier is what makes that merge cheap.

When that day comes, the merge has a name and a set of preconditions worth knowing in advance. It is called **jamming**, or fusion, and what it buys is the loop overhead of one traversal instead of two — measured between roughly 4 and 32 percent depending on the language, which is the usual reminder that the gain has to be confirmed where you work rather than assumed. Two conditions gate it. The loops must run over the same range, so if the counters have drifted apart since they were written they have to be reconciled first. And the combined body must still be correct with respect to the code around it: two loops that were separated by something reading the first loop's results cannot simply be fused. Checking both before merging is what keeps a benchmark-driven change from becoming a defect.
