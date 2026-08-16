---
object_id: PAT_dont_mutate_input_parameters
object_type: pattern
name: Don't Mutate Input Parameters; Copy Before Mutating
library_path:
- software-engineering
- core
- avoiding-surprises
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- side_effects
- mutation
- avoid_surprises
- defensive_copying
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_unexpected_side_effects
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Don't Mutate Input Parameters; Copy Before Mutating

## Pattern Rule
**IF** a function needs to work with values held in an object passed to it as a parameter
**THEN** treat that object as borrowed and leave it unchanged — copy the values into a new structure before mutating — rather than modifying the caller's object in place.

## Do
- Produce a new result instead of editing the input: filter the `userInvoices` map into a new list of billable invoices rather than calling `removeAll` on the map the caller still needs.
- If in-place mutation is genuinely required for performance — sorting a huge list, running on low-end hardware — make the function's name and documentation state plainly that it mutates its argument.

## Don't
- Don't quietly strip entries from a passed-in collection; removing free-trial users from the shared `userInvoices` map means a later step enables no services for them, a bug far from its cause.
- Don't assume mutating parameters is expected everywhere; conventions vary (C++ output parameters), so where it is not idiomatic it will surprise callers.

## Checklist
- Does this function change any object the caller passed in?
- If it must mutate for performance, does its name say so unmistakably?
- Could the caller reasonably still need that object intact after the call?

## Notes
Long's borrowed-book analogy names the failure: a function that mutates its input is like a friend who returns your book with pages torn out and margins scribbled on. The `getBillableInvoices` bug is textbook — it mutates the map it was only meant to read from, so a later reuse of that map silently misbehaves. Copying before mutating costs some memory and CPU, usually the lesser evil against such surprises; when in-place mutation is a necessary performance choice, honesty in the name is the mitigation. The flip side — defending objects you own from other code — is chapter 7's immutability.
