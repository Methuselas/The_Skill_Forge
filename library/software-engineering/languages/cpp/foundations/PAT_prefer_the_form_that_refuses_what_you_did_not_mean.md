---
object_id: PAT_prefer_the_form_that_refuses_what_you_did_not_mean
object_type: pattern
name: Prefer the Form That Refuses What You Did Not Mean
library_path:
- software-engineering
- languages
- cpp
- foundations
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- type_safety
- modernization
- overloading
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_adapt_rules_to_active_cpp_sublanguage
- rel: related_to
  target_object_id: PAT_delete_the_functions_you_want_to_forbid
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
- rel: related_to
  target_object_id: PAT_prefer_auto_for_local_variables
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Prefer the Form That Refuses What You Did Not Mean

## Pattern Rule
**IF** you are writing a construct that has both a permissive C++98 spelling and a narrower modern one — a null pointer, an enumeration, a type alias, an iterator
**THEN** take the narrower spelling, because what it buys is not brevity but the refusal of uses you never intended
**ELSE** where you are maintaining code that must build under C++98, the older forms are what you have, and the point is to know what each one fails to prevent.

## Do
- Write `nullptr` rather than `0` or `NULL`, and treat the reason as correctness rather than style. Neither `0` nor `NULL` has a pointer type, so a call passing one to overloads on integer and pointer selects the integer overload. The decisive case is templates: passing `0` through a forwarding function deduces `int`, and the call to a function expecting a smart pointer then fails to compile, having been told the argument was an integer. `nullptr` deduces its own type, which converts to every pointer type and to no integral one.
- Keep the older guideline that goes with it, since it survives: avoid overloading on integral and pointer types at all, because some callers will keep writing `0`.
- Use alias declarations rather than typedefs. Typedefs cannot be templatized, so the C++98 workaround is a nested type inside a struct, which callers must reach through a trailing `::type` and, inside templates, prefix with `typename` because the compiler cannot tell whether the name is a type. An alias template is a type directly and needs neither.
- Use scoped enumerations, whose enumerators are visible only inside the enumeration and convert to other types only with a cast. Unscoped enumerators leak into the surrounding scope, where they collide with other names, and convert implicitly to numbers, where they participate in arithmetic and comparisons nobody intended.
- Ask for `const_iterator` wherever you are not modifying. It states that the traversal is read-only, and the practical objection from C++98 — that the standard containers made const iterators awkward to obtain and unusable where an iterator was expected — no longer applies.
- Prefer the non-member forms of `begin`, `end`, and their reverse counterparts in maximally generic code, since types you do not control may not have the member versions.

## Don't
- Don't treat these as cosmetic modernizations to be applied when convenient. Each of the older forms is permissive in a specific way, and each replacement is narrower in exactly that way — the value is in what stops compiling.
- Don't assume the old spelling is harmless because the code works today. `0` as a null pointer works until the call goes through a template; an unscoped enumerator works until a name collides or a comparison against an unrelated enumeration silently succeeds.
- Don't reach for a cast to make a scoped enumeration behave like an unscoped one. The refusal is the feature; needing to convert repeatedly is a sign the underlying type, not the enumeration, is what the code wants.
- Don't read `nullptr` as merely clearer at a call site. It is that too — a comparison against `nullptr` tells a reader the operand is a pointer, which a comparison against `0` does not — but clarity is the smaller half.

## Checklist
- Does any function here overload on both an integral and a pointer type?
- Could a null pointer argument reach a function through a template, and what type would be deduced?
- Do any enumerators appear in the enclosing scope, or convert to numbers, where they should not?
- Is a type alias here blocked from being templatized by being a typedef?
- Is a traversal declared with an iterator where nothing is modified?

## Notes
The four replacements are separate items and they share one shape, which is why they belong together: the older construct is untyped or unscoped, and the newer one carries the information the older one discarded. `nullptr` has a type instead of being an integer that gets reinterpreted. A scoped enumeration has a scope and refuses implicit conversion. An alias declaration is a type rather than a member of a struct. A `const_iterator` says what a plain iterator leaves unsaid.

The reason this matters more in modern C++ than it did is templates and deduction. When a value is passed straight to a known function, an untyped construct usually reaches its intended meaning through a conversion. When it passes through a deduced context, deduction fixes the type as what it actually is rather than what it was meant for, and the mismatch surfaces somewhere else entirely — or does not surface at all.

There is a general form of this worth holding beyond the four instances, since C++ keeps adding them: prefer the spelling whose failures happen at the point of the mistake. That is the same standard by which deleted functions beat private undefined ones, and by which a narrow interface beats a permissive one — the value of a language feature is often measured by what it refuses.
