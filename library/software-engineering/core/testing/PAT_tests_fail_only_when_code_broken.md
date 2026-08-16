---
object_id: PAT_tests_fail_only_when_code_broken
object_type: pattern
name: Make Tests Fail When and Only When the Code Is Broken
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
- regression_testing
- flaky_tests
- determinism
cross_links:
- rel: related_to
  target_object_id: PAT_make_breakage_fail_compile_or_test
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Make Tests Fail When and Only When the Code Is Broken

## Pattern Rule
**IF** you are writing a unit test
**THEN** ensure it fails whenever the code under test is broken, and only when it is genuinely broken — never intermittently for reasons unrelated to a real defect.

## Do
- Lock in every behavior with a test so a later change that breaks it (a regression) is caught, giving both initial confidence and protection against future breakage.
- Remove sources of nondeterminism that cause flakiness — randomness, timing-based race conditions, or dependence on an external system — so a pass or fail reflects the code, not luck.

## Don't
- Don't tolerate a flaky test that sometimes fails on correct code; like the boy who cried wolf, it trains engineers to ignore failures and eventually to switch the test off, leaving no protection at all.
- Don't assume "fails when broken" implies "fails only when broken"; the two are separate properties and a test can have one without the other.

## Checklist
- Does every behavior have a test that would fail if that behavior broke?
- Could this test fail while the code is actually correct, and if so why?
- Is the test free of randomness, timing dependence, and reliance on external systems?

## Notes
Accurate breakage detection is the primary purpose of a unit test, and Long stresses its two-sided nature: a test that misses breakages leaves gaps, but a flaky one that false-alarms is arguably worse, because ignored failures are no different from having no tests. This is the testing-side counterpart to chapter 3's rule that breakage should fail compile or a test — here the emphasis is that the test signal must be trustworthy in both directions.
