---
object_id: PAT_pick_and_choose_testing_philosophies
object_type: pattern
name: Pick and Choose From Testing Philosophies
library_path:
- software-engineering
- core
- testing
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- unit_testing
- tdd
- methodology
- judgment
cross_links:
- rel: related_to
  target_object_id: PAT_design_for_testability
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: medium
references: []
variants: []
---

# Pick and Choose From Testing Philosophies

## Pattern Rule
**IF** you are considering a testing methodology such as TDD, BDD, or acceptance-test-driven development
**THEN** adopt the practices from it that make you more effective rather than treating it as all-or-nothing, because the goal — good, thorough tests and high-quality software — matters more than adherence to any one method.

## Do
- Take the useful parts even if you skip the headline rule: many engineers who do not write tests strictly before code still adopt TDD's other practices — keeping tests isolated, focused, and free of implementation-detail testing.
- Judge a methodology by whether it helps you produce the outcome, since philosophies mostly document ways of working that some engineers found effective.

## Don't
- Don't treat a philosophy as a package you must accept whole or reject entirely; that framing is rarely how effective work actually happens.
- Don't confuse following a method to the letter with the goal; the tests and the software quality are the point, not the ritual.

## Checklist
- Which specific practices from this methodology would improve your tests?
- Are you adopting a practice because it helps, or because a philosophy prescribes it?
- Is the outcome — thorough tests, quality software — actually being served?

## Notes
Long lists TDD (test first, minimal code, refactor, repeat), BDD (capture desired behaviors, often from a user or business view), and ATDD (customer-facing acceptance tests written before the code) not as creeds but as menus. His example is TDD's write-tests-first rule, which many admire yet few practice, while still adopting its isolation and focus practices. The durable stance is pragmatic: methodologies encode what worked for someone, but the goal outranks the method.
