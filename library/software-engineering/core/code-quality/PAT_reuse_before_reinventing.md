---
object_id: PAT_reuse_before_reinventing
object_type: pattern
name: Reuse Existing Solutions Instead of Reinventing
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- reuse
- libraries
- code_quality
- decomposition
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_reusable_and_generalizable
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u01, pp. 10-11
  evidence_type: text
confidence: high
references: []
variants:
- variant_id: VAR_cpp_know_standard_library_and_tr1
  variant_name: Know the C++ Standard Library and TR1 So You Reuse Them
  variant_basis: emphasis
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  locator: u09, pp. 263-272
  difference_from_foundation: Frames reuse as first being familiar with the C++ standard library and TR1 (smart pointers, function, bind, hash containers, algorithms) and with Boost, so you reach for these vetted, portable, well-maintained facilities instead of hand-rolling equivalents; familiarity is the prerequisite for reuse in C++.
  when_to_use: Implementing a C++ subproblem that a standard library, TR1, or Boost facility likely already covers.
  when_not_to_use: When no suitable standard/TR1/Boost facility exists, or an added dependency is unacceptable.
  absorbed_from_object_id: none
---

# Reuse Existing Solutions Instead of Reinventing

## Pattern Rule
**IF** a subproblem you face — reading bytes from a file, parsing an image format, low-level system communication — is likely already solved by the language or an existing library
**THEN** call the existing built-in or library rather than writing your own, and conversely structure the solutions you do write so other engineers can reuse them.

## Do
- Break the big problem into subproblems first (load bytes, parse to image, transform, encode, save), then check each subproblem against existing solutions before writing any of it.
- Weigh the four concrete benefits: it saves time (a few lines versus thousands and days of reading standards docs), lowers bug risk (existing code is already tested in the wild), inherits maintainers' expertise (they track changes like new JPEG encodings), and stays familiar (engineers recognize the standard approach).

## Don't
- Don't hand-roll low-level logic such as filesystem I/O or image parsing that a mature, maintained library already provides.
- Don't write your subproblem solution in a shape only you can call — leave it reusable so the next engineer doesn't reinvent it.

## Checklist
- For each subproblem, did you look for a built-in or library before coding it?
- Is the code you wrote for a subproblem structured so another engineer could reuse it?

## Notes
Long uses loading, grayscaling, and saving an image to show that most subproblems are already solved by the platform or a library. The rule runs both directions: consume others' solved subproblems, and expose your own solutions for reuse. This is goal 4 ("don't reinvent the wheel") made operational; the producing side is developed further under reusability and generalizability.

Variant `VAR_cpp_know_standard_library_and_tr1` (Effective C++, Items 54-55) supplies the C++ prerequisite for reuse: you cannot reach for existing solutions you do not know exist, so become familiar with the standard library and TR1 (smart pointers, function, bind, hash-based containers, algorithms) and with Boost, then prefer those vetted, portable, maintained facilities over hand-rolled equivalents. Use this emphasis when picking how to implement a C++ subproblem; the component inventories themselves are reference material, not skills, and were left unextracted.
