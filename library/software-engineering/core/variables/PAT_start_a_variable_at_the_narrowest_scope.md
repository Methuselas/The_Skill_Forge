---
object_id: PAT_start_a_variable_at_the_narrowest_scope
object_type: pattern
name: Start a Variable at the Narrowest Scope and Widen Only on Demand
library_path:
- software-engineering
- core
- variables
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- variables
- scope
- visibility
- information_hiding
cross_links:
- rel: related_to
  target_object_id: PAT_ask_what_should_be_hidden
- rel: related_to
  target_object_id: PAT_avoid_global_state_inject_shared_state
- rel: related_to
  target_object_id: PAT_minimize_variable_span_and_live_time
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Start a Variable at the Narrowest Scope and Widen Only on Demand

## Pattern Rule
**IF** you are deciding how widely a variable should be visible
**THEN** declare it at the narrowest level that works and widen only when something concrete demands it, because widening later is nearly free and narrowing later is not.
**ELSE** where you genuinely cannot confine it to the class most responsible for it, share the data through access routines rather than exposing the variable itself.

## Do
- Walk the rungs in order and stop at the first one that works — local to a single loop, local to a routine, private to a class, protected, package where the language has one, and reachable from anywhere only as a last resort.
- Price the two directions before choosing, because they are not symmetric. Turning a class variable into a widely visible one is a local edit. Going the other way means finding every use, understanding each, and proving none of them needed the reach — which is why the cheap moment to be strict is the first one.
- Reach for access routines at the boundary rather than widening. If the owning class cannot keep the data to itself, letting other classes ask it for the value keeps the decision about representation inside one place.
- Settle convenience arguments with the measurements instead of with preference. A variable reachable from everywhere has an enormous span and live time by construction, and that is the concrete form of the objection.

## Don't
- Don't widen to avoid parameter lists and scoping rules. That trade buys ease of writing and sells ease of reading, and the reading happens far more often and by more people.
- Don't mistake universal reach for flexibility. In a program where any routine can touch any variable at any time, no routine can be understood on its own — you have to understand every other routine that shares the data, which is what makes such programs hard to read, debug, and change.
- Don't read this as a prohibition. The last rung exists and is occasionally right; what the ladder rules out is arriving there without having tried the others.

## Checklist
- What is the narrowest rung this variable would actually work at?
- What specifically forced it wider than that — a real requirement, or the convenience of not passing it?
- If you had to narrow it tomorrow, how many places would you have to read first?
- Could the class that owns this expose a routine instead of the data?
- Have you tried the restrictive version and watched it fail, or assumed it would?

## Notes
The asymmetry is the whole argument, and it is what makes this different from a general preference for encapsulation. Both directions are available at any time, but they cost wildly different amounts, so the rational play is to start where the cheap move is the one you are likely to need. Starting wide and narrowing later is the expensive direction, and it is the one you are committed to the moment you declare the variable broadly.

Underneath the ladder sits a genuine disagreement about what code is for. One position treats a variable's reach as a convenience question — reachable data is data you do not have to thread through parameter lists, and the risk is worth the saving. The other treats it as a question of how much has to be held in mind at once, on the grounds that the less you must remember the smaller the chance of forgetting something that mattered. The two positions are really a disagreement about whether writing or reading is the activity to optimize for, and once it is put that way the answer follows from how many times each will happen.

This is the variable-level instance of a decision the package also makes at the design level, where the question is what secret a class or module should keep. The connection is worth holding because it explains why the rungs are ordered the way they are — each one exposes a decision to a wider audience, and the discipline is the same whether the thing exposed is a representation or a value.
