---
object_id: PAT_treat_a_compound_condition_as_several_branches
object_type: pattern
name: Treat a Compound Condition as Several Branches
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
- control_flow
- optimization
cross_links:
- rel: related_to
  target_object_id: PAT_confirm_a_branch_is_mispredicted_before_optimizing_it
- rel: related_to
  target_object_id: PAT_trade_a_branch_for_unconditional_work
- rel: related_to
  target_object_id: PAT_order_branches_so_the_common_case_is_found_first
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Treat a Compound Condition as Several Branches

## Pattern Rule
**IF** a hot conditional joins several tests with short-circuiting logical operators and the mispredictions are concentrated there
**THEN** count one branch per operand rather than one per `if`, and ask whether each of those is predictable — not whether the expression as a whole is
**ELSE** where the operands carry side effects or the later ones are unsafe to evaluate when an earlier one fails, the short-circuiting is load-bearing and the branches stay.

## Do
- Test the parts, not the result. A condition of the form `b1[i] || b2[i]` where the two arrays are exact complements is true on every single iteration, and it mispredicts at the rate of a coin flip, because which operand made it true alternates randomly — and that is what the hardware is predicting.
- Recognize the shape in real code: an expression that is nearly always true for varying reasons. Something like `(c1 && c2) || c3` where `c3` holds about half the time and `c1 && c2` covers most of the rest is three conditional jumps whose individual outcomes are unpredictable, wearing the costume of one reliable condition.
- Precompute the combined result into an array when the same conditions are consumed in a loop many times. Evaluating `c[i] = (c1[i] && c2[i]) || c3[i]` in one pass and branching on `c[i]` in another gives the consuming loop a perfectly predicted branch. The cost moves into the first loop, so this pays only when the second loop runs far more often than the first.
- Replace the logical operators with bitwise `&` and `|`, or with arithmetic `+` and `*`, to evaluate the whole expression without jumps. This requires the operands to be genuine booleans holding zero or one — `2 & 1` is zero while `bool(2) & bool(1)` is one, so an integer that merely tests as true will give the wrong answer.
- Weigh what unconditional evaluation costs before making the swap. Every operand now runs, side effects included; if `f1() || f2()` becomes `f1() + f2()`, the prediction improves and an expensive `f2()` may cost more than it saved.

## Don't
- Don't hoist the expression into a named boolean and expect the branches to go away. Assigning `const bool c = (c1 && c2) || c3;` and branching on `c` changes nothing: the operators still short-circuit, so the jumps are still there, and the compiler will likely delete the temporary variable entirely so the object code is unchanged.
- Don't expect the compiler to fix this for you. It may legally skip short-circuiting only when it can prove no operand has side effects, some compilers take that opportunity and most do not — and none of them know that the expression as a whole is usually true, which is the fact that makes the transformation worth doing.
- Don't apply this to a condition nobody measured. The transformations cost readability and change evaluation semantics, and a compound condition whose branches happen to be predictable is already free.
- Don't reach for it where the short-circuit is protecting something. A null check guarding a dereference, or a cheap test guarding an expensive call, is doing correctness or cost work that unconditional evaluation destroys.

## Checklist
- How many conditional jumps does this one `if` compile into?
- For each operand, is its own outcome predictable, or only the expression's?
- Do any operands have side effects, or depend on an earlier operand having passed?
- If precomputing into an array, does the consuming loop run enough times to repay the producing loop?
- Are all the operands actual booleans before you switch to bitwise or arithmetic operators?

## Notes
The gap this closes is between two meanings of "condition." A programmer reads `(c1 && c2) || c3` as one question with one answer. The processor sees the sequence the language mandates: test `c1`, and only if it holds test `c2`; if either fails, test `c3`. Each of those is a separate jump with its own prediction history, and a prediction history is kept per branch, not per expression.

Short-circuit evaluation is a language guarantee rather than an optimization choice, which is why the compiler's hands are largely tied. As soon as the result of the expression is determined, evaluation must stop — necessary when the operands have side effects, and the reason a programmer holding knowledge the compiler lacks is the one who has to make this call.

There is no general recipe here, and that is worth stating plainly rather than hiding behind a technique list. Which transformation wins depends on how often the condition holds, why it holds, what the operands cost, and what the compiler already did. The knowledge that decides it — which case is the normal one — is problem knowledge, and it has to be combined with a profile rather than applied on sight.
