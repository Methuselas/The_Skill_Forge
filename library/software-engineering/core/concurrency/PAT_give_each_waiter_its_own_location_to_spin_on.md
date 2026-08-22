---
object_id: PAT_give_each_waiter_its_own_location_to_spin_on
object_type: pattern
name: Give Each Waiter Its Own Location to Spin On
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
- locking
- contention
- cache
- fairness
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_match_the_lock_to_the_length_of_the_critical_section
- rel: related_to
  target_object_id: PAT_separate_per_thread_data_by_a_cache_line
- rel: related_to
  target_object_id: PAT_split_acquisition_into_a_bounded_doorway_and_a_wait
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Give Each Waiter Its Own Location to Spin On

## Pattern Rule
**IF** a busy-waiting lock is contended by more than a couple of threads and you are seeing the release of that lock cost far more than the work it protects
**THEN** put the waiters in a line, give each one its own location to watch, and have every releaser signal exactly its successor — so that releasing invalidates one waiter's cache rather than everyone's
**ELSE** where contention is genuinely low, a single shared flag read before each attempt is smaller, needs no per-waiter storage, and is faster in the uncontended case that dominates.

## Do
- Understand the failure being fixed, because it is not the waiting. Waiters that all watch one location are quiet while the lock is held — they read a cached copy and generate no traffic. The damage happens at release: that single write invalidates every waiter at once, all of them re-read, all of them attempt to acquire, and one succeeds while the rest repeat the storm. Cost concentrates at exactly the moment throughput depends on.
- Give each waiter a distinct location and have the releaser write only to its successor's. One invalidation per release instead of one per waiter, regardless of how many are queued — that is the whole mechanism and everything else follows from it.
- Collect the ordering guarantee, which arrives free. A line of waiters is served in arrival order by construction, so the lock is first-come-first-served without a doorway, timestamps, or a scan of all participants. This is the cheap way to get the ordering property, and it is why an explicit ordering construction is worth building only when a queue genuinely does not fit.
- Collect the better handoff too. Because each waiter is signalled directly rather than discovering the lock is free, nobody has to guess when to try again, and the critical section does not sit idle while waiters are backed off — which is the specific weakness of the alternatives.
- Pad the per-waiter locations onto separate cache lines if they are slots in an array. Adjacent entries land on one line, and a write to one invalidates the neighbours that share it — which quietly reinstates the storm you built the queue to avoid.
- Prefer a linked line over an array once the participant count is unknown or large. A list needs storage proportional to the threads actually contending plus the locks, rather than to the maximum thread count times the number of locks, and it needs no advance knowledge of how many threads exist.
- Decide *whose* location a waiter watches, because it determines where this runs well. Watching your predecessor's node is compact and fine when caches are coherent; watching a node you own yourself costs more operations but keeps the spin local on machines where a remote location is genuinely remote.
- Weigh fairness against locality deliberately, since strict ordering is not free. Handing the lock to the next waiter also hands the guarded data to a cold cache; letting the same thread — or the same cluster of processors — reacquire keeps that data where it already is. For longer critical sections that locality can outweigh the contention it causes, which is why deliberately unfair locks exist and sometimes win.

## Don't
- Don't build this for a lock that is rarely contended. It costs storage per waiter and a more expensive uncontended path, to solve a problem that only appears under contention — and most locks in most programs are not contended.
- Don't expect abandoning a wait to be simple. A waiter that gives up has to be removed from the middle of a line while its neighbours are live, and a timeout facility is a substantially harder construction than the lock it is added to, rather than a flag on the same design.
- Don't leave the per-waiter nodes unreclaimed. A node can be reused once its owner is certain nobody still refers to it, and getting that wrong reintroduces the lifetime problem that lock-free structures have — in a lock implementation, where it is least expected.
- Don't assume ordering is what you wanted. First-come-first-served is a genuine guarantee and it is also the thing that forces the guarded data to migrate on every handoff; if throughput is what you are optimizing and no caller is being starved, the fair lock may be the slower choice.
- Don't tune this by benchmark alone and ship the winner everywhere. Which lock wins depends on the cache topology, whether processors are clustered, and the length of the critical section, and the ranking changes between machines.

## Checklist
- At release, how many waiters' caches are invalidated — one, or all of them?
- Do two waiters' locations ever share a cache line?
- Is the storage per lock proportional to actual contenders, or to the maximum thread count?
- Does a waiter spin on a location that is local to the processor it runs on?
- Can a waiter abandon its attempt, and what happens to the line if it does?
- Is strict arrival order worth the data migrating on every handoff here?

## Notes
The insight this rests on is that contention on a lock is not mainly a contest for the lock. It is traffic on the interconnect, and the traffic is generated by the invalidation pattern rather than by the waiting itself. Once that is clear, the design follows almost mechanically: the problem is one write reaching many watchers, so give the watchers separate locations and write to one of them. Everything the construction is famous for — the ordering, the direct handoff, the scaling — falls out of that single change.

The fairness question is the genuinely difficult part and it is worth resisting the intuitive answer. A fair lock sounds strictly better, and under short critical sections it often is. But a lock protects data, that data sits in some processor's cache, and passing the lock to a different processor drags it across the interconnect. A lock that lets the same thread or the same cluster go repeatedly keeps the data still, and for a long enough critical section that saving exceeds everything the fairness cost. This is a real tradeoff with real starvation on one side and real throughput on the other, not a case where one answer is simply correct.

What makes this family worth knowing even if you never implement one is that it explains the shape of the locks you are given. A production lock is usually some hybrid — a brief optimistic attempt for the uncontended case, backing off or queueing under contention, sometimes with cluster awareness underneath. Recognizing the parts makes its performance legible: why it is fast alone, why it degrades the way it does, and which of its behaviours are deliberate rather than accidental.
