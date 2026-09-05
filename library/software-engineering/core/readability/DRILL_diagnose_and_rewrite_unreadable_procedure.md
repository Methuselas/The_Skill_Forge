---
object_id: DRILL_diagnose_and_rewrite_unreadable_procedure
object_type: drill
name: Diagnose and Rewrite an Unreadable Procedure
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- readability
- naming
- refactoring
- comprehension
cross_links:
- rel: teaches
  target_object_id: PAT_make_code_readable
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: recognizing and fixing the concrete failure modes that make a procedure unreadable
references: []
variants: []
---

# Diagnose and Rewrite an Unreadable Procedure

## Practice Task
Take a deliberately unreadable procedure — one wall of text with vague labels and no title — rewrite it into a readable form, then name each specific defect you fixed.

## Target Skill
Spotting the specific readability failures that make code hard to follow, and correcting each one.

## Setup
No special setup required.

## Instructions
1. Take a procedure written as a single unstructured paragraph with vague labels — for example, a recipe that calls its bowls "A," "B," and "C," gives no title, and mentions a precondition like "preheat the oven" only at the very end.
2. Read it once and try to answer three questions: what is this about, what do you end up with, and what inputs and quantities are needed. Record each struggle or re-reading as it happens rather than afterwards.
3. Write down each specific defect and where it sits: missing title, wall-of-text instead of ordered steps, vague labels, and information placed far from where it is used.
4. Rewrite it: add a title, break it into ordered steps, replace each vague label with a role-describing name, and move every quantity and precondition next to where it is used.
5. Walk the rewritten steps in order and confirm nothing is required before it appears.
6. Skim your version rather than reading it, and write down what the skim produced for each of the three questions.
7. Check the rewrite for the opposite failure: steps split so finely the shape is lost, or names so long the sequence is harder to scan than the paragraph was.

## Success Check
- The three questions are attempted against the original and the struggles recorded as they happen. Noted afterwards they become a tidy list of defects rather than a record of reading.
- Each defect is named specifically and located, so the rewrite can be checked against it rather than against a general impression of improvement.
- The rewrite is tested by a skim rather than a read, and what that skim produced for each of the three questions is written down.
- Every quantity and precondition sits at its point of use, verified by walking the rewritten steps in order and confirming nothing is required before it appears.
- The rewrite is checked for the opposite failure: steps split so finely the shape is lost, or names so long the sequence is harder to scan than the paragraph was.

## Common Failures
- Renaming the labels but leaving the wall-of-text structure, so the steps still are not separable.
- Adding a title but leaving a critical precondition buried at the end where it is found too late.

## Notes
The original exercise is run on the reader: a chocolate-brownie recipe deliberately mangled into one dense block with "A/B/C" labels and a late preheat instruction, followed by the three comprehension questions. The drill turns that demonstration into repeatable practice; do it on real code by taking a dense function and applying the same four fixes.
