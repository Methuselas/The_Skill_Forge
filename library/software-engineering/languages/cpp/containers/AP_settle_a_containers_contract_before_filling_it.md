---
object_id: AP_settle_a_containers_contract_before_filling_it
object_type: ap
name: Settle a Container's Contract Before Filling It
library_path:
- software-engineering
- languages
- cpp
- containers
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- containers
- data_structures
- ownership
- api_design
cross_links:
- rel: supports
  target_object_id: PAT_decide_what_a_container_holds
- rel: supports
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
- rel: supports
  target_object_id: PAT_use_a_sorted_sequence_when_lookups_dominate
- rel: supports
  target_object_id: PAT_avoid_the_packed_bool_specialization
- rel: supports
  target_object_id: PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering
- rel: supports
  target_object_id: PAT_tell_equality_from_equivalence_when_looking_up
- rel: supports
  target_object_id: PAT_reserve_capacity_up_front_and_release_it_deliberately
- rel: supports
  target_object_id: PAT_encapsulate_the_container_choice_instead_of_abstracting_over_it
- rel: supports
  target_object_id: PAT_prefer_the_checked_element_accessor_by_default
- rel: supports
  target_object_id: PAT_recover_the_iterator_from_erase_rather_than_advancing_it
- rel: supports
  target_object_id: PAT_hand_container_data_to_a_c_api_as_a_pointer_and_a_count
- rel: related_to
  target_object_id: AP_give_an_acquired_resource_an_owner
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted C++ sources
confidence: medium
references: []
variants: []
---

# Settle a Container's Contract Before Filling It

## Objective
Given a piece of data that has to live somewhere, decide where it lives and on what terms, before any code stores anything in it. Success is that the element type, the container, the ordering, the sizing, the visibility of the choice, and the access idioms were each decided once and deliberately — rather than discovered later by a crash, a silent duplicate, or a rewrite. Not a survey of every container; a sequence of decisions where each one needs the previous one settled.

## Steps / Flow

**Entry state.** You have data and no home for it yet, or you are reviewing a home somebody else chose. If you cannot yet say what will be done to this data most often, you are not ready to choose — step 1 exists to get you there, and choosing first is how a structure ends up optimal for an operation nobody performs.

1. **Write down the operations and roughly how often each happens.** Lookup, insertion, traversal in order, erasure from the middle, erasure from the end. Everything downstream is decided against this list, and it is cheap to write and expensive to skip. A structure chosen before the list is a guess wearing a justification.

2. **Decide what the container holds before deciding which container holds it.** `PAT_decide_what_a_container_holds` owns this: the container copies and moves its elements at moments you neither write nor see, so the element's copying must be cheap, correct and conventional — and where it is not, the container holds an owning handle rather than the object. **Where the elements are pointers or handles to something allocated elsewhere, the question this raises is who releases them, and that is usually not answerable from the container's own declaration.** Go and read the call sites; the answer lives there, and getting it wrong produces either a leak or a use-after-free rather than a compile error. `AP_give_an_acquired_resource_an_owner` owns the release once you know who owes it.

3. **Choose the container on the axes complexity says nothing about.** `PAT_choose_a_container_on_more_than_algorithmic_complexity` owns the list: whether elements stay where you put them, which iterator category the code requires, whether existing elements may move, what survives an insertion or erasure, whether the storage must be readable by a C interface, and whether a multi-element insertion has to be able to roll back. Big-O is the axis everyone remembers and rarely the one that decides.

4. *Branch.* **Where the operation list separates into phases, the ordered associative container may not be the answer.** A build-up that is nearly all insertion, then a working period that is nearly all lookup, is not the interleaved workload a tree exists for. `PAT_use_a_sorted_sequence_when_lookups_dominate` owns that case and the conditions under which it does not apply.

5. *Gate.* **If the element type is boolean, resolve that before going further.** The standard's growable sequence specialized on the boolean type does not hold what it says it holds, and the decision is not stylistic. `PAT_avoid_the_packed_bool_specialization` owns the objection, and owns the narrow case in which that representation is nevertheless the right choice.

6. *Gate.* **If the container is ordered, its comparison is a contract, not a detail.** `PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering` owns the requirement that nothing precedes itself, which is the one people break. Then `PAT_tell_equality_from_equivalence_when_looking_up` owns the consequence: the container answers questions of sameness by equivalence under its ordering while the free-standing search algorithms answer by equality, and for any ordering that ignores part of the value those two give different answers. Settle which notion this data needs while the ordering is still being chosen.

7. **Size it before filling it, and decide separately how it gives memory back.** `PAT_reserve_capacity_up_front_and_release_it_deliberately` owns both halves, and they are separate acts: growth proceeds by reallocations that invalidate everything pointing into the container, and removing elements never returns any memory at all.

8. **Decide who else can see the choice.** `PAT_encapsulate_the_container_choice_instead_of_abstracting_over_it` owns this, and its point is worth stating plainly: you cannot make your own code independent of the container you picked, but you can make your clients' code independent of it. Deciding this after clients exist means changing them.

9. **Settle the access and mutation idioms once, here, rather than at each call site.** `PAT_prefer_the_checked_element_accessor_by_default` owns reading; `PAT_recover_the_iterator_from_erase_rather_than_advancing_it` owns removal during traversal, including the case where the container's erase returns nothing to recover; `PAT_hand_container_data_to_a_c_api_as_a_pointer_and_a_count` owns handing the storage outward. A decision made once here is a convention; the same decision made at forty call sites is forty chances to differ.

10. **Completion check.** The operation list exists and is written down. The element type's copying is cheap and correct, or the container holds a handle and the release has a named owner. The container choice can be defended on an axis other than complexity. Any ordering supplied is a strict weak ordering. Capacity is set where the size was predictable. The choice is either hidden behind an interface or deliberately exposed. And the access, erase and handoff idioms are stated once rather than left to each caller.

## Notes
The reason this needs a protocol is that the fifteen rules it orchestrates are individually clear and jointly unordered, and the order is where the cost lives. Choosing the container first and the element type second is the common sequence and the wrong one: what the container holds constrains which containers are even eligible, because a type that is expensive or incorrect to copy rules out every structure that relocates its elements. Reversing those two steps produces a choice that has to be revisited once the element type is settled.

Step 2's second half is the one most often skipped and the most expensive when it is. A container of raw pointers or handles states nothing about who releases them — not in its declaration, not in its type, and frequently not in the header at all. The answer is at the call sites and nowhere else, and the failure mode is not a compile error but a leak or a use-after-free discovered much later. Treat a container of anything that needs releasing as an unfinished ownership decision until a call site has been read.

The gates at steps 5 and 6 are gates rather than steps because both admit a wrong answer that compiles and runs. A packed boolean sequence behaves correctly right up until something takes an element's address or hands the storage to generic code; a comparison that reports a value as preceding itself corrupts an ordering rather than reporting an error. Neither announces itself, which is why both are settled before the container is filled rather than after something misbehaves.
