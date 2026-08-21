---
object_id: PAT_write_to_a_shared_stream_through_a_synchronized_wrapper
object_type: pattern
name: Write to a Shared Stream Through a Synchronized Wrapper
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- streams
- diagnostics
- threading
cross_links:
- rel: related_to
  target_object_id: PAT_know_when_two_accesses_are_a_data_race
- rel: related_to
  target_object_id: PAT_take_the_simplest_lock_type_that_does_the_job
- rel: related_to
  target_object_id: PAT_read_characters_with_a_streambuf_iterator_not_a_formatted_one
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Write to a Shared Stream Through a Synchronized Wrapper

## Pattern Rule
**IF** several threads write to the same output stream and you want each thread's message to arrive whole
**THEN** write through a synchronized wrapper around that stream, which accumulates into its own buffer and transfers the whole of it when it is destroyed, so no other thread's output can appear inside yours
**ELSE** where the only concern is that concurrent writes are a data race and the messages are single insertions anyway, a lock around each write is sufficient and adds nothing to learn.

## Do
- Separate the two problems, because they are usually conflated and only one of them a mutex per statement solves. Concurrent unsynchronized writes to a stream are a data race and therefore undefined; interleaved output is a legibility problem that persists even when every individual write is correctly locked.
- See why locking each insertion is not enough for a multi-part message. A line built from several insertions releases the lock between them, so another thread's output lands in the middle — the result is well-defined, correctly synchronized, and unreadable.
- Let the wrapper's lifetime define the unit that arrives together. Everything written through one wrapper object is transferred as a contiguous run when that object is destroyed, so the scope you give it is exactly the message you are promising not to have broken up.
- Reach for this in preference to holding a lock across a whole message. Both work; the wrapper does not hold anything while you format, so threads doing expensive formatting do not serialize on each other.

## Don't
- Don't leave concurrent writes to a shared stream unsynchronized at all. The output being garbled is the visible symptom; the actual status is undefined behaviour, and the garbling is what you happened to get.
- Don't build the message with several separately locked writes and expect it to arrive intact. Each write is safe and the message is not, which is the failure that survives a careless fix and looks fixed.
- Don't assume this makes the stream shareable for everything. It arranges for output to arrive in whole runs; it says nothing about a stream's state, its formatting flags, or anything else two threads might both be adjusting.

## Checklist
- Do several threads write to this stream?
- Is any message built from more than one insertion?
- Does the wrapper's scope match the run of output that must stay together?
- Is anything else about the stream — flags, precision, width — being set from more than one thread?

## Notes
The distinction between the race and the interleaving is what makes this worth a decision rather than a lookup. The obvious fix for garbled concurrent output is a mutex, and it does resolve the undefined behaviour. It leaves the output garbled at a coarser grain, because the unit it protects is the insertion rather than the message, and the person who applied it will reasonably believe the problem is solved.

Framing the wrapper's lifetime as the unit of atomicity is the useful way to hold it. You are not locking anything and then unlocking it; you are declaring a buffer whose contents transfer as one piece at a known moment. That makes the scope of the object the thing to get right, and it is visible in the code in a way that the extent of a held lock often is not.

Diagnostic output from concurrent code is where this matters most, and it is also where the temptation to skip it is strongest, because the output is "only for debugging". Interleaved diagnostics from a concurrency bug are actively misleading about the order things happened in, which is precisely the question being investigated.
