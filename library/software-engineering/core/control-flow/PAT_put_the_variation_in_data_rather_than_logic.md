---
object_id: PAT_put_the_variation_in_data_rather_than_logic
object_type: pattern
name: Put the Variation in Data Rather Than Logic
library_path:
- software-engineering
- core
- control-flow
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- table_driven
- control_flow
- data_driven
- maintainability
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_control_construct_that_fits_the_data
- rel: related_to
  target_object_id: PAT_choose_the_tables_access_scheme_by_the_key
- rel: related_to
  target_object_id: PAT_balance_adaptability_without_predicting_future
- rel: related_to
  target_object_id: PAT_prefer_composition_over_inheritance
- rel: related_to
  target_object_id: AP_shape_a_multi_way_decision
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Put the Variation in Data Rather Than Logic

## Pattern Rule
**IF** a long conditional chain, a wide case statement, or a family of near-identical subclasses exists only to select among variants of one operation
**THEN** move what varies into a table the code reads, so the program's knowledge sits in its data instead of in its control flow.
**ELSE** where there are only a few alternatives and they genuinely do different work rather than the same work with different values, the direct logic is simpler and more readable — the table earns its place as the chain lengthens.

## Do
- Separate what varies from what stays the same before deciding anything else. Twenty message formats that differ only in how many fields they have, what type each field is, and what each field is called share one printing procedure — the differences are three columns of a table.
- Store whichever of three things the lookup should yield. Where the answer is data, put the data in the table. Where the answer is an action, store either a code the caller dispatches on or, better where the language allows it, a reference to the object or routine that performs the action, which removes the dispatch entirely.
- Count what the table replaces before committing. Twenty message types handled by logic means twenty printing routines plus a twenty-way dispatch to reach them; handled by table it is one interpreting routine plus a handful of field handlers, and a twenty-first message type then changes no code at all.
- Move the table out of the program when its content is what changes and someone else controls it. Reading message descriptions from a file at startup converts a code change into a data change, which is a deliberate choice about how late the values are bound.
- Apply the same test to inheritance trees. A set of subclasses differing only in constants is this pattern wearing different syntax, and asking whether a lookup table would replace them is as productive there as it is on a conditional chain.

## Don't
- Don't assume restructuring into objects has improved anything. The rote object-oriented version of the message reader still needs the twenty-way dispatch, this time to instantiate the right subclass, and still needs twenty printing routines. It requires as much code as the rote procedural design or more, because it made the solution space more complicated rather than less. Inheritance and polymorphism being present is not evidence that a design is good.
- Don't hard-code the contents of a table whose whole purpose is being easy to change. That keeps the indirection cost and gives away the benefit it was paying for.
- Don't reach for a table where the logic is short. Simple cases really are easier and more direct written as conditionals, and the trade only turns as the chain grows.
- Don't judge the table version by the size of its interpreting routine. That routine is longer than any single one it replaces, which looks like a loss until you notice it is the only one.

## Checklist
- What actually differs between these branches — the operation, or a few values?
- How many places have to change when a new variant is added?
- Does the lookup yield data, a code to dispatch on, or something callable?
- Is the table's content the part most likely to change, and does it live where changing it is cheap?
- Would this still be complicated in a language with no inheritance?

## Notes
The finding worth carrying out of this is about paradigms rather than tables. Presented with a tangle of twenty message-handling routines, the reflexive modern response is to reach for an abstract base class and twenty subclasses — and that version needs the same twenty-way selection to decide which subclass to build, plus twenty implementations behind it. The paradigm changed and the complexity did not, because the actual insight was orthogonal to it. The key design decision here is neither object orientation nor procedural decomposition; it is recognizing that the variation was data all along.

Two questions have to be answered separately once you decide on a table, and conflating them is where table-driven designs go wrong. The first is how an entry gets found, which is a question about the shape of the key. The second is what the entry contains, which is a question about whether the answer is a value or a behaviour. A table returning data is straightforward; a table returning behaviour is where the design gets interesting, because storing something callable collapses the remaining dispatch into an array access.

The honest cost is that a table adds a level of indirection and takes the logic out of the place a reader is looking. That is why the length of the chain matters — below some size the conditional says plainly what happens and the table makes you look somewhere else to find out. Above it, the conditional stops being readable at all while the table stays the same size, and the crossing point arrives sooner than most people expect once the same structure has to be repeated for a second and third dimension of variation.
