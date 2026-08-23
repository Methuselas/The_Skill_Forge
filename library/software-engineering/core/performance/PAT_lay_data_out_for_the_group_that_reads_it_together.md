---
object_id: PAT_lay_data_out_for_the_group_that_reads_it_together
object_type: pattern
name: Lay Data Out for the Group That Reads It Together
library_path:
- software-engineering
- core
- performance
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- performance
- memory
- gpu
- data_layout
- concurrency
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_keep_a_lockstep_group_on_one_path
- rel: related_to
  target_object_id: PAT_budget_per_thread_resources_against_residency
- rel: related_to
  target_object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
- rel: related_to
  target_object_id: PAT_separate_per_thread_data_by_a_cache_line
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Lay Data Out for the Group That Reads It Together

## Pattern Rule
**IF** a group of threads executes in lockstep and issues its memory accesses at the same instant, on hardware that serves memory in fixed-size aligned units
**THEN** choose the mapping from thread index to address so the group's simultaneous accesses fall into as few of those units as possible, because the cost is the number of distinct units touched rather than the number of threads asking
**ELSE** where threads access memory independently over time rather than together in a group, the ordinary locality reasoning applies instead and this does not.

## Do
- Count units, not accesses. The hardware fetches a fixed-size aligned span and serves every request that lands inside it from that one transaction. Thirty-two threads reading thirty-two adjacent values may cost one transaction; the same thirty-two threads reading values spread across memory cost thirty-two. The work done is identical and the memory traffic differs by that factor.
- Recognise that this is the same decision as keeping a group on one control path, made about data instead of branches. Both are consequences of the index-to-data mapping, both are invisible in the source, and a mapping chosen to make one good usually makes the other good too — which is why the layout question belongs with the decomposition rather than after it.
- Turn a collection of records into a collection of fields when threads each want the same field. If thread *i* reads one member of record *i*, and records are large, every thread lands in a different unit and the group pays the maximum. Storing each member as its own array makes the group's reads adjacent and collapses the transaction count — the same data, reorganized against who reads it simultaneously.
- Align collections to the unit boundary and keep elements from straddling it. A span that begins partway into a unit costs an extra fetch for the same data, and an element crossing a boundary is served by two transactions instead of one. Both are free to fix at allocation time and expensive to notice later.
- Apply the identical reasoning to fast scratch memory, where the partitioning is interleaved rather than contiguous. Such memory is typically divided into banks by address, so a group whose threads hit distinct banks proceeds at once, while several threads hitting different addresses in one bank are serialized — the worst case being every thread in the group waiting on a single bank. The unit here is the bank rather than the block, and the same mapping question decides it.
- Break a bad stride by padding rather than by rewriting the access. Where a group's threads access a two-dimensional tile down a column, a row length that shares a factor with the number of banks puts every thread on one bank. Widening each row by one element shifts the mapping so the same loop touches every bank instead — a change to the declaration, not to the algorithm.
- Take the free case where several threads want the same address. Reading one location that many threads need is usually broadcast at no extra cost, so shared constants and lookup values are not the problem they appear to be; it is distinct addresses within one partition that serialize.
- Measure before restructuring, and expect this to outrank most other tuning on such hardware. Memory behaviour is more often the limit than control flow or resource pressure, so it is the first of the three to examine, not the last.

## Don't
- Don't reason about one thread's access pattern in isolation. A loop that looks perfectly sequential from a single thread's point of view can be the worst possible pattern for the group, because what matters is where the *simultaneous* accesses land and that is a property of the mapping, not of the loop.
- Don't assume a layout that is good for a cache is good here. Sequential access over time lets a cache amortize a fetch across many uses; simultaneous access needs the addresses to be close *at one instant*. The two coincide often enough to be misleading and are not the same requirement.
- Don't leave the record-of-fields decision to convenience. Grouping related values into one record is the natural way to model data and the wrong layout when threads want one field each — and the modelling instinct is strong enough that this survives review.
- Don't treat writes to one location by several threads as harmless because nothing serialized. Where the hardware permits it without a conflict, one write still wins and which one is undefined; the absence of a performance penalty is not the absence of a race.
- Don't tune the layout for a unit size read off one device. The span the hardware fetches, and the number of banks, vary by generation — so a padding constant or a tile width tuned to today's device is a value to derive rather than embed.

## Checklist
- For one instruction, where do the group's simultaneous accesses land, and how many distinct units is that?
- Does each thread want the same field of a different record, and would separating the fields help?
- Do collections start on a unit boundary, and does any element straddle one?
- For scratch memory, does the access stride put multiple threads on one bank?
- Would padding a row or tile change that stride?
- Are the unit size and bank count derived from the device or assumed?

## Notes
The counting rule is the whole idea and it is easy to state and easy to forget: cost is the number of distinct units the group touches. Everything else — separating records into fields, aligning collections, padding a row to break a stride — is a way of lowering that count. Holding the rule rather than the recipes is what lets you recognise the situation on hardware whose specifics differ from the one you learned on.

The reason this deserves attention alongside control flow is that they share a cause and are usually fixed together. Divergence and scattered access are both determined by how thread indices map onto data; a mapping that assigns contiguous work to contiguous threads tends to keep groups on one path *and* keep their accesses in one unit, while a mapping that interleaves by some property tends to break both. That makes the mapping a single decision with two large consequences, and it belongs where the decomposition is designed rather than in a later tuning pass.

The trap worth naming explicitly is that single-threaded intuition is not merely incomplete here, it can be exactly inverted. A stride that walks memory in order looks ideal by every habit formed on ordinary processors, and if consecutive threads are given consecutive *rows* rather than consecutive *elements*, that same orderly-looking loop has every thread in the group reading from a different unit at every step. Nothing in the source distinguishes it from the good version.
