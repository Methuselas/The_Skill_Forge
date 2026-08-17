---
object_id: AP_build_a_loop_from_the_inside_out
object_type: ap
name: Build a Loop From the Inside Out
library_path:
- software-engineering
- core
- control-flow
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- loops
- construction
- nesting
- indexes
cross_links:
- rel: related_to
  target_object_id: AP_build_a_routine_from_intent_level_pseudocode
- rel: related_to
  target_object_id: PAT_keep_a_loops_control_outside_its_body
- rel: related_to
  target_object_id: PAT_write_design_notation_at_the_level_of_intent
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Build a Loop From the Inside Out

## Objective

Write a loop that is right the first time by starting from a single concrete case and generalizing outward, so that at every step you are looking at working code and changing one thing about it — rather than starting from an empty loop structure and trying to get the indexes, the bounds, the body, and the initializations all correct simultaneously.

Reach for this when the loop is nested, when its body indexes something by more than one dimension, or whenever you notice yourself about to guess at a subscript. Simple single-level iteration does not need it.

## Steps / Flow

1. **Write the body's steps as comments, before any syntax.** Two lines are typical — get the rate from the table, add the rate to the total. Writing what has to happen is easier while you are not simultaneously thinking about indexes, bounds, and array order.

2. **Turn those comments into code for one case, using concrete values and leaving the subscripts empty.** Fetch from the table and accumulate, with the table access written but unindexed. You are not trying to produce runnable code yet; you are fixing what the body does before deciding how it is reached.

3. **Fill in the subscripts for that one case, still without a loop.** The table is accessed by age and by sex, so those are what index it. At this point the statement is specific, complete, and correct for one person, and you have never had to hold a loop variable in mind while working it out.

4. **Wrap a loop around it and indent.** The loop is indexed by whatever the repetition is over — here, by person. This step is mechanical: the body already exists and does not change.

5. **Generalize the values that vary with the new index.** Anything in the body that was concrete and now depends on the loop variable gets rewritten in terms of it. This is where the person index reaches into the record for each person, and it is the only step where an index error can be introduced — which is the point, because you are making one change with everything else already known to be right.

6. **Repeat steps 4 and 5 for each further level of nesting.** Each new loop wraps the previous one, and each time only the newly-varying values change. Three levels of nesting built this way involve three separate one-thing-at-a-time decisions rather than one simultaneous six-way decision.

7. **State the loop invariant once the shape is settled, even if you never write it as code.** An invariant is the loop's eventual goal rewritten so that it is already true before the first iteration and stays true after every one — for a maximum-finding loop, *m holds the largest value seen so far in the range already examined*. Its use is that if the invariant holds when the loop ends, the result is correct by construction, so the boundary questions that produce off-by-one and fencepost errors get answered by writing one sentence instead of by tracing cases.

8. **Add the initializations last.** Accumulators and counters get initialized once the loop's shape is settled, immediately above the loop that uses them. Leaving this to the end is deliberate — you cannot know what needs initializing until you know what varies.

## Notes

The method's value is that it never asks you to be right about more than one thing at a time, and loop defects are overwhelmingly errors of simultaneity. An index in the wrong position, a bound off by one, an accumulator initialized in the wrong place, a subscript that should have varied and did not — each is easy in isolation and they are hard together, which is what writing the structure first and filling in the body demands. Building outward reverses that: the body is settled and correct before any index exists, and each index is introduced against code that already works.

The order is not sacred and the source says so. What matters is starting from something concrete, working on one thing at a time, and building up from simple components. If it helps to write the innermost subscripts before the comments, or to sketch the loop bounds on paper first, the method still holds as long as you never have two unknowns open at once.

This is the same shape as designing a routine in intent-level pseudocode before coding it, applied one level down, and the two compose naturally — the comments written in step 1 are pseudocode at the level of intent, and they survive into the finished loop as its explanation. The difference is direction. A routine is designed top-down, from its purpose to its steps; a loop is built bottom-up, from one concrete case to the general one, because the thing that is hard about a loop is not what it does but how its indexes reach.
