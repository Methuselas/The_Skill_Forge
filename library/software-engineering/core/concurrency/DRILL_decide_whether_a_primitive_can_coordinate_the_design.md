---
object_id: DRILL_decide_whether_a_primitive_can_coordinate_the_design
object_type: drill
name: Decide Whether a Primitive Can Coordinate the Design
target_skill: Ruling a nonblocking design in or out from its primitives before building it
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- lock_free
- atomics
- design
cross_links:
- rel: related_to
  target_object_id: PAT_check_a_primitives_coordination_power_before_designing_on_it
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Decide Whether a Primitive Can Coordinate the Design

## Practice Task
Take three proposed nonblocking designs — a shared counter built on atomic addition, a work queue built on atomic exchange, and a set built on compare-and-set — and for each, decide before writing anything whether the primitive can coordinate the number of threads the design needs.

## Target Skill
Ruling a nonblocking design in or out from its primitives, before effort is spent.

## Setup
No special setup required.

## Instructions
1. For each design, state how many threads must agree on a single outcome. Distinguish that from how many threads merely touch the structure, which is a different and usually larger number.
2. Name the strongest primitive each design relies on, and place it: plain reads and writes, an unconditional read-modify-write, or a conditional update.
3. Rule each design in or out. Where the primitive is below the required thread count, say so and stop — the design is impossible rather than difficult.
4. For any design ruled out, write the two available responses: move to a stronger primitive, or accept a blocking implementation. Choose one and say why.
5. For any design ruled in, state the consequence explicitly — that no impossibility remains, so further failures are engineering problems and the design is worth persisting with.
6. Repeat the test on an object rather than an instruction: decide whether a concurrent queue could be built wait-free from plain registers, and give the reason without examining any attempt.

## Success Check
- Each design has a thread count and a primitive tier written down, and a verdict that follows from the two.
- At least one design is ruled out, with the ruling stated as impossibility rather than difficulty.
- The ruled-in design comes with the observation that its remaining problems are engineering ones.
- The object-level test reaches its answer without inspecting a candidate implementation.

## Common Failures
- Counting the threads that touch the structure rather than the threads that must agree on one outcome.
- Assuming that more bookkeeping state, or more instances of a weak primitive, lifts the ceiling.
- Treating an operation as strong because it is atomic, when atomicity and coordination power are separate properties.
- Reading the result as an argument for using a conditional update everywhere, when a cheaper operation is correct wherever two threads are all that must agree.

## Notes
The value here is almost entirely negative and that is what makes it worth rehearsing. Nonblocking designs fail in a way that reads as insufficient ingenuity — each fix narrows the race and never removes it — so without this test there is no way to tell a hard problem from an impossible one. Running it takes minutes and the alternative is weeks.
