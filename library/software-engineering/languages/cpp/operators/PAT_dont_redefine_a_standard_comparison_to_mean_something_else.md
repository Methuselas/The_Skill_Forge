---
object_id: PAT_dont_redefine_a_standard_comparison_to_mean_something_else
object_type: pattern
name: Don't Redefine a Standard Comparison to Mean Something Else
library_path:
- software-engineering
- languages
- cpp
- operators
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- operators
- avoiding_surprises
- api_design
- comparison
cross_links:
- rel: related_to
  target_object_id: PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
- rel: related_to
  target_object_id: PAT_convey_usage_through_names_and_types
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Don't Redefine a Standard Comparison to Mean Something Else

## Pattern Rule
**IF** you want your type ordered by something other than its natural ordering, and are considering specializing the library's default comparison for your type to achieve it
**THEN** don't — write a differently named comparison type and name it wherever the ordering is needed, because every place in the library that uses the default lets you supply an alternative, and there is no place where you must reach for the specialization
**ELSE** where the specialization exists to make your type behave the way the corresponding built-in already behaves — a handle type ordering the way the raw pointer inside it orders — it surprises nobody and is reasonable.

## Do
- Say what you mean at the point of use. A container declared with a named comparison type reads as ordered by that criterion; a container declared without one reads as ordered the default way, and readers will take the default to mean the natural ordering whatever you did to it elsewhere.
- Reserve the specialization for the case where it removes a surprise rather than creating one. Making a pointer-like type order the way the pointer it wraps orders is a case where clients expect exactly that, which is why the practice is common for smart pointer types.
- Recognize that this is permitted, so the compiler will not stop you. Specializing library templates for your own types is legal, unlike modifying the library generally — which makes the constraint here a matter of judgment rather than of what compiles.

## Don't
- Don't make the default comparison do anything other than what the corresponding operator does. Programmers assume a copy constructor copies, that taking an address yields a pointer to the object, that addition adds and equality compares — and equally that the default ordering is the natural one. Breaking that assumption costs a reader more than the keystrokes it saves the writer.
- Don't take the ability to specialize as evidence that specializing is intended. The mechanism exists so that user-defined types can participate in library machinery, not so that a type's meaning can be redefined out from under code that never mentions it.
- Don't hide the criterion where the affected code cannot see it. The specialization is written once, somewhere else, and silently changes what every container of that type does — which is the property that makes it hard to diagnose when the ordering turns out to be wrong.

## Checklist
- Is the ordering you want the type's natural one, or a different criterion?
- If different, does a named comparison type express it at each point of use?
- If a specialization is being written, does it make the type behave like something clients already understand?
- Would a reader of a declaration that names no comparison guess correctly how the container is ordered?

## Notes
The principle behind this is broader than comparison and is worth naming: the cost of a surprising definition is paid by every reader who does not know it exists, and that population grows over time while the convenience is captured once by the author. This is the principle of least astonishment applied to a place where the language happens to allow the astonishment.

What makes this particular case tempting is that it appears to save work. Wanting a container ordered by some secondary attribute, specializing the default seems to make all such containers order that way with no further effort. That is exactly the problem — all such containers now order that way, including ones written by people who never saw the specialization and had every reason to expect otherwise.

The legitimate use is narrow and recognizable by a single test: does the specialization make the type behave the way an analogous built-in behaves? Ordering a handle type by what it refers to passes that test. Ordering a type by a different one of its attributes does not, and the alternative — a named comparison, supplied where it applies — costs almost nothing and states the criterion where the reader is standing.
