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
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
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
3. Fix the rule for what one row represents before filling anything, and apply that rule throughout. A row is usually one loop iteration, with an initialisation row before it; it can also be a branch of a large conditional, a coherent group of lines, or — in genuinely terse code — a single line.
4. Work through the code and write the value of *every* variable in each row, including the ones that did not change. Mark any value that comes out surprising.
5. Check the finished table for gaps before using it.
6. Read off the table which variables drive the computation and which are carried along unchanged.
7. On a second read of the program, use the completed table as a reference and write down what the code is for, rather than a restatement of the arithmetic the table already holds.

## Success Check
- Every cell is filled, unchanged values included, and the table is checked for gaps before it is used. A table with holes cannot serve as the reference it was built to be.
- The rule for what a row represents is fixed in advance and applied throughout, because a table whose rows mean different things in different places cannot be read across.
- Variables driving the computation are separated from those carried along unchanged, and that separation is read off the table rather than recalled from the code.
- The second read produces a statement of purpose rather than a restatement of the arithmetic the table already holds. If the output is more numbers, the table was not used as a reference.
- Any value that came out surprising is marked. Nothing surprising means either the code was already understood, or the table was filled from what the code intends rather than by executing it.

## Common Failures
- Filling in only the variables that look interesting. Hermans names this as the temptation to resist: the meticulous pass is where the understanding comes from.
- Choosing rows that do not line up with the code's real dependencies, so values appear to jump without cause.
- Using it on code that is confusing structurally rather than numerically — that is the dependency graph's job.
- Stopping once the table is built. The payoff is the second read it enables.

## Notes
A worked example shows the shape on a nine-line BASIC program that converts a number to binary: columns `N`, `N2`, `B$`, `N1`, rows `Init`, `Loop 1`, `Loop 2`. The `Init` row holds 7, 7, —, 7 and `Loop 1` holds 3, 1, 3, and `Loop 2` is deliberately left empty — it is a *partial* table, filled as you trace rather than produced complete. Two things become visible immediately that the code does not show: `N` never changes while everything around it does, and `B$` is accumulating a string rather than a number.

Mentally executing code this way is called tracing, or cognitive compiling. Tools can generate the same picture automatically — Philip Guo's Python Tutor steps through execution and renders the frames, making visible, for instance, that an integer is stored by value while a list is held through a pointer. Hermans's point in favour of doing it by hand anyway is that the manual pass forces the detailed examination that produces the understanding; the tool shows you a result you did not compute.
