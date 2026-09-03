---
object_id: DRILL_compare_a_new_language_against_a_known_one
object_type: drill
name: Map a New Language Against One You Already Know
target_skill: Predicting where prior language knowledge will help and where it will mislead, before it does either
library_path:
- software-engineering
- core
- deliberate-practice
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- transfer
- learning
- deliberate_practice
- onboarding
cross_links:
- rel: supports
  target_object_id: PAT_set_up_for_transfer_when_learning_a_new_language
- rel: supports
  target_object_id: PAT_expect_negative_transfer_between_similar_languages
- rel: related_to
  target_object_id: DRILL_elaborate_a_new_concept_against_known_ones
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Map a New Language Against One You Already Know

## Practice Task
Before starting a new language in earnest, fill in a six-row comparison against a language you already know, and mark each row as expected help or expected trap.

## Target Skill
Predicting where prior language knowledge will help and where it will mislead, before it does either.

## Setup
The new language's documentation or a primer, and a language you genuinely know well — mastery of the source is what makes the comparison worth anything. A table with three columns: similarities, differences, remarks.

## Instructions
1. Take the six rows Hermans uses: syntax, type system, programming concepts, runtime, programming environment or IDE, and testing environment or practices.
2. For each row, write what is similar and what is different, filling both columns including the rows where you had to go and look something up. Do the similarities column first — naming the commonalities is what makes prior knowledge reachable, and it is the step people skip.
3. Mark each entry as verified or assumed, so the two are distinguishable later.
4. In the remarks column, mark each row as expected help or expected trap. A row where the two languages are *almost* the same is a trap row, not a help row.
5. Classify anything you have already transferred, using the two axes from exercise 7.2: high-road versus low-road, and near versus far. Reusing an editor shortcut without thinking is low-road; assuming a variable must be declared because most languages require it is high-road.
6. Look specifically for constructs sharing a name across the two languages and behaving differently, and name at least one before you meet it in anger. Put those at the top of the trap list.
7. Keep the table while you learn and correct it as you are proved wrong; the corrections are your personal misconception list for this language pair.

## Success Check
- Every row is filled in both columns, including the rows where you had to go and look something up.
- You can name at least one construct that exists in both languages and differs, before meeting it in anger.
- The table distinguishes what you verified from what you assumed.

## Common Failures
- Filling only the differences column. The similarities are what produce transfer, and skipping them wastes the exercise's main benefit.
- Comparing against a language you know only moderately. Transfer scales with mastery of the source, so a weak source language gives a weak map.
- Treating the table as reference material rather than a prediction to be falsified — the value arrives when a row turns out wrong.
- Stopping at syntax. Runtime, tooling, and testing practice are where the expensive surprises live, which is why they are rows in their own right.

## Notes
This combines Hermans's exercises 7.2 and 7.4 into one pass. Exercise 7.4 supplies the six-row comparison table and the instruction to fill it out to show "where you can expect transfer and where you will need to pay specific attention while learning"; exercise 7.2 supplies the high-road/low-road and near/far classification. Both are empty grids in the book, so the structure is the content — the rows and axes are what the exercise contributes, and the entries are yours.

It is deliberately kept separate from the elaboration drill, which runs at the moment a single new concept is met and asks what it connects to. This one runs once, before the learning starts, over a whole language, and its output is a prediction about where transfer will fail. The elaboration drill builds retrievability; this one builds a trap map.

The far-transfer caveat applies to the choice of comparison language. If the new language is genuinely distant — the chapter's example is SQL against JavaScript — expect most rows to come out as differences, and expect to need new strategies rather than only new syntax.
