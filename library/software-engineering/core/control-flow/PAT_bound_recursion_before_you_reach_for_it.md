---
object_id: PAT_bound_recursion_before_you_reach_for_it
object_type: pattern
name: Bound Recursion Before You Reach For It
library_path:
- software-engineering
- core
- control-flow
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- recursion
- control_flow
- termination
- stack
cross_links:
- rel: related_to
  target_object_id: PAT_keep_a_loops_control_outside_its_body
- rel: related_to
  target_object_id: PAT_choose_the_loop_by_where_it_tests
- rel: related_to
  target_object_id: PAT_instrument_for_defects_that_cannot_announce_themselves
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Bound Recursion Before You Reach For It

## Pattern Rule
**IF** a problem decomposes into smaller versions of itself and you are considering solving it recursively
**THEN** confirm first that the recursive version is genuinely simpler than the iterative one, and then establish what stops it before writing the call.
**ELSE** where iteration expresses it as clearly, take the iterative version — anything achievable with recursion is achievable with a stack and a loop, and the iterative form has predictable memory behaviour that the recursive form does not.

## Do
- Name the terminating condition before writing the recursive call, and check that some path through the routine does not recurse. The maze walker stops on two of them — the position has already been tried, or the position is the exit — and both are tested before any further move is attempted.
- Record what you have already visited when the structure can contain cycles. Marking each position as it is reached is what prevents the walker from circling forever, and it is a separate mechanism from the terminating test rather than a refinement of it.
- Add a depth counter where no simple terminating test exists. It has to survive across calls, so it is a member of the enclosing object or a parameter passed down — a local re-created on each call counts nothing.
- Keep the recursion inside one routine. A cycle that runs through two or three routines before returning to the first is genuinely hard to see, and if the design will not collapse to a single self-calling routine, the depth counter stops being optional.
- Watch what the routine puts on the stack. Recursion gives no guarantee about how much stack it will consume and no way to predict the run-time behaviour in advance, so size any depth limit against the stack you are willing to spend, and allocate memory-heavy locals from the heap rather than letting each level carry them.

## Don't
- Don't use recursion for problems that are plainly iterative. A factorial computed recursively is slower, uses run-time memory unpredictably, and is harder to read than the loop that does the same job — and the same goes for a Fibonacci sequence. That these are the standard textbook examples has done real damage, because they teach the mechanism using the cases where it is least appropriate.
- Don't reach for it because the problem *can* be expressed recursively. The band where recursion produces a simple and elegant solution is narrow; just outside it lies a band where the solution is elegant and hard to understand, and beyond that most problems where it produces something massively complicated.
- Don't rely on the terminating test being obviously correct. The whole failure mode here is unbounded descent, and it is the one bug in this area whose symptom — an exhausted stack — points nowhere near its cause.

## Checklist
- What exactly stops this, and is there a path through the routine that does not call itself?
- Can the structure being traversed contain a cycle, and if so what records where you have been?
- Does anything guarantee a maximum depth, and does that guarantee survive across calls?
- Does the recursion stay within one routine, or does it travel through others?
- What does each level place on the stack, and how many levels can the stack hold?
- Would a loop express this as clearly?

## Notes
The selection question deserves more weight than it usually gets, because recursion is taught as a technique to be admired rather than one to be chosen. The honest range is narrow — a small group of problems where the recursive solution is genuinely simpler, a slightly larger group where it is elegant but hard to follow, and most problems where it produces something far more complicated than a loop would. The maze walker is a fair example of the first group: the alternative is substantially more complex, and the recursive version reads almost as a description of the strategy. The factorial is the standard example of the third, and it is the one most people learn from.

The bounding mechanisms are worth distinguishing because they fail differently. A terminating test is the primary defence and the only one that expresses the problem's own structure — the recursion stops because the work is done. A visited-marker is a second, separate mechanism needed only when the thing being traversed can lead back to itself, and forgetting it produces unbounded descent even though a correct terminating test exists. A depth counter is a backstop rather than a solution: it does not make the recursion correct, it makes the failure detectable and survivable, which is why it belongs where the first two cannot be established.

The stack is the part that makes this different from an unbounded loop. A runaway loop spins and can be interrupted; a runaway recursion consumes a resource you did not allocate, cannot easily observe, and whose exhaustion surfaces as a failure with no useful information about what caused it. That is the same shape as any defect that produces no signal at its source, and the same response applies — the depth counter is instrumentation, added because the natural failure mode tells you nothing.
