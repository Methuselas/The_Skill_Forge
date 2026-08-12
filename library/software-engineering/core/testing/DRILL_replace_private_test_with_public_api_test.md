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
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u11, pp. 305-311
  evidence_type: text
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
- The behavior is verified through the public API, with no private function exposed.
- The test would catch the entry function failing to use the helper correctly.
- Any over-complex class has been split so each unit is testable through its own surface.

## Common Failures
- Rewriting the assertion but leaving the private function public "just in case."
- Forcing a public-API test on a class that should have been split, producing a tangled test.

## Notes
This drills Long's `MortgageAssessor` example across both fixes — test via the public `assess` function, and when the class does too much, extract a `CreditRatingChecker`. The reflex is that a private function you feel you must test is a signal to test the behavior through the public API or to split the class, never to widen visibility.
