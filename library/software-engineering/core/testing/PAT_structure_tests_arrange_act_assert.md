---
object_id: PAT_structure_tests_arrange_act_assert
object_type: pattern
name: Structure a Test Case as Arrange, Act, Assert
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
- arrange_act_assert
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_design_for_testability
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u10, pp. 266-268
  evidence_type: text
confidence: high
references: []
variants: []
---

# Structure a Test Case as Arrange, Act, Assert

## Pattern Rule
**IF** you are writing a unit test case for anything beyond the very simplest scenario
**THEN** divide it into three distinct blocks — arrange, act, assert — so a reader can see the setup, the exercised behavior, and the checks at a glance.

## Do
- Put all setup in the arrange block: define test values, set up dependencies, and construct a correctly configured instance of the code under test.
- Invoke the one behavior under test in the act block, keeping it a small, clear step distinct from setup.
- Check the outcome in the assert block, verifying return values or resulting state produced by the act.

## Don't
- Don't interleave setup, invocation, and checks so the reader cannot tell what is being exercised from what is being prepared or verified.
- Don't let the act block do the arranging; a test that constructs and configures inside the call being tested obscures what the case actually exercises.

## Checklist
- Can a reader identify the setup, the exercised behavior, and the checks as separate blocks?
- Does the act block invoke exactly the behavior this case is about?
- Are all assertions about the outcome of that single act?

## Notes
The arrange-act-assert shape is the conventional skeleton of a test case: a test file holds many test cases, each a function exercising one behavior, and each splits into setup, invocation, and verification. Long presents it as the everyday structure that keeps a test case legible, which underpins the later principles — one behavior per case and understandable test code both build on cleanly separated arrange, act, and assert sections.
