---
object_id: PAT_make_const_member_functions_thread_safe
object_type: pattern
name: Make const Member Functions Thread Safe
library_path:
- software-engineering
- languages
- cpp
- const-correctness
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- const_correctness
- concurrency
- threading
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_use_logical_constness_with_mutable
- rel: related_to
  target_object_id: PAT_put_the_thread_safety_guarantee_at_the_transaction_boundary
- rel: related_to
  target_object_id: PAT_match_the_lock_to_the_length_of_the_critical_section
- rel: related_to
  target_object_id: PAT_verify_an_object_is_as_immutable_as_you_think
- rel: related_to
  target_object_id: AP_make_a_class_const_correct
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Make const Member Functions Thread Safe

## Pattern Rule
**IF** a member function is declared const but modifies mutable state — a cache, a validity flag, a memoized result
**THEN** synchronize that state, because callers are entitled to treat a const member function as a read and to call it concurrently without any coordination of their own
**ELSE** where you are certain the type will never be used from more than one thread, the synchronization is overhead you can decline — and that certainty is part of the type's documented contract, not an assumption.

## Do
- Recognize the shape, because it is a normal and correct design that becomes a data race for free. A function that computes an expensive result, caches it, and returns the cache on later calls is logically a read; the flag and the stored value are `mutable` so it can stay const. Two threads calling it at once are then reading and writing the same memory with no synchronization, which is the definition of a data race.
- Accept that the const is not the error. Retrieving a value that does not change the object's logical state is correctly const, in C++11 exactly as in C++98. What is missing is thread safety, and that is what needs fixing.
- Reach for a mutex first, held for the whole function. It covers the check, the computation, and the store as one operation, which is what the caller needs. The mutex itself is a `mutable` data member, and declaring it so is legitimate — it is implementation detail rather than logical state.
- Use an atomic only where one variable is genuinely enough. Atomics are cheaper than a mutex and they synchronize a single location; a cache that consists of a flag *and* a value is two locations, and guarding them separately leaves the window between them open.
- Notice that a mutex makes the class uncopyable and unmovable, and decide what that means for the type. That is a design consequence of the fix, not an accident, and it usually wants deciding rather than discovering.
- Publish which guarantee the type offers. A type that is safe for concurrent const calls and a type that is not are both legitimate; a caller cannot tell them apart from the interface, so the contract has to say.

## Don't
- Don't assume a const interface means no writes are happening. `mutable` exists precisely so that it can, and a caller reading the declaration has no way to see it.
- Don't guard two related pieces of state with two atomics. Each operation is atomic and the pair is not, so a second thread can observe the flag set before the value is stored — the same non-composition that defeats any sequence of individually safe steps.
- Don't skip the synchronization because the caching is idempotent. Computing the same value twice is harmless; the concurrent read and write of the same memory is undefined behaviour regardless of what the values would have been.
- Don't take a shipped library's constness as a promise of thread safety unless it says so. The standard's own containers offer the weaker guarantee — concurrent const calls are safe on containers that nothing is modifying — and that is a different statement.

## Checklist
- Does this const member function write to any `mutable` member?
- How many distinct locations does it write, and are they guarded as one?
- Could two threads reasonably call this function on the same object at once?
- If a mutex was added, is the resulting loss of copyability and movability acceptable?
- Does the type's documentation state which concurrency guarantee it offers?

## Notes
What makes this worth a rule of its own is the mismatch between two conventions that are each reasonable. The language convention is that const means the logical state does not change, and `mutable` is the sanctioned way to keep that true while caching. The concurrency convention — inherited from the standard library and relied on everywhere — is that const member functions are reads and reads need no synchronization. Every caching const function sits in the gap between them.

The cost question is real and the answer is usually to pay it. Synchronizing a const function costs on every call including the single-threaded ones, and the alternative is a type whose contract says it must not be shared. Both are defensible; what is not is leaving the question unanswered, because the failure mode is a data race that appears under load in someone else's code.

The atomic-versus-mutex choice looks like a performance decision and is first a correctness one. An atomic is the right instrument for a single value; the moment the cached state is a value plus a flag saying whether the value is good, one atomic cannot express the transaction and two atomics do not compose into it.
