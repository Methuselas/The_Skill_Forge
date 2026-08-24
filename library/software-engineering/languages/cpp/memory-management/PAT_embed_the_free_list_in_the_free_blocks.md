---
object_id: PAT_embed_the_free_list_in_the_free_blocks
object_type: pattern
name: Embed the Free List in the Free Blocks
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- allocator
- alignment
- data_structures
cross_links:
- rel: related_to
  target_object_id: PAT_reach_for_a_custom_allocator_only_for_what_it_can_buy
- rel: related_to
  target_object_id: PAT_name_the_allocation_pattern_before_choosing_a_strategy
- rel: related_to
  target_object_id: PAT_follow_new_delete_conventions
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Embed the Free List in the Free Blocks

## Pattern Rule
**IF** you are managing a pool of equally sized blocks and need to track which of them are free
**THEN** keep the free list inside the free blocks themselves — each one holding the index of the next free block in its own first bytes — because the contents of a block belong to you until the moment you hand it out.

## Do
- Hold one index in the pool's header, naming the first free block, and let each free block name the next. Taking a block reads its stored index into the header; returning one writes the header's index into the block and points the header at the block. Both are a handful of instructions with no search.
- Write the chain once when the pool is initialized, so every block starts out pointing at its successor and the whole pool is one list from the first use.
- Choose a byte-sized index. It has no alignment requirement, so it can sit at the front of a block whatever the block's own size and alignment are, and reading it through a character pointer is always defined.
- Accept the block count the index width implies rather than widening it. A byte caps a pool at a couple of hundred blocks, which is a cap on one pool and not on the allocator, because more pools cost only their own headers.

## Don't
- Don't keep a parallel array or bitmap of free flags. That is exactly the per-block bookkeeping the technique exists to remove, and it costs cache traffic on a structure that is otherwise touched only at its head.
- Don't widen the index to fit more blocks in one pool. A wider integer needs suitable alignment, so casting a block's address to it is undefined for blocks that are not aligned for it, and it imposes a minimum block size equal to its own — fatal for a pool whose whole purpose is small blocks.
- Don't read or write a block's stored index after handing it out. The bytes are the caller's from that instant, and the list is intact only because the two uses never overlap in time.
- Don't hand this a pointer it did not give out. Nothing in the arrangement can tell a foreign pointer from one of its own, and returning the wrong one corrupts the chain rather than reporting an error.

## Checklist
- Is the per-block overhead of the free list actually zero, or is there a side structure I have not counted?
- Can the index type sit at the front of every block without an alignment assumption?
- Does the smallest block this pool must serve still fit an index?
- Are allocation and release both free of any search?

## Notes
The insight is that free memory is memory you own. A block awaiting a caller has no contents anyone can observe, so storing bookkeeping there costs nothing that was not already spare — the list is free in space and constant in time, which is a combination the usual side-table arrangement cannot reach.

The index-width decision is where this is usually got wrong, and the two failures pull in opposite directions. Widening the index buys more blocks per pool and costs both an alignment assumption and a floor under the block size; narrowing it costs pool capacity and buys freedom from both. For small blocks the narrow choice is right, and the resulting cap is not the constraint it appears to be, since the layer above simply holds more pools.

This is the structure underneath most pool and slab allocators, and it is the reason they can report near-zero metadata overhead while still answering in constant time. It also explains their characteristic failure: a double release, or a release of a pointer from elsewhere, does not fault — it links a block into the chain twice and hands the same memory to two callers later on.
