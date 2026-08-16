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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_choose_containment_or_inheritance_by_what_is_shared
  variant_name: Choose Containment or Inheritance by What Is Shared
  variant_basis: method_sequence
  difference_from_foundation: The foundation defaults to composition and reserves inheritance for genuine is-a relationships. This variant supplies a four-way decision procedure for the same question, keyed on what the classes actually share. Common data but not behaviour - create a common object for them to contain. Common behaviour but not data - derive from a common base class defining the routines. Common data and behaviour - inherit from a base class defining both. And the control test cutting across all three - inherit when you want the base class to control your interface, contain when you want to control it yourself.
  when_to_use: Use when several classes visibly overlap and the is-a question is genuinely ambiguous, which is where a default alone gives no traction. Also use its repair rule - a derived class that overrides a routine to do nothing means the base class asserted something untrue, so fix it at the source by extracting the optional capability into its own contained class rather than bandaging the descendant.
  when_not_to_use: Do not read the third case as licence for depth. Deep inheritance trees are significantly associated with increased fault rates, most people cannot hold more than two or three levels at once, and a base class with exactly one derived class usually means somebody was designing ahead.
  absorbed_from_object_id: none
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

`VAR_choose_containment_or_inheritance_by_what_is_shared` adds a decision procedure where this foundation gives a default. Sorting by *what is shared* - data, behaviour, or both - resolves cases the is-a test leaves ambiguous, and the control question underneath it is the sharper one: inheriting hands your interface to the base class, containing keeps it. McConnell's own explanation for why the section needs so many rules is worth carrying - inheritance works against the primary technical imperative of managing complexity, so the bias against it is deliberate rather than stylistic. Two of his diagnostics travel especially well. A derived class that overrides a routine to do nothing, the declawed cat given a no-op scratch, is evidence the base class claimed something false about its subjects, and the fix belongs in the base by extracting the capability into a contained object. And a base class with a single derived class is usually anticipation rather than abstraction.
