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
- Verify the first half by breaking the code on purpose. Having written a test to catch a particular defect, introduce that defect deliberately and confirm the test complains; a test that has never been seen to fail is an assumption, not a safety net. On work where the suite genuinely has to be trusted, make it somebody's job — a separate copy of the source tree, defects introduced into it on purpose, and a check that the tests catch each one.

## Don't
- Don't tolerate a flaky test that sometimes fails on correct code; like the boy who cried wolf, it trains engineers to ignore failures and eventually to switch the test off, leaving no protection at all.
- Don't assume "fails when broken" implies "fails only when broken"; the two are separate properties and a test can have one without the other.

## Checklist
- Does every behavior have a test that would fail if that behavior broke — and have you watched it do so?
- Could this test fail while the code is actually correct, and if so why?
- Is the test free of randomness, timing dependence, and reliance on external systems?

## Notes
Accurate breakage detection is the primary purpose of a unit test, and Long stresses its two-sided nature: a test that misses breakages leaves gaps, but a flaky one that false-alarms is arguably worse, because ignored failures are no different from having no tests. This is the testing-side counterpart to the rule that breakage should fail compile or a test — here the emphasis is that the test signal must be trustworthy in both directions.

The asymmetry between the two properties is what makes deliberate sabotage worth the trouble. Flakiness announces itself: a test that fails on correct code fails in front of someone, repeatedly, until they deal with it. The opposite defect is completely silent — a test that would not notice the behaviour breaking passes exactly like a good one, contributes to the coverage figure exactly like a good one, and is indistinguishable from a good one until the day it is needed. The only way to tell the two apart is to break the code and watch, because a green suite is evidence about the tests only when you already know they can go red.

Treating the suite as a security system is the useful frame: the question you would ask about an alarm is not whether it is installed but whether anyone has tried to trip it. On projects where the tests are carrying real weight, formalising that into a role — someone working from a separate copy of the tree, planting defects and confirming each is caught — turns an assumption held by everybody into a check performed by somebody.
