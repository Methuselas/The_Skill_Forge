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
2. Read it once and try to answer three questions: what is this about, what do you end up with, and what inputs and quantities are needed. Note exactly where you had to struggle or re-read.
3. Write down each specific defect: missing title, wall-of-text instead of ordered steps, vague labels, and information placed far from where it is used.
4. Rewrite it: add a title, break it into ordered steps, replace each vague label with a role-describing name, and move every quantity and precondition next to where it is used.
5. Re-read your version and confirm the three questions are now answerable on a skim.

## Success Check
- A skim-reader can state the subject, the result, and the required inputs without decoding.
- Every vague label has been replaced by a name describing the thing's role.
- Each precondition and quantity sits where it is needed, not stranded elsewhere.

## Common Failures
- Renaming the labels but leaving the wall-of-text structure, so the steps still are not separable.
- Adding a title but leaving a critical precondition buried at the end where it is found too late.

## Notes
The book runs this exact exercise on the reader: a chocolate-brownie recipe deliberately mangled into one dense block with "A/B/C" labels and a late preheat instruction, followed by the three comprehension questions. The drill turns that demonstration into repeatable practice; do it on real code by taking a dense function and applying the same four fixes.
