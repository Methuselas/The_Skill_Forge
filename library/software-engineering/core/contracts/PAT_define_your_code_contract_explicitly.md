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
- rel: related_to
  target_object_id: AP_harden_a_code_contract
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
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
- Name the invariants: what must be unchanged between before and after the call. A class invariant holds whenever a caller can observe the object — on entry and on exit — and may legitimately be false partway through a routine, which is why no member participating in it can be left publicly writable.
- Put the precondition on the *caller*. Once the domain is stated in the contract, the routine may be written assuming its inputs are in range, and the burden of ensuring that sits where the knowledge is. It follows that a precondition is never the place to validate user input: breaking a contract is a bug in the program, not a fact about the data.
- Be strict in what you accept and promise as little as you can get away with. A contract that takes anything and guarantees the world is a contract you have to write all the code for.
- Where inheritance is in play, write the contract once in the base class. A subclass may accept a *wider* range of input and make *stronger* guarantees, but never less of either — that is what makes it genuinely usable through the base interface rather than merely compiling against it.

## Don't
- Don't assume "I'm not programming by contract" means there is no contract — any function with parameters, a return value, or a side effect already imposes obligations and expectations.
- Don't leave contract terms in your head; problems arise precisely when a caller is unaware of some or all of the terms.

## Checklist
- Have you stated what a caller must set up or supply before calling (preconditions)?
- Have you stated what they get back and what state results (postconditions)?
- Have you named what must stay unchanged (invariants)?

## Notes
Long draws on the design-by-contract idea: interactions between pieces of code are a contract where the caller meets obligations and the callee delivers a result, with nothing left unclear. The value for everyday coding is the habit of making the three term-types conscious, because the failures come from unstated terms. Making the contract explicit is the setup for the next decision — which terms to make unmistakable versus leave as small print, and how to enforce them.
