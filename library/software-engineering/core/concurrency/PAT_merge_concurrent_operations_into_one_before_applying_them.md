---
object_id: PAT_merge_concurrent_operations_into_one_before_applying_them
object_type: pattern
name: Merge Concurrent Operations Into One Before Applying Them
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
- contention
- scalability
- latency
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_cancel_complementary_operations_instead_of_applying_them
- rel: related_to
  target_object_id: PAT_announce_the_operation_so_another_thread_can_finish_it
- rel: related_to
  target_object_id: PAT_name_the_performance_metric_before_you_optimize
- rel: related_to
  target_object_id: PAT_trade_exact_ordering_for_independent_substructures
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Merge Concurrent Operations Into One Before Applying Them

## Pattern Rule
**IF** many threads apply the same kind of update to one shared location, and that location sets the ceiling on how fast the system can go
**THEN** let threads that arrive at about the same time merge their updates into a single combined update, have one of them apply it on everyone's behalf, and hand each contributor back its own result
**ELSE** where the update is not associative, or arrivals are sparse enough that threads rarely coincide, there is nothing to merge and each operation has to be applied on its own.

## Do
- Check associativity before anything else, because it is the precondition and it is what decides whether this is available at all. Many increments become one increment by their sum; many appends become one append of a batch; many set-insertions become one insertion of a union. An update whose result depends on being interleaved with others in a particular way cannot be merged, and no amount of machinery changes that.
- Be explicit that this raises the cost of one operation to lower the cost of many. An individual update now travels further and waits for partners, so its own completion time gets worse — while the number of updates the system completes per unit time gets better, often dramatically. Adopting it while being measured on individual response time is a straightforward way to make things worse.
- Have exactly one participant carry the merged update and the rest wait on its outcome. The carrier is responsible for more than success: where the operation returns something, it must hand each contributor the answer *that contributor* would have received, which for merged increments means apportioning a range of values rather than reporting one.
- Merge in stages when there are many participants. Pairing up, then pairing the pairs, and so on, means the number of rounds grows with the logarithm of the participants rather than linearly — which is where the throughput win actually comes from, since the alternative is everyone queueing at one point.
- Give up quickly when no partner appears, and proceed alone. A thread that waits indefinitely to be merged with has converted a throughput optimization into a latency failure, and the light-load case — where there is nobody to merge with — is precisely when waiting is worst.
- Place this in the family and choose the right member. Where operations *annihilate* each other, pair them off and neither reaches the shared structure. Where they *merge*, combine them so one reaches it on behalf of many. Where a thread simply cannot get through, have another finish its work outright. All three move work off a bottleneck; they differ in what they demand of the operations — inverses, associativity, or reifiability.
- Expect the benefit to arrive only under load, and to be negative without it. Contention is what supplies partners, so the technique pays exactly when the system is busy and costs when it is not — which makes a benchmark at low concurrency actively misleading.

## Don't
- Don't merge updates whose outcome depends on their order. Associativity is a property of the operation, not a preference about it, and a merged update that reorders what callers observed is producing a result no sequential execution would have produced.
- Don't let the merging structure become the bottleneck you were escaping. The place where threads meet to combine is itself shared, and a design where everyone meets in one spot has moved the contention rather than removed it.
- Don't leave a waiting contributor without a route to its own answer. The merged operation succeeded as a unit; each participant still needs to learn what its individual call returned, and a design that only reports overall success has changed the operation's contract.
- Don't adopt it for a structure that is not actually the limit. It adds latency, machinery, and a coupling between unrelated threads, all to relieve pressure at one point — which is worth nothing if the pressure is elsewhere.
- Don't overlook that merging couples the fates of everyone merged. A carrier that is descheduled or fails leaves every contributor waiting on it, so a technique adopted for throughput has introduced a shared failure mode among threads that had nothing to do with each other.

## Checklist
- Is the operation associative, and is that a property or an assumption?
- Which metric is this design being judged on — completion time for one call, or calls completed per unit time?
- Who carries the merged update, and how does each contributor learn its own result?
- Where do threads meet to merge, and is that place itself contended?
- What does a thread do when no partner arrives?
- If the carrier stalls, who else is stuck behind it?

## Notes
This is the least intuitive of the ways to relieve a shared bottleneck, because it makes the individual operation unambiguously worse. A single update under a lock is a short trip; the same update through a merging structure travels several levels and waits for company. The reason to accept that is that the two quantities being traded are not on the same scale — a modest constant added to each operation can buy a reduction from linear to logarithmic in how long a batch of them takes, and under load the batch is what anyone is waiting on.

The family resemblance to the other bottleneck-relief techniques is worth holding, because the three are chosen by what the operations allow rather than by preference. Cancellation needs operations that undo each other, which is a strong requirement and rare. Merging needs only associativity, which is common — counters, accumulators, appends, unions, maxima all qualify — so it applies far more widely. Completing another thread's work needs the operation to be describable as data, and buys a progress guarantee rather than throughput. Knowing which property your operations have tells you which of the three is even available.

The coupling this introduces deserves more attention than it usually gets. Merging makes one thread's progress depend on another's, between threads that share nothing but a moment of arrival. Under normal conditions that is invisible. Under a stall it is not: a carrier that loses its processor holds up everyone whose work it absorbed, and the resulting latency spike is concentrated rather than spread. A design that adopts merging for throughput should know it has traded some independence to get it.
