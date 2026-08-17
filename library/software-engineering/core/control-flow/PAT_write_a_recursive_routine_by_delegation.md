---
object_id: PAT_write_a_recursive_routine_by_delegation
object_type: pattern
name: Write the Recursive Call as a Call to Something Else
library_path:
- software-engineering
- core
- control-flow
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- recursion
- control_flow
- decomposition
- working_memory
cross_links:
- rel: related_to
  target_object_id: PAT_bound_recursion_before_you_reach_for_it
- rel: related_to
  target_object_id: PAT_reason_with_a_notional_machine_at_a_chosen_level
reference:
  source_title: 'Think Like a Programmer: An Introduction to Creative Problem Solving'
  author: V. Anton Spraul
confidence: high
references: []
variants: []
---

# Write the Recursive Call as a Call to Something Else

## Pattern Rule
**IF** you have settled that a problem should be solved recursively and are about to write the routine
**THEN** write it as though the recursive call went to a different routine that already works and simply returns the right answer for a smaller input — fully handle the trivial case without delegating, hand off the largest share you can, combine what comes back — and only then let it call itself.

## Do
- Fix the question the routine answers, in one sentence, before writing any of it, and make the delegated call ask that same question about a smaller input. A routine whose question you cannot state has nothing to hand off, which is why it will not come out.
- Obey two rules while writing the delegating version. It must completely handle the most trivial case without delegating at all, and every delegated call must be given a strictly smaller version of the problem.
- Hand off as much as possible and keep as little as you can. Summing an array of n by asking for the sum of the first n−1 and adding the last element leaves almost nothing behind — which is the shape you want, because whatever you keep is work that has to be right at every level.
- Give the recursive routine the parameters it actually needs, then hide them behind the interface the caller deserves. A tree asked how many leaves it has should take no arguments, but the descent needs a node to start from — so write the recursive routine separately with the parameter it requires and have the public method call it with the starting value.
- Pick the trivial case so the routine keeps its tolerance. Terminating on the empty input rather than the single-element one usually costs nothing and leaves the routine working on degenerate input a caller may legitimately pass.

## Don't
- Don't try to hold the whole descent in your head. Tracing what happens three levels down is what makes recursive code feel hard, and it is precisely the work this construction removes — the correctness argument is local, and every level below is by construction somebody else's problem.
- Don't over-guard. Code written by somebody uneasy about recursion has a recognisably too-careful look, with several special cases where one was needed, and the surplus branches are usually where the defects are.
- Don't start typing before the question and the trivial case are settled. Beginning too early is what produces a routine held together by fixes bolted on as unforeseen interactions surfaced.
- Don't drive the descent through a global or a member variable instead of through a parameter. If nothing in the call changes, nothing moves the problem toward its base case, and no terminating test can save it.

## Checklist
- What question does this routine answer, in one sentence?
- Does the delegated call ask that same question about a strictly smaller input?
- Is the trivial case handled completely, with no delegation at all?
- Have you kept the smallest share of the work that you could?
- Do the parameters the descent needs appear in the caller's interface, and should they?

## Notes
The reframing is the whole technique: when you delegate, you are concerned with *what* comes back and not with *how* it was produced. A worker who asks the next person down the line for a count does not prescribe a method, and would get the right answer even if that person counted some other way. Writing a recursive routine as if the call went somewhere else buys exactly that indifference — and the payoff is that the reasoning stays local, which is what makes recursion writable before it is intuitive.

The construction can be run literally as a two-step when the recursion is not obvious. Write a version that delegates to a *separate* routine that solves the smaller problem, satisfy yourself that the two rules hold, then rename the delegate to be the routine itself and delete the separate one. Nothing about the logic changes at that step, which is the point — if the delegating version was correct, the self-calling version is the same code. In practice you stop writing the intermediate version once you trust the shape, but it is worth doing once, because it demonstrates that the recursion was never the hard part.

The parameter tension is worth expecting rather than discovering. The interface a caller wants and the interface a descent needs pull in opposite directions: asking an object about itself should require no arguments, while a recursion with no changing argument cannot progress. Writing the recursive routine first, as a free function with whatever parameter it needs, and wrapping it afterwards resolves this in the right order — the alternative is contorting the public method until it can carry bookkeeping the caller should never see.

This sits alongside the bounding rule rather than overlapping it. That one decides whether recursion is the right choice at all and establishes what stops the descent; this one is how to get a correct routine written once those questions are answered. Both are needed, and they fail differently — a routine built this way can still recurse forever if nothing terminates it.
