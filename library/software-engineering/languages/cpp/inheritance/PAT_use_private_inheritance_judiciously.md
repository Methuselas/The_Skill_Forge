---
object_id: PAT_use_private_inheritance_judiciously
object_type: pattern
name: Use Private Inheritance Only When Composition Cannot Do the Job
library_path:
- software-engineering
- languages
- cpp
- inheritance
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- private_inheritance
- composition
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_model_has_a_with_composition
- rel: related_to
  target_object_id: PAT_use_multiple_inheritance_judiciously
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u06, pp. 187-192
  evidence_type: text
confidence: high
references: []
variants: []
---

# Use Private Inheritance Only When Composition Cannot Do the Job

## Pattern Rule
**IF** a relationship is is-implemented-in-terms-of
**THEN** model it with composition by default, and use private inheritance only when you must access the other class's protected members or redefine its virtual functions.

## Do
- Default to composition for is-implemented-in-terms-of; it is easier to understand and keeps the borrowed interface out of your class's public face.
- Reach for private inheritance when you must redefine an inherited virtual (a Widget privately inheriting Timer to override onTick) or reach protected members.
- Consider a nested class that publicly inherits the helper (a private WidgetTimer) as a composition-based alternative that also blocks further overriding and cuts compilation dependencies.

## Don't
- Don't use private inheritance where composition works; private inheritance means implementation only, so it buys nothing over a member except when virtuals or protected access are involved.
- Don't mistake private inheritance for is-a; the compiler will not convert a privately-derived object to its base, and all inherited members become private.

## Checklist
- Is this is-implemented-in-terms-of (not is-a)?
- Do I actually need to redefine a virtual or reach protected members — or will composition suffice?
- Would a nested publicly-inheriting helper give the same result with less coupling?

## Notes
Private inheritance means is-implemented-in-terms-of, the same as composition, so composition wins by default. Its narrow justification is redefining inherited virtuals or reaching protected members — the Widget/Timer onTick case. Even then a private nested class that publicly inherits the helper often works and adds the ability to stop derived classes overriding the virtual and to reduce compilation dependencies. One niche bonus: private inheritance enables the empty base optimization, which composition cannot, occasionally mattering to library authors minimizing object size.
