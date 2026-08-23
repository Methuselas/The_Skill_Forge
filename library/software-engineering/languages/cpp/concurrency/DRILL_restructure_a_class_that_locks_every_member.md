---
object_id: DRILL_restructure_a_class_that_locks_every_member
object_type: drill
name: Restructure a Class That Locks Every Member Function
target_skill: Moving locking to the public boundary and keeping it out of the implementation
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 3 rough
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- locking
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_lock_at_the_public_boundary_and_nowhere_inside
- rel: related_to
  target_object_id: PAT_dont_call_unknown_code_while_holding_a_lock
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Restructure a Class That Locks Every Member Function

## Practice Task
Take a class made thread-safe by acquiring the same mutex at the top of every member function, public and private alike, where at least one public function calls another — and restructure it so locking happens only at the public boundary.

## Target Skill
Moving locking to the public boundary and keeping it out of the implementation.

## Setup
No special setup required.

## Instructions
1. Find every path where a public function calls another public function on the same object. Say what happens at each with an ordinary mutex, and what happens with a recursive one.
2. Move the locking so that public functions acquire it and non-public functions never do. Where a public function needed another's behaviour, extract that behaviour into a non-public function both can call.
3. Check the accessibility of every function that still locks, and every function that no longer does, against the rule — not against what the code happened to need.
4. Do this for both kinds of virtual, because they are reached differently. Make the public interface function virtual, override it in a derived class with the override declared private, and decide whether that override locks. Then add a non-public virtual hook that a public function calls, and decide whether that one locks. Justify each answer from how dispatch reaches the function.
5. Make one piece of the guarded state static, and decide what that does to the mutex. Say what breaks if the mutex stays per-object.
6. Find any place the class calls out to something it does not control while holding the lock — a callback, a comparator, a virtual call — and restructure so the call happens outside the guarded region.

## Success Check
- Every public member function acquires the lock; no non-public one does.
- No public function calls another public function on the same object.
- Each of the two virtuals has its locking decision stated with its reason, and each reason is drawn from how dispatch reaches that function rather than from its declared accessibility.
- Static state is guarded by a static mutex, and the failure of the per-object version is stated.
- No unknown code executes while the lock is held.

## Common Failures
- Switching to a recursive mutex to make the original version work, which converts a hang into repeated redundant work and hides where the critical section actually ends.
- Leaving a private helper that locks, so a public caller deadlocks or double-locks depending on the mutex type.
- Assuming a private override needs no lock, when dispatch reaches it through the base's public entry point and it replaces everything the base version did.
- Guarding static state with a per-instance mutex, where two objects each believe themselves protected while corrupting the same data.

## Notes
The defect this removes survives review because both halves are individually correct: a function that locks before touching shared state is right, a function that calls a helper is right, and the composition stops the program. Nothing at the call site distinguishes a helper that locks from one that does not, so it is only visible from a view of the whole class — which is what this exercise forces.
