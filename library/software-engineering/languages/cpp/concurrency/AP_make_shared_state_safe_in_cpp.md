---
object_id: AP_make_shared_state_safe_in_cpp
object_type: ap
name: Make Shared State Safe in C++
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
- threading
- atomics
- locking
cross_links:
- rel: supports
  target_object_id: PAT_know_when_two_accesses_are_a_data_race
- rel: supports
  target_object_id: PAT_choose_a_thread_safe_initialization_mechanism
- rel: supports
  target_object_id: PAT_keep_volatile_and_atomic_apart
- rel: supports
  target_object_id: PAT_check_an_atomic_is_lock_free_before_relying_on_it
- rel: supports
  target_object_id: PAT_specify_a_memory_order_the_operation_can_actually_carry
- rel: supports
  target_object_id: PAT_make_the_acquire_actually_observe_the_release
- rel: supports
  target_object_id: PAT_choose_the_compare_exchange_form_by_whether_you_loop
- rel: supports
  target_object_id: PAT_make_shared_pointer_atomicity_a_property_of_the_type
- rel: supports
  target_object_id: PAT_take_the_simplest_lock_type_that_does_the_job
- rel: supports
  target_object_id: PAT_lock_at_the_public_boundary_and_nowhere_inside
- rel: supports
  target_object_id: PAT_dont_call_unknown_code_while_holding_a_lock
- rel: supports
  target_object_id: PAT_choose_between_a_semaphore_a_latch_and_a_barrier
- rel: supports
  target_object_id: PAT_wait_on_a_predicate_not_on_a_notification
- rel: related_to
  target_object_id: AP_give_an_acquired_resource_an_owner
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted C++ sources
confidence: medium
references: []
variants: []
---

# Make Shared State Safe in C++

## Objective
Given data that more than one thread reaches, arrive at the mechanism that makes it safe — and at the ordering, the boundary and the lifecycle that mechanism drags along with it. Success is that the choice was made from what must be atomic rather than from what is familiar, that every rule the chosen mechanism carries has been applied rather than the first one, and that a reader can say which threads touch this data and under what protection. Not a survey of concurrency primitives; a sequence in which each answer removes most of the remaining ones.

## Steps / Flow

**Entry state.** Two or more threads reach the same data, or you are about to arrange that they will. If you cannot yet name which threads and which of them write, stop and find out — every branch below turns on that, and guessing produces protection aimed at the wrong access.

1. **Establish that you have a race at all, by the definition rather than by feel.** `PAT_know_when_two_accesses_are_a_data_race` owns it: two threads reach the same object, at least one writes, and exactly two escapes exist — the access goes through an atomic operation, or one access is ordered before the other. Anything that is not one of those two is undefined behaviour rather than a risk to be weighed. Where no escape applies, the rest of this protocol is what fixes it; where one already does, you may be finished before step 2.

2. *Branch.* **If the data is written once during initialization and only read afterwards, that is a smaller problem with its own answer.** `PAT_choose_a_thread_safe_initialization_mechanism` owns the mechanisms. Take that route and stop — reaching for a lock or an atomic here buys protection against writes that never happen.

3. *Gate.* **Do not solve this with `volatile`.** `PAT_keep_volatile_and_atomic_apart` owns why the two keywords answer unrelated questions, and this gate exists because the wrong turn is taken confidently and the result compiles, runs, and frequently appears to work. If the reasoning for a mechanism was "so other threads see it," that reasoning has already gone wrong.

4. **Choose the mechanism from what has to be indivisible, not from what is available.** One variable with simple operations wants an atomic. An invariant spanning several variables — where a reader must never see one updated and the other not — wants a lock, because that invariant is the unit of atomicity and no per-variable mechanism can carry it. A count of permits, a one-time gate, or a repeated phase wants neither, and step 8 owns that case. This is the fork the rest of the protocol hangs on, and naming the unit of atomicity out loud is what decides it.

