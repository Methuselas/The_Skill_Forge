---
object_id: PAT_calibrate_code_reading_scope_to_reader_knowledge
object_type: pattern
name: Calibrate Code-Reading Scope to Reader Knowledge
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 0 design
lane_fit: teach
foundation_role: foundation
routing_class: teaching
specialization_axis: none
foundation_object_id: none
tags:
- onboarding
- teaching
- code_comprehension
- cognitive_load
cross_links:
- rel: related_to
  target_object_id: DRILL_reproduce_code_to_diagnose_knowledge
- rel: related_to
  target_object_id: PAT_space_practice_across_widening_intervals
- rel: related_to
  target_object_id: AP_prepare_an_onboarding_for_all_three_memory_systems
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants:
- variant_id: VAR_hermans_close_the_knowledge_gap_instead_of_only_sizing_around_it
  variant_name: Close the Knowledge Gap Instead of Only Sizing Around It
  variant_basis: method_sequence
  difference_from_foundation: The foundation answers missing long-term knowledge by shrinking the reading slice and supplying concepts at the point of need, which accommodates the gap each time it appears. This variant treats the same gap as something to remove — the reader deliberately acquires the missing syntax and concepts through attempted recall, spaced revisiting, and elaboration, so that later reading needs less accommodation.
  when_to_use: Use when the same person will keep returning to this language, framework, or domain, when the same concepts are looked up repeatedly, or when onboarding is expected to reach unaided fluency rather than a single guided pass.
  when_not_to_use: Do not use it to justify withholding scope control now. Acquisition takes weeks, so a reader facing the code today still needs the smaller slice today; the two run together rather than one replacing the other. It is also the wrong route for genuinely fringe syntax that is not worth holding.
  absorbed_from_object_id: none
---

# Calibrate Code-Reading Scope to Reader Knowledge

## Pattern Rule
**IF** someone is reading a codebase, language, or domain whose key concepts are not yet in their long-term memory
**THEN** reduce the amount of code they must process at once and supply the missing concepts before expecting expert-sized comprehension.

## Do
- Choose a small coherent function or path whose behavior can be explained without chasing many dependencies.
- Identify unfamiliar keywords, structures, algorithms, and domain terms before increasing the size of the reading task.
- Compare progress on meaningful code, where learned concepts can form chunks, rather than on scrambled or arbitrary lines.

## Don't
- Don't assume strong performance in another language or domain gives immediate access to this codebase's chunks; unfamiliar local knowledge returns an expert to low-level reading.
- Don't interpret fewer recalled lines as lower general ability when the reader has had less opportunity to organize the relevant concepts.

## Checklist
- What language, algorithm, and domain knowledge does this reading slice assume?
- Can the reader explain each assumed concept before tackling the whole slice?
- Is the next increment in scope small enough to reuse concepts already learned?

## Notes
McKeithen's experiments found that experts recalled more meaningful ALGOL code than intermediates, who recalled more than beginners, but the groups performed similarly on scrambled programs. Hermans draws the onboarding lesson directly: a newcomer can process less code because fewer local chunks are available, even when that person is capable elsewhere. The teaching response is to adjust scope and prerequisites, not lower the learner's ceiling.

`VAR_hermans_close_the_knowledge_gap_instead_of_only_sizing_around_it` retains **Close the Knowledge Gap Instead of Only Sizing Around It** as a bounded alternative. Sizing the slice accommodates the missing knowledge every time it comes up; the variant instead removes it, using attempted recall, spaced revisiting, and elaboration so that later reading demands less accommodation. Reach for it when the same reader keeps returning to this codebase or keeps looking up the same concepts, and when onboarding is meant to end in unaided fluency. It does not license dropping scope control today — acquisition takes weeks, so the smaller slice is still what makes this week's reading possible, and the two run in parallel.
