---
object_id: PAT_atomic_steps_do_not_compose_into_a_safe_whole
object_type: pattern
name: Two Atomic Operations Are Not One Atomic Operation
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
- concurrency
- atomicity
- invariants
- threading
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_check_concurrent_code_for_safety_and_liveness
- rel: related_to
  target_object_id: PAT_assume_calls_can_overlap_and_arrive_in_any_order
- rel: related_to
  target_object_id: PAT_define_your_code_contract_explicitly
reference:
  source_title: 'Implementing Effective Code Reviews: How to Build and Maintain Clean Code'
  author: Giuliana Carullo
confidence: high
references: []
variants: []
---

# Two Atomic Operations Are Not One Atomic Operation

## Pattern Rule
**IF** you are relying on individually indivisible operations — an atomic counter, a thread-safe collection, a single-statement update — to keep shared state correct
**THEN** find the invariant that spans more than one of them and protect the whole span, because indivisibility of each step says nothing about what another thread can do between two steps
**ELSE** where each operation genuinely stands alone and no relationship between them has to hold, the individual guarantees are sufficient and adding a wider lock buys nothing.

## Do
- Start by writing down what must be true of the state, rather than which operations touch it. The rule that has to hold across two updates is the thing under threat, and it is usually implicit — a total matching a sum of parts, two collections staying in step, a flag agreeing with the data it describes.
- Look specifically at read-then-act sequences. Checking a condition and then doing something because of it is two operations, each of which may be individually safe, with a window between them in which the condition can stop being true.
- Widen the protected region to cover the invariant rather than each operation. What needs to be indivisible is the span across which the rule is temporarily violated, and that is a property of the rule, not of any single call.
- Distinguish a collection that is safe to call concurrently from one that makes your use of it safe. A structure guaranteeing that no individual operation corrupts it says nothing about a sequence of your operations on it, and the guarantee is frequently read as the stronger claim.
- Prefer moving the compound operation inside the thing that owns the state, where it can be made indivisible once, over asking every caller to remember to acquire something first.
- Treat the roll-back case as part of the design. Where a span cannot complete, the state must return to a valid configuration rather than stopping halfway through a violated rule.

## Don't
- Don't infer safety from the safety of the parts. This is the specific inference to distrust — every operation being individually correct is compatible with every ordering of them being wrong.
- Don't reason about a compound sequence as though the elapsed time between steps were negligible. A scheduler can suspend a thread anywhere, and the gap between two adjacent statements is unbounded in principle.
- Don't rely on a type's concurrency guarantee without reading what it actually promises. Guarantees are made about individual method calls, and the interesting invariants nearly always span several.
- Don't scatter the protection across the call sites. A rule enforced by convention at each caller is enforced until somebody writes a new caller.

## Checklist
- What has to remain true across this sequence, stated as a sentence about the state?
- Where does that statement stop being true, and how long is the window?
- Is any decision here made on a value that another thread could change before the decision is acted on?
- Does the guarantee you are leaning on cover a call, or a sequence of calls?
- If the middle of this sequence fails, what configuration does the state end up in?
- Is the protection inside the thing that owns the state, or remembered by each caller?

## Notes
The trap is a reasoning error about composition rather than a gap in knowledge, which is why experienced people walk into it. Indivisibility feels like it should accumulate — if step one cannot be interrupted and step two cannot be interrupted, the pair feels protected. But indivisibility is a property of each step in isolation, and the danger has moved to the space between them, which no amount of strengthening either step addresses. The guarantee is real and is simply about something other than what is needed.

Framing the problem around invariants rather than operations is what makes the right boundary visible. Ask which operations need protecting and the answer is each of them, which is what the individual guarantees already provide. Ask instead what rule must hold about the state, and the boundary appears on its own: protection has to cover the whole stretch during which the rule is temporarily false. That reframing also explains why the correct region is often larger than anyone expects and cannot be found by inspecting the operations one at a time.

The read-then-act shape deserves recognition on sight because it is the overwhelmingly common instance. Checking whether something exists before creating it, reading a balance before debiting it, testing a flag before acting on it — all are two operations with a decision made in the first and acted on in the second, and all are wrong under concurrency no matter how safe each half is individually. Once the shape is recognisable, most instances of this fault become visible during reading rather than during an incident, which is the difference between a review catching it and production catching it.
