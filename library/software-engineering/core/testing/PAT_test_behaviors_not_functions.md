---
object_id: PAT_test_behaviors_not_functions
object_type: pattern
name: Test Behaviors, Not Just Functions
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
- test_coverage
- behaviors
- error_handling
cross_links:
- rel: related_to
  target_object_id: PAT_write_well_explained_test_failures
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Test Behaviors, Not Just Functions

## Pattern Rule
**IF** you are deciding what test cases a piece of code needs
**THEN** enumerate its important behaviors and write a case for each, rather than writing a single test per function and assuming that covers it.

## Do
- Map the behaviors a function actually exhibits: a mortgage assessor decides eligibility, computes a maximum loan, and handles ineligible applicants, each a behavior deserving its own case.
- Include error scenarios as behaviors: a debit that throws on a negative amount is an important behavior, so test both that it throws and that the exception carries the expected message.

## Don't
- Don't settle for one test case per function; a single case exercises only some of what the function does and leaves other behaviors unprotected.
- Don't count a function as tested just because a test calls it; calling it is not the same as verifying each behavior it should exhibit.

## Checklist
- Have you listed every important behavior, including error and edge cases?
- Does each behavior have its own test case exercising and checking it?
- Are you testing behaviors, or merely that each function is called once?

## Notes
Long reframes coverage from functions to behaviors: a class with a single test on its entry function looks tested but leaves most of its behaviors unchecked. The debit-throws-on-negative example shows error handling is itself a behavior to lock in. This practice is the concrete driver behind the chapter-10 principles — once you test one behavior per case, descriptive naming and well-explained failures follow naturally.
