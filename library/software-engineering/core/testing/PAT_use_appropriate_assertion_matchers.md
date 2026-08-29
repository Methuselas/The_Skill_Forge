---
object_id: PAT_use_appropriate_assertion_matchers
object_type: pattern
name: Use an Assertion Matcher That Fits the Behavior
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
- assertions
- failure_messages
- matchers
cross_links:
- rel: related_to
  target_object_id: PAT_write_well_explained_test_failures
- rel: related_to
  target_object_id: AP_write_a_unit_test_suite
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Use an Assertion Matcher That Fits the Behavior

## Pattern Rule
**IF** you are writing an assertion in a test case
**THEN** choose a matcher that checks exactly the behavior under test and produces a clear failure message, not one that over-constrains or that reports failures opaquely.

## Do
- Match the matcher to the claim: to check that a result contains certain items regardless of order, use a contains-at-least matcher rather than a full-equality comparison.
- Prefer a matcher that explains a failure — one that reports the missing entry — so the person who broke the code learns what differs.
- Favor matchers that read like a sentence, since asserting that a list contains a value reads more clearly than asserting that a contains-check returned true.

## Don't
- Don't over-constrain with a full-equality assertion when only part of the result matters; it tests more than intended and breaks on details the contract does not guarantee, like an unspecified ordering, causing false alarms.
- Don't assert on a bare boolean (that a contains-check is true); its failure message says only that something expected to be true was false, explaining nothing.

## Checklist
- Does the matcher assert exactly the behavior this case is about, and no more?
- Would its failure message tell an unfamiliar engineer what actually differs?
- Are you avoiding equality checks on results whose order or extra content is not guaranteed?

## Notes
The assertion matcher decides both whether a test passes and how a failure reads. Long's class-names example runs the ladder: a full-equality assertion tests too much and breaks on an unguaranteed order, a bare boolean contains-check fixes that but fails opaquely, and a contains-at-least matcher tests just the behavior and names the missing entry on failure. Choosing the right matcher is how the chapter-10 principle of well-explained failures is realized in each assertion.
