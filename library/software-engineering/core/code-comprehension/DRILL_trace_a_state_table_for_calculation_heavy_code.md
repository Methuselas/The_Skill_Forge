---
object_id: DRILL_trace_a_state_table_for_calculation_heavy_code
object_type: drill
name: Build a State Table for Calculation-Heavy Code
target_skill: Tracing code whose variables depend on each other too tightly to follow by reading
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
- tracing
- code_comprehension
cross_links:
- rel: teaches
  target_object_id: PAT_externalize_intermediate_state_when_tracing
- rel: related_to
  target_object_id: DRILL_annotate_a_dependency_graph_over_code
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u04, pp. 59-60
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Build a State Table for Calculation-Heavy Code

## Practice Task
For code whose difficulty is arithmetic rather than structure, build a table of variables against execution steps and fill it in completely by hand.

## Target Skill
Tracing code whose variables depend on each other too tightly to follow by reading.

## Setup
No special setup required. Paper or a scratch file. If you have already drawn a dependency graph over this code, the variables are the ones you circled first.

## Instructions
1. List every variable in the code.
2. Give each variable its own column.
3. Add one row per distinct part of the execution. A row is usually one loop iteration, with an initialisation row before it; it can also be a branch of a large conditional, a coherent group of lines, or — in genuinely terse code — a single line.
4. Work through the code and write the value of *every* variable in each row, including the ones that did not change.
5. On a second read of the program, use the completed table as a reference so you can attend to what the code means rather than to what the numbers are.

## Success Check
- Every cell is filled. A table with gaps cannot be trusted as a reference, which was the whole reason to build it.
- You can state which variables are actually driving the computation and which are carried along unchanged.
- The second read is about the program's purpose rather than its arithmetic.

## Common Failures
- Filling in only the variables that look interesting. Hermans names this as the temptation to resist: the meticulous pass is where the understanding comes from.
- Choosing rows that do not line up with the code's real dependencies, so values appear to jump without cause.
- Using it on code that is confusing structurally rather than numerically — that is the dependency graph's job.
- Stopping once the table is built. The payoff is the second read it enables.

## Notes
Figure 4.7 shows the shape on a nine-line BASIC program that converts a number to binary: columns `N`, `N2`, `B$`, `N1`, rows `Init`, `Loop 1`, `Loop 2`. The `Init` row holds 7, 7, —, 7 and `Loop 1` holds 3, 1, 3, and `Loop 2` is deliberately left empty — it is a *partial* table, filled as you trace rather than produced complete. Two things become visible immediately that the code does not show: `N` never changes while everything around it does, and `B$` is accumulating a string rather than a number.

Mentally executing code this way is called tracing, or cognitive compiling. Tools can generate the same picture automatically — Philip Guo's Python Tutor steps through execution and renders the frames, making visible, for instance, that an integer is stored by value while a list is held through a pointer. Hermans's point in favour of doing it by hand anyway is that the manual pass forces the detailed examination that produces the understanding; the tool shows you a result you did not compute.
