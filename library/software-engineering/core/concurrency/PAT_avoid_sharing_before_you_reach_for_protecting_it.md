---
object_id: PAT_avoid_sharing_before_you_reach_for_protecting_it
object_type: pattern
name: Avoid Sharing Before You Reach for Protecting It
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- shared_state
- threading
- encapsulation
- design
cross_links:
- rel: related_to
  target_object_id: PAT_keep_thread_aware_code_away_from_thread_ignorant_code
- rel: related_to
  target_object_id: PAT_lock_the_smallest_region_that_must_be_atomic
- rel: related_to
  target_object_id: PAT_verify_an_object_is_as_immutable_as_you_think
- rel: related_to
  target_object_id: PAT_avoid_global_state_inject_shared_state
- rel: prerequisite_for
  target_object_id: PAT_keep_thread_aware_code_away_from_thread_ignorant_code
- rel: prerequisite_for
  target_object_id: PAT_verify_an_object_is_as_immutable_as_you_think
- rel: prerequisite_for
  target_object_id: PAT_give_a_shared_object_its_own_thread_instead_of_a_lock
- rel: prerequisite_for
  target_object_id: AP_design_a_parallel_decomposition
- rel: prerequisite_for
  target_object_id: DRILL_classify_the_dependencies_in_a_loop
reference:
  source_title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
  author: Robert C. Martin, with Brett L. Schuchert
confidence: high
references: []
variants: []
---

# Avoid Sharing Before You Reach for Protecting It

## Pattern Rule
**IF** several threads will need the same data and you are deciding how to keep them from interfering
**THEN** work first on removing the sharing — partition the data, hand each thread its own copy, keep what it needs in local state — and reserve guarding for what genuinely cannot be divided
**ELSE** where the data is inherently one thing that everyone must see the latest of, guarding is the answer and the work becomes minimising how many places touch it.

## Do
- Split the problem into independent portions before splitting the work across threads. Where each thread can take a slice, work it through from unshared inputs, and produce an independent result, the coordination problem disappears rather than being solved.
- Hand out copies where the data is read rather than modified, or where results can be merged afterwards. Each thread accumulates into its own copy and one thread combines them at the end, which needs no guarding anywhere along the way.
- Price the copying honestly and expect it to win more often than instinct suggests. Extra allocation is a visible cost and the guarding it avoids is an invisible one, so the comparison is usually made wrongly — measure rather than assume.
- Expect the measured gap between guarding and not sharing to be larger than an order of magnitude, not a percentage. Summing a hundred million integers across four threads has been measured at roughly three and a third seconds with a guarded shared accumulator and roughly one and a third with an atomic one, against seven hundredths of a second for the same sum on one thread and three hundredths for four threads each accumulating locally and combining once at the end. Both shared versions lose to not threading at all; only the unshared one wins, and it wins by about a factor of two.
- Prefer state local to a thread over state reachable by all of them. Anything a thread holds privately for the duration of its work is outside the problem entirely, and moving data there is usually a smaller change than protecting it where it is.
- Reduce the number of places that touch whatever genuinely stays shared. Each additional site is another chance to forget the guard, another copy of the same protective logic to keep aligned, and another candidate when something goes wrong and nobody can tell where.
- Change the shape of the shared object to serve its callers rather than requiring every caller to manage the sharing correctly. Protection arranged by convention holds until somebody writes the next caller.

## Don't
- Don't treat guarding as the first move. It is the answer to sharing you could not eliminate, and reaching for it early means never asking whether the sharing was necessary.
- Don't leave data shared because copying it seems wasteful. That trade is usually assumed rather than measured, and the guarding it avoids has costs in contention and in the faults it fails to prevent.
- Don't spread the protective logic across the callers. Duplicated guarding drifts out of step, and the site that drifts is the one nobody was looking at.
- Don't assume a portion is independent because it looks independent. Shared connections, pools, caches, and logs are easy to overlook and are shared by every thread that touches them.
- Don't expect the guarded portion to get faster with more threads. It cannot: the best case for concurrent access to shared data is single-threaded speed, and measurement shows it going the other way — an atomic increment of a shared counter took *longer* on two threads than on one, and a mutex-guarded increment degraded faster still.

## Checklist
- Can this data be divided so each thread works on a portion nobody else touches?
- Could each thread take a copy, with results merged by one thread afterwards?
- How much of what a thread needs could be held locally for its duration?
- How many places modify what remains shared, and is that number falling?
- Has the cost of copying been measured, or estimated and assumed?
- What is shared here that was never named — a pool, a connection, a cache?

## Notes
The ordering matters because the two approaches differ enormously in what they demand afterwards. Data nobody shares cannot be corrupted by interleaving, needs no guard, cannot deadlock, and stays correct however the scheduler behaves — the property is structural and holds without anyone maintaining it. Guarded data is correct only while every site that touches it does so properly, which is a property that has to be preserved by every future change made by everyone. Eliminating a share is permanent; protecting one creates an ongoing obligation.

The copying trade is worth stating plainly because it is habitually judged wrong. Creating extra objects looks wasteful in a way that is easy to see, while the cost of the guarding avoided is spread across contention, blocked threads, and the faults that eventually escape — none of which appears at the point of decision. Where copying removes the need to guard at all, it frequently wins outright, and the recommendation is not to assume that in either direction but to treat it as measurable, because it is.

Concentrating whatever remains shared is the second-best outcome and deserves as much attention as the first. The number of sites that touch shared data drives everything difficult about it: the chance of an unguarded one, the effort of keeping the protective logic consistent, and the size of the search when a value turns out wrong. A design where one component owns the shared state and exposes operations that are correct by construction converts a rule every caller must remember into a property the callers cannot break, which is the same move that makes any other invariant survive contact with people who did not write it.

The price of the guarding this card asks you to avoid has been measured, and it is worth carrying as a number rather than an intuition. A mutex-guarded increment cost around twenty-three nanoseconds against seven for an atomic one, on a single thread with no contention at all — before any of the scaling behaviour above. Whatever fraction of a program runs inside that guarded region is a fraction that additional threads cannot speed up, which is the concurrency version of the sequential-remainder ceiling.

A second measurement makes the point at a scale that is hard to argue with. Summing a large array of integers across four threads, with the running total kept in one shared variable, ran roughly a hundred times slower than the same summation on a single thread — and that was with the shared variable made atomic rather than mutex-guarded, and with its memory ordering weakened below the default. Four threads did not merely fail to help; they turned a fast computation into a slow one. The same summation with each thread accumulating into its own local and combining the four results at the end was faster than the single-threaded version. Nothing about the arithmetic changed between those two; only whether the threads were writing to the same place.
