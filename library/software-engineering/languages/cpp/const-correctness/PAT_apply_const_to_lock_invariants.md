---
object_id: PAT_apply_const_to_lock_invariants
object_type: pattern
name: Apply const Wherever a Value Should Not Change
library_path:
- software-engineering
- languages
- cpp
- const-correctness
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: PAT_prefer_immutable_objects
tags:
- cpp
- const
- immutability
- pointers
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_immutable_objects
- rel: related_to
  target_object_id: PAT_return_by_const_value_to_block_assignment
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Apply const Wherever a Value Should Not Change

## Pattern Rule
**IF** a pointer, parameter, return value, or variable holds something that should not be modified
**THEN** declare it `const` so the compiler enforces the constraint and the invariant is visible to other programmers.

## Do
- Place `const` precisely on pointers: in `const char * const p`, `const` left of the `*` freezes the pointee and `const` right of the `*` freezes the pointer — reading the declaration right-to-left makes this fall out.
- Reach for `const_iterator` when you want the pointed-to element to stay fixed; a plain `const` iterator only stops the iterator from moving.
- Mark parameters and locals `const` unless you must change them — six characters that turn the `if (a * b = c)` assignment typo into a compile error.

## Don't
- Don't leave a "never changes" value non-const; you give up the compiler's help and let accidental writes slip through.
- Don't treat a `const` iterator (a fixed iterator) and a `const_iterator` (a fixed element) as interchangeable — they constrain different things.

## Checklist
- Have I marked every value that should stay put as `const`?
- For each pointer, is `const` on the side(s) matching what must not change?
- Do I actually need a `const_iterator` here rather than a const iterator?

## Notes
`const` lets you state a semantic constraint — this should not change — and hands enforcement to the compiler, which is why it is the C++ mechanism behind immutability. It spans more than data: pointers (on either side of the `*`), iterators (the `const_iterator` distinction), parameters, return types, locals, and member functions. The payoff is that a whole class of "I typed `=` and meant `==`" errors becomes illegal at compile time.
