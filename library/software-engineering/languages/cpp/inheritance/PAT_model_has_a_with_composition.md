---
object_id: PAT_model_has_a_with_composition
object_type: pattern
name: Model Has-A and Is-Implemented-In-Terms-Of with Composition
library_path:
- software-engineering
- languages
- cpp
- inheritance
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- composition
- inheritance
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_composition_over_inheritance
- rel: related_to
  target_object_id: PAT_use_public_inheritance_only_for_is_a
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u06, pp. 184-186
  evidence_type: text
confidence: high
references: []
variants: []
---

# Model Has-A and Is-Implemented-In-Terms-Of with Composition

## Pattern Rule
**IF** the relationship between two types is has-a (application domain) or is-implemented-in-terms-of (implementation domain) rather than is-a
**THEN** model it with composition — one object holding another as a member — not with public inheritance.

## Do
- Use composition for application-domain has-a: a Person has a name, an address, and phone numbers, so it holds them as members.
- Use composition for implementation-domain is-implemented-in-terms-of: a Set implemented on a list holds a list member and forwards member/insert/remove/size to it.
- Give the composing class only the interface that fits it, delegating to the contained object rather than exposing the contained object's whole interface.

## Don't
- Don't reach for public inheritance because the contained type already has useful functions; a Set is not-a list (a list allows duplicates, a Set does not), so deriving Set from list is wrong.
- Don't confuse the two composition meanings — has-a is about modeled things, is-implemented-in-terms-of is about implementation artifacts — but note both map to composition, not inheritance.

## Checklist
- Is this relationship has-a or is-implemented-in-terms-of rather than is-a?
- Am I holding the other type as a member and forwarding, instead of inheriting publicly?
- Does public inheritance here import behavior (like duplicate storage) that breaks the new type's contract?

## Notes
Composition has two meanings that both point away from public inheritance: has-a for application objects (Person has an Address) and is-implemented-in-terms-of for implementation objects (Set built on list). The Set/list case is the trap — list looks reusable, but is-a fails because a list may hold duplicates and a Set may not, so Set holds a list member and delegates. Reserve public inheritance for genuine is-a; use composition for the rest.
