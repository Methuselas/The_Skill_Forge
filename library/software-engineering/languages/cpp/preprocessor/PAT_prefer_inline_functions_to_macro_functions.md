---
object_id: PAT_prefer_inline_functions_to_macro_functions
object_type: pattern
name: Prefer inline Functions to Function-Like Macros
library_path:
- software-engineering
- languages
- cpp
- preprocessor
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: PAT_adopt_language_features_when_best_tool
tags:
- cpp
- preprocessor
- inline
- templates
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_const_and_enum_to_define
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u01, pp. 16-17
  evidence_type: text
confidence: high
references: []
variants: []
---

# Prefer inline Functions to Function-Like Macros

## Pattern Rule
**IF** you are tempted to write a function-like macro to dodge call overhead
**THEN** write an `inline` function instead — a template if the argument types vary — so you keep the speed without the macro's evaluation and type hazards.

## Do
- Turn `#define CALL_WITH_MAX(a,b) f((a) > (b) ? (a) : (b))` into an `inline` function template `callWithMax` that takes `const T& a, const T& b` and calls `f(a > b ? a : b)`.
- Pass by reference-to-const in the template so it works without knowing `T`, and let `inline` recover the macro's efficiency.

## Don't
- Don't accept a macro's evaluation surprises: `CALL_WITH_MAX(++a, b)` increments `a` a different number of times depending on the value it is compared against.
- Don't lean on remembering to parenthesize every macro argument; a real function needs none of that and still honors scope and access rules, so it can even be private to a class.

## Checklist
- Does this genuinely need to be a macro, or will an inline function do?
- Could any argument be evaluated more than once when passed to the macro?
- Would a member or private inline function express this more safely?

## Notes
A function-like macro buys speed at the cost of predictability: arguments can be evaluated the wrong number of times, and the whole thing ignores scope and access. An inline function gives the same no-call-overhead performance while behaving like the real function it is — type-checked, single-evaluation, scoped. `#include`, `#ifdef`, and `#ifndef` still earn their keep, but function-like `#define` macros almost never do.
