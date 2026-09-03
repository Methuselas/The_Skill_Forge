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
2. List the implementation details the original test depends on, before changing it.
3. Identify the actual behavior a caller cares about (the return value or resulting state), separate from how the code achieves it.
4. Rewrite the test to arrange and assert only through the public API, checking the behavior rather than the mechanism.
5. Search the rewritten test for any reference to a non-public member and state the result of that search.
6. Perform a behavior-preserving refactoring of the code under test (rename internals, split a function) and run the tests untouched.
7. Then change a behavior and show the test failing.
8. Name what coverage, if any, was lost in moving to the public surface.

## Success Check
- The implementation details the original test depends on are listed before the rewrite, so what is being given up is visible rather than implied.
- The rewritten test arranges and asserts only through the public surface, checked by searching the test for any reference to a non-public member and stating the result of that search.
- A behaviour-preserving refactoring is actually applied and the suite run untouched. That it would pass is precisely the claim under test.
- A behaviour is then actually changed and the test shown to fail. A test surviving every refactoring may simply have stopped asserting anything, and only this check tells the two apart.
- The run names what coverage was lost in moving to the public surface, if any, so the trade is recorded rather than assumed to be free.

## Common Failures
- Moving assertions to the public API but keeping one that peeks at internal state.
- Rewriting the test so loosely that a real behavior change no longer fails it.

## Notes
This drills Long's approach A versus approach B contrast. The habit is to test the behavior callers depend on, not the internals, so that green tests after a refactoring are trustworthy evidence that no behavior changed.
