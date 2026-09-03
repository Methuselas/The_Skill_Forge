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
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
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

The reproduction is evidence only if the sample is genuinely unreadable while it is being written. Closing the file achieves that for a reader whose access to the text ends when the file closes, and achieves nothing for one that keeps whatever it has been shown — anybody working from a transcript, a shared buffer, or a context that does not forget. Where closing is not enough, either have a second person or process supply the sample and withdraw it before reproduction begins, or take the concept route in step 4. A reproduction written while the text was still readable is a copy, and every marking made against it describes the copying rather than the reading.

## Instructions
1. Set a two-minute timer and study the sample without copying it.
2. Make the sample unreadable for the whole of the reproduction. Covering or closing it counts only where that actually ends access; where it does not, the sample has to be withdrawn by something other than whoever is reproducing it.
3. Recreate as much code as possible in a blank file or on paper without peeking, numbering each block in the order you wrote it.
4. Where step 2 cannot be satisfied, take the concept route instead of reproducing. Write a different routine that solves the same problem using the same construct, working from the concept rather than from the text, and number the blocks in the order you wrote them. This gives up the literal comparison and keeps everything from step 6 onward, because what it tests is whether the construct is available as a chunk rather than whether the lines are remembered.
5. State which route you took and what made the sample unavailable, then compare against the original. For a reproduction, mark exact, partial, missing, and invented regions. For the concept route, mark which of the sample's constructs your routine reached for and which it replaced with something else — the replacement is the finding, and reaching for a lock where the sample used a compare-and-swap retry says more than any missing line would.
6. For each difference, state whether the missing support was syntax, a programming construct, an algorithm, a domain concept, or a local literal/name — or state explicitly that the cause is still unknown.
7. Read the write order as its own signal: lines that arrived together as a unit mark a concept you already hold, while lines rebuilt one at a time from the top of the file mark one you do not.
8. Choose one recurring conceptual gap to study, then repeat the drill later with a different sample that uses it.

## Success Check
- The run states which route it took and what made the sample unavailable. A comparison produced while the original was still readable describes a copy, and its exact and partial markings carry no information about reading.
- The comparison distinguishes conceptual structure from literal details.
- Every missed region has a specific proposed knowledge gap or an explicit statement that the cause is still unknown.
- A later repetition shows improved reconstruction of the practiced concept, not merely memorization of the first sample. This is the one condition a single sitting cannot close, so a run that reports it satisfied on the day has repeated the sample rather than transferred to another use of the concept.
- The write order has been examined, not just the finished text.

## Common Failures
- Marking a reproduction as exact when the original was readable throughout. The result is a record of transcription, and it is the most confident-looking output this drill can produce.
- Selecting code known so intimately that recall measures prior memorization instead of reading.
- Treating every changed literal or identifier as a conceptual failure.
- Repeating the identical sample until it is memorized rather than testing transfer to another use of the concept.

## Notes
Hermans first uses insertion sort, then a less recognizable Java routine, to expose how syntax and algorithm knowledge fill gaps in literal recall. Exercise 2.6 turns that observation into a repeatable self-diagnosis: what is easy to reproduce often corresponds to concepts already available as chunks, while missing regions point toward language, programming, or domain knowledge to strengthen. Grouping order carries the same evidence: when programmers were asked to list memorized ALGOL keywords, beginners chained them into sentences while experts emitted them in semantic groups such as TRUE with FALSE and IF with THEN and ELSE. The sequence in which code comes back therefore exposes chunk boundaries that the finished reproduction hides.

The concept route exists because the diagnosis does not actually depend on recalling those particular lines. What the drill is after is which constructs were available as units while reading, and a routine written from the concept alone exposes that from the other direction: the construct you reach for instead is the chunk you hold, and the one you had to assemble is the one you do not. It costs the literal comparison, which is the weaker half of the evidence anyway, since a changed identifier was never a conceptual failure.
