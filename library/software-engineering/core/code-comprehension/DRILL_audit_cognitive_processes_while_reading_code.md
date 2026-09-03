---
object_id: DRILL_audit_cognitive_processes_while_reading_code
object_type: drill
name: Audit Cognitive Processes While Reading Code
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_comprehension
- cognitive_load
- deliberate_practice
- tracing
cross_links:
- rel: teaches
  target_object_id: PAT_diagnose_source_of_code_confusion
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
target_skill: distinguishing retrieved knowledge, temporary information, and active processing during code comprehension
references: []
variants: []
---

# Audit Cognitive Processes While Reading Code

## Practice Task
Read three short programs that perform different operations, explain each one, and record which parts depended on remembered knowledge, temporary information, or active mental execution.

## Target Skill
Recognizing the cognitive source of difficulty while reading unfamiliar code instead of labeling the whole program confusing.

## Setup
Choose three short snippets in languages or notations with different familiarity levels. Do not choose three implementations of the same operation, because the first solution would supply knowledge for the later ones.

## Instructions
1. Read the first snippet and write a one-sentence behavior explanation without executing it, quoting the code that supports it.
2. List the syntax, algorithms, domain facts, and prior examples you retrieved from long-term memory.
3. List the names, types, and local facts you had to hold temporarily, plus any text you ignored as irrelevant.
4. Mark the expressions or state changes you mentally executed and note where processing became effortful.
5. Check the three lists against each other and place each item in exactly one of them.
6. Repeat for the other two snippets, then classify each difficulty as missing knowledge, missing information, or processing overload, justifying each classification by what would remove it.
7. For one difficulty in each class, name the next action that would remove it.

## Success Check
- Each snippet's behaviour explanation is written before the audit and quotes the code supporting it. An explanation produced after the analysis has been contaminated by it.
- The three lists are kept disjoint, each item appearing in exactly one — retrieved from memory, held temporarily, or executed mentally. An item in two places means the distinction was not made, and that distinction is the drill.
- The text ignored as irrelevant is written down. What was skipped is the part of reading nobody records, and it is where a wrong explanation usually begins.
- Each difficulty is classified as missing knowledge, missing information, or overload, and the classification is justified by what would remove it rather than by how it felt.
- The next action named for each class differs by class. If all three resolve to reading it again, the classification changed nothing and was not applied.

## Common Failures
- Choosing snippets that all share one algorithm, which lets knowledge from the first hide the differences in later readings.
- Recording language names instead of the exact retrieved facts, such as the meaning of an operator or the shape of a loop.
- Calling every difficult expression a knowledge gap without checking whether all needed facts were already visible.

## Notes
Exercise 1.1 uses APL, Java, and BASIC programs that perform different operations, then asks what the reader retrieved, stored, ignored, and processed. Varying both notation and operation prevents one solved example from carrying the rest of the exercise and makes the three forms of confusion easier to distinguish.
