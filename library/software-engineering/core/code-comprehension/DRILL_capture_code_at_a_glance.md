---
object_id: DRILL_capture_code_at_a_glance
object_type: drill
name: Capture Code Structure at a Glance
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
- structural_reading
- deliberate_practice
- iconic_memory
cross_links:
- rel: supports
  target_object_id: PAT_read_code_as_semantic_chunks
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
target_skill: forming an accurate first structural image of code before detailed reading
references: []
variants: []
---

# Capture Code Structure at a Glance

## Practice Task
View a half-page of somewhat familiar code for a few seconds, hide it, and reconstruct only its visible structure before reading any details.

## Target Skill
Using a brief first look to notice nesting, whitespace, standout lines, gaps, and dense blocks without pretending to understand the full behavior.

## Setup
Choose about half a printed page of code in a familiar language. A paper copy or a view that can be hidden instantly works best.

## Instructions
1. Look at the code for only a few seconds; do not trace expressions or follow calls.
2. Hide the code completely.
3. Sketch the nesting shape and the relative size of its major blocks.
4. Note whether whitespace separates sections, whether any line stood out, and whether the page contained gaps or dense blobs.
5. Reveal the code and mark observations that were accurate, missing, or invented.
6. Repeat with a second snippet, keeping the glance equally brief.

## Success Check
- The sketch captures the major nesting and block boundaries without adding behavior not observed.
- At least one whitespace or density observation is checked against the original.
- Accuracy improves on the second snippet without increasing viewing time.

## Common Failures
- Reading one expression in detail and missing the page-wide structure.
- Claiming a function's purpose from its shape alone instead of limiting the result to an initial image.
- Leaving the code visible while answering, which turns the drill into ordinary inspection.

## Notes
The exercise follows the chapter's iconic-memory discussion: more of a visual scene is briefly available than short-term memory can process. The goal is not photographic recall. It is deliberate selection of structural information before detailed reading consumes attention.
