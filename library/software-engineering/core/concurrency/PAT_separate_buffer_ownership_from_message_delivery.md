---
object_id: PAT_separate_buffer_ownership_from_message_delivery
object_type: pattern
name: Separate Buffer Ownership From Message Delivery
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
- distributed
- io
- design
- latency
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_dispatch_on_readiness_or_on_completion
- rel: related_to
  target_object_id: PAT_classify_synchronization_by_progress_guarantee
- rel: related_to
  target_object_id: PAT_block_with_a_deadline_before_polling_on_an_interval
- rel: related_to
  target_object_id: PAT_give_every_operation_one_instant_where_it_takes_effect
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Separate Buffer Ownership From Message Delivery

## Pattern Rule
**IF** you hand a buffer of data to something that will transmit it — to another machine, another process, a device, or a disk — and the call returns
**THEN** establish which of two entirely different facts that return told you: that you may reuse the buffer, or that the far side has the data — because transports routinely guarantee only the first, and the interface almost never says which
**ELSE** where the transport is genuinely synchronous end-to-end and does not return until the peer has taken the data, the two facts coincide and there is nothing to separate.

## Do
- Hold three distinct events apart, because a transport may signal any one of them and call it completion. The bytes have been copied somewhere else, so your buffer is free. The peer has begun receiving, so it is committed to the transfer. The peer has the data and could act on it. Each is a useful thing to know and they can be separated by an unbounded interval.
- Assume a send returns at the first of those unless documented otherwise. Handing off to the transport is the cheapest guarantee to provide and the one nearly every implementation actually gives — so code written as though a returned send means an arrived message is relying on something it was never promised.
- Notice when the guarantee changes with the payload. A transport may take a small message into its own storage and return at once, while a large one waits for the peer to start receiving — so the same call is locally satisfied in one case and end-to-end synchronized in the other, and which you get depends on a size threshold you do not control. Testing with small messages and deploying with large ones is how this is discovered.
- Price the copy that buffering costs. Returning immediately with your buffer freed requires the data to be somewhere else, which means a copy — real work proportional to the message. A mode that waits for the peer avoids the copy entirely, so "returns sooner" and "does less work" point in opposite directions here.
- Reach for an explicitly deferred transfer when you want the overlap, and understand what it obliges. Initiating without waiting lets you compute while the transfer proceeds, which is the entire reason to want it — and until you explicitly check or wait for that transfer, you know nothing, and the buffer is not yours. Reading it is questionable and writing it is a defect.
- Put real work between initiating and completing, or do not use the deferred form. Initiating a transfer and immediately waiting for it is the synchronous version with extra steps and worse readability. The gap is where the benefit lives, and if there is nothing to put in the gap there is no benefit.
- Design an acknowledgment when you genuinely need to know the peer received it. That fact is application-level and the transport is not offering it; a reply message, a sequence number the peer echoes, or a commit protocol are the ways to obtain it, and each has a cost that should be paid deliberately rather than assumed away.
- Add this to the list of things the word "blocking" can mean. It already names a property of correctness conditions, of progress conditions, and of interfaces; here it distinguishes a call that waits until your buffer is safe from one that waits until the peer has the data. A claim that an operation is blocking has still not said which.

## Don't
- Don't touch a buffer whose transfer you have not confirmed complete. It compiles, it usually works, and it corrupts a message under exactly the timing you were not testing — the transport may still be reading from it, and nothing will tell you.
- Don't read a successful return as evidence the peer is alive. A send that succeeded locally against a peer that has already failed is an ordinary outcome, and the failure surfaces much later somewhere unrelated.
- Don't leave a deferred transfer uncompleted. Every initiation has a matching completion that must eventually happen; skipping it leaks the transport's bookkeeping and, in the cases that matter, silently abandons the transfer.
- Don't reach for buffered transmission to avoid thinking about the ordering. It converts a waiting problem into a copying problem and a capacity problem — you now have to supply and size the storage — and it is usually the more expensive answer rather than the easier one.
- Don't assume the receiving side has symmetric semantics. Receiving completion generally does mean the data has arrived, so the asymmetry between the two ends is real; reasoning about one from the other is how a protocol ends up correct in one direction only.

## Checklist
- When this send returns, which of the three events has actually occurred?
- Does that answer change with message size, and has it been tested at both?
- Between initiating a deferred transfer and completing it, does anything touch the buffer?
- Is there real work in that gap, or is it initiate-then-immediately-wait?
- If the code depends on the peer having received the data, where does that acknowledgment come from?
- Does any completion path leave a transfer initiated but never awaited?

## Notes
The confusion this prevents comes from the word rather than the mechanism. A call named "send" that returns successfully reads, to almost everyone, as a message that was sent — and the transport meant something narrower and more useful to itself: that it has taken custody of the bytes. Both parties are behaving reasonably and the gap between them is where a whole class of protocol defects lives, all of which look like the peer misbehaving.

The overlap argument is the reason deferred transfers exist and it is worth stating as an economic one. Communication takes time during which the processor has nothing to do; the deferred form exists so that time can be spent computing instead of waiting. That means the technique's value is exactly proportional to how much useful work sits between initiation and completion — which makes initiate-then-immediately-wait not merely pointless but actively worse, since it pays the bookkeeping cost of the deferred form for none of its benefit.

The asymmetry between the two ends is easy to miss and worth carrying. Receiving is a fact about data that has arrived; sending is a fact about data that has departed. Only one of those tells you anything about the other machine. Protocols that assume otherwise generally work perfectly in testing, where both ends are healthy and fast, and fail in the one situation the acknowledgment existed to detect.
