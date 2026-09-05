---
object_id: PAT_classify_variables_by_role
object_type: pattern
name: Classify Variables by the Role They Play
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
- variables
- beacons
cross_links:
- rel: related_to
  target_object_id: PAT_use_beacons_to_test_code_hypotheses
- rel: related_to
  target_object_id: PAT_separate_text_knowledge_from_plan_knowledge
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Classify Variables by the Role They Play

## Pattern Rule
**IF** you are reading unfamiliar code and the variables are not telling you what the program does
**THEN** name each one's role from a fixed mid-level vocabulary — what it does across the program's execution — rather than reasoning from its type or its name

## Do
- Work the roles as a decision sequence rather than a list to scan. Ask in order: is it constant after initialization; is it temporary storage; is it checking something; is it involved in repetition. Only the repetition branch subdivides further, into counting, delaying, accumulating, and picking.
- Use the eleven roles as the vocabulary: fixed value, stepper, flag, walker, most recent holder, most wanted holder, gatherer, container, follower, organizer, temporary.
- Distinguish the pairs that look alike. A stepper moves through a succession known before the loop starts; a walker traverses a structure whose path is not known in advance. A most recent holder keeps the latest value seen; a most wanted holder keeps the best one found so far.
- Read role *combinations* as program shapes. A stepper together with a most wanted holder is a search; recognising the pair tells you the program's purpose before you have read its body.
- Apply it beyond procedural code. In a Java class, a `name` field set once in the constructor is a fixed value and an `age` field incremented on each birthday is a stepper.

## Don't
- Don't settle for the two granularities that come naturally. "It's an integer" is too coarse to reason with and "it's `number_of_customers`" is too specific to generalise; the role sits deliberately between them.
- Don't infer the role from the name alone. `counter` tells you almost nothing on its own — whether it is fixed, stepping, or accumulating is a property of how the code uses it.
- Don't treat this as new material to learn. Most of these roles are already familiar under other names; the value is in having one shared vocabulary, particularly across a team.

## Checklist
- For each variable: what is its name, its type, the operations it participates in, and its role?
- Which decision in the sequence settled the role, and would a colleague reach the same answer?
- Do the roles present in this code combine into a recognisable kind of program?

## Notes
Jorma Sajaniemi's argument for the framework is cognitive rather than stylistic: programmers struggle with variables because they have no schema of the right size to attach them to. The eleven roles supply that missing middle layer, and studies of students using the framework showed them outperforming those who did not.

The classification flowchart is the part that does not survive being read as prose — the questions are ordered, and the ordering is what makes classification fast. Hermans's own practice is to print the code and mark each variable with a small icon per role, which becomes a strong memory aid once the icon set is learned. The same idea runs the other way when writing code: putting the role into the variable name saves every later reader the work of deducing it.
