---
object_id: PAT_diagnose_source_of_code_confusion
object_type: pattern
name: Diagnose the Source of Code Confusion Before Acting
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_comprehension
- cognitive_load
- debugging
- learning
cross_links:
- rel: related_to
  target_object_id: PAT_externalize_intermediate_state_when_tracing
- rel: related_to
  target_object_id: DRILL_audit_cognitive_processes_while_reading_code
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u01, pp. 4-7
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Diagnose the Source of Code Confusion Before Acting

## Pattern Rule
**IF** a piece of code is confusing and the next useful move is unclear
**THEN** decide whether the obstacle is missing knowledge, missing information, or exhausted processing capacity, then use the response that matches that cause.

## Do
- Treat an unknown operator, language rule, algorithm, or domain term as a knowledge gap; learn that concept instead of repeatedly rereading the same tokens.
- Treat a call whose behavior is hidden elsewhere as an information gap; navigate to the definition or documentation while preserving what the caller was doing.
- Treat an execution that has too many changing values or steps to follow as a processing-capacity gap; move the intermediate state out of your head.

## Don't
- Don't assume every failure to understand code means you need more general programming knowledge; the needed fact may exist elsewhere in the codebase, or the facts may already be available but too numerous to process mentally.
- Don't keep applying one remedy after its diagnosis no longer fits, such as searching for documentation when the real difficulty is tracing a known algorithm through many state changes.

## Checklist
- Can I name the specific unknown concept, missing definition, or overloaded state that blocks understanding?
- Does my next action add knowledge, retrieve information, or reduce the amount held in working memory?
- After taking that action, can I explain the previously confusing line or step?

## Notes
Hermans holds the task constant by showing three programs that all convert a number to binary. The APL example is opaque because an operator is unknown; the Java example is readable at the call site but hides the method's implementation; the BASIC example exposes its operations yet is difficult to execute mentally. Because the behavior is comparable, the examples isolate three different causes that otherwise feel like one vague state of confusion. The distinction is a reader-side diagnostic and therefore does not duplicate the existing author-side readability foundations.
