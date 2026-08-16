---
object_id: PAT_use_beacons_to_test_code_hypotheses
object_type: pattern
name: Use Beacons to Form and Test Code Hypotheses
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
- beacons
- hypothesis_testing
- reading
cross_links:
- rel: related_to
  target_object_id: PAT_read_code_as_semantic_chunks
- rel: related_to
  target_object_id: DRILL_inventory_beacons_in_unfamiliar_code
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Use Beacons to Form and Test Code Hypotheses

## Pattern Rule
**IF** you are reading an unfamiliar function and have only a tentative idea of its data structure or behavior
**THEN** collect simple and compound beacons, state the hypothesis each one suggests, and keep or discard that hypothesis as later beacons agree or conflict.

## Do
- Use a meaningful name, operator, literal, or control keyword as a simple signal, but treat it as evidence rather than a conclusion.
- Combine cooperating elements into stronger signals: paired left/right fields suggest a tree, and a loop's initializer, boundary, and increment together reveal its traversal shape.
- Record the exact element that produced each "aha" moment so the emerging explanation remains auditable.

## Don't
- Don't anchor on the first suggestive word and reinterpret every later line to fit it; a beacon is valuable because it can also refute a hypothesis.
- Don't overlook natural-language evidence such as a high-level comment or output string when it carries domain information the syntax does not.

## Checklist
- What is my current behavior or data-structure hypothesis?
- Which exact simple or compound signals support it, and which contradict it?
- Can I explain the whole function after resolving the conflicting evidence?

## Notes
In the binary-tree example, a comment and the class name first suggest trees; the root name and paired left/right fields narrow that idea to a binary tree. Hermans distinguishes small syntactic signals from larger combinations that carry semantic meaning. This is a reader-side decision distinct from the absorbed writer-side beacon variant in the readability foundation.
