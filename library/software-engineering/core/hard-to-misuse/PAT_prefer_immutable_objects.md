---
object_id: PAT_prefer_immutable_objects
object_type: pattern
name: Prefer Immutable Objects Set Only at Construction
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- immutability
- hard_to_misuse
- class_design
- concurrency
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_dont_mutate_input_parameters
- rel: related_to
  target_object_id: PAT_make_misuse_impossible_by_removing_invalid_states
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u07, pp. 171-175
  evidence_type: text
confidence: high
references: []
variants: []
---

# Prefer Immutable Objects Set Only at Construction

## Pattern Rule
**IF** you are designing a class whose instances will be passed around to other code
**THEN** default to making it immutable — take all values at construction, mark the members final (const/readonly), and provide no setters — so no other code can change it after creation, making it mutable only where mutation is genuinely required.

## Do
- Remove setter functions and set every member in the constructor; marking `font` and `fontSize` final stops even code inside the class from reassigning them and signals they never change.
- Treat immutability as a tamper-proof seal: an immutable object can be passed anywhere with certainty that no caller altered it, the way a sealed juice carton guarantees its contents.
- Lean on immutability for thread safety — a mutable object read by one thread while another modifies it is a classic source of concurrency bugs that immutability removes.

## Don't
- Don't expose setters on a value class; a `renderTitle` that calls `setFontSize(18)` on a shared instance silently changes the font size seen by the next caller.
- Don't make things mutable by default "just in case"; mutable objects are harder to reason about, so reserve mutability for the parts of the code that must track changing state.

## Checklist
- Can any code change this object's state after construction?
- Are all members final and set once, with no setter functions?
- Would passing this object to another function risk it being mutated underneath you?

## Notes
This is the core hard-to-misuse technique the book pointed toward from chapters 3 and 6. The `TextOptions` setter bug is the anchor: a shared instance mutated by one render call corrupts the next, and removing setters plus final members makes that impossible. Immutability also answers the reason-about-it and multithreading concerns raised earlier. The one wrinkle — needing an optional value or a modified copy — is handled by the builder and copy-on-write patterns rather than by reintroducing mutability.
