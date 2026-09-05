---
object_id: PAT_dont_leak_implementation_details_in_return_types
object_type: pattern
name: Don't Leak Implementation Details in Return Types
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
- abstraction
- modularity
- return_types
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_expose_clean_api_hide_implementation
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Don't Leak Implementation Details in Return Types

## Pattern Rule
**IF** a function, class, or module returns a value to its callers
**THEN** return a type appropriate to its own layer of abstraction, exposing only the concepts callers need, rather than a type coupled to how the class is implemented internally.

## Do
- Define a minimal type for exactly what the caller needs: a profile-picture lookup should expose a small custom status (success, user-does-not-exist, other-error) and a list of bytes, not the transport's own types.
- Judge the return type against the problem the class solves, not the tools it happens to use, and keep the exposed concepts to the minimum that problem requires.

## Don't
- Don't return a type that reveals an internal mechanism: returning an `HttpResponse.Status` and `HttpResponse.Payload` tells every caller the service uses HTTP and forces them to reason about dozens of HTTP status codes.
- Don't let callers become dependent on those leaked types; once they are, switching the implementation (say to a WebSocket) requires changes rippling across every caller.

## Checklist
- Does the return type name concepts from the class's own domain, or from its internals?
- Would changing the internal implementation force a change to this return type?
- Are you exposing the minimal set of concepts a caller actually needs?

## Notes
Return types sit in the unmistakable part of the contract, so a leak here is both easy to spot and easy to avoid once noticed. Long's `ProfilePictureService` returning HTTP response types is the anchor: it burdens callers with HTTP status semantics and cements the HTTP implementation into every dependent, making a later transport change hugely expensive. Defining a purpose-built result type restores the clean layer of abstraction — this is that leak rule applied specifically to what a function returns.
