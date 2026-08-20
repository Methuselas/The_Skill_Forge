---
object_id: PAT_lift_a_stable_runtime_value_to_compile_time
object_type: pattern
name: Lift a Stable Runtime Value to Compile Time
library_path:
- software-engineering
- languages
- cpp
- optimization
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- optimization
- templates
- performance
- branches
cross_links:
- rel: related_to
  target_object_id: PAT_optimize_for_what_the_compiler_can_prove
- rel: related_to
  target_object_id: PAT_confirm_a_branch_is_mispredicted_before_optimizing_it
- rel: related_to
  target_object_id: PAT_give_the_compiler_a_local_it_can_prove_is_unaliased
- rel: related_to
  target_object_id: PAT_factor_parameter_independent_code_from_templates
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Lift a Stable Runtime Value to Compile Time

## Pattern Rule
**IF** a hot loop tests a configuration value that does not change while the loop runs, and the compiler will not hoist the test out
**THEN** make the value a non-type template parameter and dispatch to the instantiation once, outside the loop, so the test becomes a compile-time constant and the untaken side disappears
**ELSE** where the configuration genuinely varies per iteration, the test is doing real work and there is nothing to lift.

## Do
- Change the parameter, not the body. Turning the function into a template on the configuration value and leaving the loop exactly as written is enough — inside each instantiation the condition is a constant, so the branch and its dead side are eliminated by ordinary constant folding.
- Keep the runtime decision, and move it to the top. A small non-template overload reads the value once and calls the right instantiation, so callers are unaffected and the test happens once per call instead of once per element.
- Reach for a lookup table when several independent flags combine. Packing the flags into an integer key and switching on it dispatches to one of the combinations without a chain of conditions — the shape that appears when a function computes several optional outputs and each null argument means "not wanted."
- Ask first why the compiler declined. If the value arrives by reference, no hoisting is possible at all, because a called function might change it — fixing that may be the whole job. If it arrives by value, the compiler *could* hoist and often will not, since doing so means duplicating the loop body.
- Confirm with a profile, not with the reasoning that got you here. The transformation generates a distinct function per combination, and whether that pays depends on how many elements are processed per configuration change.

## Don't
- Don't apply it where the configuration changes often. The gain comes from amortizing one dispatch over a long run of elements; with a short run, you have added a dispatch and a great deal of code for nothing.
- Don't ignore what the extra code costs. Every instantiation is another function in the binary: slower to load, and competing for the instruction cache against the code that actually runs. Five independent flags is thirty-two copies of the loop.
- Don't take the branch elimination as the only benefit, or you will misjudge which cases are worth it. Removing the test also removes the dead side, which can be most of the body, and lets the remaining code be optimized for the one configuration that survives.
- Don't leave the dispatch incomplete. A key computed from flags has a value for every combination, including ones the code does not implement, and the default case should say so rather than silently doing nothing.

## Checklist
- How many elements are processed between changes to this configuration value?
- Is the value reaching the loop by value or by reference?
- How many instantiations does this produce, and how large is each?
- Does the dispatch cover every combination the key can take?
- Does a profile show the gain, measured on realistic data volumes?

## Notes
The mechanism is worth stating plainly because it is why the loop body needs no editing: a template parameter is known during compilation, so a test against it is a test between two constants, and the compiler removes both the test and the branch that can never be taken. The refactoring that would otherwise be required — hoisting a condition out of a complex loop by hand and duplicating the body — is done by the compiler, correctly, from a change to the signature.

The compilers' reluctance here is reasonable rather than a defect. Hoisting a condition out of a loop means emitting the body more than once, and a compiler applying that eagerly across a program would produce a binary nobody wants. What the programmer supplies is not a better transformation but the knowledge of *where* the duplication is worth its cost.

This is the same trade as the branchless transformations, arriving by a different route. Both spend code size and complexity to remove a conditional from a hot path; the difference is that this one removes it at compile time and therefore costs nothing at run time, where the branchless version pays by doing both sides' work. Where the condition is genuinely stable, this is the better instrument.
