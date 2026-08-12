---
object_id: PAT_keep_immutable_with_builder_or_copy_on_write
object_type: pattern
name: Keep Classes Immutable With Builder or Copy-on-Write
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
- builder_pattern
- copy_on_write
- design_patterns
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_immutable_objects
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u07, pp. 175-181
  evidence_type: text
confidence: high
references: []
variants: []
---

# Keep Classes Immutable With Builder or Copy-on-Write

## Pattern Rule
**IF** a class needs to stay immutable but has optional construction values, or callers need a slightly modified version of an instance
**THEN** reach for a design pattern rather than adding setters — the builder pattern for optional values, or the copy-on-write pattern for modified copies.

## Do
- Use a builder when some values are optional: a mutable builder takes required values in its constructor and optional ones through chained setters, then `build()` returns the immutable object — so an invalid object cannot be constructed and no runtime check is needed.
- Use copy-on-write when callers need a tweaked instance: `with`-style functions (`withFontSize`) return a new object with one value changed and leave the original untouched, backed by a private all-values constructor.
- Prefer copy-on-write over the builder when getting modified copies is the common need, as prepopulating a builder from an existing instance is more cumbersome.

## Don't
- Don't add setters to make optional values or modified copies convenient; that reintroduces the mutability the class was made immutable to avoid.
- Don't require a caller to specify every optional value in one giant constructor; that is exactly the unwieldiness the builder exists to remove.

## Checklist
- Are optional values handled by a builder rather than by mutating the built object?
- Do modified copies come from copy-on-write functions that leave the original unchanged?
- Is it impossible to build an instance missing a required value?

## Notes
These are the two escape hatches that keep immutability practical. The builder splits `TextOptions` into a mutable `TextOptionsBuilder` and an immutable result, taking the required font in the builder's constructor so an invalid build cannot compile — a compile-time guarantee superior to a runtime check. Copy-on-write instead adds `withFont`/`withFontSize` that each mint a new instance, letting `renderTitle` get an 18-point copy without touching the caller's object. Both preserve the tamper-proof seal while restoring the flexibility that plain construction-only immutability lacks.
