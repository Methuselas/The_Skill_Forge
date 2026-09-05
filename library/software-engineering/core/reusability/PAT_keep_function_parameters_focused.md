---
object_id: PAT_keep_function_parameters_focused
object_type: pattern
name: Make Functions Take Only What They Need
library_path:
- software-engineering
- core
- reusability
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- function_parameters
- reusability
- readability
- modularity
cross_links:
- rel: related_to
  target_object_id: PAT_encapsulate_related_data_together
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Make Functions Take Only What They Need

## Pattern Rule
**IF** a function uses only part of an object passed to it
**THEN** narrow the parameter to just what it actually needs, so the function is reusable and its calls are honest — while using judgment when it needs most of an encapsulating object.

## Do
- Pass the specific value: a `setTextColor` that reads only the color from a styling object should take a color, not the whole options object.
- Notice the call-site symptom: forcing callers to build a full options object with irrelevant made-up font, size, and line-height values just to set a color signals the parameter is too broad.
- Keep calls truthful — narrowing the parameter makes a warning-styling call simply set the color red, with no misleading extra values.
- Read the finished list as an interface, not only parameter by parameter. Order it input, then input-and-output, then output-only, so the list narrates the sequence inside; keep similar parameters in the same order across similar routines; put status and error variables last.
- Delete unused parameters. This is the mechanical one and the one to run first: 46 percent of routines carrying no unused variables came back error-free, against 17 to 29 percent of those carrying more than one.
- Read the call site for setup and takedown code, which is the observable signal that the parameter list has the wrong shape. A caller that fills in an object field by field before the call and unpacks it field by field afterwards is telling you the routine wants the fields. The converse counts equally: a caller that already holds the object and has to pass four of its accessors is telling you the routine wants the object.

## Don't
- Don't demand a whole object when one field will do; it makes the function unreusable elsewhere and makes callers fabricate values that imply effects that never happen.
- Don't overcorrect into unencapsulating everything; if a function genuinely needs most of a grouped object, passing the object beats threading many loose values, which harms modularity.

## Checklist
- Does the function read only a fraction of the object it takes?
- Are callers inventing irrelevant values just to satisfy the parameter?
- If it needs most of an encapsulating object, is passing the whole object the cleaner choice?

## Notes
An over-broad parameter couples a function to more than it uses, blocking reuse and misleading readers. Long's `setTextColor` taking a full `TextOptions` forces a warning-styler to concoct a font, size, and line height that suggest it sets them — it does not. Taking a color instead makes the function reusable and the call self-evident. The judgment clause guards against the opposite mistake: when a function needs most of a cohesive object, keep it encapsulated rather than exploding it into loose arguments.

The setup-and-takedown signal is worth having because it converts this card's judgment call into something you can see rather than something you have to weigh. Neither direction is wrong on its own — the deciding question is what abstraction the interface is meant to present, and whether it expects four distinct pieces of data or one object. What the call site tells you is which answer the callers actually need, and a caller doing clerical work either side of the call is doing that work precisely because the interface picked the other one. Watch for the related shape too: a special constructor that exists only to take a subset of a class's initialization data so that a call can be written more conveniently is the same complaint arriving as a new member instead of as setup code.

Widening the unit of attention from the single parameter to the whole list is worth the effort because interfaces between routines are where defects concentrate — Basili and Perricone attributed 39 percent of all errors to internal interface communication. The ordering rules are deliberately conventions rather than judgment calls, since their value comes from being applied uniformly across a family of related routines; inconsistent ordering is pure memory tax with no compensating benefit. Two limits: ordering never overrides narrowing, because a well-ordered list of parameters the function does not need is still the wrong interface, and language conventions may conflict with these — the C library's modified-parameter-first habit is the standing example — in which case consistency within your own codebase matters more than which convention you picked. Note that `PAT_dont_mutate_input_parameters` already covers McConnell's related warning against using parameters as working variables, so that guidance is not duplicated here.
