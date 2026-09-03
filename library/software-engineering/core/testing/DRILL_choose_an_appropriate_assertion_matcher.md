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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
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
2. Write and run a full-equality assertion, then demonstrate its two problems separately: once by adding content the case does not care about, and once by reordering the unguaranteed sequence and watching the test fail.
3. Write and run a bare boolean contains-check, and record its failure message verbatim.
4. Rewrite with a contains-at-least matcher that asserts the required items are present regardless of order, and run it.
5. Force a failure by removing one required item and record the message, confirming it names the missing entry.
6. State what the final assertion no longer checks, compared with full equality.

## Success Check
- All three assertion forms are written and run rather than one written and two described. The comparison is the drill, and it does not survive being imagined.
- Both problems with full equality are demonstrated separately: one by content the case does not care about, one by reordering the unguaranteed sequence and watching the test fail.
- The bare boolean's failure message is recorded verbatim. Its uselessness is the evidence, and paraphrasing it into "unhelpful" discards exactly what was being shown.
- The final matcher is failed deliberately and its message recorded, naming the missing entry. A matcher chosen because it sounds right, and never failed, has not been evaluated.
- The run states what the assertion no longer checks, so narrowing is visible as a deliberate loss of coverage rather than as an unqualified improvement.

## Common Failures
- Keeping a full-equality assertion out of habit, so the test breaks on order or unrelated changes.
- Settling for a boolean assertion whose failure output explains nothing.

## Notes
This drills Long's class-names example through its three assertions — over-constrained equality, opaque boolean, and a fitting contains-at-least matcher. The lesson is that the matcher determines both whether the test fails for the right reason and whether its failure teaches the next engineer what broke.
