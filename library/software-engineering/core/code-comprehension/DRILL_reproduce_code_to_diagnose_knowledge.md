---
object_id: DRILL_reproduce_code_to_diagnose_knowledge
object_type: drill
name: Reproduce Code to Diagnose Knowledge Gaps
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
- chunking
- deliberate_practice
- self_assessment
cross_links:
- rel: teaches
  target_object_id: PAT_read_code_as_semantic_chunks
- rel: related_to
  target_object_id: PAT_calibrate_code_reading_scope_to_reader_knowledge
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u02, pp. 15-17, 25, 30-31
  evidence_type: mixed
confidence: high
target_skill: using timed code reproduction to identify missing programming and domain concepts
references: []
variants: []
---

# Reproduce Code to Diagnose Knowledge Gaps

## Practice Task
Study a coherent code sample briefly, reproduce it from memory, and use what was retained, partially retained, or lost to identify which concepts need practice.

## Target Skill
Diagnosing the programming constructs, algorithms, and domain concepts available as chunks during code reading.

## Setup
Choose a coherent method or function of roughly half a page and no more than 50 lines. Use a language you know and a codebase you know somewhat but not intimately.

## Instructions
1. Set a two-minute timer and study the sample without copying it.
2. Hide or close the original when time expires.
3. Recreate as much code as possible in a blank file or on paper without peeking, numbering each block in the order you wrote it.
4. Compare the reproduction with the original and mark exact, partial, missing, and invented regions.
5. For each difference, state whether the missing support was syntax, a programming construct, an algorithm, a domain concept, or a local literal/name.
6. Read the write order as its own signal: lines that arrived together as a unit mark a concept you already hold, while lines rebuilt one at a time from the top of the file mark one you do not.
7. Choose one recurring conceptual gap to study, then repeat the drill later with a different sample that uses it.

## Success Check
- The comparison distinguishes conceptual structure from literal details.
- Every missed region has a specific proposed knowledge gap or an explicit statement that the cause is still unknown.
- A later repetition shows improved reconstruction of the practiced concept, not merely memorization of the first sample.
- The write order has been examined, not just the finished text.

## Common Failures
- Selecting code known so intimately that recall measures prior memorization instead of reading.
- Treating every changed literal or identifier as a conceptual failure.
- Repeating the identical sample until it is memorized rather than testing transfer to another use of the concept.

## Notes
Hermans first uses insertion sort, then a less recognizable Java routine, to expose how syntax and algorithm knowledge fill gaps in literal recall. Exercise 2.6 turns that observation into a repeatable self-diagnosis: what is easy to reproduce often corresponds to concepts already available as chunks, while missing regions point toward language, programming, or domain knowledge to strengthen. Grouping order carries the same evidence: when programmers were asked to list memorized ALGOL keywords, beginners chained them into sentences while experts emitted them in semantic groups such as TRUE with FALSE and IF with THEN and ELSE. The sequence in which code comes back therefore exposes chunk boundaries that the finished reproduction hides.
