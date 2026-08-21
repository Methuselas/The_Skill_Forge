---
object_id: PAT_make_shared_pointer_atomicity_a_property_of_the_type
object_type: pattern
name: Make Shared-Pointer Atomicity a Property of the Type
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
- smart_pointers
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_price_shared_ownership_before_choosing_it
- rel: related_to
  target_object_id: PAT_publish_shared_data_through_one_atomic_handle
- rel: related_to
  target_object_id: PAT_know_when_two_accesses_are_a_data_race
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Make Shared-Pointer Atomicity a Property of the Type

## Pattern Rule
**IF** several threads will write to the same shared-pointer object — not merely share the pointee, but assign to or reset the same handle
**THEN** declare that handle as an atomic shared pointer, so the type system requires every access to be atomic, rather than relying on everyone remembering to route accesses through free atomic functions
**ELSE** where each thread holds its own copy of the handle, the reference-counting machinery is already thread-safe and nothing further is needed.

## Do
- Separate the two guarantees the plain type gives you, because conflating them is the source of most of the confusion. The control block is thread-safe: reference-count adjustments are atomic and the resource is destroyed exactly once. The pointee is not, and neither is a single handle object that two threads both assign to.
- Read the two derived rules straight off that split. Multiple threads may read one handle simultaneously; multiple threads may write to *different* handles simultaneously even when those handles share a control block. Neither permits two threads writing to the same handle.
- Let the type carry the requirement. When the handle is an atomic shared pointer, an ordinary assignment to it will not compile, so the discipline is enforced rather than remembered — which is the whole argument for the facility over the free functions it replaces.
- Expect the atomic version to be cheaper than a general-purpose lock around the same handle, since an implementation can specialize for this one case, often over a lightweight flag, rather than paying for synchronization the single-threaded uses would not want.

## Don't
- Don't rely on the free atomic functions. They were the only mechanism available for a long time, they are deprecated, and their defect is structural: nothing distinguishes a correct atomic store from a plain assignment at the point of use, so a single forgotten call is a data race that compiles cleanly and reviews cleanly.
- Don't conclude from the thread-safe control block that the handle is thread-safe. That inference is what makes the plain type look usable here, and it is exactly wrong about the case where two threads assign to one handle.
- Don't reach for shared ownership *because* of thread safety. What the reference counting buys is a guarantee about destruction, not about concurrent mutation, and the cost of the counting is real whether or not you needed it.

## Checklist
- Do two threads write to the same handle object, or do they each hold their own copy?
- If they share one handle, is its type atomic?
- Does any code path assign to a shared handle with a plain assignment?
- Is the pointee itself mutated concurrently, which this addresses not at all?

## Notes
The general principle here is worth more than the specific facility, and the proposal that introduced it argues it explicitly: of the three benefits claimed — consistency, correctness, and performance — correctness is the decisive one, because it moves a requirement from discipline into the type system. A rule that must be remembered at every use site will eventually not be, and the failure is silent.

The oddity being corrected is worth noticing too. The shared pointer was the only non-atomic type in the library with atomic operations defined on it, which is precisely the shape that invites the mistake: the operations exist, they look optional, and using the ordinary syntax instead produces undefined behaviour rather than a diagnostic.

None of this touches the pointee. A handle that is safe to assign from several threads still points at an object those threads can corrupt freely, and the guidance about not sharing mutable data applies there unchanged.
