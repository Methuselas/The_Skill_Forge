---
object_id: PAT_externalize_varying_behavior_with_strategy
object_type: pattern
name: Externalize Varying Behavior with the Strategy Pattern
library_path:
- software-engineering
- languages
- cpp
- virtual-functions
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- virtual_functions
- strategy
- callable
cross_links:
- rel: related_to
  target_object_id: PAT_wrap_virtuals_with_nvi_idiom
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Externalize Varying Behavior with the Strategy Pattern

## Pattern Rule
**IF** a behavior varies and need not depend on an object's type at all
**THEN** move it out of the class as a Strategy — a function pointer, a tr1::function object, or a separate hierarchy the object holds — instead of a member virtual function.

## Do
- Hold a callable the object calls to do the work (a health calculator passed to the constructor), so different instances of one type can behave differently and the behavior can change at runtime.
- Prefer a tr1::function member over a bare function pointer: it accepts any compatible callable — a free function, a function object, or a bound member function — and any return type convertible to what you need.
- Use a separate strategy hierarchy when you want the classic Strategy shape and the ability to extend algorithms by deriving new strategy classes.

## Don't
- Don't reach for Strategy when the behavior genuinely needs the object's private data; a non-member strategy has no special access, so you would have to weaken encapsulation with friends or accessors.
- Don't assume the strategy must be a plain function returning an exact type; that rigidity is exactly what a tr1::function member removes.

## Checklist
- Does this behavior really depend on the object's type, or can it be supplied from outside?
- Do I need per-instance or runtime-swappable behavior (Strategy) rather than per-type (virtual)?
- Does the strategy need private data — and if so, is weakening encapsulation worth it?

## Notes
Strategy externalizes what a virtual function keeps inside the hierarchy. A function-pointer member already gives per-object, runtime-swappable behavior; a tr1::function member generalizes it to any compatible callable (free function, functor, or a member bound with tr1::bind), even with a convertible return type. A separate strategy hierarchy is the textbook form. The one cost is access: an external strategy cannot see private members, so pick it only when the calculation needs no private state or the encapsulation trade is acceptable.

Locking is a varying behavior worth recognizing as a candidate, and it is one people rarely think to externalize. A component written for reuse has to protect its critical sections to be safe in a concurrent program, and every single-threaded client then pays for synchronization it cannot use. Making the lock a pluggable strategy — a real mutex for concurrent callers, a do-nothing object for the rest — lets one implementation serve both without the component knowing which it is serving.

The choice between resolving that strategy at run time and at compile time matters more here than in most applications of the pattern. A virtual call to acquire a lock adds an indirection to something that may be executed extremely often and does almost nothing; supplying the strategy as a template parameter instead resolves it during compilation, so the do-nothing case optimizes away entirely rather than becoming a virtual call that returns immediately.