5. **On the atomic route, the ordering rules travel with the choice.** `PAT_specify_a_memory_order_the_operation_can_actually_carry` owns matching the order to the kind of operation, and `PAT_make_the_acquire_actually_observe_the_release` owns the pairing that makes preceding writes visible — an acquiring load that runs before the releasing store simply does not see the data, so it must keep loading until it does. Where the operation is a compare-and-exchange, `PAT_choose_the_compare_exchange_form_by_whether_you_loop` owns which form. Reach for a standalone fence only where no atomic you are already performing can carry the order; `PAT_reach_for_a_fence_only_when_no_atomic_carries_the_order` owns that judgement.

6. *Gate.* **If the reason for the atomic was lock-freedom, verify it rather than assuming it.** `PAT_check_an_atomic_is_lock_free_before_relying_on_it` owns this, and the check matters because a type that silently uses a lock underneath defeats the entire reason it was chosen. Where the shared thing is a smart-pointer handle that several threads assign to — not merely the object it points at — `PAT_make_shared_pointer_atomicity_a_property_of_the_type` owns making that a property of the declaration rather than of every call site.

7. **On the lock route, take the least capable construct and put it at one boundary.** `PAT_take_the_simplest_lock_type_that_does_the_job` owns the choice of construct. `PAT_lock_at_the_public_boundary_and_nowhere_inside` owns where it goes: public functions lock, non-public functions do not, and a public function does not call another public function of the same object. *Gate:* before the critical section is written, `PAT_dont_call_unknown_code_while_holding_a_lock` owns what it may call — a callback, a virtual, or a caller-supplied comparison inside a held lock hands control of your deadlock behaviour to somebody else. **Where the mutex is a raw handle from a C-style interface with no scope-bound guard available, write the guard before writing the critical section**; `AP_give_an_acquired_resource_an_owner` owns that, and a lock is one of the resources it exists for.

8. **Where threads coordinate on counts or phases rather than competing for one thing, that is a different mechanism.** `PAT_choose_between_a_semaphore_a_latch_and_a_barrier` owns the choice by shape of the coordination. Where a condition variable carries it, `PAT_wait_on_a_predicate_not_on_a_notification` owns the rule that makes it correct, and that rule is not optional — a wait without a predicate is a bug that appears as a hang under timing you did not test.

9. **Settle how the work starts and how it ends before the first thread runs.** `PAT_prefer_a_task_to_a_thread_when_work_returns_something` owns the choice when a result or a failure has to come back, and `PAT_specify_the_launch_policy_when_asynchrony_is_required` owns saying so explicitly where the program depends on it actually running. `PAT_make_threads_unjoinable_on_every_path` owns the exits, including the ones an exception takes, and `PAT_stop_a_thread_by_asking_it_rather_than_killing_it` owns early termination. Deciding this last is normal; deciding it after the threads exist is where it gets expensive.

10. **Completion check.** The threads that touch this data are named, and which of them write. Either an escape from the race definition applies or one has been introduced. The unit of atomicity is stated, and the mechanism matches it rather than matching habit. Every rule the chosen mechanism carries has been applied — orderings paired on the atomic route, boundary and callout rules on the lock route. Nothing reached for `volatile` to make a value visible. And every thread has a decided end, reachable on every path out including the exceptional ones.

## Notes
The reason this is a protocol is step 4, and everything before it exists to make step 4 answerable. Naming the unit of atomicity — the thing that must never be observed half-done — decides the mechanism almost by itself, and it is the question that gets skipped, because a mechanism can be chosen from familiarity and will then be defended on its own merits rather than against what the data actually needs. An atomic guarding one of two variables that share an invariant is correct about that variable and wrong about the program.

Steps 5 and 7 are where the protocol earns its cost, because each route carries obligations that arrive with the choice rather than after it. Choosing an atomic is not one decision but four — the order, the pairing, the exchange form, and whether a fence is warranted — and each is silently wrong rather than loudly wrong when got wrong. Choosing a lock brings a boundary rule and a rule about what may be called from inside. An unordered set of concurrency rules lets a reader take the first one and stop, which is how code ends up with a correctly declared atomic carrying a memory order that cannot express what the algorithm needs.

The gate at step 3 is placed before the fork rather than inside a branch on purpose. It is not a choice between mechanisms; it is a wrong turn that removes the question, because a value declared to keep its accesses intact looks to its author like a value that is now safe to share. Putting it after step 4 would let it be reached only by people who had already chosen correctly.
