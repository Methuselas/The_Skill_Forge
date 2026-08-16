---
object_id: PAT_prefer_const_and_enum_to_define
object_type: pattern
name: 'Prefer const Objects and enums to #define Constants'
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
- constants
- enum_hack
cross_links:
- rel: related_to
  target_object_id: PAT_name_unexplained_values
- rel: related_to
  target_object_id: PAT_prefer_inline_functions_to_macro_functions
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Prefer const Objects and enums to #define Constants

## Pattern Rule
**IF** you need a symbolic constant in C++
**THEN** define it as a `const` object — or, for a compile-time integral value, an `enum` — rather than a `#define`, so the name reaches the compiler's symbol table and obeys scope.

## Do
- Replace `#define ASPECT_RATIO 1.653` with `const double AspectRatio = 1.653;` so the name survives into the symbol table and debugger, and the literal is stored once instead of copied at every use.
- Scope a class constant by making it a `static const` member; supply a separate out-of-class definition only if you take its address.
- Use the "enum hack" — `enum { NumTurns = 5 };` — when you need an integral constant expression during compilation (an array bound, say) or want to forbid taking the constant's address or allocating storage for it.

## Don't
- Don't leave a constant as a `#define` you might meet in a compiler error: the macro name vanishes before compilation, so the message cites the bare literal `1.653` and you waste time hunting its origin.
- Don't expect a macro to respect class scope or privacy — there is no such thing as a private `#define` constant.

## Checklist
- Is this constant visible to the compiler and debugger by its name?
- If it belongs to a class, is it a `static const` member or an `enum` rather than a macro?
- Do I need a compile-time integral value or to block address-taking? Then reach for the enum.

## Notes
The theme is "prefer the compiler to the preprocessor." A `#define` is text-substituted before compilation, so it has no symbol-table entry, no scope, and can bloat object code with repeated literals. A `const` fixes the first two; the enum hack covers the case where you need a compile-time integral constant an old compiler won't accept as an in-class `static const`, and as a bonus it can't have its address taken and allocates no storage — behaving more like a `#define` where that is what you want. The enum hack is also foundational to template metaprogramming, so it is worth recognizing on sight.
