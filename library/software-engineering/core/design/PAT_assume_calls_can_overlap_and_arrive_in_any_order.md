---
object_id: PAT_assume_calls_can_overlap_and_arrive_in_any_order
object_type: pattern
name: Assume Calls Can Overlap and Arrive in Any Order
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- temporal_coupling
- concurrency
- api_design
- coupling
cross_links:
- rel: related_to
  target_object_id: PAT_watch_for_semantic_coupling
- rel: related_to
  target_object_id: PAT_make_misuse_impossible_by_removing_invalid_states
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Assume Calls Can Overlap and Arrive in Any Order

## Pattern Rule
**IF** you are designing an object, an interface, or a service, whether or not the program that will use it runs anything concurrently
**THEN** design it to hold up when calls overlap and arrive in any order — no state carried implicitly between calls, no required call sequence, and a valid state at every point a caller can reach it — because those constraints produce a better design even when nothing ever runs in parallel.

## Do
- Ask at which moments it is valid to query this object's state. If there is a window between two calls where the honest answer is "not right now," the design is resting on the coincidence that nobody calls in during that window.
- Remove state held implicitly between calls. A tokenizer whose first call takes the string and whose later calls take a placeholder to mean "same one as before" cannot parse two strings at once, threads or no threads — handing each caller an object that carries its own position removes the limitation and the surprise together.
- Separate a described workflow from its real dependencies. People narrate steps serially because that is how narration works, not because each step waits on the one before it; take the stated sequence and test each step for what it genuinely waits on, and the ones with no real predecessor can all start at once.
- Decouple in time by putting a queue between producers and consumers. Independent tasks pulling work from a shared queue each proceed at their own pace, and one that bogs down lets the others take up the slack instead of stalling them.
- Treat needing a global or static as a design question before it is a locking question — the first move is to ask why it exists, not how to protect it.

## Don't
- Don't pair a constructor that leaves the object half-built with an initialization routine that finishes the job. Between the two the object exists, is reachable, and is invalid, and nothing about the code says so.
- Don't defer this to "when we need to scale." Adding concurrency to a design built on linear assumptions is much harder than designing for it and then choosing to run single-threaded; the second order costs nothing and keeps the option.
- Don't read this as a demand for threads. It constrains the design, not the runtime model — standalone, client-server, and n-tier deployment all stay available, including the one where nothing overlaps.

## Checklist
- Is there any moment between two calls where this object would answer wrong?
- Could two callers use this at the same time on different data, or does it retain something that makes that impossible?
- Which of these steps genuinely waits on the previous one, and which merely got listed that way?
- Does anything here depend on a global or static already being in a particular condition?

## Notes
Time is the aspect of a design that most people never consciously decide, and it has two faces: ordering, meaning what must come before what, and simultaneity, meaning what can be underway at once. Linear thinking produces linear designs by default — do this, then always do that — and the dependency on ordering gets baked in without anyone choosing it. Method A must precede method B, one report at a time, the click ignored until the redraw finishes.

The claim worth carrying is that the payoff is largely independent of concurrency. The constraints that concurrency forces — no unprotected shared mutable state, valid state at every observable moment, no hidden state surviving between calls — are the same constraints that make code predictable to a single-threaded reader. What concurrency contributes is that it makes violating them fail loudly instead of silently, so designing under the assumption of overlap catches sloppiness that a linear design lets through. That is why the rule applies to code you are confident will never be threaded.

The two-string tokenizer is the sharpest illustration because it needs no threads to break. A parser that keeps its position in a hidden static cannot be used on a second string while the first is still being processed; the interface admits a use it cannot honour, and the failure looks like corrupted output rather than a rejected call. Handing the caller an object holding its own position fixes the ordering dependency, the reentrancy problem, and the thread-safety problem in one move — which is the general shape of what this constraint buys.
