---
object_id: PAT_look_for_hot_data_when_there_is_no_hot_code
object_type: pattern
name: Look for Hot Data When There Is No Hot Code
library_path:
- software-engineering
- core
- performance
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- memory
- profiling
- diagnosis
- caching
cross_links:
- rel: related_to
  target_object_id: PAT_read_a_profile_as_a_statement_about_machine_code
- rel: related_to
  target_object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
- rel: related_to
  target_object_id: AP_locate_a_performance_bottleneck_by_measurement
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Look for Hot Data When There Is No Hot Code

## Pattern Rule
**IF** a program is measurably too slow but the time profile shows the cost spread thinly across many functions with no hot spot
**THEN** stop looking for hot code and profile the cache counters instead, treating a data structure rather than a function as the thing to find
**ELSE** where the time profile does concentrate in one region, follow it — this is the procedure for when that has already failed.

## Do
- Recognize the signature before spending a week on it: no single function or loop stands out, optimizing any one fragment yields almost nothing, and the total is nonetheless bad. That pattern says the cost is attached to data touched everywhere rather than to code executed somewhere.
- Take the whole-program cache counters first, since it is one run and it either opens the investigation or closes it. Counting loads against load misses at the innermost data cache separates a program whose working set is resident from one that is missing constantly.
- Ask for the counters explicitly, because they are not in the default set. Data-cache events are distinct from instruction-cache events, and the full list of what a given processor exposes has to be queried from the tool rather than assumed.
- Move to a line-level profile keyed to the miss counter once the summary indicts the program. It attributes misses to functions and lines exactly as a time profile attributes cycles.
- Read the detailed profile for what the locations have in common, not for the worst one. The finding here is never a single line; it is that dozens of scattered functions contributing a percent each all operate on the same collection.
- Expect encapsulation to make some of this answerable without tools. A class whose interface permits only forward iteration over a contiguous member is accessing memory about as well as it can, whatever else may be wrong with it.

## Don't
- Don't conclude the program is already optimal because the profile is flat. A flat time profile is compatible with the program spending most of its time waiting for memory, and it is one of the two things that shape usually means.
- Don't act on a miss rate without finding the shared structure. The line-level cache profile will be as diffuse as the time profile was; the diagnosis is only complete when the misses have been traced to one data organization.
- Don't confuse a high miss rate with an inefficient traversal. Reading every element of a large array in order will miss on each new region and still be running at the hardware's limit — the question is whether the pattern could have been better, not whether misses occurred.
- Don't expect this to indict an algorithm's operation count. A linear search over an array makes ideal memory accesses and far too many of them; the counters will look healthy and the code will still be wrong.

## Checklist
- Is the time profile genuinely flat, or merely not yet detailed enough?
- What is the data-cache miss rate for the whole program?
- Which data structure do the high-miss locations share?
- Would that structure's access pattern have been predictable from its layout without the profile?
- Is the miss rate explained by the volume of data, or by the order it is touched in?

## Notes
The reason conventional profiling misses this is structural. A time profile attributes cost to the instruction that was executing, and the cost of a scattered data layout is paid in small amounts at every site that touches it. Aggregating by code location is exactly the wrong aggregation, and no amount of finer resolution fixes it; what is needed is aggregation by data, which no profiler offers directly and which the analyst has to perform by noticing what the hot locations have in common.

Knowing which structures are memory-efficient is only half of the diagnosis, and the easier half. The other half is how much of the program's time is spent on a given body of data, which is not visible from the structure's definition and is what the counters supply.

The easy cases get optimized first, and that is precisely why this situation appears later in a program's life. A function that both takes obvious time and moves obvious quantities of data is found and fixed early. What remains afterwards is the diffuse cost, and a team that only knows how to read time profiles will conclude at that point that the program cannot be improved.
