---
object_id: PAT_mark_a_node_removed_before_unlinking_it
object_type: pattern
name: Mark a Node Removed Before Unlinking It
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- concurrency
- data_structures
- lock_free
- invariants
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_search_without_locks_then_lock_and_validate
- rel: related_to
  target_object_id: PAT_keep_memory_alive_until_the_compare_and_swap_completes
- rel: related_to
  target_object_id: PAT_give_every_operation_one_instant_where_it_takes_effect
- rel: related_to
  target_object_id: PAT_make_every_concurrent_operation_a_complete_transaction
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Mark a Node Removed Before Unlinking It

## Pattern Rule
**IF** removing an element from a shared structure means detaching it while other threads may be traversing through it
**THEN** make removal two steps — set a flag on the element saying it is no longer part of the structure, and only afterwards detach it — and let every reader treat a flagged element as absent
**ELSE** where removal is rare and readers already exclude removers, one step is correct and the flag is state to maintain for nothing.

## Do
- Make the flag the moment of removal, and the detaching an afterthought. The element leaves the structure when it is marked; unlinking it is cleanup that can happen later, be done by another thread, or be batched. That reordering is the whole idea and everything below follows from it.
- State the invariant the flag creates, because it is what makes the design checkable: everything not marked is reachable. A reader that traverses to an element and finds it unmarked can conclude it is genuinely present, without confirming anything else.
- Collect the cheap validation this buys. Where confirming a position previously meant traversing the structure again to prove it was still attached, it now means reading a flag — so an optimistic operation stops paying for a second traversal, which is usually what made the optimistic version not worth it.
- Let read-only traversal stop taking locks entirely, and notice what that gains. A search becomes: walk to the position, report present if what you find is unmarked. It excludes nobody, blocks on nothing, and completes in a bounded number of steps — so the operation that usually dominates the workload gets the strongest progress guarantee while modifications stay simple and blocking.
- Keep traversal correct across marked elements. Readers walk *through* marked elements rather than around them, so a marked element must keep leading onward correctly until it is detached — its outgoing links stay valid, and its ordering position stays where it was.
- Fix where the removal takes effect and write it down: at the marking step, not the unlinking. This is the operation's committing instant, and a reviewer looking at the unlink will find the wrong one and conclude the design is racy.
- Keep the two steps of one removal atomic with respect to each other, or accept that another thread may find a marked but still-attached element. Usually that is fine and is precisely what makes the design tolerant of delay — but it must be a decision, since it means the structure is routinely in a state the sequential version never has.
- Recognize the same move under other names. A tombstone in a store that is cleaned up later, a soft-delete flag with a separate purge, and a record retired from an index before its space is reused are all this, and they are all trading a prompt physical removal for a cheap logical one.

## Don't
- Don't leave the physical removal to nobody. A structure that only ever marks fills with marked elements, and traversals slow steadily in a way that looks like a leak and is one — someone must eventually detach them, whether the next writer through, a background pass, or a threshold-triggered sweep.
- Don't let a marked element be found by anything that reports it as present. Every path that answers a question about membership has to consult the flag, and one that forgets is a resurrection bug: an element that was removed comes back on some code paths and not others.
- Don't confuse this with knowing when the memory can be released. Marking says the element has left the structure; it says nothing about whether a thread is still holding a reference to it, and the reclamation question is separate and harder.
- Don't mark and unlink in the belief that this alone makes the structure nonblocking. Readers get a strong guarantee out of it; modifications still take locks and can still be delayed, and reaching a nonblocking structure needs the marking and the link update to be one atomic step, which costs more.
- Don't apply it where readers can afford to be excluded. The complexity buys concurrent readers, and where reads are rare or already synchronized, one-step removal is simpler and has no invariant to maintain.

## Checklist
- Is the element considered removed at the marking step, and is that written down?
- Does every membership question consult the flag?
- Who performs the physical detachment, and what triggers it?
- Can a traversal pass safely through a marked element and continue correctly?
- Is a marked-but-attached element a state the design intends?
- What decides when the element's memory can actually be released?

## Notes
The reason this pays is that it converts an expensive question into a cheap one. Asking whether an element is still part of a structure normally means examining the structure — following it from the start and seeing whether you arrive. Putting a flag on the element itself replaces that with a single read at the place you already are. Everything the design is known for follows from that substitution: validation stops needing a traversal, and readers stop needing locks because they no longer need to establish reachability.

It is worth being precise that this creates a state the sequential structure never has — an element that is logically gone but physically present, visible to any thread walking past. That is not a flaw being tolerated; it is what makes the design robust to threads being delayed, since a slow remover leaves the structure correct rather than half-updated. But it does mean the representation no longer maps one-to-one onto the abstract value, and everyone reasoning about the structure needs the mapping stated: an element is present exactly when it is reachable and unmarked.

The relationship to memory reclamation is the thing most often conflated, and the two are genuinely separate steps. Marking removes an element from the structure. Unlinking makes it unreachable to new traversals. Neither tells you that no thread is still standing on it, which is a third question with its own machinery. A design that treats "unlinked" as "safe to free" has skipped the step that matters, and the failure it produces surfaces as memory corruption far from the removal.
