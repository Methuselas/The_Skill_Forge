---
object_id: PAT_dont_expose_privates_for_testing
object_type: pattern
name: Don't Make Things Visible Just for Testing
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
- encapsulation
- public_api
- implementation_details
cross_links:
- rel: related_to
  target_object_id: PAT_dont_widen_api_for_reuse_or_testing
- rel: related_to
  target_object_id: PAT_keep_tests_agnostic_to_implementation
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Don't Make Things Visible Just for Testing

## Pattern Rule
**IF** you are tempted to expose a private function so a test can call it directly
**THEN** don't; test the behavior that matters through the public API instead, leaving the private function private.

## Do
- Test the outcome callers care about: verify a mortgage application is rejected for a bad credit rating by calling the public assess function, not the private eligibility helper.
- Recognize that a private helper is an implementation detail, so exercising it through the public API keeps the test aligned with what actually matters.

## Don't
- Don't test a private function directly; it verifies that the helper returns the right value, not that the public behavior actually happens — the entry function could stop calling it and the test would still pass.
- Don't rely on a "visible only for testing" comment; that small print is easily overlooked, so the newly public function effectively joins the public API and other code starts depending on it, freezing your ability to refactor.

## Checklist
- Is the behavior being tested reachable through the public API?
- Would this test still pass if the entry function stopped calling the helper it checks?
- Are you widening visibility with a comment that others will overlook?

## Notes
Making a private function visible to tests fails on three counts Long spells out: it tests an intermediate detail rather than the real outcome, it couples tests to internals so a rename or move breaks them, and the "visible for testing" comment is unreliable small print that quietly expands the public API. This is the testing-specific case of chapter 2's rule against widening the API to reach internals, and it keeps tests agnostic to implementation details.
