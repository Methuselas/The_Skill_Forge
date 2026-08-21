---
object_id: PAT_reach_for_a_coroutine_when_work_must_pause_and_resume
object_type: pattern
name: Reach for a Coroutine When Work Must Pause and Resume
library_path:
- software-engineering
- languages
- cpp
- coroutines
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- coroutines
- design
- lazy_evaluation
- concurrency
cross_links:
- rel: related_to
  target_object_id: PAT_choose_lazy_or_eager_by_how_often_the_result_is_needed
- rel: related_to
  target_object_id: PAT_prefer_a_task_to_a_thread_when_work_returns_something
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Reach for a Coroutine When Work Must Pause and Resume

## Pattern Rule
**IF** a computation naturally produces values over time, or must wait for something without occupying a thread while it waits
**THEN** consider expressing it as a coroutine — a function that suspends where you say and resumes where it left off, keeping its state somewhere other than the call stack
**ELSE** where the work runs once to completion and hands back an answer, an ordinary function or a task expresses that directly and a coroutine only adds machinery.

## Do
- Recognise the generator shape by what it lets you write. A function that returns a container has to decide up front how many values there are and compute all of them; a coroutine yields one per request, which makes an unbounded sequence a perfectly ordinary thing to express.
- Recognise the cooperative-multitasking shape by who decides when to switch. Under pre-emption a scheduler takes the processor away; here each piece of work runs for as long as it needs and then yields deliberately rather than sleeping or blocking — which is why this suits event-driven code, simulations, games, servers, and user interfaces.
- Know the three properties of the C++ form, because they bound what you can build. It is asymmetric, so suspending returns control to the caller rather than to another coroutine of your choosing. It is first-class, so a coroutine object can be stored, passed, and returned like any other value. It is stackless, so the state kept across a suspension lives separately from the stack.
- Read stacklessness as the deliberate consequence of a scalability goal rather than as a limitation. The design targets enormous numbers of concurrent coroutines, and a stackful design reserves a stack per instance — on the order of a megabyte or two — which caps the count long before the work does.
- Weigh a coroutine against a thread for waiting work specifically. A thread that blocks holds a stack and a scheduler slot while it does nothing; a suspended coroutine holds neither.

## Don't
- Don't hand an unbounded generator to something that consumes until exhaustion. The infinite sequence is a feature of the shape and a hazard at the call site: a loop over a generator with no termination condition does not terminate, and nothing about the generator suggests otherwise.
- Don't reach for this where the deferred computation is the whole point but the resumption is not. Deciding to compute something only when it is asked for is a separate and older decision with cheaper expressions; the coroutine earns its machinery when the computation must be *interrupted and continued*, not merely postponed.
- Don't expect suspension to happen where the reader assumes. Control returns to the caller at each suspension point, so the coroutine's code reads as a straight line while executing in pieces interleaved with everything the caller does between resumptions.

## Checklist
- Does this produce a sequence of values, or one answer?
- If a sequence, is it bounded, and does every consumer know that?
- Does the work need to wait, and would waiting otherwise occupy a thread?
- How many of these will exist at once, and would a stack each be affordable?
- Is the requirement to postpone the work, or to interrupt and continue it?

## Notes
The comparison that makes the case is the pair of generators: one function builds a container of every value the caller might want and returns it; the other yields one value and suspends, resuming exactly where it stopped when the next is requested. The second is not merely lazier — it can express sequences the first cannot represent at all, because it never has to decide how many values there are.

The design goals stated for the facility are worth knowing because they explain its shape rather than just its features: scaling to enormous numbers of concurrent coroutines, suspend and resume costing about what a function call costs, interoperating with existing facilities without overhead, leaving the high-level semantics to libraries rather than fixing them in the language, and remaining usable where exceptions are unavailable. Nearly every awkwardness in the machinery follows from one of those.

The last of those goals explains why using coroutines in C++ feels like assembling rather than calling. The language supplies the suspension mechanism and almost no policy, so generators, tasks, and asynchronous jobs are all things you or a library build on top — which is a deliberate trade of convenience for range.
