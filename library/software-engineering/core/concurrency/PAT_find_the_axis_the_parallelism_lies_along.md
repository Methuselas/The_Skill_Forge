---
object_id: PAT_find_the_axis_the_parallelism_lies_along
object_type: pattern
name: Find the Axis the Parallelism Lies Along
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- concurrency
- design
- decomposition
- patterns
- scalability
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
- rel: related_to
  target_object_id: PAT_derive_the_parallelism_from_work_and_span
- rel: related_to
  target_object_id: PAT_let_idle_workers_take_work_rather_than_busy_ones_hand_it_out
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Find the Axis the Parallelism Lies Along

## Pattern Rule
**IF** you have decided a computation is worth parallelizing and must now choose how to cut it up
**THEN** answer two questions before designing anything — along which axis do the independent pieces lie, and is the set of pieces known before the computation starts — because those two answers between them determine both the decomposition and how the work will have to be distributed
**ELSE** where the computation is one operation applied independently to every element of a collection, the axis is the data, the set is known, and both questions are already answered.

## Do
- Take the first question as a choice among three, not two. The independent pieces may be the *steps* — distinct operations that can proceed at once on the same data. They may be the *data* — one operation applied to disjoint regions. Or they may be neither: a stream of items flowing through a sequence of stages, where the parallelism is that different items occupy different stages at the same moment. That third axis is the one most often missed, because nothing about it looks parallel until you notice that stage two can work on item one while stage one works on item two.
- Take the second question as deciding how work gets distributed, not merely how it is described. If every piece is known before starting, the pieces can be assigned once and the distribution problem is a partitioning problem. If pieces are generated as the computation proceeds — a recursive split that stops on a condition discovered at run time, an event whose handling produces more events — then no assignment made up front can be right, and the design needs a mechanism for moving work to whoever is free.
- Derive the pieces from the dependency graph, not from the call graph, and expect the two to differ. A recursive divide-and-conquer algorithm reads as strictly nested calls, and its dependency graph is a tree in which entire subtrees are independent — the parallelism is invisible in the source order and obvious in the dependencies. Working from the call structure is the standard way to conclude that a parallelizable algorithm is sequential.
- Check the axes against each other rather than stopping at the first that works. The same computation frequently admits more than one, and they produce different communication patterns, different piece sizes, and different sensitivity to load imbalance. The point of knowing all three is to have something to compare, not to classify the problem correctly.
- Prefer the axis that makes the pieces independent over the one that makes them equal. Pieces that need nothing from each other can be distributed anywhere and rearranged freely; equal-sized pieces that exchange data at every step have fixed most of the design before the mapping question is even asked.
- Say which axis you chose where the design is recorded. It determines what the pieces are, what has to cross between them, and which failures to expect — and a reader who assumes the data axis on a design built along the stage axis will misread every part of it.

## Don't
- Don't treat the categories as a classification exercise. They overlap, most real problems admit several, and the value is in seeing the alternatives rather than in naming the one true answer. A taxonomy that produces one label per problem has been used wrongly.
- Don't assume the data axis because it is the familiar one. Splitting a collection is the decomposition everyone reaches for, and it is the wrong one whenever the work is a sequence of transformations over a stream, or a handful of genuinely different operations that could all run at once.
- Don't commit to a static assignment when the piece set is discovered at run time. The pieces will be uneven and unpredictable, and an assignment fixed up front converts that unevenness directly into idle workers.
- Don't decompose along an axis whose pieces all need the same shared state. That produces many pieces and no parallelism, and it usually means the axis was chosen from how the code is organized rather than from where the independence is.
- Don't skip this because the answer seems obvious. It often is — and the cost of asking is a minute, while the cost of discovering halfway through that the parallelism was along a different axis is the design.

## Checklist
- Which of the three axes are the independent pieces on — steps, data, or items moving through stages?
- Does the computation admit more than one axis, and what does each cost?
- Is the set of pieces known before the computation begins, or produced as it runs?
- Was the piece set derived from dependencies or from the order the code happens to call things in?
- What must cross between pieces under the chosen axis?
- Do all the pieces need the same shared state?

## Notes
The two questions do different jobs and it is worth keeping them apart. The first is about the problem: where does the independence actually live, and the answer is a property of the computation rather than of any implementation. The second is about the future design: it determines whether work can be placed once or has to be moved around while running, which is the difference between a partitioning problem and a load-balancing one. Answering the first and forgetting the second produces a correct decomposition attached to a distribution scheme that cannot serve it.

The stage axis deserves separate emphasis because it is genuinely easy to miss. A computation that transforms each item through a fixed sequence of steps looks entirely sequential — every item must go through every step in order — and it parallelizes perfectly all the same, because different items can occupy different stages simultaneously. Nothing in the code suggests this. It is visible only once you stop asking what can happen at once *to an item* and start asking what can happen at once *in the machine*.

The call-graph trap is worth carrying as a habit rather than a fact. Source order is the order one processor happened to need; dependencies are what the algorithm actually requires. Those coincide in sequential code by construction, which is exactly why reading parallelism off the source is so misleading — the nesting that looks like a chain of dependencies is often just the single-threaded execution the author had in mind.
