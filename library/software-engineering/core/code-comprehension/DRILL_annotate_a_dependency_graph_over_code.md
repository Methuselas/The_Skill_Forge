---
object_id: DRILL_annotate_a_dependency_graph_over_code
object_type: drill
name: Annotate a Dependency Graph Over Printed Code
target_skill: Reading highly interconnected code without holding its structure in working memory
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
- cognitive_load
- code_comprehension
- tracing
cross_links:
- rel: teaches
  target_object_id: PAT_separate_intrinsic_from_extraneous_load
- rel: related_to
  target_object_id: DRILL_trace_a_state_table_for_calculation_heavy_code
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants:
- variant_id: VAR_hermans_expand_a_slice_from_one_focal_point
  variant_name: Expand a Slice From One Focal Point
  variant_basis: method_sequence
  difference_from_foundation: The foundation annotates every variable, call and class instance on the page, producing a complete map with no starting point. This variant runs the same annotation from a chosen focal point outward, marking only entities that transitively relate to it — the slice of that line — so the result is a partial map organised around one question rather than a total map of the file. Hermans states the relationship directly, calling the six-step procedure an instantiation of Sillito's four-stage model with the entry point left out.
  when_to_use: Use when you have a specific reason to be in the code — a runtime error at a known line, a profiler-flagged hotspot, a feature to place — and when the file is too large to annotate exhaustively. The slice also answers questions the full map cannot, such as which method is called from many places within it and therefore warrants study.
  when_not_to_use: Do not use it when you need the shape of the whole file, when no focal point stands out, or when the framework scatters entry points far enough apart that picking one would mislead you about the structure.
  absorbed_from_object_id: none
---

# Annotate a Dependency Graph Over Printed Code

## Practice Task
Take a piece of code whose structure keeps defeating you and mark its dependencies directly on the page in colour, until the drawing tells you where to read next.

## Target Skill
Reading highly interconnected code without holding its structure in working memory.

## Setup
The code printed on paper, or as a PDF on a tablet you can annotate. Three pen colours. This does not work well in an editor — the point is annotation the code itself cannot carry.

## Instructions
1. Circle every variable.
2. Draw a line between occurrences of the same variable. Where it helps, link related accesses too, such as `customers[0]` and `customers[i]`.
3. Circle every method and function call in a second colour.
4. Draw a line from each definition to each place it is invoked.
5. Circle every instance of a class in a third colour.
6. Link class instances to their definition, or to each other when the definition is not on the page.
7. Record anything you deliberately skipped while circling and linking.
8. Before working out what the code computes, name the data flow from the shape of the lines alone and write it down.
9. Read the code from an entry point such as `main()`, following your own drawn lines only, and note every moment you searched the file instead of following a line.
10. Name at least one method invoked exactly once, and say whether inlining it is right here.
11. Identify the densest region of lines and compare it against where reading was actually hardest.

## Success Check
- Variables, calls, and class instances are each circled in their own distinguishable colour before any line is drawn, and anything deliberately skipped is recorded. A gap left silently reads afterwards as an absence of dependency.
- The entry-point read is performed by following drawn lines only, and every moment of searching the file instead is noted. Searching means a dependency was never drawn, and those omissions are the finding rather than untidiness.
- The data flow is named from the shape of the lines and written down before the computation is understood. Written afterwards it is a summary of what was read, and the claim being tested is that the picture arrives first.
- At least one single-invocation method is named, and the run says whether inlining it is right here. A method called once for the sake of a name is not a candidate, so the count alone does not decide it.
- The densest region of lines is identified and compared against where reading was actually hardest, so the annotation is checked against experience rather than treated as self-evidently correct.

## Common Failures
- Circling only the variables that look important. The value comes from completeness — a variable you skipped is the one you will hunt for later.
- Doing it in the editor with folding and jump-to-definition. Those operate at the cost of the working memory you are trying to protect.
- Treating the drawing as the goal. It is a reference you consult while reading, not an artifact to finish and admire.
- Reaching for it when the problem is arithmetic rather than structure — that is the state table's job.

## Notes
Two annotated views of the same Python program show the technique in stages: first every variable ringed in green, then the same page with lines arcing between occurrences of `digits`, `num`, `result`, `b`, `revb`, `trial`. The second image is visibly a graph laid over source text, and its usefulness is obvious in a way the instruction list alone does not convey.

Two distinct overloads motivate this. You may not know which parts of the code you need to read, so you read too much; or the code is connected enough that you are parsing individual lines and working out where to go next at the same time. The annotation removes the second job. Hermans's diagnostic is having read the same code five times without progress — a sign you understood each line but never the shape.

`VAR_hermans_expand_a_slice_from_one_focal_point` retains **Expand a Slice From One Focal Point** as a bounded alternative. Rather than annotating everything on the page, it runs the same marking outward from a chosen starting line — an error site, a profiler hotspot, `main()` — and stops at the entities transitively related to it, which is that line's slice. Reach for it when you are in the code for a specific reason or the file is too big to map exhaustively; stay with the foundation when you need the shape of the whole. Hermans notes the two are the same model at different settings: the six steps here are Sillito's four-stage process with the entry point omitted.
