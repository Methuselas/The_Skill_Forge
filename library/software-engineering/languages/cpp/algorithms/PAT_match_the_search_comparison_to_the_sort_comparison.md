---
object_id: PAT_match_the_search_comparison_to_the_sort_comparison
object_type: pattern
name: Match the Search Comparison to the Sort Comparison
library_path:
- software-engineering
- languages
- cpp
- algorithms
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- algorithms
- sorting
- undefined_behavior
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_weakest_ordering_operation_that_does_the_job
- rel: related_to
  target_object_id: PAT_tell_equality_from_equivalence_when_looking_up
- rel: related_to
  target_object_id: PAT_use_a_sorted_sequence_when_lookups_dominate
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Match the Search Comparison to the Sort Comparison

## Pattern Rule
**IF** you are calling an algorithm that requires its input already ordered — a binary search, a bound query, a set operation, a merge, a containment test
**THEN** confirm the range really is ordered, and that the comparison you hand the algorithm is the same one the range was ordered by, because these algorithms take both as a promise and check neither
**ELSE** where the range came from an ordered associative container, it is ordered by that container's own comparison and the same one is what you must supply.

## Do
- Know why the requirement exists, since it makes the list easy to reconstruct instead of memorize: every one of these algorithms trades the ordering promise for speed. The searches give logarithmic comparisons, the set operations and the merges give linear time — none of which is achievable on an unordered range.
- Pass the comparison explicitly to the search whenever the range was ordered by anything other than the default. A range put in descending order and then searched with the default comparison is the canonical instance, and it is undefined rather than merely wrong.
- Watch for the two algorithms that merely *prefer* ordered input rather than requiring it. Collapsing adjacent duplicates is well defined on any range, and only does what people usually intend — remove every duplicate — when equal elements are already adjacent, which is what ordering achieves.
- Note which notion of sameness each family uses, because it differs. The algorithms requiring ordered input decide sameness by the ordering, the way the ordered containers do; the duplicate-collapsing ones decide it by equality unless you hand them a predicate saying otherwise.
- Expect logarithmic *comparisons* rather than logarithmic *time* when the iterators are not random access. A binary search over a linked list still halves the candidate set each step, and still takes linear time getting from one candidate to the next.

## Don't
- Don't rely on a diagnostic. Violating an iterator-category requirement fails to compile, which is inconvenient and safe; violating the ordering requirement compiles, runs, and returns answers that are wrong in ways that depend on the data.
- Don't assume "sorted" is a property of the range alone. A range is sorted with respect to some comparison, and two ranges of the same elements can both be sorted under comparisons that disagree entirely — by ascending value, by descending value, by one field, by another.
- Don't hand these algorithms a comparison that differs from the sorting one in any respect, including strictness. A comparison that reports equal values as ordered breaks these for the same reason it breaks an ordered container.

## Checklist
- Was this range ordered, and by which comparison?
- Is that same comparison being passed to the search or set operation?
- If the default comparison is being relied on, was the range ordered by the default?
- For duplicate collapsing, are equal elements actually adjacent?
- Does the iterator category deliver the complexity the algorithm advertises?

## Notes
The eleven or so algorithms in this family are best remembered by what they buy rather than by name. Binary searching and the bound queries buy logarithmic comparisons; the four set-theoretic operations and the two merges buy linear time; the containment test buys linear time. In each case the ordering is the price, and it is paid by the caller because the algorithm cannot afford to verify it — checking would cost as much as the ordering saves.

The failure mode is the same shape as a broken comparison inside an ordered container: an invariant the code depends on is not held, nothing notices, and every operation downstream navigates a structure that is not what it claims to be. What makes this version harder to spot is that the invariant lives in a plain sequence with nothing to enforce it, so there is no type carrying the promise and no constructor to establish it.

The descending-order trap is worth carrying as a specific instance. Ordering a sequence with a reversing comparison and then searching it with the default is a two-line bug where each line is individually correct and reads correctly, and only the pairing is wrong.
