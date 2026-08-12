---
object_id: PAT_define_your_code_contract_explicitly
object_type: pattern
name: Identify Your Code's Contract Explicitly
library_path:
- software-engineering
- core
- contracts
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_contracts
- preconditions
- postconditions
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_unmistakable_over_small_print
- rel: prerequisite_for
  target_object_id: PAT_convey_usage_through_names_and_types
- rel: prerequisite_for
  target_object_id: PAT_make_breakage_fail_compile_or_test
- rel: prerequisite_for
  target_object_id: PAT_prefer_unmistakable_over_small_print
- rel: prerequisite_for
  target_object_id: PAT_make_misuse_impossible_by_removing_invalid_states
- rel: prerequisite_for
  target_object_id: PAT_enforce_contracts_at_runtime_with_checks
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u03, pp. 55-56
  evidence_type: text
confidence: high
references: []
variants: []
---

# Identify Your Code's Contract Explicitly

## Pattern Rule
**IF** you are writing a function or class that takes inputs, returns values, or changes state
**THEN** recognize you have created a contract and spell out its three kinds of terms — preconditions, postconditions, and invariants — so that nothing a caller must know is left implicit or surprising.

## Do
- Name the preconditions: what must be true before the code runs — required inputs and the state the system must already be in.
- Name the postconditions: what will be true after — values returned and the new state the system is left in.
- Name the invariants: what must be unchanged between before and after the call.

## Don't
- Don't assume "I'm not programming by contract" means there is no contract — any function with parameters, a return value, or a side effect already imposes obligations and expectations.
- Don't leave contract terms in your head; problems arise precisely when a caller is unaware of some or all of the terms.

## Checklist
- Have you stated what a caller must set up or supply before calling (preconditions)?
- Have you stated what they get back and what state results (postconditions)?
- Have you named what must stay unchanged (invariants)?

## Notes
Long draws on the design-by-contract idea: interactions between pieces of code are a contract where the caller meets obligations and the callee delivers a result, with nothing left unclear. The value for everyday coding is the habit of making the three term-types conscious, because the failures come from unstated terms. Making the contract explicit is the setup for the next decision — which terms to make unmistakable versus leave as small print, and how to enforce them.
