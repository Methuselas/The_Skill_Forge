---
object_id: DRILL_choose_an_appropriate_assertion_matcher
object_type: drill
name: Choose an Assertion Matcher for a Correct, Clear Failure
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
- matchers
- failure_messages
cross_links:
- rel: teaches
  target_object_id: PAT_use_appropriate_assertion_matchers
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u11, pp. 328-331
  evidence_type: text
confidence: high
target_skill: selecting an assertion matcher that tests exactly the behavior and explains failures clearly
references: []
variants: []
---

# Choose an Assertion Matcher for a Correct, Clear Failure

## Practice Task
Take a test whose assertion over-constrains or fails opaquely, and rewrite it with a matcher that checks exactly the behavior and reports failures clearly.

## Target Skill
Selecting an assertion matcher matched to the behavior under test and to failure explainability.

## Setup
No special setup required.

## Instructions
1. Start from a test verifying that a result contains certain items, where the result's order is documented as not guaranteed.
2. Try a full-equality assertion and note two problems: it also checks items the case does not care about, and it will fail if the unspecified order changes.
3. Try a bare boolean contains-check and note the new problem: a failure message says only that something expected to be true was false, explaining nothing.
4. Rewrite with a contains-at-least matcher that asserts the required items are present regardless of order.
5. Force a failure by removing one required item and confirm the message names the missing entry.

## Success Check
- The assertion checks only the behavior under test, not incidental content or order.
- A change to unguaranteed order does not fail the test.
- A failure message identifies what actually differs (the missing entry).

## Common Failures
- Keeping a full-equality assertion out of habit, so the test breaks on order or unrelated changes.
- Settling for a boolean assertion whose failure output explains nothing.

## Notes
This drills Long's class-names example through its three assertions — over-constrained equality, opaque boolean, and a fitting contains-at-least matcher. The lesson is that the matcher determines both whether the test fails for the right reason and whether its failure teaches the next engineer what broke.
