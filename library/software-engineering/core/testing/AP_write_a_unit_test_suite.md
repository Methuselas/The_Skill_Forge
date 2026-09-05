---
object_id: AP_write_a_unit_test_suite
object_type: ap
name: Write a Unit Test Suite for a Piece of Code
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
- test_design
- behaviors
- test_doubles
cross_links:
- rel: supports
  target_object_id: PAT_test_behaviors_not_functions
- rel: supports
  target_object_id: PAT_prefer_fakes_over_mocks_and_stubs
- rel: supports
  target_object_id: PAT_keep_tests_agnostic_to_implementation
- rel: supports
  target_object_id: PAT_split_code_to_make_it_testable
- rel: supports
  target_object_id: PAT_use_test_double_only_when_needed
- rel: supports
  target_object_id: PAT_test_one_behavior_per_case
- rel: supports
  target_object_id: PAT_structure_tests_arrange_act_assert
- rel: supports
  target_object_id: PAT_use_appropriate_assertion_matchers
- rel: supports
  target_object_id: PAT_write_well_explained_test_failures
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Write a Unit Test Suite for a Piece of Code

## Objective
Produce a unit test suite that locks in every important behavior of a piece of code, stays agnostic to implementation details, and fails clearly when something breaks.

## Steps / Flow
1. **Enumerate the important behaviors.** List everything the code should do that matters — normal results, edge cases, and error scenarios — rather than planning one test per function. `PAT_test_behaviors_not_functions` owns what counts as a behavior.
2. **Plan to test each behavior through the public API.** Decide how to trigger and verify each behavior via public functions, parameters, return values, and error signals; if a behavior is important but unreachable through a narrow public API, plan to set up the needed dependency and verify the side effect. `PAT_keep_tests_agnostic_to_implementation` owns how far through the surface a test may reach.
3. **If testing via the public API is infeasible, split the code.** When a class is too complex to test through its surface, extract the tangled subproblem into its own class with its own testable public API instead of exposing private functions. The split is `PAT_split_code_to_make_it_testable`.
4. **Choose real dependencies, then fakes, then mocks or stubs.** Use real dependencies where feasible; substitute a fake when the real one is slow, causes real-world side effects, or is nondeterministic; fall back to a mock or stub only as a last resort. Make dependencies injectable so tests can supply doubles. `PAT_prefer_fakes_over_mocks_and_stubs` owns the ordering, and `PAT_use_test_double_only_when_needed` owns whether a double is warranted at all.
5. **Write one focused case per behavior.** Give each behavior its own descriptively named case structured as arrange, act, assert; use parameterized tests for behaviors that differ only by input, and keep outcome-affecting setup inside each case with helper functions for boilerplate. `PAT_test_one_behavior_per_case` owns the granularity, and `PAT_structure_tests_arrange_act_assert` owns the shape.
6. **Assert with fitting matchers, then verify the suite's signals.** Pick a matcher that checks exactly the behavior and explains a failure clearly; then confirm the suite fails when a behavior breaks, survives a behavior-preserving refactoring, and runs fast enough to run often. `PAT_use_appropriate_assertion_matchers` owns the matcher, and `PAT_write_well_explained_test_failures` owns what the failure has to say.

## Notes
This threads the principles and the practices into one procedure: the good-test principles (accurate, agnostic, well-explained, understandable, fast) become the checks in steps 5 and 6, while the practices (behaviors not functions, public-API testing, splitting to test, careful shared setup, appropriate matchers, injection for testability) become the steps. The ordering matters — behaviors first because they define the suite, public-API testing before test doubles because doubles are a fallback, and signal verification last because a suite that does not fail on real breakage, or fails on refactoring, has not met its purpose.
