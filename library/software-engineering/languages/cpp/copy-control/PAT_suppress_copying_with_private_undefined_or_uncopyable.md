---
object_id: PAT_suppress_copying_with_private_undefined_or_uncopyable
object_type: pattern
name: Suppress Unwanted Copying by Making Copy Operations Private and Undefined
library_path:
- software-engineering
- languages
- cpp
- copy-control
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- copy_control
- hard_to_misuse
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_know_compiler_generated_special_members
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u02, pp. 37-40
  evidence_type: text
confidence: high
references: []
variants: []
---

# Suppress Unwanted Copying by Making Copy Operations Private and Undefined

## Pattern Rule
**IF** a class models something that must not be copied — a unique entity, a sole resource owner
**THEN** stop copying by declaring the copy constructor and copy assignment operator private and leaving them undefined, or by inheriting from a small Uncopyable base, so copy attempts do not compile or link.

## Do
- Declare both copy operations private with no bodies; a member or friend that copies then fails at link time.
- Push the failure to compile time by inheriting privately from an Uncopyable base whose copy operations are themselves private and undefined.
- Omit the parameter names on those declarations — the functions are never defined or called.

## Don't
- Don't just leave the copy operations undeclared; the compiler then generates public ones and the class becomes silently copyable.

## Checklist
- Are both the copy constructor and copy assignment operator suppressed, not only one?
- Is a copy attempt rejected at link time (private and undefined) or compile time (Uncopyable base)?

## Notes
Because the generated copy operations are public, the only way to block copying is to declare them yourself and deny access. Private-and-undefined turns a copy into a link error; an `Uncopyable` base (Boost calls it `noncopyable`) turns it into a compile error, which is better because it surfaces earlier. In C++11 the direct successor is `= delete` (see *Effective Modern C++*); this Item is the pre-C++11 idiom. It is the C++ mechanism for making a whole capability impossible rather than merely discouraged.
