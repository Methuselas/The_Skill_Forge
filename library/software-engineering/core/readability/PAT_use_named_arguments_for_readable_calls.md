---
object_id: PAT_use_named_arguments_for_readable_calls
object_type: pattern
name: Make Call-Site Arguments Self-Explanatory
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- named_arguments
- function_calls
- readability
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
- rel: related_to
  target_object_id: PAT_replace_primitives_with_descriptive_types
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 120-124
  evidence_type: text
confidence: high
references: []
variants: []
---

# Make Call-Site Arguments Self-Explanatory

## Pattern Rule
**IF** a function call's bare arguments do not reveal what they mean — like `sendMessage("hello", 1, true)`
**THEN** make each value's meaning visible at the call site, using named arguments where the language supports them, and a documented fallback where it does not.

## Do
- Use named arguments so the call reads without opening the definition: `sendMessage(message: "hello", priority: 1, allowRetry: true)`.
- Where the language lacks them, use a conventional workaround engineers recognize — object destructuring of a params object in TypeScript achieves the same association of names to values.
- As a last resort for something like a four-integer `BoundingBox(10, 50, 20, 5)` constructor, add inline argument comments (`/* top= */ 10`), accepting they can go stale.

## Don't
- Don't leave a reader to guess what `1` and `true` mean and then hunt down the definition, possibly in another file hundreds of lines away.
- Don't rely on an IDE that displays argument names to make the code readable — merge tools, review tools, and other engineers' setups may not show them.

## Checklist
- Can a reader tell what every argument means without opening the callee?
- If named arguments are unavailable, is there a recognized workaround or documented fallback in place?
- Are same-typed positional arguments (four integers) protected against being silently reordered?

## Notes
The `sendMessage("hello", 1, true)` call is unreadable because positional primitives carry no meaning; the readable fix depends on language support, so Long ranks the options — true named arguments, a familiar destructuring workaround, then inline comments as an unsatisfactory last resort whose staleness risk can make a wrong comment worse than none. He also warns against leaning on IDE argument-name overlays, since code is read in many tools that lack them. When there is no good call-site fix, descriptive parameter types are the stronger remedy.
