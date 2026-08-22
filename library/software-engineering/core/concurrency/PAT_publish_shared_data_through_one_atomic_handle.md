---
object_id: PAT_publish_shared_data_through_one_atomic_handle
object_type: pattern
name: Publish Shared Data Through One Atomic Handle
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
- memory_order
- threading
- data_structures
cross_links:
- rel: related_to
  target_object_id: PAT_weaken_a_memory_order_only_against_a_measurement
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_put_the_thread_safety_guarantee_at_the_transaction_boundary
- rel: related_to
  target_object_id: PAT_verify_an_object_is_as_immutable_as_you_think
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Publish Shared Data Through One Atomic Handle

## Pattern Rule
**IF** one thread builds data that other threads must read once it is ready, and locking every read afterwards would serialize them
**THEN** make the only route to that data a single handle, keep it at an invalid value while the producer builds, and hand it over with one atomic store carrying a release barrier against acquiring loads
**ELSE** where the data keeps changing after other threads can see it, this does not apply — the protocol depends on the published data being immutable from the moment it becomes reachable.

## Do
- Build where nothing else can reach. The producer works through its own reference, in memory no other thread has a valid way to name; until the handle is set, the data does not exist as far as the consumers are concerned, so no synchronization is needed while it is being assembled.
- Set the handle atomically with a release barrier, and read it atomically with an acquire barrier. That pairing is what carries the guarantee: a consumer that observes the new handle value is guaranteed to see every write the producer made beforehand, without either side locking anything.
- Let the handle be whatever can be swapped atomically and can hold an impossible value. A pointer against null is the usual case; an index into a preallocated array against any value at or beyond its size works identically.
- Publish arbitrarily complex data through one handle. What the handle refers to may contain further pointers to further data — the barrier covers everything the producer wrote before the store, so a whole subgraph becomes visible in one act.
- Wrap the protocol in a type rather than writing the atomic operations at each site. A pointer class exposing publish and get is the natural unit, keeps both barriers correct in one place, and measured no slower to dereference than a raw pointer.
- Distinguish a counter from an index in the interface, not just in the memory order. Both are an atomic integer with increment and read; the index carries release and acquire so that reading N proves the first N elements are complete, the counter carries neither because nothing depends on it. Publish two types with documented guarantees, so a reader can tell which one a given use needs.
- Extend this to data that must keep changing by publishing a new version rather than modifying the old one. A writer takes a copy, modifies the copy, and publishes it through the same handle; readers continue to hold whatever version they loaded, and each published version stays immutable for its whole life. The rule above is untouched — no published data is ever modified — and what changes is that several versions exist at once. This is the arrangement the Linux kernel calls read-copy-update, and its point is that readers synchronize with nothing at all: no lock, no read-modify-write, no barrier beyond the acquiring load of the handle.
- Settle when an old version dies before adopting the versioning form, because that is the whole of its difficulty. A version can be released once no reader still holds it, which is the same reclamation question a lock-free structure faces and has the same answers — waiting for a quiescent point at which no reader is in progress, or having readers publish what they hold.
- Keep ownership explicit where you can. Reference counting across threads costs heavily — a standard shared pointer driven by explicit atomic operations measured around sixty times slower to publish than a purpose-built publishing pointer on a single thread, and the gap widened with more threads.

## Don't
- Don't publish through a handle that ordinary code can bypass. The guarantee rests on there being exactly one route to the data; a second reference held anywhere else is the same defect as reading an array out of bounds, and it will be found by a reader that sees a half-built object.
- Don't modify published data. Once the handle is visible the data must be treated as constant, which is what allows every consumer to read it concurrently with no guarding at all — the exception being a further handle inside it, which is itself atomic.
- Don't use it with several producers. One publisher through one handle is the whole protocol; two threads publishing through the same handle race, and some consumers will see one result and some the other. Multiple producers need a separate mechanism.
- Don't expect it to solve reclamation. It says when data becomes visible and nothing about when it stops being needed, and that gap is what makes the repeated form above a harder design than the one-shot one.
- Don't reach for the versioning form where writes are frequent. Every write copies the whole structure and every old version has to be held until its readers drain, so the arrangement is paid for entirely on the write side; it earns that back only where reads overwhelmingly outnumber writes, and turns into copying with extra steps where they do not.
- Don't expect it to solve reclamation. It says when data becomes visible and nothing about when it stops being needed — consumers that already read the handle still hold the value after the owner is destroyed, so lifetime has to be settled by the surrounding algorithm, usually at a point where the whole structure is known to be unreachable.
- Don't assume the standard smart pointers implement it. Neither the value stored in a unique pointer nor a shared pointer's own pointer value is guaranteed to be read or written atomically, so publishing through either requires the explicit atomic operations or a language version that provides an atomic form.

## Checklist
- Is there exactly one handle through which consumers can reach this data?
- Does the store carry release and every load carry acquire?
- Is the data immutable from the moment the handle is set?
- Is there exactly one producer for this handle?
- Who deletes this, and how is it known that no consumer still holds the value?
- Does the interface say which guarantee it offers — visibility, or only a value?

## Notes
This is the general form of a result that looks like a rule violation. Several threads access the same memory, one of them writes it, and none of them lock — which is a data race by the usual statement of the rule. It is not, because the write and the reads are separated by a barrier pairing that establishes an order between them: everything the producer did happens before the store, the consumer's load happens before everything it does afterwards, and the two are linked through one atomic variable.

The payoff is the reason to bother. Locking the data instead would be correct and would keep every consumer serialized against every other long after the producer has finished — a shared array read by many threads, one at a time, for the rest of the program. What the protocol buys is a defined boundary between the mutable phase and the immutable one, after which unsynchronized concurrent reading is simply safe.

Publishing is the first half of every concurrent data structure, and the half that has a clean general answer. Making data appear is a matter of one atomic store; making it disappear requires knowing that nobody is still looking, which no barrier can establish and which is where the difficulty of these structures actually lives.
