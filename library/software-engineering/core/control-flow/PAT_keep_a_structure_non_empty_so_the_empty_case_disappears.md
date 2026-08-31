---
object_id: PAT_keep_a_structure_non_empty_so_the_empty_case_disappears
object_type: pattern
name: Keep a Structure Non-Empty So the Empty Case Disappears
library_path:
- software-engineering
- core
- control-flow
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- control_flow
- data_structures
- invariants
- special_cases
cross_links:
- rel: related_to
  target_object_id: PAT_make_misuse_impossible_by_removing_invalid_states
- rel: related_to
  target_object_id: PAT_trade_a_branch_for_unconditional_work
- rel: related_to
  target_object_id: PAT_model_an_unknown_end_as_a_sentinel_rather_than_a_position
- rel: related_to
  target_object_id: PAT_choose_the_control_construct_that_fits_the_data
confidence: medium
references: []
variants: []
---

# Keep a Structure Non-Empty So the Empty Case Disappears

## Pattern Rule
**IF** you are writing the insert, remove, or traversal operations of a linked structure and finding that each one opens with a test for empty, or for first, or for last
**THEN** give the structure a permanently present node that belongs to no caller, so the container is never empty and every operation becomes the same unconditional sequence of writes
**ELSE** where the structure is a value that gets copied, serialized, or compared, the permanent node has to be excluded from all three, and that exclusion is usually more special-casing than it removed.

## Do
- Count the branches before deciding. The technique pays when the same emptiness test appears in several operations; on a structure with one insert and one traversal it adds a node and buys almost nothing.
- Make the permanent node point at itself when the structure holds nothing. Emptiness then has a definition a reader can check in one line — the node's forward link is the node — instead of a null that every operation must anticipate.
- Write insertion and removal as unconditional link updates. With no empty case and no ends, both become the same four pointer writes regardless of where in the structure they happen, and there is no arm of a conditional that is exercised only by the first or last element.
- Say in the type what the permanent node is for, because it is the one member whose purpose is not visible from its declaration. A reader who mistakes it for real data will write a traversal that returns it.
- Terminate traversals on identity with the permanent node rather than on null. That is the loop condition the structure actually has, and writing it as a null test is how the permanent node ends up being handed to a caller.
- Keep the node's payload unread rather than merely unset. A permanent node holding a plausible-looking zero is one bug away from being treated as an element; one whose payload is never read cannot be.

## Don't
- Don't reach for it to remove a branch you have not counted. This buys states, not speed — the payoff is fewer arms of fewer conditionals to get wrong, and a card about branch elimination for pipeline reasons is answering a different question with a different prerequisite.
- Don't forget that it converts a crash into silence, which is the cost that matters and the one nobody prices. Unlinking a node twice from a null-terminated structure tends to fault on the second attempt; from a self-linked one it quietly leaves the forward chain and the backward chain disagreeing, and the disagreement surfaces later, somewhere else, as a value that never updates. Decide whether you would rather have the fault.
- Don't let the permanent node escape. Every accessor that can return a node needs to be checked against the case where the structure is empty and the only node present is the one that is not an element.
- Don't apply it to a structure that gets copied. A copy constructor now has to build a new permanent node rather than copy the old one, equality has to skip it, and serialization has to omit it — three special cases in place of the one that was removed.
- Don't assume the invariant survives contact with the rest of the program. "Never empty" is only true while every path that removes an element maintains it, and the technique's whole value is that no operation checks.

## Checklist
- How many operations currently open with a test for empty, first, or last?
- Is emptiness expressible as one identity comparison after the change?
- Does any accessor have a path on which the permanent node reaches a caller?
- What happens now on a double removal that previously would have faulted?
- Is this structure ever copied, compared, or serialized?
- Would a reader of the type know which member is not an element, and why?

## Notes
The reason this is worth stating separately from the general advice to remove special cases is that the mechanism is unusual: nothing about the operations changes, and the branches disappear because the state they tested for was made unreachable. Most special-case removal works the other way round, by handling the case better. Here the case stops existing, and the code that would have handled it is not simplified so much as deleted.

The name is unfortunate and worth separating from its neighbour. A sentinel *value* — a number or pointer standing in for absence inside the range of ordinary values — is a thing this library warns about repeatedly, because a reader cannot tell it from data and a caller can forget to check it. A permanently present *node* is close to the opposite: it exists so that absence never has to be represented at all, and the value it holds is never read. The two share a word and almost nothing else, which means the word is not a reliable way to find either.

The cost belongs in the decision rather than in a footnote, because it is genuinely two-sided. A structure with no empty state also has no state that faults when an operation is performed twice, so a class of double-unlink and double-free error that would have announced itself immediately becomes a quiet inconsistency between two views of the same structure. That is not an argument against the technique — the invariant is cheap to hold and the alternative is a test in every operation — but it does mean the removal path deserves the scrutiny that was saved elsewhere, and it is the reason a structure using this benefits from an idempotent removal more than one that does not.
