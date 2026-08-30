---
object_id: DRILL_replace_private_test_with_public_api_test
object_type: drill
name: Replace a Private-Function Test With a Public-API Behavior Test
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
- public_api
- refactoring
- encapsulation
cross_links:
- rel: teaches
  target_object_id: PAT_dont_expose_privates_for_testing
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: converting a test of a private helper into a public-API behavior test, splitting the class if needed
references: []
variants: []
---

# Replace a Private-Function Test With a Public-API Behavior Test

## Practice Task
Take a test that calls a made-visible private function, rewrite it to verify the real behavior through the public API, and split the class if the public-API test proves too hard.

## Target Skill
Testing behaviors through the public API and recognizing when untestability means a class should be split.

## Setup
No special setup required.

## Instructions
1. Start from a class with a private helper made "visible only for testing" and a test that calls the helper directly.
2. Name the behavior that actually matters (an application is rejected for a bad credit rating), distinct from the helper's return value.
3. Rewrite the test to trigger and verify that behavior through the public entry function, and remove the helper's added visibility.
4. If testing through the public API feels infeasible because the class does too much, extract the complex subproblem into its own class with its own public API.
5. Confirm the behavior test passes, would fail if the entry function stopped calling the helper, and survives renaming the helper.

## Success Check
- The behaviour that matters is written as a sentence about the caller's outcome, before any rewrite, and it does not mention the helper.
- The added visibility is removed and the code still compiles, which is what establishes that the test no longer depends on it. A test rewritten while the escape hatch stays open has not been tested.
- The test is shown to fail when the entry function stops using the helper correctly, by actually breaking that link. This is the bullet separating a real behaviour test from one that passes for unrelated reasons.
- The helper is renamed and the test still passes untouched, demonstrating coupling to behaviour rather than to structure.
- Where a class had to be split instead, the new class's public surface is written out and the same checks are run against it. The split is the setup for this drill, not its conclusion.

## Common Failures
- Rewriting the assertion but leaving the private function public "just in case."
- Forcing a public-API test on a class that should have been split, producing a tangled test.

## Notes
This drills Long's `MortgageAssessor` example across both fixes — test via the public `assess` function, and when the class does too much, extract a `CreditRatingChecker`. The reflex is that a private function you feel you must test is a signal to test the behavior through the public API or to split the class, never to widen visibility.
