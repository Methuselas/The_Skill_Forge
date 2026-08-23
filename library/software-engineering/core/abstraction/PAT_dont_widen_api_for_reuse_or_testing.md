---
object_id: PAT_dont_widen_api_for_reuse_or_testing
object_type: pattern
name: Don't Widen the Public API Just to Reuse or Test Internals
library_path:
- software-engineering
- core
- abstraction
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- api_design
- encapsulation
- testability
- reuse
cross_links:
- rel: related_to
  target_object_id: PAT_dont_expose_privates_for_testing
- rel: related_to
  target_object_id: PAT_expose_clean_api_hide_implementation
- rel: related_to
  target_object_id: PAT_use_interfaces_for_swappable_layers
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Don't Widen the Public API Just to Reuse or Test Internals

## Pattern Rule
**IF** you are tempted to make a private helper public so another caller can reuse it, or to expose an internal function only so a test can reach it
**THEN** resist, and instead extract that subproblem into its own class or layer so it can be reused and tested through a clean public surface of its own.

## Do
- Recognize the pull: a caller wants to count paragraphs and it would be handy to just make `splitIntoParagraphs()` public on `TextSummarizer`.
- Extract the subproblem into its own unit (a `ParagraphFinder` class) so reuse and testing happen against an interface that was designed to be public.
- Treat a "// only publicly visible for testing" comment as a smell pointing at the same underlying design problem, not a fix.

## Don't
- Don't pollute a class's public API with a seemingly unrelated function; external code will start depending on it and freeze your ability to change it.
- Don't reach for making internals public as the first move when the real signal is that a subproblem deserves its own layer.

## Checklist
- Is the function you want to expose actually part of this class's concept, or a separable subproblem?
- Would extracting it into its own class give reuse and tests a clean surface instead?
- Are you adding a "visible for testing" exception rather than fixing the structure?

## Notes
This sharpens the API-cleanliness rule at the exact moment engineers break it. Long shows both temptations from the `TextSummarizer` example — exposing `splitIntoParagraphs()` for reuse and exposing `calculateImportance()` for testing — and notes each pollutes the public API, couples outside code to internals, and raises cognitive load. The correct response is the class-splitting the chapter already argues for: give each subproblem its own layer, and reuse and testability follow from clean surfaces rather than leaks.
