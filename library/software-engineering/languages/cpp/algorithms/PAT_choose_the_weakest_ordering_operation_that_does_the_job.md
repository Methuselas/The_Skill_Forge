---
object_id: PAT_choose_the_weakest_ordering_operation_that_does_the_job
object_type: pattern
name: Choose the Weakest Ordering Operation That Does the Job
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
- performance
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering
- rel: related_to
  target_object_id: PAT_use_a_sorted_sequence_when_lookups_dominate
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Choose the Weakest Ordering Operation That Does the Job

## Pattern Rule
**IF** you need elements arranged — the best few, the element at a given rank, a split into those meeting a criterion and those not, or a genuine total order
**THEN** name the operation that produces exactly that and no more, because the library offers a graded set and the weaker ones cost less while saying more clearly what you actually wanted
**ELSE** where you truly need every element in order and equal elements must keep their original relative positions, the stable full sort is the strongest of them and the right answer.

## Do
- Match the operation to the requirement rather than reaching for the full sort by reflex. Splitting a range by a predicate needs a partition; finding the element at a rank, or the best few in no particular order, needs the selection operation; the best few *in order* needs the partial sort; everything in order needs the full sort.
- Use the selection operation for more than the top few, since it generalizes better than its name suggests. Positioning the middle element gives you the median; positioning at a computed offset gives you any percentile.
- Reach for the stable variants only when equal elements must retain their relative order, and know which exist: the full sort and the partition have stable counterparts, the partial sort and the selection operation do not.
- Check the iterators the operation demands against the container you have. The sorting and selection operations need random access, so they do not apply to linked lists; partitioning needs only bidirectional iterators and works on any standard sequence.
- Go indirect when a linked list needs an operation it cannot support — copy into a random-access container, or build a container of iterators into the list and order that.

## Don't
- Don't choose among these on performance grounds. Choose on what the job needs, and the performance follows, because the operation that does only what you asked is generally both the clearest statement of intent and the cheapest way to get it.
- Don't expect any of the weaker operations to say anything about elements it did not have to order. The selection operation guarantees only that the element at your position is the one that belongs there and that nothing before it follows it in the ordering — the arrangement within those groups is not yours to predict.
- Don't sort a container that maintains its own ordering. The ordered associative containers are sorted at all times by construction, and applying a sorting operation to one is at best redundant.

## Checklist
- What exactly does the code downstream require — a total order, a rank, a group, or a split?
- Does anything depend on equal elements keeping their original relative positions?
- Does the container supply the iterator category the chosen operation requires?
- Is a full sort being used where a partition or a selection would answer the question?

## Notes
The graded set, ordered by the work each does, runs: partition, stable partition, selection by rank, partial sort, sort, stable sort. That ordering is worth knowing not to optimize by but to recognize how much of the set sits *below* the full sort — which is where most code lands by default.

The reason the advice is to choose by need rather than by cost is that the two agree here, and that is unusual enough to be worth relying on. Asking for a split when you need a split produces code that reads as a split and happens to be the fastest way to get one; asking for a full sort produces code whose reader has to work out that only the partition mattered.

Selection by rank is the operation most often overlooked, largely because its name describes its mechanism rather than its use. Read it as "put the element that belongs at this position at this position, and divide the rest around it" and its three applications — top n, median, percentile — all fall out of the same call.
