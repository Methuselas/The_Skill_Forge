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
- rel: related_to
  target_object_id: PAT_break_one_of_deadlocks_four_conditions
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
4. Do this for both kinds of virtual, because they are reached differently. Make the public interface function virtual, override it in a derived class with the override declared private, and decide whether that override locks. Then add a non-public virtual hook that a public function calls, and decide whether that one locks. Justify each answer by tracing the call path that reaches the function and saying what is held at each point on it. If you would refuse the public virtual in real code, say why, then build it anyway — the two dispatch routes are what this step is for, and you cannot compare them with only one of them present.
5. Make one piece of the guarded state static and leave the rest per-object. Decide what that does to the mutex, and say what breaks if the static state stays on the per-object mutex. Then say what it costs to go the other way and make the single mutex static for everything — the answer is not that it becomes unsafe. Keep both mutexes for the rest of the exercise.
6. You now hold two mutexes with different lifetimes. Find every path that acquires both — any member function that touches per-object and static state in one call — and name the order they are taken in. Show that every such path takes them in that order. If no path takes both, say so, and say what keeps that true as the class grows.
7. Find any place the class calls out to something it does not control while holding either mutex — a callback, a comparator, a virtual call — and restructure so the call happens outside the guarded region. Then check what is left in the guarded regions that you did not write, including the calls that take locks without saying so.

## Success Check
- Every public member function that touches guarded state acquires the mutex that guards it, and nothing called from inside a guarded region acquires that same mutex again — not a non-public member, not a free function, not a lambda. Constructors, destructors, and members that touch only state which is immutable after construction are exempt; each exemption is named, with the reason it is one.
- No public function reaches another public function on the same object, including through a stored callable, a base-class pointer, or a virtual dispatch that lands back on this object.
- Each virtual's locking decision is stated together with the call path that reaches it and what is held at each point on that path, so the decision follows from the trace rather than from an assertion about dispatch. A run that declines to make the interface function virtual, and wraps a non-public virtual instead, answers for the virtual it has and states why the public one was refused.
- The static state is guarded by something whose lifetime matches it — a static mutex, an atomic, or a container that synchronises itself — and the per-object state is still on the per-object mutex. Both failures are stated: guarding static state per-object, and collapsing everything onto one static mutex.
- Every path that acquires both mutexes takes them in one stated order, and those paths are named individually; or no path acquires both, and what keeps that true is stated.
- No caller-supplied or cross-component code runs while a mutex is held. Every remaining call in a guarded region that reaches code the class does not own — an allocation, a formatting or logging call, a standard-library entry point — is listed, and each is either relocated or kept deliberately with the reason it cannot participate in a cycle here.

## Common Failures
- Switching to a recursive mutex to make the original version work, which converts a hang into repeated redundant work and hides where the critical section actually ends.
- Leaving a private helper that locks, so a public caller deadlocks or double-locks depending on the mutex type.
- Moving a locking helper out of the class to a free function or a lambda, so that no non-public member locks and the double acquisition survives intact. Where the helper lives is not the property that matters; what is held when it runs is.
- Assuming a private override needs no lock, when dispatch reaches it through the base's public entry point and it replaces everything the base version did.
- Guarding static state with a per-instance mutex, where two objects each believe themselves protected while corrupting the same data.
- Moving all the state onto the static mutex to make the previous failure go away. It is safe and it serializes every object against every other, which is the concurrency the per-object mutex existed to provide; the cost is the answer, not the safety.
- Adding the second mutex without deciding in what order the two are taken, so one member function locks per-object then static while another locks static then per-object. Each function is correct read on its own, and the pair can seize up.
- Relocating the callback and the comparator, then leaving a logging or formatting call inside the guarded region because it is not the kind of thing the instruction named. It takes locks of its own and says so nowhere in its signature; the question is what it can reach, not what it is called.
- Answering the virtual question with a reason that sounds like dispatch but was never traced. "It is reached through the base's public entry point" is the right shape of reason and is worth nothing until the path is followed and the state of the lock at each point on it is written down.

## Notes
The defect this removes survives review because both halves are individually correct: a function that locks before touching shared state is right, a function that calls a helper is right, and the composition stops the program. Nothing at the call site distinguishes a helper that locks from one that does not, so it is only visible from a view of the whole class — which is what this exercise forces.

Instruction 6 turns the same observation on the repair rather than on the original defect. Step 5 introduces a second mutex, and a second mutex is a fresh opportunity for exactly the composition failure the exercise opened with: two member functions, each correct read alone, that take the pair in opposite orders. The ordering question therefore belongs to this drill rather than to a later one, because this drill is where the hazard is created. Which of deadlock's four conditions an acquisition order removes, and what that choice costs, is `PAT_break_one_of_deadlocks_four_conditions`.
