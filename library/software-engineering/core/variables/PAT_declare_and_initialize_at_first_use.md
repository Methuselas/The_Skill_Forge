---
object_id: PAT_declare_and_initialize_at_first_use
object_type: pattern
name: Declare and Initialize a Variable Where It Is First Used
library_path:
- software-engineering
- core
- variables
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- variables
- initialization
- declarations
- proximity
cross_links:
- rel: related_to
  target_object_id: PAT_minimize_variable_span_and_live_time
- rel: foundation_of
  target_object_id: PAT_postpone_variable_definitions
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Declare and Initialize a Variable Where It Is First Used

## Pattern Rule
**IF** you are adding a variable to a routine
**THEN** put its declaration and its first value together at the point where it is first needed, rather than in a declaration block at the top.
**ELSE** where the language will not let a declaration carry a value, keep the assignment adjacent to the declaration and keep both adjacent to the first use.

## Do
- Give every declaration a value at the moment it is declared where the language allows it, so the variable never exists in a state nobody chose.
- Recognize the failure shape by its silhouette — a block of declarations, then a block of initializations, then the actual code far below. Beyond the distance, it misinforms — grouping the initializations implies all of those variables are used throughout the routine, when the last of them may be touched only at the very end.
- Watch the specific decay path, because it is what makes the habit expensive later rather than now. Straight-line code turns into loops as a program is modified, and an initialization stranded at the top of the routine then runs once where it needed to run once per pass.
- Reset counters and accumulators deliberately. The variables named `i`, `j`, `k`, `sum`, and `total` are the ones people forget before the second use.
- Initialize a class's data in its constructor, and free in the destructor whatever the constructor allocated.
- Separate the two cases before deciding where a value gets set. Something standing in for a named constant can be set once at startup; a true variable has to be set in executable code near its use, because a routine that was written to be called once and is later called twice will not run the startup path again.

## Don't
- Don't group declarations at the top out of habit. Every line between the declaration and the first use is a line where someone can modify the value without realizing the variable was already live.
- Don't assume a variable holds what you believe you left there. It fails three ways — never assigned at all, so it holds whatever bits were in that memory; assigned once and now stale; or partly assigned, with some members of an object set and others not.
- Don't rely on a compiler option that initializes everything for you. The assumption then lives in the build configuration rather than in the source, it does not survive a move to another compiler, and nobody reading the code can see that it was made.

## Checklist
- Does every declaration carry a value?
- Is each declaration within a few lines of the first use?
- Will this initialization run on every pass of every loop that needs it?
- Have the counters and accumulators been reset before their second use?
- If this routine ran twice in succession, would anything carry over from the first call?

## Notes
This is one application of a broader habit worth naming — keep related actions together. The same instinct puts a comment beside the code it describes, the loop setup beside the loop, and the statements of one straight-line job in one place instead of interleaved with another's.

The partial-initialization case deserves separate attention because it is the one that resists debugging. An object with some members set behaves consistently enough to look correct. A pointer used before its memory was allocated is worse — it writes into some arbitrary region, which may hold data, may hold code, may belong to the operating system, and the symptom differs on every run. That is what makes these harder to chase than an ordinary wrong value, and why the cheap defensive habit is worth more here than the effort it costs.

There is a language-specific route to the same placement, reached from a different direction. `PAT_postpone_variable_definitions` argues from cost — defining an object before an early-exit check means paying for a constructor and destructor you may never use. This card argues from correctness — the window between declaration and use is where wrong values come from. Both land on the same instruction, which is a good sign, but they diverge on loop variables, where the efficiency argument sometimes says to hoist a definition out of the loop and this one has no objection provided the initialization stays inside it.
