---
object_id: PAT_provide_access_to_raw_resource_in_raii_class
object_type: pattern
name: Provide Access to the Raw Resource in an RAII Class
library_path:
- software-engineering
- languages
- cpp
- resource-management
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- raii
- resource_management
- conversions
cross_links:
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Provide Access to the Raw Resource in an RAII Class

## Pattern Rule
**IF** an RAII class wraps a resource that other APIs need in raw form
**THEN** give clients a way to obtain the raw resource — an explicit accessor such as get(), or an implicit conversion operator — choosing between them on safety versus convenience.

## Do
- Offer an explicit get() that returns the raw handle when you want to minimize accidental conversions; this is the safer default.
- Offer an implicit conversion operator when frequent API calls make explicit get() calls onerous enough that clients might avoid the class and leak the resource instead.

## Don't
- Don't treat an implicit conversion as risk-free: a client can accidentally obtain and copy the raw handle when they meant to copy the managing object, leaving a handle that dangles once the manager releases it.

## Checklist
- Can clients reach the raw resource when an API requires it?
- Did I weigh explicit access (safer) against implicit conversion (more convenient) for this class's use?
- Would an implicit conversion here let a raw handle escape by accident?

## Notes
Real APIs demand raw resources, so an RAII class that hides its resource completely becomes unusable. Smart pointers show both routes: an explicit get() plus implicit access through operator-> and operator*. The `Font`/`FontHandle` example weighs a get() accessor against an implicit conversion operator; implicit wins on convenience but risks a stray handle (the `FontHandle f2 = f1` slip). RAII exists to guarantee release, not to encapsulate, so exposing the raw resource is not a design failure.
