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
---

# Reuse Existing Solutions Instead of Reinventing

## Pattern Rule
**IF** a subproblem you face — reading bytes from a file, parsing an image format, low-level system communication — is likely already solved by the language or an existing library
**THEN** call the existing built-in or library rather than writing your own, and conversely structure the solutions you do write so other engineers can reuse them.

## Do
- Break the big problem into subproblems first (load bytes, parse to image, transform, encode, save), then check each subproblem against existing solutions before writing any of it.
- Weigh the four concrete benefits: it saves time (a few lines versus thousands and days of reading standards docs), lowers bug risk (existing code is already tested in the wild), inherits maintainers' expertise (they track changes like new JPEG encodings), and stays familiar (engineers recognize the standard approach).
- Pick the granularity, not just whether to reuse. The same idea is usually available at several levels — a library class holding a tested implementation, an abstract data type describing the concept, an algorithm given as pseudocode, or a pattern that is only an idea like "a class with a single instance." They trade the same two quantities against each other: the library end is ready to use and hard to bend, the pattern end bends to fit anything and makes you write all of it.
- Distrust a prepackaged component that does *most* of what you need. The gap shows up late — one method returning the wrong shape, then another accommodation, then the component discarded and that part written from scratch anyway. Where the fit is partial, taking the idea from a higher level and implementing it yourself produces something that fits exactly, because you built it for this problem.
- Recognise the ceiling that overrides the default. A first-class product may need its own scientific functions for speed or accuracy, or its own container, interface, and database classes so every surface has a consistent feel — but name the dimension the existing part falls short on before you build, because an unnamed dimension is an excuse rather than a reason.

## Don't
- Don't hand-roll low-level logic such as filesystem I/O or image parsing that a mature, maintained library already provides.
- Don't write your subproblem solution in a shape only you can call — leave it reusable so the next engineer doesn't reinvent it.

## Checklist
- For each subproblem, did you look for a built-in or library before coding it?
- Is the code you wrote for a subproblem structured so another engineer could reuse it?

## Notes
Long uses loading, grayscaling, and saving an image to show that most subproblems are already solved by the platform or a library. The rule runs both directions: consume others' solved subproblems, and expose your own solutions for reuse. This is goal 4 ("don't reinvent the wheel") made operational; the producing side is developed further under reusability and generalizability.

Variant `VAR_cpp_know_standard_library_and_tr1` (Effective C++, Items 54-55) supplies the C++ prerequisite for reuse: you cannot reach for existing solutions you do not know exist, so become familiar with the standard library and TR1 (smart pointers, function, bind, hash-based containers, algorithms) and with Boost, then prefer those vetted, portable, maintained facilities over hand-rolled equivalents. Use this emphasis when picking how to implement a C++ subproblem; the component inventories themselves are reference material, not skills, and were left unextracted.

The house-building parallel (Code Complete, ch. 2) is what makes the ceiling legible. Most of the time you buy the appliances and the prefabricated cabinets; when the house is a fancy one, the cabinets are custom-made and the appliances built in to match them. In software that means the case for building your own arrives only when the product's differentiator is precisely the dimension the off-the-shelf part is mediocre at — numerical accuracy, latency, or a consistent feel across every surface a user touches. Naming that dimension first is the whole discipline: if you cannot say which property the existing part falls short on, the default still holds. And the exception never reaches low-level infrastructure such as filesystem I/O or image parsing, which is exactly what this card exists to protect — no amount of product ambition makes a hand-rolled version of those better than a maintained library.
