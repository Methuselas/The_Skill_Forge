---
object_id: PAT_keep_memory_alive_until_the_compare_and_swap_completes
object_type: pattern
name: Keep the Memory Alive Until the Compare-and-Swap Completes
library_path:
- software-engineering
- core
- concurrency
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- lock_free
- memory_management
- threading
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_publish_shared_data_through_one_atomic_handle
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_buy_concurrent_performance_with_restrictions
- rel: related_to
  target_object_id: PAT_run_threaded_code_under_conditions_built_to_break_it
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Keep the Memory Alive Until the Compare-and-Swap Completes

## Pattern Rule
**IF** a lock-free design reads a pointer and later uses that value in a compare-and-exchange to decide that nothing has changed
**THEN** guarantee the memory at that address cannot be freed between the read and the exchange, because an address that has been recycled makes an unchanged comparison a lie
**ELSE** where nothing in the structure is ever deallocated during its lifetime, the guarantee already holds and no scheme is needed.

## Do
- Recognize the failure by its shape. A pointer moves from one value to another and back again; the thread that only saw the first and the last observes no change, its exchange succeeds, and it installs a value computed from a structure that has since been rearranged. Removing two nodes and adding one is enough — an allocator handing back the most recently freed block is not misbehaving, it is doing the cache-friendly thing.
- Separate removal from deallocation, because only the second one is the problem. A node can be unlinked so nothing can reach it, and the value it held can even be destroyed; what must not happen is the memory being handed to the allocator where another node can be built at the same address.
- Take the application-specific escape when there is one. Where few nodes are ever removed, holding them all on a deferred list until the whole structure is destroyed is trivially correct and costs a bounded amount of memory.
- Use a quiescent period when removals are ongoing. Freed memory accumulates on a garbage list; periodically, operations in progress are allowed to finish and new ones are held off while the list is returned to the allocator. No exchange can then span the collection, so no operation ever meets recycled memory. Read-copy-update is a refinement of this shape, and hazard pointers are a different route to the same guarantee.
- Consider reference-counted handles where the structure's shape allows it. If every pointer into a node keeps it alive — the links between nodes and the ones held by iterators alike — a removed node stays allocated while anyone can still reach it, the new node necessarily lands at a different address, and the stale exchange fails and retries as it should.
- Plan capacity growth as a rare event handled by one thread. Preallocating to a known bound is best; failing that, store in fixed-size blocks so growth links a new block rather than copying the structure, and gate it so one thread grows while the others wait. If growth is not rare, the design should have been a guarded one.

## Don't
- Don't treat a successful comparison as proof that the structure is unchanged. It proves the observed word holds the value it held before — which is a much weaker statement than the code around it usually assumes.
- Don't rely on an allocator not reusing addresses. Reuse of just-freed memory is the normal, deliberate behaviour, and it makes the failure more likely under exactly the conditions that make the structure fast.
- Don't expect weak references to solve the cycles that reference counting creates. In a structure whose nodes point to each other, a weak link breaks the cycle by *not* extending lifetime, which is the one property this needs; those structures need collection or hazard pointers instead.
- Don't assume two atomic pointer updates make a consistent step. Changing one link and then another is two operations, so a doubly linked structure can be observed mid-update, where following a link forward and back does not return you where you started.
- Don't validate this by testing alone. Races here occur in narrow windows; a race detector reports what *could* have raced rather than what happened to, and in a small test that difference is most of the defects.

## Checklist
- Which pointer values does this design read and later feed to a compare-and-exchange?
- Between those two moments, what stops the memory at that address being freed and reused?
- Are removal and deallocation separated, with a stated point where deallocation becomes safe?
- If reference counting is used, can the structure form a cycle?
- Has this run under a race detector as well as a functional test?

## Notes
The root cause is worth stating in one line because it explains every fix: once memory can be recycled, an address no longer identifies the data that was at it. Every solution — deferred deallocation, quiescent collection, hazard pointers, reference-counted handles — is the same guarantee reached differently, and choosing between them is a question of how many removals happen and what the structure's shape permits.

Making nodes outlive their removal has a second benefit that is easy to overlook and often larger than the fix itself: traversal becomes safe without locking. An iterator holding a counted reference stays valid through insertions and removals anywhere in the structure, so searches and modifications run concurrently. Against a guarded structure that must hold its lock for the whole traversal, that is not a marginal gain — the advantage grows without limit as the structure gets longer.

Accepting this means accepting that a traversal may visit nodes no longer reachable from the root, and that there is no meaningful notion of the structure's current contents. Nothing can be learned about it except by walking it, and by the time the walk ends the earlier part may have changed. That is a property of concurrent structures rather than a defect in any one of them, and designs that quietly assume otherwise are the ones that fail.
