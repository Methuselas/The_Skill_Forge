---
object_id: PAT_specify_a_memory_order_the_operation_can_actually_carry
object_type: pattern
name: Specify a Memory Order the Operation Can Actually Carry
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
- memory_model
- atomics
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_weaken_a_memory_order_only_against_a_measurement
- rel: related_to
  target_object_id: PAT_make_the_acquire_actually_observe_the_release
- rel: related_to
  target_object_id: PAT_choose_the_compare_exchange_form_by_whether_you_loop
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Specify a Memory Order the Operation Can Actually Carry

## Pattern Rule
**IF** you are naming a memory order on an atomic operation rather than taking the default
**THEN** match it to what kind of operation this is — the acquiring orders on reads, the releasing order on writes, the combined and sequentially consistent orders on read-modify-writes — because an order the operation cannot use is not rejected, it is silently reduced to a weaker one
**ELSE** where the operation is a read-modify-write, it always observes the most recent value regardless of which order you name, so counting and similar uses are safe on that axis without further thought.

## Do
- Learn the reduction rules, since they are where the surprise lives. Asking a load for the combined acquire-release order gives you an acquire; asking a load for the releasing order gives you *relaxed* — the strongest-looking annotation on the list becomes the weakest guarantee available, and nothing warns you.
- Classify the operation before annotating it. Loading, testing, and reading a value are reads; storing and clearing are writes; exchanging, comparing-and-exchanging, and the arithmetic and bitwise fetch operations are read-modify-writes.
- Lean on the guarantee read-modify-writes carry independently of ordering: each one sees the newest value, so a sequence of them across threads produces no gaps and no duplicates. A shared countdown built from fetch-and-subtract is correct on that count whatever order is named.
- Keep the annotation matched to what the protocol needs rather than to what looks strong. The three families are a global order across all threads, an ordering between reads and writes of the same atomic variable, and no ordering at all — and only the middle one is anchored to a particular variable.

## Don't
- Don't use the consume ordering. It orders only those operations that are data-dependent on the value loaded, so anything published alongside but not derived from it is unordered — which turns a correct release-acquire publication into a data race on the unrelated data the moment acquire is swapped for consume. Compilers have generally implemented it as acquire anyway, so the intended saving does not materialize either.
- Don't read the relaxed ordering as a mild weakening of the others. It supplies no synchronization and no ordering at all, which is why it does not fit the read/write/read-modify-write taxonomy — it is a separate thing rather than the bottom of a scale.
- Don't assume an annotation that compiles was accepted as written. Every one of the six is well-formed on every operation; the mismatch is resolved by reduction rather than by diagnosis.

## Checklist
- Is this operation a read, a write, or a read-modify-write?
- Is the named order one that this kind of operation can carry?
- If a load names the releasing order anywhere, is the code relying on ordering it does not have?
- Does anything here use the consume ordering, and is data being published that is not derived from the loaded value?

## Notes
The reduction is the part worth carrying, because it inverts the usual relationship between what you write and what you get. Elsewhere in the language a request the compiler cannot honour is an error; here it is quietly downgraded, and the specific downgrade that matters — a load annotated with the releasing order behaving as relaxed — looks like the most cautious thing on the page.

The consume ordering is the one place in this area where the honest advice is simply not to use it. Its intent was real: on architectures that track data dependencies in hardware, ordering only the dependent operations is cheaper than a full acquire. What it delivers is a rule about dependency chains that is difficult to reason about, easy to break by refactoring, and that implementations have declined to exploit — so the cost is paid in comprehension and the benefit is not collected.

The independent guarantee on read-modify-writes is easy to lose among the ordering rules and is often the property a program actually depends on. Ordering is about what *other* memory operations become visible; seeing the newest value is about the atomic variable itself, and it holds unconditionally.
