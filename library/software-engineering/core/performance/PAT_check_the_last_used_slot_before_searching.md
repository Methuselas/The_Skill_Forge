---
object_id: PAT_check_the_last_used_slot_before_searching
object_type: pattern
name: Check the Last-Used Entry Before Searching
library_path:
- software-engineering
- core
- performance
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- locality
- caching
- lookup
- data_structures
cross_links:
- rel: related_to
  target_object_id: PAT_name_the_allocation_pattern_before_choosing_a_strategy
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
- rel: related_to
  target_object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Check the Last-Used Entry Before Searching

## Pattern Rule
**IF** an operation repeatedly searches a collection for the entry that serves the current request, and consecutive requests tend to want the same entry
**THEN** keep a direct reference to the entry that served the previous request and test that one first, falling back to the full search only when it does not match.

## Do
- Keep the hint as a plain reference beside the collection. One reference and one comparison is the entire mechanism, and the comparison is the same test the search would have made anyway.
- Keep a separate hint per distinct kind of request. Where the same collection is searched by two operations with independent locality — one taking, one returning — one shared hint is worse than none, because each operation keeps evicting the other's.
- Size the hint to how many entries are wanted *at once*, not to how many operations do the wanting. Where a fixed, small set of call sites each has its own locality, one hint apiece is the whole answer. Where instead a single call site interleaves requests for several entries — a batch walked in an order nobody chose, a queue mixing work for several keys — the number of live entries is a property of the data rather than of the code, and no arrangement of one-entry hints covers it. That case wants a short most-recently-used list scanned front to back: still a linear scan of a handful of entries, still no index to maintain, and it degrades to the one-entry hint when the working set turns out to be one.
- Read a bad hit rate as a question rather than a verdict. Requests that alternate between a few entries look exactly like requests that do not cluster, and the two want opposite fixes — the first wants a slightly longer hint, the second wants a real index. Count how many distinct entries the misses name before deciding which you have.
- Update the hint on every completed lookup, hit or miss, so a workload that moves to a new entry pays the search once rather than on every request afterwards.
- Invalidate the hint anywhere an entry can be removed, and prefer arranging removal so the hint cannot dangle rather than remembering to clear it at each site.

## Don't
- Don't reach for an index or a map first. Either costs memory and maintenance on every mutation, where a one-entry hint costs a pointer and is often the whole of the available win. A short most-recently-used list sits between them and is the right first move only where the working set is several entries wide and discovered at run time.
- Don't add the hint without evidence that requests cluster. Where consecutive requests are genuinely unrelated it adds a failed comparison to every lookup and removes nothing.
- Don't let the hint become the only path. It is an accelerator over a search that must remain correct on its own, and code that starts assuming the hint is right has stopped having a fallback.
- Don't measure it on a loop that requests the same entry every time. That reports a hit rate no real workload will see; the informative case is a run that moves between entries at the rate the program actually does.

## Checklist
- Do consecutive requests want the same entry often enough to have been measured?
- Is there a separate hint for each operation with its own locality?
- How many distinct entries are wanted at once, and is that number fixed by the code or by the data?
- What happens to the hint when the entry it names is removed?
- Does the code still produce the right answer with the hint forced to miss every time?

## Notes
This works for the same reason caches work at all, applied at the smallest possible size. Programs touch a little of their data at a time, so the entry wanted now is very often the entry wanted a moment ago — and capturing just that costs one reference, where a general cache costs a structure to maintain and invalidate.

It is worth reaching for before anything larger because the ceiling is often close to the same. A structure that turns a linear search into a logarithmic one improves the misses; a hint removes the search entirely on the hits, and where the hit rate is high the hits are nearly all of the traffic. Where the hit rate is low, that is the finding — requests are not clustering, and the fix is a real index rather than a bigger hint.

The per-operation point is the one most often got wrong. Two operations sharing a collection frequently have unrelated locality, and giving them one hint between them produces a hint that is wrong almost every time, which reads as evidence the technique does not work rather than that it was shared.

There is a second version of that same mistake, and it is harder to see because the fix looks like the thing this card warns against. Sizing the hint per operation is only correct while the number of entries in play is a property of the code. Where one call site walks a batch that interleaves requests for several entries, the number in play is a property of the data, and it cannot be recovered by adding hints at call sites — there is only one. The result is the same symptom as an unshared hint used on unclustered requests: a miss rate that looks like proof the locality is not there. It usually is there, spread over a handful of entries rather than concentrated on one, and a most-recently-used list a few entries long recovers nearly all of it while remaining a linear scan with nothing to invalidate. The distinction to hold is between a cache, which is a structure you maintain, and a short list you scan, which is a hint that happens to remember more than one thing.
