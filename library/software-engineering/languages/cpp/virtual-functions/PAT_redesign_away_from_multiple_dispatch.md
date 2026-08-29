---
object_id: PAT_redesign_away_from_multiple_dispatch
object_type: pattern
name: Redesign Away From Multiple Dispatch
library_path:
- software-engineering
- languages
- cpp
- virtual-functions
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- virtual_functions
- polymorphism
- design
- extensibility
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_dynamic_cast_with_alternatives
- rel: related_to
  target_object_id: PAT_give_a_polymorphic_class_a_virtual_clone
- rel: related_to
  target_object_id: PAT_externalize_varying_behavior_with_strategy
- rel: related_to
  target_object_id: AP_design_a_customization_point
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Redesign Away From Multiple Dispatch

## Pattern Rule
**IF** an operation's behavior has to depend on the dynamic types of two or more of its operands rather than just one
**THEN** treat that requirement as a reason to revisit the design, because the language offers no construct for it and every way of emulating it trades one maintenance problem for a different one
**ELSE** where the set of participating types is genuinely closed and you control it, holding the operands in a discriminated union and visiting them gives you the dispatch with compile-time exhaustiveness checking, which none of the hand-rolled emulations provide.

## Do
- Price the four emulations against each other before choosing, since each fails somewhere specific. A virtual function that then interrogates the other operand's type is the easiest to write and destroys encapsulation, because every class ends up knowing its siblings. A pair of single dispatches — virtual functions overloaded on each participating type — removes the interrogation entirely and makes the unknown-type case impossible, at the cost of every class needing a new member whenever any class is added. A table mapping type pairs to functions confines additions to the table's initialization. Wrapping that table in a class with add and remove operations lets the mapping change while the program runs.
- Where neither escape applies — the set of participating types is open, or you do not control it — pick the emulation deliberately against how many types there are and whether you may modify them. An unrolled chain of type tests is fastest for a handful and grows as the product of the two type counts, so it stops being maintainable quickly and must name every class in one place. A table keyed by runtime type identity costs a lookup, needs no change to the hierarchy, and lets entries be registered from the files they belong to. A matrix indexed by per-class numbers dispatches in constant time and requires adding something to every participating class, which is only available where the hierarchy is yours.
- Register both orders explicitly where the operation is symmetric. A table keyed by an ordered pair has no idea that the two arguments are interchangeable, so the reversed entry has to be added and has to swap the arguments back before calling — omitting it means the operation works and its mirror image silently finds nothing.
- Use the checked cast in the dispatch layer rather than the static one. `PAT_use_a_dynamic_downcast_where_a_base_repeats` owns why: knowing the type at registration does not establish that a single path leads to it.
- Notice which failure you can actually tolerate. The pair-of-dispatches approach cannot be used at all when some participating classes come from a library you cannot edit, and it forces a recompile of everything on each addition; the table approach accepts new types without touching existing classes.
- If you take the table route, key it on something the standard actually specifies. The name available from run-time type identification is not required to have any particular form, so a wrapper type around the type information is what makes the table portable.
- Register entries once rather than on every lookup — either from a function that builds and returns the table, or from objects whose construction registers a mapping before the program's main entry point begins.

## Don't
- Don't reach for the interrogation chain because it is the quickest thing to write. Adding a class then means finding and updating every chain in the program, compilers cannot tell you that you missed one, and the fallthrough case exists only so it can report at run time that something impossible happened — to a caller with no better idea what to do about it than you had.
- Don't adopt the table if derived operands must match entries registered for their bases. The lookup uses the operand's actual type, so a class derived from a registered one simply is not found, and no reasonable amount of work makes it found; only the pair-of-dispatches approach gets inheritance-based conversion right, because it is the only one letting the compiler do the matching.
- Don't read the availability of these emulations as permission to require the capability. Every one of them is a hand-built reimplementation of the machinery compilers already provide for dispatch on one operand, and hand-built versions are neither checked for consistency nor updated automatically.

## Checklist
- Is the set of participating types closed, and do you control all of it?
- If a new type were added tomorrow, which existing files would have to change?
- Do operands of derived types need to match behavior registered for their bases?
- What happens at run time when a combination has no registered behavior, and who could act on that?
- Has the design been examined for a formulation where one operand's type determines the behavior?

## Notes
The reason there is no good answer is worth stating plainly, because it stops the search. Dispatching on one operand is a service the compiler provides, complete with a guarantee that every derived class supplies an implementation. Dispatching on two is the same service with no provider, so whoever needs it becomes responsible for the table, the lookup, the key, and the completeness check that compilers otherwise perform silently.

Other languages did solve this. The construct is called a multi-method where it exists, and the emulations here are all approximations of it — which is useful context, since it explains why the problem feels like it should have a clean solution and does not.

The modern position differs from Meyers's in one respect that changes the recommendation's shape rather than its direction. A discriminated union visited by an overload set gives genuine dispatch on several operands with the compiler enforcing that every combination is handled — but only over a set of types fixed at compile time. So the pivotal question has become whether the type set is closed. If it is, that facility is the answer and nothing here needs hand-building. If it is not, the trade-offs above are still the whole of what is available.

When the emulation is unavoidable, the three arrangements differ along axes worth naming before choosing. Code size grows with the product of the type counts in the unrolled form and not in the other two; the table form is the only one that lets a new pairing be added from the file that introduces it, rather than in a central place that must know every class; and the constant-time form buys its speed by requiring the hierarchy to cooperate, which decides the question outright when the types come from someone else's library.
