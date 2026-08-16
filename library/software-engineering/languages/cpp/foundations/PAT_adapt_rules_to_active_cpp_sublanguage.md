---
object_id: PAT_adapt_rules_to_active_cpp_sublanguage
object_type: pattern
name: Adapt Your Rules to the Active C++ Sublanguage
library_path:
- software-engineering
- languages
- cpp
- foundations
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- sublanguages
- idioms
- parameter_passing
cross_links:
- rel: related_to
  target_object_id: PAT_manually_initialize_builtin_objects
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Adapt Your Rules to the Active C++ Sublanguage

## Pattern Rule
**IF** a "proper usage" rule of thumb you are applying in C++ seems to have exceptions
**THEN** work out which of C++'s four sublanguages you are in — C, Object-Oriented C++, Template C++, or the STL — and follow that sublanguage's conventions, expecting to switch strategy when you cross a boundary.

## Do
- Program the C part (built-in types, arrays, pointers, the preprocessor) with C-era rules: no templates, exceptions, or overloading, and pass small built-ins by value.
- Switch to pass-by-reference-to-const once you enter Object-Oriented C++, where user-defined constructors and destructors make copying expensive.
- Fall back to pass-by-value for STL iterators and function objects, which are modeled on C pointers.

## Don't
- Don't assume a single rule holds everywhere: what is right for the C part can be wrong in Template C++, where you may not even know the object's type.
- Don't drag template-metaprogramming rules into everyday code; they rarely interact with mainstream C++.

## Checklist
- Which of the four sublanguages does the code in front of me belong to?
- Does the rule I am about to apply change when I move to an adjacent sublanguage?
- Am I using the parameter-passing convention that fits this sublanguage?

## Notes
The federation-of-languages model is what makes C++'s contradictory advice cohere: within one sublanguage the rules are simple; the confusion comes from carrying a rule across a boundary. Meyers' anchor is parameter passing — value for C-like types, reference-to-const in the object-oriented and template worlds, then value again for STL iterators because they behave like pointers. Hold the four sublanguages in mind and the exceptions stop looking arbitrary.
