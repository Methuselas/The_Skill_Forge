---
object_id: DRILL_rewrite_test_to_use_public_api
object_type: drill
name: Rewrite an Implementation-Coupled Test to Use the Public API
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
- refactoring
- public_api
- implementation_details
cross_links:
- rel: teaches
  target_object_id: PAT_keep_tests_agnostic_to_implementation
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: converting tests that verify internals into tests that verify behavior through the public API
references: []
variants: []
---

# Rewrite an Implementation-Coupled Test to Use the Public API

## Practice Task
Take a test that reaches into internals, rewrite it to verify behavior through the public API, and confirm a behavior-preserving refactoring now leaves it passing.

## Target Skill
Converting implementation-coupled tests into behavior tests that survive refactoring.

## Setup
No special setup required.

## Instructions
1. Start from a test that locks in implementation details — it exposes private functions, manipulates private member variables, or asserts on internal state.
2. Identify the actual behavior a caller cares about (the return value or resulting state), separate from how the code achieves it.
3. Rewrite the test to arrange and assert only through the public API, checking the behavior rather than the mechanism.
4. Perform a behavior-preserving refactoring of the code under test (rename internals, split a function) and run the tests.
5. Confirm the rewritten test still passes untouched, while the original would have failed and needed edits.

## Success Check
- The test sets up and verifies solely through the public API.
- A behavior-preserving refactoring leaves the test green with no edits.
- The test would still fail if an actual behavior changed.

## Common Failures
- Moving assertions to the public API but keeping one that peeks at internal state.
- Rewriting the test so loosely that a real behavior change no longer fails it.

## Notes
This drills Long's approach A versus approach B contrast. The habit is to test the behavior callers depend on, not the internals, so that green tests after a refactoring are trustworthy evidence that no behavior changed.
