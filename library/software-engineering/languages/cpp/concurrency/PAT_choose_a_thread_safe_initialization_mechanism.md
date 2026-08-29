---
object_id: PAT_choose_a_thread_safe_initialization_mechanism
object_type: pattern
name: Choose a Thread-Safe Initialization Mechanism
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- initialization
- immutability
- threading
cross_links:
- rel: related_to
  target_object_id: PAT_replace_nonlocal_statics_with_local_statics
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_restrict_a_special_member_to_control_where_objects_can_exist
- rel: related_to
  target_object_id: AP_make_shared_state_safe_in_cpp
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Choose a Thread-Safe Initialization Mechanism

## Pattern Rule
**IF** a variable is written once during initialization and only read thereafter, and several threads may reach it
**THEN** pick one of the mechanisms that makes the initialization itself thread-safe rather than guarding every subsequent read, because a value that is never modified after initialization needs no lock and no atomic once it exists
**ELSE** where the variable is genuinely modified after startup, this does not apply and the access needs synchronizing like any other shared mutable state.

## Do
- Ask first whether the initialization can happen before any thread exists. Initializing in the main thread before spawning anything is the cheapest correct answer and requires no mechanism at all — it is worth ruling out before reaching for the others.
- Take compile-time evaluation where the value permits it, since a value computed by the compiler is thread-safe by construction with nothing to arrange at run time. A user-defined type qualifies when it has no virtual functions and no virtual base, its constructor is itself evaluable at compile time, and every base and non-static member is initialized.
- Use a function-local static when the value must be computed at run time and you want it built on first use. The language guarantees that exactly one thread performs the initialization and the others wait, and the object is never built at all if nothing reaches it.
- Reach for the call-once facility with its flag when the initialization is not naturally expressed as constructing one object — registering a handler, opening a connection, populating something that already exists. Exactly one of the functions registered against a given flag runs, no call returns before that one has completed, and if it throws, another registered function is selected on the next attempt.

## Don't
- Don't hand-roll a check-then-lock-then-check sequence. It is the intuitive optimization, it is famously wrong without careful atomics and ordering, and every mechanism above supplies the same effect correctly with less code.
- Don't guard the reads once the initialization is safe. If nothing writes after initialization, concurrent reads are not a race and the lock is pure cost on the path that dominates.
- Don't assume compile-time evaluation is available because the initializer looks constant. The requirements on user-defined types are specific, and a type that fails one of them falls back to run-time initialization without saying so.

## Checklist
- Is this variable actually written only during initialization?
- Could it be initialized before any thread is created?
- Can the value be computed at compile time, and does its type meet the requirements?
- If it is built on first use, is that a function-local static rather than a hand-written guard?
- Is anything here implementing a check-lock-check sequence by hand?

## Notes
The framing that makes this a decision rather than a lookup is that thread safety is being established once, at initialization, rather than continuously, at every access. That is the same move as making data immutable: pay once to remove the question instead of paying repeatedly to answer it.

The mechanisms form a rough order of preference by how little they cost at run time — initialize before threads exist, then compile-time evaluation, then a function-local static, then the call-once facility — and the right choice is usually the first one on that list that the situation permits rather than the most capable one.

The hand-written double-check deserves its reputation. It is the optimization everyone independently invents, it appears to work, and getting it right requires exactly the atomics-and-ordering reasoning that the language facilities exist to spare you. Its presence in a codebase is usually a sign that it predates the facilities rather than that it was chosen over them.

The preference order above has been measured, and the measurement is emphatic enough to be worth carrying. Across four threads repeatedly obtaining one lazily initialized object, the function-local static came within a whisker of the single-threaded baseline — roughly 0.03 to 0.04 against 0.02 to 0.03 — which means it achieves essentially perfect concurrency on this access. Both atomic-based hand-rolled versions were about twice as slow as that, whether sequentially consistent or using acquire-release. The call-once facility was several times slower again and varied sharply by platform, being far more expensive on Windows than on Linux. Guarding every access with a lock was catastrophic: several hundred times the function-local static's cost.

So the cheapest correct option is also the one requiring the least code, which is unusual enough to state plainly. The measurement additionally rules out the intuition that hand-rolled atomics must beat a language facility — here they lose to it, twice over, while carrying all the reasoning burden.
