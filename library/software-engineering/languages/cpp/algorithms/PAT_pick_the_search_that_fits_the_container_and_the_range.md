---
object_id: PAT_pick_the_search_that_fits_the_container_and_the_range
object_type: pattern
name: Pick the Search That Fits the Container and the Range
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
- containers
- lookup
- efficiency
cross_links:
- rel: related_to
  target_object_id: PAT_tell_equality_from_equivalence_when_looking_up
- rel: related_to
  target_object_id: PAT_match_the_search_comparison_to_the_sort_comparison
- rel: related_to
  target_object_id: PAT_remember_an_algorithm_cannot_change_a_containers_size
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Pick the Search That Fits the Container and the Range

## Pattern Rule
**IF** you are looking something up and the container offers a member function with the same name as a free-standing algorithm
**THEN** take the member, because on an ordered associative container it searches in logarithmic rather than linear time, decides sameness the way the container does, and on a keyed container looks at keys rather than whole entries
**ELSE** where the range is an ordinary sequence with no such member, choose among the free-standing operations by whether the range is ordered and by what you actually need to know.

## Do
- Route the decision through two questions in order — is there a member function of this name, and is the range ordered — because between them they settle almost every case. A member exists, take it; no member and the range is ordered, use the bound or range-of-equivalents operations; no member and unordered, use the linear ones.
- Ask for exactly what you need to know from an ordered range. Whether the value is present at all is a membership test; where it would go is a lower bound; the whole run of matching elements is the range-of-equivalents operation, which is also the one that tests sameness the way an ordered container does rather than tempting you back into equality.
- Test membership in a unique-keyed container by counting, which reads as a membership test and is idiomatic there. In a container permitting duplicates, prefer finding, because it can stop at the first match while counting must in the worst case examine everything.
- Use a lower bound, not a find, when you need the *first* element with a value in a container permitting duplicates. Finding is only required to locate one of them, not the first — and having done so, complete the equivalence check yourself to confirm what you landed on.
- Extend the same preference past searching. A linked list's own removal, uniquing, sorting, and merging members manipulate node links instead of copying elements, and its removal members genuinely remove rather than compacting and leaving a tail behind.

## Don't
- Don't reach for the free-standing search on an ordered associative container. It walks the range linearly, and it decides sameness by equality where the container decides by its ordering — so it can fail to find something the member finds, and the two disagreeing is not a bug in either.
- Don't use the free-standing search on a keyed container and expect it to look at keys. Those containers hold key-and-value entries, and an algorithm knows nothing about that structure, so it compares whole entries where every member function compares keys alone.
- Don't assume the member and the algorithm agree about what they modify. A linked list's merge changes the lists it operates on, while the free-standing merge is not permitted to alter its sources.

## Checklist
- Does this container have a member function with the name you were about to call?
- Is the range ordered, and by which comparison?
- Are you asking whether something is present, where it belongs, or which elements match?
- If duplicates are possible and you need the first match, is a lower bound being used rather than a find?
- Is the container keyed, and does the search look at keys or at whole entries?

## Notes
The three advantages of the member version on an ordered associative container are worth separating, because only the first is about speed. Logarithmic rather than linear time is the one people cite. Deciding sameness by the container's ordering rather than by equality is the one that changes *answers* rather than timings. Looking at keys rather than whole entries is the one that makes keyed containers usable at all without contortions.

The performance figures are worth a moment for scale. Searching a million-element ordered container takes at most thirty-eight comparisons on the red-black trees implementations typically use, and usually no more than twenty-two; a linear search over the same container averages five hundred thousand. Implementations use red-black trees rather than perfectly balanced ones — which would cap the count at twenty-one — because the balanced version's overall performance is worse despite the better bound.

For the linked list the story is almost entirely about copying. The complexity of the member and the algorithm match; the member manipulates pointers between nodes while the algorithm assigns elements around, so the member wins by as much as copying an element costs. The behavioural differences alongside that — really removing, and modifying the sources of a merge — matter more than the speed does.
