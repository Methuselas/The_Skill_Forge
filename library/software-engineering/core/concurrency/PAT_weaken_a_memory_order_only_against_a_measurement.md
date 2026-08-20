---
object_id: PAT_weaken_a_memory_order_only_against_a_measurement
object_type: pattern
name: Weaken a Memory Order Only Against a Measurement
library_path:
- software-engineering
- core
- concurrency
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- memory_order
- threading
- correctness
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_atomic_steps_do_not_compose_into_a_safe_whole
- rel: related_to
  target_object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
- rel: related_to
  target_object_id: PAT_run_threaded_code_under_conditions_built_to_break_it
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Weaken a Memory Order Only Against a Measurement

## Pattern Rule
**IF** you are considering specifying a relaxed or one-directional memory order on an atomic operation instead of taking the default
**THEN** keep the strongest order until a measurement shows the ordering itself is costing something you need back, because the default is correct by construction and the weaker ones are correct only if your reasoning is
**ELSE** where the ordering restrictions demonstrably cover a large fraction of the program's work, weakening them is exactly where the gain is and the analysis is worth doing carefully.

## Do
- Know what the default buys. Unannotated atomic operations are sequentially consistent: a bidirectional barrier at every operation, plus the guarantee that the whole program behaves as if every processor's operations were merged into one global order with each processor's own sequence preserved. That property is what makes a concurrent program reasonable about, and it is why it is the default.
- Understand the pairing before using half-barriers. Release on the writing side guarantees that everything the writer did beforehand is visible to a reader that observes the write; acquire on the reading side guarantees that nothing the reader does afterwards is moved before it. Both sides must use them, on the same variable — a release paired with a relaxed read guarantees nothing at all.
- Anchor the reasoning to a specific variable. Two threads have no meaningful order relative to each other until one observes the other's atomic operation on the same object; before that, "before" and "after" have no content.
- Take the ordering that locks already give you rather than reinventing it. Acquiring a lock is an acquire operation and releasing it is a release operation, so a critical section is a membrane that outside work can enter but nothing inside can leave — everything one thread did before its critical section is visible to another thread after its own.
- Run the weakened version under a race detector, and run it on more than one architecture if it will ship on more than one. Tooling of the thread-sanitizer kind is what finds an ordering bug that the hardware is hiding.
- Measure the ordering itself when you suspect it. A benchmark that performs nothing but atomic stores under different orders isolates the cost of the barrier, which is the quantity in question.
- State the order the protocol actually requires even where it costs nothing to omit. Asking for relaxed order on an x86 atomic increment buys no speed, and it still says which guarantee the code depends on — to the next architecture, and to the next reader, who otherwise has to search for the subtle place that relies on a barrier the code never mentions.

## Don't
- Don't reason about which interleavings would go wrong. Unsynchronized access to one location from several threads where at least one writes is undefined behaviour, full stop; whether you can construct a failing sequence is not the test and there is nothing to gain from that line of thought.
- Don't mix mechanisms on one location. Atomic operations guarantee freedom from races only if every thread uses them; one non-atomic or differently-locked access anywhere voids the guarantee for all of them.
- Don't take a passing test on x86 as evidence the ordering is right. That architecture gives every store a release barrier and every load an acquire barrier for free, so a program with the wrong order on the reading side runs correctly there and fails on a weakly-ordered processor such as an ARM part.
- Don't expect weakening to pay on hardware that was already doing it. Going from release to relaxed on a store buys nothing on x86 for the same reason — the hardware provides the stronger order regardless, and most compilers do not optimize across atomic operations either.
- Don't specify an order stronger than the protocol needs and call it safe. It is safe, and it is also the thing this decision is about: acquire-release on both sides of a producer-consumer handshake gives guarantees in directions neither side depends on.

## Checklist
- Does the default order actually appear in a profile as a cost, or is this being changed on principle?
- For each weakened operation, which operation on which variable is its counterpart?
- Do both sides of every pairing use the matching order?
- Has this run under a race detector, and on a weakly-ordered architecture?
- Would a lock give the same guarantees with less to reason about?

## Notes
The ordering guarantees exist because compilers and processors reorder freely by default, and they do it for speed. That framing is the honest way to hold the trade: every restriction you impose removes an optimization the machine would otherwise have taken, so the goal is the weakest order that is still correct — and the difficulty is that "still correct" is a proof obligation rather than a test result.

The portability trap deserves separate weight from the performance question because it inverts the usual relationship between testing and confidence. On a strongly ordered architecture the incorrect program passes, repeatedly, on every machine available, and the defect is latent until the code moves. Nothing about the program's behaviour on the development machine can distinguish a correct ordering from a lucky one.

The language-level model is not the only model in play. Hardware, operating system, and runtime each impose their own, and what a program actually gets is the superposition. That is occasionally exploitable in code targeting one processor, and for portable code it is a complication rather than a resource — the only guarantees that travel are the language's own.

Two smaller consequences of having a language memory model at all are worth carrying. Before one existed, nothing in the language stopped a compiler from reordering an unrelated update past a lock operation, and multi-threaded programs worked because compilers honoured platform models the standard said nothing about. And writing to distinct adjacent variables from different threads is guaranteed safe only under a model that says so — hardware that updates a single byte by rewriting the enclosing word makes neighbouring `bool` or `char` variables unsafe without that guarantee.
