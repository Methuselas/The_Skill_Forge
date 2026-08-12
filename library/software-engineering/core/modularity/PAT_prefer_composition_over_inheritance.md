---
object_id: PAT_prefer_composition_over_inheritance
object_type: pattern
name: Prefer Composition Over Class Inheritance
library_path:
- software-engineering
- core
- modularity
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- composition
- inheritance
- modularity
- interfaces
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
- rel: related_to
  target_object_id: PAT_depend_on_interfaces_not_concrete_classes
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u08, pp. 215-225
  evidence_type: text
confidence: high
references: []
variants: []
---

# Prefer Composition Over Class Inheritance

## Pattern Rule
**IF** you want to reuse another class's functionality
**THEN** compose it in — hold an instance (ideally typed as an interface) and forward the calls you need — rather than inheriting from it, reserving inheritance for genuine is-a relationships and even then weighing its pitfalls.

## Do
- Hold and forward instead of extend: an `IntFileReader` that contains a `FileValueReader` and forwards `close()` exposes only `getNextInt` and `close`, not the whole file handler.
- Depend on the interface you compose so you can reconfigure: because `IntFileReader` takes a `FileValueReader`, it works with a comma-separated or semicolon-separated handler through a factory, with no duplicated class.
- For a real hierarchy, define the hierarchy with interfaces and reuse code through composition — cars implement a `Car` interface and hold a `DrivingAction` — which sidesteps single-inheritance dead-ends like a flying car that is both a car and an aircraft.

## Don't
- Don't extend a class just to reuse it; inheritance drags the whole superclass API into your public API, so an integer reader ends up exposing `getNextValue` and `writeValue`, freezing the implementation once callers use them.
- Don't accept the inheritance duplication tax: needing a semicolon variant forces a near-duplicate subclass, whereas composition needs only a different injected handler.
- Don't assume a genuine is-a makes inheritance safe; the fragile base class problem and the diamond problem still bite.

## Checklist
- Are you reusing a class by containing it or by extending it?
- Does your public API expose only your own functions, or also everything inherited?
- Would supporting a sibling implementation force a duplicate subclass, or just a different injected instance?

## Notes
Long's `IntFileReader` example is the case against inheritance-for-reuse: extending `CsvFileHandler` leaks its reader-and-writer API and, when a semicolon format arrives, forces a duplicate `SemicolonIntFileReader`. Composition — holding a `FileValueReader` injected through the constructor and forwarding `close` — yields a clean API and trivial reconfiguration, with delegation features easing the forwarding boilerplate. Even genuine is-a relationships carry the fragile-base-class, diamond, and single-inheritance hazards, so the durable stance is interfaces for hierarchy plus composition for reuse.
