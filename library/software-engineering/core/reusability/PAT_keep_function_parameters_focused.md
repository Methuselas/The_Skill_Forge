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
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u09, pp. 257-259
  evidence_type: text
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

## Don't
- Don't demand a whole object when one field will do; it makes the function unreusable elsewhere and makes callers fabricate values that imply effects that never happen.
- Don't overcorrect into unencapsulating everything; if a function genuinely needs most of a grouped object, passing the object beats threading many loose values, which harms modularity.

## Checklist
- Does the function read only a fraction of the object it takes?
- Are callers inventing irrelevant values just to satisfy the parameter?
- If it needs most of an encapsulating object, is passing the whole object the cleaner choice?

## Notes
An over-broad parameter couples a function to more than it uses, blocking reuse and misleading readers. Long's `setTextColor` taking a full `TextOptions` forces a warning-styler to concoct a font, size, and line height that suggest it sets them — it does not. Taking a color instead makes the function reusable and the call self-evident. The judgment clause guards against the opposite mistake from chapter 8: when a function needs most of a cohesive object, keep it encapsulated rather than exploding it into loose arguments.
