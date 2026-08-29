---
object_id: PAT_lock_at_the_public_boundary_and_nowhere_inside
object_type: pattern
name: Lock at the Public Boundary and Nowhere Inside
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- locking
- class_design
- deadlock
cross_links:
- rel: related_to
  target_object_id: PAT_put_the_thread_safety_guarantee_at_the_transaction_boundary
- rel: related_to
  target_object_id: PAT_wrap_virtuals_with_nvi_idiom
- rel: related_to
  target_object_id: PAT_dont_call_unknown_code_while_holding_a_lock
- rel: related_to
  target_object_id: PAT_give_a_shared_object_its_own_thread_instead_of_a_lock
- rel: prerequisite_for
  target_object_id: DRILL_restructure_a_class_that_locks_every_member
- rel: related_to
  target_object_id: AP_make_shared_state_safe_in_cpp
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Lock at the Public Boundary and Nowhere Inside

## Pattern Rule
**IF** you are making a class usable from several threads by locking its member functions
**THEN** lock in the public functions only, leave every non-public function unlocked, and forbid public functions from calling other public functions — because a locking function that calls another locking function on the same object either locks redundantly or deadlocks outright
**ELSE** where the object's whole state is one thing that already carries its own guarantee — a single atomic, or a container built for concurrent use — there is no interface to structure and the guarantee is already where it belongs.

## Do
- Apply the three rules together, since each one alone is insufficient. Public functions take the lock; protected and private functions never do; and public functions call only non-public ones. The third is what keeps the first two consistent as the class grows.
- Make the mutex static when the state it protects is static. The critical section then covers every instance of the class rather than one object, and a per-object mutex would let two instances corrupt the shared state while each believed itself protected.
- Give an override a lock even when it is private, where the interface function is virtual. Dispatch reaches the override through the base's public entry point, and the override replaces the base version entirely — including the locking the base version did.
- Recognise this as the same construction as the non-virtual interface idiom, arrived at from a different direction. A public non-virtual entry point that does the bookkeeping and delegates to non-public workers is the answer to both problems, which is why a class already built that way is most of the way here.
- Pair the boundary lock with a condition where a public function has a precondition the caller cannot check. Exclusion alone makes the object safe and says nothing about a client that arrives when there is nothing to take or no room to add; the lock keeps it from corrupting the state, and a condition it waits on — releasing the lock while it waits, re-acquiring it on being woken, and re-testing the predicate rather than trusting the wakeup — is what lets it eventually proceed instead of failing or spinning. Safety and progress are two guarantees and the object needs both.
- Notify from inside the same public function that changed the state, not from the caller. The whole point of locking at the boundary is that clients are unaware of the synchronization, and an object that requires its callers to signal after using it has moved half the mechanism back into the interface.
- Package the lock-and-condition pairing once and derive from it. Every class that needs this needs the same three operations — take the lock for the duration of a public function, wait for a predicate, wake the waiters — and rebuilding them per class is how the variants drift apart.

## Don't
- Don't lock every member function on principle. It is the obvious way to make a class thread-safe and it is wrong in both directions: with a recursive mutex the inner lock is redundant work on every nested call, and with an ordinary mutex it is undefined behaviour that in practice deadlocks.
- Don't switch to a recursive mutex to make the naive version work. It converts a hang into wasted work and leaves the real defect in place, which is that the extent of the critical section is no longer visible at any single point in the code.
- Don't let a public function call another public function on the same object, even when it currently does not lock. The moment someone adds a lock to the callee — which the rules above say they should — the caller deadlocks, and nothing about the call site suggests why.

## Checklist
- Does every public member function take the lock?
- Does any non-public member function take it?
- Does any public function call another public function on this object?
- Is any protected state static, and if so is the mutex static too?
- Are any interface functions virtual, and do their overrides lock?
- Does any public function have a precondition the caller cannot test, and if so does it wait on a predicate rather than turn the caller away?
- Is every notification issued from inside the object, or is some caller expected to signal on its behalf?

## Notes
The failure this prevents survives review because both halves are individually correct. A function that locks before touching shared state is right; a function that calls a helper is right; and the composition is a program that stops. Nothing at the call site distinguishes a helper that locks from one that does not, so the defect is only visible from a view of the whole class.

This sits underneath the question of which level should carry the guarantee rather than beside it. Deciding that the guarantee belongs on this class is one decision; building the class so that the guarantee does not destroy itself is another, and the rules above are the second. A design that puts the boundary in the right place and then locks every member function has answered the first correctly and the second wrongly.

The static case is worth checking for explicitly because the class reads identically either way. Instance state with a per-instance mutex and static state with a per-instance mutex differ by one keyword on a member declaration, and only the first is safe.
