---
object_id: PAT_check_an_atomic_is_lock_free_before_relying_on_it
object_type: pattern
name: Check an Atomic Is Lock-Free Before Relying on It
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
- lock_free
- portability
cross_links:
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_know_when_two_accesses_are_a_data_race
- rel: related_to
  target_object_id: PAT_choose_the_compare_exchange_form_by_whether_you_loop
- rel: prerequisite_for
  target_object_id: PAT_choose_the_compare_exchange_form_by_whether_you_loop
- rel: prerequisite_for
  target_object_id: PAT_make_shared_pointer_atomicity_a_property_of_the_type
- rel: related_to
  target_object_id: AP_make_shared_state_safe_in_cpp
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Check an Atomic Is Lock-Free Before Relying on It

## Pattern Rule
**IF** you are using an atomic type because you intend the code to be lock-free — no thread can be suspended holding the data hostage, or the code runs somewhere a lock is not permitted
**THEN** verify that the type actually is lock-free on your targets rather than assuming it, because the standard permits every atomic type except the atomic flag to be implemented with an internal mutex
**ELSE** where you want atomicity for correctness and have no requirement about how it is achieved, the implementation's choice is its own business and this check is noise.

## Do
- Know which guarantee you actually have. Exactly one atomic type — the atomic flag — is guaranteed lock-free by the standard. Everything else may be a mutex wearing an atomic interface, and on the popular architectures usually is not, which is precisely what makes the assumption easy to carry unexamined onto an architecture where it fails.
- Prefer the compile-time check to the runtime one when you can, because it answers a stronger question. The runtime query tells you about this object on this machine; the constant expression tells you the type is lock-free on *every* platform the executable might run on, and it is available to static assertions and to conditional compilation.
- Understand why a user-defined atomic type usually is not lock-free, since the requirements point at the answer. Such a type must have a trivial copy assignment operator, no virtual functions and no virtual bases, and must be bitwise comparable so the raw memory operations can be applied to it. Types that satisfy all that and are no larger than a machine word tend to get hardware atomics; larger ones tend to get the mutex.
- Check those requirements at compile time with the type traits rather than discovering them from a compiler error, since the traits for trivial copyability, triviality, and polymorphism answer exactly the questions the requirements ask.

## Don't
- Don't equate "atomic" with "lock-free". They are different properties: atomicity says the operation is indivisible, lock-freedom says the mechanism achieving that guarantees system-wide progress. An atomic implemented over a mutex is still perfectly atomic.
- Don't rely on a check performed only on your development machine. The runtime query is honest about the machine it runs on and says nothing about the target, which is the platform where the property mattered.
- Don't overlook that lock-free is expected to imply address-free. Operations that are genuinely lock-free are atomic with respect to other processes touching the same location, which is what makes them usable across shared memory — a mutex-backed implementation is not.

## Checklist
- Does anything here depend on lock-freedom rather than merely on atomicity, and what would break without it?
- Is the check the runtime query or the compile-time constant?
- If a user-defined type is being made atomic, does it meet all three requirements, and how large is it?
- Do all target architectures answer the same way?

## Notes
The gap this closes is between what the name promises and what the standard guarantees. Reading an atomic type as necessarily lock-free is a reasonable inference from the word and it is not what the specification says, and because the common architectures make it true in practice the mistaken inference survives testing indefinitely.

Where it matters is narrow and worth stating, because otherwise this reads as ceremony. It matters when a thread being suspended mid-operation would be unacceptable — a signal handler, a real-time deadline, code shared between processes through a mapped region — and it matters when the atomic is the whole point of a non-blocking algorithm, since an internal mutex silently converts that algorithm into a locking one with worse performance than an honest lock.

The user-defined-type requirements read as arbitrary restrictions until you see what they are for: they are the conditions under which the implementation can treat the object as a bag of bits and use a hardware instruction on it. A virtual function means a hidden pointer, a non-trivial copy means the copy has meaning beyond the bits, and neither is something a compare-and-exchange instruction can respect.
