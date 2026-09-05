---
object_id: PAT_keep_tests_agnostic_to_implementation
object_type: pattern
name: Test Through the Public API, Not Implementation Details
library_path:
- software-engineering
- core
- testing
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- unit_testing
- implementation_details
- refactoring
- public_api
cross_links:
- rel: related_to
  target_object_id: PAT_expose_clean_api_hide_implementation
- rel: related_to
  target_object_id: PAT_design_for_testability
- rel: related_to
  target_object_id: AP_write_a_unit_test_suite
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Test Through the Public API, Not Implementation Details

## Pattern Rule
**IF** you are deciding how a test should set up state and verify behavior
**THEN** do it through the code's public API and lock in behaviors only, never reaching into private functions, member variables, or other implementation details.

## Do
- Test what callers care about: for a kinetic-energy function, assert the returned value for given inputs rather than checking that it happens to call a power function internally.
- Lock in behaviors so a correct refactoring leaves tests green — that passing signal is exactly how you confirm a structural change did not alter behavior.
- Separate the two kinds of change: make a functional change (which should alter behavior and its tests) or a refactoring (which should not), but not both at once, so you can reason about what changed.

## Don't
- Don't lock in implementation details by exposing private functions to tests, manipulating private variables, or asserting on internal state; such tests break on every refactoring whether or not you made a mistake, destroying the refactoring signal.
- Don't leave a passing test after a functional change; if behavior changed and no test needed updating, the tests were insufficient.

## Checklist
- Does the test set up and verify through the public API rather than internals?
- Would a behavior-preserving refactoring leave this test passing untouched?
- Are functional changes and refactorings kept in separate commits?

## Notes
Mature codebases refactor constantly — often more than they add new code — so the value of a test hangs on surviving a behavior-preserving refactoring. Long's approach A (tests locked to internals) versus approach B (tests locked to behaviors via the public API) makes the difference stark: only approach B gives a clean refactoring signal where green means safe and red means a real mistake. This applies the public-API-versus-implementation-detail split to test design.
