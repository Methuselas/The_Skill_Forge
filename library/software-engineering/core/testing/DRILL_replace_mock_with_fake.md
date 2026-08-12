---
object_id: DRILL_replace_mock_with_fake
object_type: drill
name: Replace a Mock With a Fake and Catch the Hidden Bug
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
- fakes
- mocks
- refactoring
cross_links:
- rel: teaches
  target_object_id: PAT_prefer_fakes_over_mocks_and_stubs
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u10, pp. 288-294
  evidence_type: text
confidence: high
target_skill: swapping a mock-based test for a fake-based one to catch realism bugs and decouple from internals
references: []
variants: []
---

# Replace a Mock With a Fake and Catch the Hidden Bug

## Practice Task
Take a test that mocks a dependency and passes despite a real bug, replace the mock with a contract-faithful fake, and watch the bug surface.

## Target Skill
Swapping mock-based verification for a fake that enforces the real contract and asserts on end state.

## Setup
No special setup required.

## Instructions
1. Start from a test that mocks a dependency and verifies a specific call was made — for example checking that debit was called with a negative amount to "handle" a refund.
2. Read the real dependency's contract and find the assumption the mock silently repeats (the real debit rejects negative amounts).
3. Write or obtain a fake that implements the contract faithfully — storing state internally and throwing on a negative debit, matching the real behavior.
4. Rewrite the test to use the fake and assert on the resulting state (the final balance) rather than on which calls were made.
5. Run it and confirm the previously hidden bug now fails the test; then refactor the code (switch to a single transfer call) and confirm the fake-based test still passes.

## Success Check
- The fake enforces the same contract as the real dependency.
- The test now fails on the bug the mock concealed.
- After a behavior-preserving refactoring, the fake-based test still passes.

## Common Failures
- Writing a fake that is as lenient as the mock, so it re-hides the bug.
- Asserting on internal calls even with a fake, reintroducing implementation coupling.

## Notes
This drills Long's negative-invoice-balance example, where a mock made a broken payment pass and later broke on a `transfer` refactor. The lesson is that a fake catches realism bugs the mock repeats and, by asserting on end state, stays agnostic to how the code moves the money.
