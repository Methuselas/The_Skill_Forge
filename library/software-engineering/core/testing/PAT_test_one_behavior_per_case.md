---
object_id: PAT_test_one_behavior_per_case
object_type: pattern
name: Test One Behavior Per Test Case
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
- test_structure
- parameterized_tests
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_write_well_explained_test_failures
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u11, pp. 312-317
  evidence_type: text
confidence: high
references: []
variants: []
---

# Test One Behavior Per Test Case

## Pattern Rule
**IF** a piece of code has several behaviors to verify
**THEN** give each behavior its own well-named test case rather than checking everything in one large case, so the tests stay understandable and failures pinpoint the broken behavior.

## Do
- Split a catch-all case into focused ones: instead of one `testGetValidCoupons_allBehaviors`, write a case per rule that a coupon must satisfy, each named for its behavior.
- Keep each case simple enough that a reader can follow its arrange, act, and assert and see exactly what it verifies.
- Use parameterized tests to avoid repetition: write one case function that runs over several named input sets, so each set's failure is reported with its own descriptive suffix.

## Don't
- Don't cram many behaviors into one giant case; it is hard to understand and a failure does not reveal which behavior broke.
- Don't let a parameterized set go unnamed; without a per-set name the failure message loses the specificity that made splitting worthwhile.

## Checklist
- Does each test case verify exactly one behavior?
- Can you tell from a failing case's name which behavior broke?
- Where cases differ only by input, are they a parameterized test with named sets?

## Notes
Long contrasts one bloated `testGetValidCoupons_allBehaviors` with a focused case per behavior: the split versions are simpler to read and their names alone identify what failed. Parameterized tests reconcile "one behavior per case" with avoiding duplication — one function, many named input sets, each failure tagged with its set name. This operationalizes the chapter-10 principles of understandable test code and well-explained failures.
