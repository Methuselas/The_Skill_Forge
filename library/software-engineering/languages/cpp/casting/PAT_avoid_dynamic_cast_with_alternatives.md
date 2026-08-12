---
object_id: PAT_avoid_dynamic_cast_with_alternatives
object_type: pattern
name: Avoid dynamic_cast with Virtuals or Type-Safe Containers
library_path:
- software-engineering
- languages
- cpp
- casting
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- casting
- polymorphism
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_minimize_and_prefer_cpp_style_casts
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u05, pp. 119-123
  evidence_type: text
confidence: high
references: []
variants: []
---

# Avoid dynamic_cast with Virtuals or Type-Safe Containers

## Pattern Rule
**IF** you are tempted to dynamic_cast a base pointer down to a derived type so you can call a derived operation
**THEN** redesign to remove the cast — store derived pointers in a type-safe container, or declare a virtual function on the base — because dynamic_cast is often slow and cascades of it are brittle.

## Do
- Hold the objects in a container of pointers to the derived type when only that type is involved, so no cast is needed to call its operations.
- Move the operation into the base class as a virtual function, giving it a safe default, so you call it through the base interface with no cast.

## Don't
- Don't write cascading if/else dynamic_cast chains; they generate big, slow code and must be revisited every time the hierarchy changes.
- Don't reach for dynamic_cast in performance-sensitive code; some implementations compare class-name strings, so a deep hierarchy costs several comparisons per cast.

## Checklist
- Can a type-safe container or a base-class virtual remove this dynamic_cast?
- Am I about to write a chain of dynamic_casts that a single virtual call would replace?
- Is this dynamic_cast sitting in a hot path?

## Notes
When only `SpecialWindow` objects blink, a container of pointers to that type calls blink() directly; a mixed container instead gets a virtual blink() on `Window` with a no-op default. Either removes the cast. Cascading dynamic_casts are the worst case — big, slow, and needing an edit for every new derived class — and should be replaced with virtual dispatch. dynamic_cast also carries a real runtime cost, so keep it out of hot code.
