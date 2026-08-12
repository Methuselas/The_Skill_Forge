---
object_id: PAT_manually_initialize_builtin_objects
object_type: pattern
name: Manually Initialize Objects of Built-in Type Before Use
library_path:
- software-engineering
- languages
- cpp
- initialization
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- initialization
- undefined_behavior
- builtins
cross_links:
- rel: related_to
  target_object_id: PAT_adapt_rules_to_active_cpp_sublanguage
- rel: related_to
  target_object_id: PAT_initialize_members_with_init_list
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u01, pp. 26-27
  evidence_type: text
confidence: high
references: []
variants: []
---

# Manually Initialize Objects of Built-in Type Before Use

## Pattern Rule
**IF** you declare a non-member object of built-in type (int, pointer, double, and the like)
**THEN** give it an explicit initial value, because C++ only sometimes zero-initializes built-ins and reading an uninitialized one is undefined behavior.

## Do
- Initialize at the point of declaration: `int x = 0;`, `const char* text = "A C-style string";`, or "initialize" by reading a value in with `std::cin >> d;`.
- Remember the sublanguage split: an array from the C part of C++ is not guaranteed to have its contents initialized, whereas an STL `vector` is — so initialize the array yourself.

## Don't
- Don't assume `int x;` or a struct of built-ins like `Point p;` comes out zeroed; whether it does depends on context, and guessing wrong hands you semi-random bits that pollute later reads and produce inscrutable bugs.

## Checklist
- Does every built-in object receive an explicit value before its first read?
- Am I relying on a zero-initialization the standard does not actually guarantee in this context?
- Is this an array (C part) I must initialize by hand rather than a vector (STL part)?

## Notes
C++ is deliberately inconsistent about initializing built-ins so it can avoid a runtime cost in the C-like part of the language — which is why the guarantee tracks the sublanguage (see the federation-of-languages rule). The safe habit is simply to always initialize before use: for non-member built-ins that means doing it by hand, since no constructor will do it for you. The cost of a missed initialization is undefined behavior, up to and including a program that halts on the read.
