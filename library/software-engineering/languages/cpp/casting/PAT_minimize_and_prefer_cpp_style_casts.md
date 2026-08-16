---
object_id: PAT_minimize_and_prefer_cpp_style_casts
object_type: pattern
name: Minimize Casting and Prefer C++-Style Casts
library_path:
- software-engineering
- languages
- cpp
- casting
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- casting
- type_safety
- maintainability
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_dynamic_cast_with_alternatives
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Minimize Casting and Prefer C++-Style Casts

## Pattern Rule
**IF** you find yourself writing a cast
**THEN** minimize it, and when a cast is genuinely needed use the named C++-style casts (static_cast, const_cast, dynamic_cast, reinterpret_cast) rather than an old C-style cast.

## Do
- Prefer the named C++ casts: they are easy to spot for you and for tools, and each has a narrow, compiler-checkable purpose.
- Hide a necessary cast inside a function so callers work with a clean interface instead of scattering casts through their code.
- Remember casts can run real code: an int-to-double conversion or a derived-pointer to base-pointer conversion may change representation or apply an address offset at runtime.

## Don't
- Don't cast *this to a base type to call a base version of a function; that operates on a temporary copy of the base part, so the current object is not changed — write the qualified call, `Base::onResize()`, instead.
- Don't make assumptions about object layout and cast on them, such as casting an object address to a char pointer and doing pointer arithmetic; layout varies by compiler and this is undefined behavior.

## Checklist
- Is this cast necessary, or can the design avoid it?
- Am I using a named C++ cast rather than an old-style cast?
- If I need the base version of a function, am I using a qualified `Base::func()` call rather than casting *this?

## Notes
The four named casts each say what they do, so misuse (like casting away const with anything but const_cast) fails to compile and greps stand out. The subtle trap is casting *this to a base to reach a base method: it constructs a temporary base copy and calls the method on the copy, leaving the real object half-updated — the fix is the qualified `Base::func()` call. Casts are not free relabeling; type conversions frequently emit runtime code.
