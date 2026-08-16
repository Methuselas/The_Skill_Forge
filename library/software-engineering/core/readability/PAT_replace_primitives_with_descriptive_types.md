---
object_id: PAT_replace_primitives_with_descriptive_types
object_type: pattern
name: Replace Primitive Parameters With Descriptive Types
library_path:
- software-engineering
- core
- readability
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- types
- readability
- hard_to_misuse
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_use_named_arguments_for_readable_calls
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Replace Primitive Parameters With Descriptive Types

## Pattern Rule
**IF** a function parameter is a bare primitive whose meaning is ambiguous — an `Int` that is really a priority, a `Boolean` that is really a policy
**THEN** give it a descriptive type that names what it represents, so the call site is readable whether or not the language has named arguments.

## Do
- Wrap a bare number in a purpose type: make the priority parameter a `MessagePriority` class rather than a raw `Int`.
- Replace a bare Boolean with an enum that names both states: `RetryPolicy.ALLOW_RETRY` / `DISALLOW_RETRY` instead of `true`/`false`, so `sendMessage("hello", new MessagePriority(1), RetryPolicy.ALLOW_RETRY)` reads clearly.

## Don't
- Don't leave `Int` and `Boolean` parameters to mean "all manner of things depending on the scenario"; the reader cannot recover the meaning from the type.
- Don't rely on a Boolean flag where the two states are not obvious from context — an enum names them and is harder to pass wrongly.

## Checklist
- Does each parameter's type name what it represents, not just its primitive shape?
- Are two-state flags expressed as named enum values rather than bare Booleans?
- Is the call readable from the types alone, independent of named-argument support?

## Notes
This is the stronger remedy when call-site fixes fall short: an `Int priority` and `Boolean allowRetry` say nothing, but a `MessagePriority` type and a `RetryPolicy` enum make every call self-describing regardless of language features. Beyond readability, naming the type narrows what can be passed, which is why it also serves the hard-to-misuse pillar; chapter 7 develops dedicated types further as a defense against misuse.
