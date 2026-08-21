---
object_id: PAT_encapsulate_the_container_choice_instead_of_abstracting_over_it
object_type: pattern
name: Encapsulate the Container Choice Instead of Abstracting Over It
library_path:
- software-engineering
- languages
- cpp
- containers
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- containers
- encapsulation
- design
- abstraction
cross_links:
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
- rel: related_to
  target_object_id: PAT_depend_on_interfaces_not_concrete_classes
- rel: related_to
  target_object_id: PAT_minimize_compilation_dependencies
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Encapsulate the Container Choice Instead of Abstracting Over It

## Pattern Rule
**IF** you want the freedom to change which container holds your data later, and are tempted to write code that would work with several of them
**THEN** abandon that and hide the container inside a class whose interface reveals as little of it as possible, because you cannot make your own code container-independent but you can make your clients' code independent of what you chose
**ELSE** where the container is a local variable inside one function, changing it later costs one function's worth of edits and no structure is needed to make that cheap.

## Do
- Test the ambition by intersecting the capabilities before committing to it, since the result is usually decisive. Supporting a growable array, a double-ended queue, and a linked list at once forbids reserving capacity, subscripting, adding at the front, splicing, the member sort, and every algorithm needing random access — which leaves a container where all insertions and erasures are linear and invalidate everything.
- Name what actually differs, because the differences are not only in which member functions exist. Inserting into a sequence puts the element where you asked; inserting into an ordered associative container puts it where the ordering says. Erasing by iterator hands back a new iterator from one category and nothing from the other.
- Alias the container type and its iterator type, then use the aliases everywhere. A change of allocator becomes a one-line edit, and the alias also spares you spelling out the type of a nested iterator more than once.
- Put the container in the private section of a class and expose operations rather than the container. That is what limits the blast radius: when the choice changes, the audit is over that class's members and friends rather than over every call site in the program.
- Audit for behavior and not just for compilation when you do switch. The compiler will find the calls that no longer exist; it will not find the code that assumed an iterator stayed valid across an insertion.

## Don't
- Don't treat a type alias as encapsulation. It is a synonym, so it saves typing and localizes edits, and it prevents a client from depending on precisely nothing — everything the underlying container can do remains available and everything about it remains dependable.
- Don't attempt to span sequence and associative containers under one abstraction. One stores elements, one stores keyed pairs; even the pair of ordered containers that differ only in whether duplicates are allowed have insert members with different return types.
- Don't reach for a general principle here that was written about a different situation. The advice to depend on an interface rather than a concrete type assumes the implementations behind the interface are genuinely substitutable. These are deliberately not: they have different complexity, different iterator categories, and different invalidation rules, and the interface you would extract from them is the intersection above.

## Checklist
- Is the container a private member of something, or is its type visible in a public interface?
- Do the aliases for the container and its iterator exist and get used consistently?
- How many call sites would see a compile error if the container type changed, and how many would silently change behavior?
- Does any part of the public interface hand out an iterator, and does that commit you to a category?

## Notes
The tension with the general design principle is worth stating rather than smoothing over, because both positions are correct about different things. Depending on an abstraction rather than a concrete type is right where the implementations behind it are interchangeable by design. The standard containers are the opposite case — they exist as separate types precisely because their trade-offs differ — so the abstraction that would cover all of them is defined by what they have in common, and what they have in common is worse than any of them individually.

The insidious half of the problem is the invalidation rules rather than the missing member functions. Code that calls something a container does not have fails to build, which is an inconvenience. Code written against one container's invalidation rules and then run against another's builds cleanly and reads memory that has been freed or relocated.

There is a real payoff on the far side of accepting this. A customer list implemented as a linked list because the name said list, then found to need the top fifth of its entries quickly, wants an algorithm requiring random access — which the list cannot provide. If the container was private, that discovery costs a change inside one class. If its type was in the interface, it costs a change everywhere.
