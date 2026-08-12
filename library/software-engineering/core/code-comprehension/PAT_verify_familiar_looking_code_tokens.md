---
object_id: PAT_verify_familiar_looking_code_tokens
object_type: pattern
name: Verify Familiar-Looking Code Instead of Autocorrecting It
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_review
- code_comprehension
- expectations
- defects
cross_links:
- rel: related_to
  target_object_id: PAT_follow_a_consistent_coding_style
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u01, p. 8
  evidence_type: text
confidence: high
references: []
variants: []
---

# Verify Familiar-Looking Code Instead of Autocorrecting It

## Pattern Rule
**IF** a line looks so conventional that you can predict it before inspecting every token
**THEN** compare the actual names, operators, and control conditions with the expected form before accepting the line as routine.

## Do
- Pause at convention-heavy lines such as entry points, loop headers, standard calls, and repeated boilerplate, where prior experience can fill in what normally appears.
- Read identifiers character by character when a small spelling change would alter whether the code is invoked or resolved.
- State the observed token and the expected token separately during review, so a familiar shape cannot silently collapse the distinction.

## Don't
- Don't count instant recognition as proof that the text matches the convention; recognition may have come from long-term memory rather than the characters in front of you.
- Don't weaken shared conventions to compensate for inattentive reading; conventions remain useful, but reviewers must verify the places where expectation is strongest.

## Checklist
- Did I inspect the exact identifier and operator rather than mentally substitute the usual one?
- Would a one-character change on this line affect entry, dispatch, comparison, or control flow?
- Can I quote the actual token that supports my review conclusion?

## Notes
Hermans presents a Java entry-point method spelled `mian`. Readers familiar with Java often report the method's purpose without noticing the transposition because long-term memory supplies the expected `main`. The trap complements the existing convention and mental-model foundations: conventions accelerate comprehension, but that speed creates a distinct review decision at high-familiarity lines.
