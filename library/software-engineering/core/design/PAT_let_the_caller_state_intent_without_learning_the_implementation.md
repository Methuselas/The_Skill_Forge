---
object_id: PAT_let_the_caller_state_intent_without_learning_the_implementation
object_type: pattern
name: Let the Caller State Intent Without Learning the Implementation
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- design
- api_design
- performance
- abstraction
- interfaces
cross_links:
- rel: related_to
  target_object_id: PAT_expose_clean_api_hide_implementation
- rel: related_to
  target_object_id: PAT_choose_among_good_designs_by_what_they_foreclose
- rel: related_to
  target_object_id: PAT_convey_usage_through_names_and_types
- rel: related_to
  target_object_id: PAT_choose_the_data_structure_for_the_dominant_access_pattern
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Let the Caller State Intent Without Learning the Implementation

## Pattern Rule
**IF** you are designing an interface between two components where performance may eventually matter
**THEN** apply opposite rules to the two sides — the provider promises the least it can while still answering the request, and the interface gives the caller a way to say what it actually wants, including why
**ELSE** where the interaction is rare or trivially cheap, either rule can be relaxed, and the cost of an over-general call is not worth the design attention.

## Do
- Promise only what was asked on the answering side. A caller asking whether a collection is empty did not ask how many elements it holds; some implementations can answer emptiness cheaply and a count expensively, and volunteering the count in the contract removes those implementations forever.
- Judge an interface by how many implementations satisfy it. A queue that can be built on an array, a block-allocated deque, or a linked list has an interface that reveals nothing; a hash container whose interface exposes bucket counts has committed every implementation to separate chaining, and an open-addressing version cannot conform.
- Give the requesting side a way to express what it will do next. Indexing an element says nothing about what comes after it, so a block-allocated container must locate the block on every access; an iterator carries the standing implication that the neighbour is wanted next, which lets the implementation keep the block located. The same traversal through the two interfaces measures very differently.
- Let the caller state the loosest requirement that meets its need. "Visit every element in order and give me each one" and "tell me whether any element matches this, in any order you like" are different requests, and only the second leaves the implementation free to traverse storage in whatever order is cheapest.
- Notice when a caller is using a powerful interface for a narrow purpose. Iterating with random access, sorting when you only need the maximum, fetching a whole record to read one field — each is a request that promised more than was needed, and the extra capability was paid for.
- Decide how much intent-carrying interface to build up front from two questions. How likely is this interaction to be performance-critical, given what the component is for? And how widely will the answer spread before it could be changed — a class used twice, or a protocol that will outlive several rewrites?

## Don't
- Don't apply the rule "never add an operation that could be written using the public interface" without asking what it costs. An external implementation that is ten times slower is not really an implementation of the same thing, and the rule assumes the two are equivalent.
- Don't treat the two sides as one principle. They pull in opposite directions on purpose: the provider constrains itself, the interface un-constrains the caller, and conflating them produces either a leaky contract or an impoverished one.
- Don't expose an internal detail because it is convenient right now. That is the direction that cannot be undone — callers build on what they can see, and withdrawing it breaks them.
- Don't over-correct into an interface nobody can use. Refusing every operation that constrains the implementation can leave a collection supporting only append and forward traversal, which is a legitimate design for streaming data and a poor one for anything else.

## Checklist
- For each operation the provider offers: what does it promise beyond what was asked?
- How many plausible implementations satisfy this interface as written?
- Can a caller doing a bulk operation say so, or must it be spelled out one element at a time?
- Is any caller here using a general operation to do something specific?
- If this interface needs an intent-carrying addition later, what breaks?

## Notes
The two halves look contradictory and are not, because they govern different parties. Everything about *how* the work is done stays with the implementer and is never promised. Everything about *what* the caller wants — including its plans — should be able to reach the implementer, since that is the information the optimization will eventually be built on. A contract that gets this backwards tells the caller how the work is done and refuses to hear why it is wanted.

The asymmetry in reversibility decides how carefully each half must be got right. Over-exposing is close to permanent: clients depend on what they can see, and the detail cannot be withdrawn. Under-exposing is cheap to fix: adding a richer operation later breaks nothing, and callers migrate to it as they need it. So the minimum-promise rule deserves discipline up front, while the intent-carrying rule can be applied where the case for it is clear and extended later.

At the design stage you will usually not know what optimization the extra information enables — and that is not an argument against providing the channel. The first implementation of a bulk operation may simply run the loop the caller would have written. What has been bought is that the freedom exists, in an interface that is going to be hard to change, for an implementation nobody has thought of yet.
