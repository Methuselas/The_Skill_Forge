---
object_id: PAT_keep_unit_tests_fast_to_run
object_type: pattern
name: Keep Unit Tests Fast and Easy to Run
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
- test_speed
- developer_experience
- presubmit
cross_links:
- rel: related_to
  target_object_id: PAT_design_for_testability
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u10, pp. 273-274
  evidence_type: text
confidence: high
references: []
variants: []
---

# Keep Unit Tests Fast and Easy to Run

## Pattern Rule
**IF** you are writing unit tests that engineers will run repeatedly
**THEN** keep them fast and easy to run, because tests are exercised constantly during development and at presubmit, and slow or awkward tests waste time and discourage testing.

## Do
- Budget for frequency: tests gate every submission and run many times while coding, so a suite that takes an hour adds an hour to even a trivial change.
- Design tests to run without heavy external setup, so they stay quick and an engineer can run them on a whim.

## Don't
- Don't let tests become slow or painful to run; when testing hurts, engineers quietly do less of it, and coverage suffers.
- Don't build in unnecessary reliance on slow real dependencies when a faster alternative would exercise the same behavior.

## Checklist
- Can the relevant tests run quickly enough to sit in a presubmit check without slowing everyone down?
- Are tests easy enough to run that engineers will actually run them often?
- Does anything make a test needlessly slow that could be trimmed without losing coverage?

## Notes
Speed is a first-class property of a good unit test because it shapes behavior: Long observes that slow, painful tests lead engineers to test less, so keeping them fast improves not just efficiency but coverage. Presubmit checks that run tests before every merge make suite speed a tax on the whole team's velocity. This property pairs with testability from chapter 1 — code designed to run in isolation is exactly the code whose tests stay fast.
