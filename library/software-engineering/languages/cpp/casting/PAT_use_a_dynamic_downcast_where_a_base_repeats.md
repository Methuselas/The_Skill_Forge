---
object_id: PAT_use_a_dynamic_downcast_where_a_base_repeats
object_type: pattern
name: Use a Dynamic Downcast Where a Base Appears More Than Once
library_path:
- software-engineering
- languages
- cpp
- casting
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- casting
- inheritance
- object_layout
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_dynamic_cast_with_alternatives
- rel: related_to
  target_object_id: PAT_minimize_and_prefer_cpp_style_casts
- rel: related_to
  target_object_id: PAT_use_multiple_inheritance_judiciously
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Use a Dynamic Downcast Where a Base Appears More Than Once

## Pattern Rule
**IF** you are casting a base reference down to a derived type and are tempted to use the static cast because you already know the type is right and want to avoid the checked cast's cost
**THEN** first establish that the base occurs exactly once in the derived type's inheritance graph, because where it occurs more than once the static cast is not a faster equivalent — it is either ill-formed or unable to name which of the base subobjects you meant.

## Do
- Look at the whole graph between the two types rather than at the declaration in front of you. What matters is how many paths lead from the derived type up to that base, and a class two levels away can introduce a second one without the class you are looking at changing at all.
- Reach for the checked cast wherever a base is inherited virtually. Sharing one base subobject among several derived classes means there is no compile-time route back down from it, and the static cast cannot express the traversal at all.
- Reach for it equally where the same base is inherited twice without virtual inheritance. The derived object then holds two distinct subobjects of that base, so neither direction of the conversion has an unambiguous answer for the compiler to compile.
- Where the cost is genuinely measured and genuinely matters, change the design rather than the cast — a single-inheritance path, or carrying the derived type in the interface, removes the need for either cast.

## Don't
- Don't treat the two casts as the same operation at different prices. One asks the compiler to compute an offset it must know statically; the other consults the object at runtime and can find the right subobject through any arrangement of bases. Where the first cannot answer, it is not slower, it is absent.
- Don't conclude the substitution is safe because it compiled. A hierarchy that is currently a simple chain compiles either way, and a class added later that inherits the same base a second time turns a working static cast into a compile error at every site that used it — or, where the ambiguity is resolvable in one direction only, into a conversion that reaches the wrong subobject.
- Don't apply the substitution across a dispatch table wholesale on the argument that every entry's type was checked at registration. The check at registration proves which type it is, not that there is a single path from the base to it.

## Checklist
- How many paths lead from the derived type up to this base — actually, in the current graph?
- Is any base in that graph inherited virtually?
- If someone later inherits this base a second time, does this cast break loudly or quietly?
- Has the checked cast's cost been measured here, or only assumed?

## Notes
The usual advice for a checked downcast is that it is slower and should be avoided where the type is already known, and that advice quietly assumes the ordinary case of one base reached one way. Where a base appears more than once the assumption fails, and the failure is not about speed — the static form has no expression for the traversal, because the layout information it needs does not exist in the direction it is being asked to go.

The two arrangements fail for different reasons, which is worth keeping separate. A virtually inherited base is shared, so nothing in the base identifies which derived object it belongs to and there is no static path back. A base inherited twice without sharing gives the derived object two of them, so the question the cast asks has two answers and the compiler declines to choose. Only the runtime form knows the whole graph, and it reaches the right object regardless of the shape.

What makes this worth a rule rather than a case-by-case judgement is that it is not stable under other people's edits. The property being relied on is a fact about a graph that anyone can extend, and the code relying on it can be a long way from the class that changes. Where the substitution is made for measured reasons in a hierarchy known to be a chain, it is fine; where it is made habitually because the checked cast looks wasteful, it is a constraint on the hierarchy that nobody wrote down.
