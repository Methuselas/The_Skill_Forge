---
object_id: PAT_reach_for_a_custom_allocator_only_for_what_it_can_buy
object_type: pattern
name: Reach for a Custom Allocator Only for What It Can Buy
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- allocators
- containers
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_replace_new_delete_only_with_clear_reason
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: medium
references: []
variants: []
---

# Reach for a Custom Allocator Only for What It Can Buy

## Pattern Rule
**IF** you are considering giving a container something other than the default allocator
**THEN** check your reason against the short list of things this actually delivers — memory drawn from a particular region, elements clustered for locality, synchronization removed that you are certain you do not need, or a measured improvement on the default's speed or fragmentation — because outside that list it buys nothing and costs you a template to maintain
**ELSE** where what you need is for the container object itself to live somewhere particular, this is the wrong mechanism: it governs where the elements go, not where the container goes.

## Do
- Establish the motivation by measurement rather than by suspicion when the reason is performance. That the default is too slow, wastes space, or fragments is a finding, and the other three motivations are facts about the deployment rather than performance claims at all.
- Keep the distinction between the container and its contents in view, because it is the one people get wrong. Declaring a container that allocates from a special region puts its *elements* there; the container object is an ordinary variable wherever you declared it. Putting the container there as well means acquiring that memory yourself, constructing the container in place, and later destroying it explicitly and releasing the memory — four manual steps worth avoiding unless the container itself genuinely has to be shared.
- Expect two surprises in the interface if you compare it to the raw allocation function. It is passed a count of objects rather than a count of bytes, so the multiplication by element size is yours to do; and its return type names the element type even though nothing has been constructed in that storage yet, so the caller still has to construct.
- Remember that the node-based containers never allocate the element type at all. A linked list of some type needs storage for nodes containing that type, so the allocator it actually uses is derived from the one you supplied rather than being the one you supplied — which is why a custom allocator is asked to support that derivation, and why watching for allocation calls that never arrive is not a sign of a bug.

## Don't
- Don't write one because the default allocator has a reputation. It is a general-purpose allocator and general-purpose allocators are good; the cases where a special-purpose one wins are cases where you know something about the allocation pattern that the general one cannot.
- Don't carry forward the stateless restriction without checking whether it still applies to you. Allocators once could not hold per-object state, because implementations were permitted to assume any two of the same type were interchangeable — which is why older code encodes a choice of heap in the allocator's *type* rather than in an object of it. That constraint has since been lifted, and code written around it is more contorted than it now needs to be.
- Don't hand-write the boilerplate when a ready-made facility covers the case. Most of these motivations are served by the standard's runtime-polymorphic allocator and its supplied memory resources, which are configured with an object rather than by instantiating a new type.

## Checklist
- Which of the four motivations is this, stated as a sentence?
- If it is performance, what measurement established it?
- Do the elements need to be in the special region, or the container object as well?
- Would a standard memory resource cover this without a new template?
- If a custom allocator is genuinely needed, does it support the derivation node-based containers require?

## Notes
The four motivations are the durable part of this and they have aged well: drawing from shared memory so several processes can reach the elements, drawing from a particular heap so that objects used together sit near each other, dropping thread-safety machinery in a program that is single-threaded, and beating a general-purpose allocator on a pattern you understand and it does not.

Almost everything else Meyers records about allocators has been overtaken, and the direction of travel is worth knowing because it inverts his advice. He documents at length that portable allocators cannot hold state, that the pointer and reference type names are decorative because implementations may ignore them, and that the derivation mechanism must be supplied by hand. Stateful allocators are supported now, the type names are honored so that non-raw pointer representations work, and the traits mechanism supplies the derivation for you.

The confidence on this card is deliberately lower than its neighbors. The motivations are solid, but allocator mechanics have been reworked more than once, and anything specific about how one is written should be checked against the current standard rather than taken from here.
