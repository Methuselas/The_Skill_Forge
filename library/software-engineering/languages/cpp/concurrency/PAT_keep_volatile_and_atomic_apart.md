---
object_id: PAT_keep_volatile_and_atomic_apart
object_type: pattern
name: Keep volatile and atomic Apart
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
- atomics
- correctness
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_weaken_a_memory_order_only_against_a_measurement
- rel: related_to
  target_object_id: PAT_make_benchmarked_work_observable
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: AP_make_shared_state_safe_in_cpp
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Keep volatile and atomic Apart

## Pattern Rule
**IF** you are reaching for `volatile` to make a variable safe to share between threads, or for an atomic type to stop the compiler optimizing an access away
**THEN** stop — the two keywords solve unrelated problems, and each is useless for the other's
**ELSE** where you are addressing genuinely special memory that several threads also touch, you need both, for their separate reasons.

## Do
- Hold the one-line distinction. Atomic types are for data reached from several threads without a mutex: they are a tool for writing concurrent software. `volatile` is for memory whose reads and writes must not be elided or reordered by the compiler because the act of reading or writing is itself meaningful: it is a tool for working with special memory.
- Know what "special memory" means, since it is what `volatile` was designed for and is rarer than its use suggests. Memory-mapped device registers, where reading twice in a row genuinely yields two different values and writing a value nobody reads still does something. Ordinary program variables are not that, and the compiler's freedom to eliminate redundant accesses to them is a large part of why optimized code is fast.
- Reach for an atomic type when the requirement is that other threads see a consistent value. It provides indivisible operations and the ordering guarantees that make one thread's writes visible to another, neither of which `volatile` provides.
- Reach for `volatile` when the requirement is that the access happens exactly as written. It provides no atomicity and no cross-thread ordering, so a shared counter declared `volatile` is a data race that happens to have the accesses the source asked for.
- Use both where the memory is genuinely special and genuinely shared. The qualifiers are orthogonal, and needing one says nothing about needing the other.

## Don't
- Don't use `volatile` for thread synchronization. It is the most persistent misconception in this area, it compiles, and it produces a program with a data race and undefined behaviour that frequently appears to work on strongly ordered hardware.
- Don't use an atomic type to prevent an access being optimized away. Atomics carry ordering and indivisibility guarantees the compiler must honour, and none of that amounts to a promise that a redundant read is preserved.
- Don't carry over the meaning `volatile` has in other languages. Some give it thread-visibility semantics; C++ does not, and the shared spelling is what makes the mistake so easy.
- Don't reason that because both keywords defeat some optimizations they must be interchangeable. Which optimizations they defeat, and why, have nothing in common.

## Checklist
- What is the actual requirement here — visibility between threads, or accesses that must not be elided?
- Is the memory in question special, in the sense that reading or writing it has an effect beyond the value?
- If this is shared between threads without a mutex, is it an atomic type?
- If a redundant access must be preserved, is that expressed with `volatile` rather than assumed?
- Are both qualifiers present, and can you say what each is for?

## Notes
The confusion has a historical root worth knowing, because it explains why experienced programmers arrive at it. Before the language had a memory model, `volatile` was the only tool that appeared to have anything to do with the compiler not caching values in registers, and it was widely pressed into service for threading on platforms where it happened to work. C++11 gave concurrency its own vocabulary, and `volatile` reverted to the one job it was designed for.

The clean statement of the difference is about what each one is a promise regarding. An atomic type promises things about the relationship between threads: that an operation is indivisible, and that operations become visible in a stated order. `volatile` promises something about the relationship between the source code and the generated code: that each access written is an access performed. Those are different axes, and a program can need a guarantee on one, the other, both, or neither.

Recognizing the "special memory" case is what keeps the rule from sounding like a prohibition on a keyword. Device registers, memory shared with hardware, and locations written for their effect rather than their value are real, and for them `volatile` is exactly right and an atomic type is not a substitute — it would make the accesses indivisible and still permit the compiler to decide that two identical reads need happen only once.
