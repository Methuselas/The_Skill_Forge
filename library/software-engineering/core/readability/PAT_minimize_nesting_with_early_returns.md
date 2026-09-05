---
object_id: PAT_minimize_nesting_with_early_returns
object_type: pattern
name: Minimize Nesting With Early Returns and Function Extraction
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- nesting
- control_flow
- readability
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
- rel: related_to
  target_object_id: PAT_write_functions_as_single_sentences
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_run_the_nominal_path_down_the_if_branches
  variant_name: Run the Nominal Path Down the If Branches and Stack the Errors
  variant_basis: method_sequence
  difference_from_foundation: The foundation removes the nesting — each branch returns early, so the successful path ends up at the top level. This variant keeps the nesting and organizes it instead, which suits code that cannot simply return. Every test is written so its main branch holds the success case and its alternative holds the failure, without exception. The nominal path then reads straight down the successive main branches, and every error case collects at the bottom of the nest in reverse order of where it was detected. That stack of error branches at the bottom is the visible signature that the convention was followed, and its absence is how you spot code where the two kinds of case were interleaved. The failure it is aimed at is not depth but inconsistency — code that handles one failure in the main branch and the next in the alternative forces a reader to work out, at every level, which kind of case they are looking at, and there is no way to tell except by reading both.
  when_to_use: Use where returning early is not available or not wanted — a house style with a single exit, a sequence whose steps each need distinct cleanup, or a chain where a bare early return would skip shared later work. It is also the better fit when each stage's failure needs its own handling rather than a common rejection, since guard clauses tend to push differing failure responses to the top where their connection to the step that failed is lost.
  when_not_to_use: Do not use it when depth itself is the problem. Five levels of consistently-ordered nesting is still five levels, and where branches genuinely can return, flattening beats organizing. It also does not rescue a routine doing two jobs — that needs the foundation's extraction step first, after which either arrangement works.
  absorbed_from_object_id: none
- variant_id: VAR_flatten_by_restructuring_the_tests_themselves
  variant_name: Flatten by Restructuring the Tests Themselves
  variant_basis: method_sequence
  difference_from_foundation: The foundation attacks depth through control flow, returning early so later logic stops being nested, and through decomposition where a branch cannot return. This variant supplies a third lever that touches neither — rewriting the conditions so the nesting was never required. Three moves belong to it. Retesting part of the condition merges an inner test into a later top-level one, so four levels become two at the cost of a compound test that repeats terms from the outer conditions. Converting a nested decision tree into a chain of alternatives removes tests that were only redundant, since a check that a quantity exceeds a thousand makes the enclosing checks against a hundred and against ten unnecessary. Converting that chain again into a multi-way branch over ranges collapses it further where the language supports ranges as case labels. What distinguishes all three from the foundation is that the routine's shape and its decomposition are untouched; only the conditions change.
  when_to_use: Use where the nesting exists because the conditions were written as they were discovered rather than as they logically relate, which the redundant decision tree makes obvious once the numbers are lined up. Retesting is the move to reach for when a branch cannot return and extraction is not wanted, since it buys a real reduction in levels for a stated price. Reach for the range-based multi-way branch last, because when it applies it reads better than anything else here.
  when_not_to_use: Do not expect the reduction to be free — retesting trades levels for a longer condition that repeats terms, and if the compound test becomes harder to read than the nesting it removed, the trade failed. These moves also do nothing for a routine that is deeply nested because it is doing several jobs, where decomposition is the only real answer and rearranging its conditions just relocates the problem.
  absorbed_from_object_id: none
---

# Minimize Nesting With Early Returns and Function Extraction

## Pattern Rule
**IF** control-flow blocks are nested several levels deep and hard to follow
**THEN** flatten them — return early from each branch so later logic is not nested — and if branches cannot simply return, extract the inner logic into its own function first.

## Do
- Rewrite nested if-else that each end in a return as a flat sequence of guard clauses: handle the scrapyard and showroom cases with early returns so the buyer case sits at the top level.
- Treat nesting that does not resolve into returns as a signal the function does too much: `sendOwnerALetter` mixes address-finding with letter-sending, so extract `getOwnersAddress` and then the early-return flattening applies cleanly.

## Don't
- Don't leave deeply nested if-statements where the eye must track indentation levels to work out when each line runs.
- Don't try to early-return your way out of a function whose branches must fall through to shared later logic (like sending the letter); extract first, because a bare early return there would skip that logic.

## Checklist
- Does each branch return early rather than wrapping the rest of the function in an else?
- Where nesting will not flatten, is it because the function is doing two jobs that should be split?
- Is the deepest nesting level shallow enough to follow without counting indents?

## Notes
Long ties nesting to the lesson on function size: the flat `getOwnersAddress` reads top-to-bottom because every branch returns, but the version that also sends a letter cannot flatten until the address logic is extracted, since an early return would skip the send. The two moves compose — extract the sub-job, then flatten with guard clauses — and deep nesting is often the visible symptom of a function doing too much.

`VAR_run_the_nominal_path_down_the_if_branches` is the alternative for code that cannot return its way out, and it disagrees with the foundation about what the actual problem is. Long treats depth as the defect and flattens it. McConnell treats *inconsistency* as the defect and leaves the depth in place: write every test so its main branch is the success case and its alternative is the failure, without exception, and the nominal path then runs straight down the successive main branches while every error collects at the bottom of the nest. His diagnostic is worth having either way — a tidy stack of error branches at the bottom is the signature of code that followed the convention, and error handling scattered through both kinds of branch is the signature of code where nobody decided. The reason both cards exist is that the remedies need different things: guard clauses need the branches to be able to return, and this needs only that you be consistent, so it survives a single-exit style, per-step cleanup, and shared work that must run after the chain. Where returning is available, flatten; where it is not, at least be uniform. Neither rescues a routine doing two jobs, which needs the extraction step first.

`VAR_flatten_by_restructuring_the_tests_themselves` adds the third lever, and naming all three is what makes the set usable. Depth can be attacked through the control flow, which is what guard clauses do; through decomposition, which is what extraction does; or through the conditions, which is this. Retesting part of the condition folds an inner test into a later top-level one and trades four levels for two at the cost of a compound test that repeats terms. Converting a nested decision tree into a chain of alternatives deletes tests that were merely redundant, which is common because conditions get written in the order they were discovered rather than in the order they relate. Converting that chain into a multi-way branch over ranges goes further still where the language allows range labels, and it produces the most readable version of the four. The reason to hold the levers separately is that they fail in different situations — restructuring conditions does nothing for a routine that is nested because it does several jobs, and decomposition does nothing for a decision tree whose tests are simply redundant.
