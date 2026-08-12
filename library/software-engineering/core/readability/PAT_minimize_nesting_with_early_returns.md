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
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 117-120
  evidence_type: text
confidence: high
references: []
variants: []
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
Long ties nesting to the chapter-2 lesson on function size: the flat `getOwnersAddress` reads top-to-bottom because every branch returns, but the version that also sends a letter cannot flatten until the address logic is extracted, since an early return would skip the send. The two moves compose — extract the sub-job, then flatten with guard clauses — and deep nesting is often the visible symptom of a function doing too much.
