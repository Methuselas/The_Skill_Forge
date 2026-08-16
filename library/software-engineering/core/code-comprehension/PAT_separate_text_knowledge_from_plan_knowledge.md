---
object_id: PAT_separate_text_knowledge_from_plan_knowledge
object_type: pattern
name: Separate Text Knowledge From Plan Knowledge
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_comprehension
- diagnosis
- intent
cross_links:
- rel: related_to
  target_object_id: PAT_diagnose_source_of_code_confusion
- rel: related_to
  target_object_id: PAT_classify_variables_by_role
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Separate Text Knowledge From Plan Knowledge

## Pattern Rule
**IF** you can follow every line of a program but still cannot say what it is for
**THEN** name the gap as missing plan knowledge rather than missing understanding, and go after the creator's intent instead of re-reading the lines

## Do
- Check which kind of knowledge you actually have. Knowing what a keyword does or what role a variable plays is surface knowledge of the text; knowing what the author was trying to achieve, and why they built it this way, is knowledge of the plan.
- Treat the frustrating case as diagnostic. The specific feeling of "this doesn't look complicated, so why don't I understand it" is the signature of holding text knowledge without plan knowledge.
- Go looking for the intent in structure and connection rather than in individual statements — how parts relate, what is called from where, what the shape of the whole implies.
- Suspect the framework when focal points are scattered. Dependency injection and similar mechanisms link code at a distance, so the running structure can be genuinely invisible even when every file is readable; understanding how the framework wires things together is then the prerequisite.

## Don't
- Don't respond to the gap by reading the lines again more slowly. Re-reading builds more of the knowledge you already have.
- Don't take fluent line-by-line reading as evidence of comprehension when you would be unable to say where a new feature belongs.
- Don't stop at the roles of the variables. Those are still text knowledge — a better grade of it, but not intent.

## Checklist
- Could you say what this code is *for* to someone who has not read it?
- Could you say where a related new feature would go, and why there?
- Can you name a decision the author made and a plausible alternative they rejected?

## Notes
Nancy Pennington's model separates the two levels: text structure knowledge covers the surface of the program, plan knowledge covers what its creator was aiming at. The distinction is useful mainly because the two failure modes feel identical from the inside and have completely different remedies.

Jonathan Sillito's observation of 25 programmers reading code gives the route from one to the other, and it starts somewhere specific rather than at the top: find a focal point, expand outward from it, assemble a concept from the entities that turn out to be related, then span concepts across entities. The focal point is often `main()` or an `onLoad()`, but just as often it is the line where an error surfaced or the line a profiler flagged — the question "where do I start reading" has a real answer, and it is not always line one.
