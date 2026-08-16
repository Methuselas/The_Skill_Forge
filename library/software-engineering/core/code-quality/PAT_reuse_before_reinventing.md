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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_cpp_know_standard_library_and_tr1
  variant_name: Know the C++ Standard Library and TR1 So You Reuse Them
  variant_basis: emphasis
  difference_from_foundation: Frames reuse as first being familiar with the C++ standard library and TR1 (smart pointers, function, bind, hash containers, algorithms) and with Boost, so you reach for these vetted, portable, well-maintained facilities instead of hand-rolling equivalents; familiarity is the prerequisite for reuse in C++.
  when_to_use: Implementing a C++ subproblem that a standard library, TR1, or Boost facility likely already covers.
  when_not_to_use: When no suitable standard/TR1/Boost facility exists, or an added dependency is unacceptable.
  absorbed_from_object_id: none
- variant_id: VAR_custom_build_for_a_first_class_product
  variant_name: Custom-Build the Parts a First-Class Product Cannot Buy
  variant_basis: constraint
  difference_from_foundation: The foundation reaches for the existing solution whenever one plausibly exists. This variant adds the quality ceiling that overrides it — a first-class product may need its own scientific functions for better speed or accuracy, or its own container, user interface, and database classes so the system has a seamless, perfectly consistent look and feel. The house-building parallel is exact — you buy the appliances and the prefabricated cabinets, unless you are building a fancy house, in which case the cabinets are custom-made and the appliances are built in to match them.
  when_to_use: Use when the product's differentiator is precisely the dimension the off-the-shelf part is mediocre at — numerical accuracy, latency, or a consistent feel across every surface a user touches. Naming that dimension first is what separates this from an excuse.
  when_not_to_use: Do not use it to justify hand-rolling filesystem I/O, image parsing, or other low-level infrastructure. Those are the cases the foundation is about, and no amount of product ambition makes writing your own better than a maintained library.
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

Variant `VAR_custom_build_for_a_first_class_product` (Code Complete, ch. 2) supplies the ceiling that overrides the default. Most of the time you buy the appliances and the prefabricated cabinets; when the house is a fancy one, the cabinets are custom-made and the appliances built in to match. In software that means a first-class product may want its own scientific functions for better speed or accuracy, or its own container, user interface, and database classes so that every surface has a consistent feel. The discipline that keeps this from becoming a licence to rewrite everything is naming the dimension first: if you cannot say which specific property — accuracy, latency, consistency — the existing part falls short on, the foundation still applies. It never covers low-level infrastructure such as filesystem I/O or image parsing, which is what the foundation exists to protect.
