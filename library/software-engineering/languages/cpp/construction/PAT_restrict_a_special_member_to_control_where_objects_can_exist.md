---
object_id: PAT_restrict_a_special_member_to_control_where_objects_can_exist
object_type: pattern
name: Restrict a Special Member to Control Where Objects Can Exist
library_path:
- software-engineering
- languages
- cpp
- construction
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- construction
- access_control
- class_design
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_replace_nonlocal_statics_with_local_statics
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
- rel: related_to
  target_object_id: PAT_dont_add_a_default_constructor_a_class_cannot_honor
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Restrict a Special Member to Control Where Objects Can Exist

## Pattern Rule
**IF** a class carries a constraint on its own instantiation — a ceiling on how many objects may exist, a requirement that they live on the heap or a prohibition on it, or a rule that nobody derives from it
**THEN** implement the constraint by making the relevant special member non-public and exposing a static function that constructs, because a rule expressed in access control is enforced and the same rule expressed in documentation is a hope
**ELSE** where you want exactly one object for the lifetime of the program, a function returning a reference to a local static is simpler, and it builds the object on first use rather than at an unpredictable moment during startup.

## Do
- Pick the member by what you are actually forbidding. Non-public constructors stop construction outright, and — as a side effect — stop derivation and containment too, since a class whose constructors are unreachable can be neither a base nor a member. A non-public destructor stops objects with automatic or static storage, because those require an implicit destruction the caller cannot perform, while leaving heap creation open; make it protected rather than private when derived classes must still exist. A non-public allocation function stops heap objects while leaving stack and static ones available.
- Pair a non-public destructor with a public member that destroys the object through itself, since clients now have no other way to end its life. Make that member const, because even objects the client holds as const have to be destroyable.
- Return the constructed object from a static member function so the class keeps control of every path into existence. Where the object is meant to be released by the caller, hand it to an owning smart pointer at the call site rather than trusting the caller to remember.
- Where a ceiling on instances is what you want, count in the constructor and throw when the ceiling is reached, but combine it with non-public constructors rather than relying on the count alone.

## Don't
- Don't count instances while leaving the constructors public. Objects come into being in three contexts — standalone, as a base subobject, and as a member of something larger — and the count sees all three, so a class with a limit of one starts throwing the moment somebody derives from it or embeds it, at a point in the program nobody will connect to the limit.
- Don't try to determine whether an object is on the heap by comparing its address against a local variable's. The reasoning ignores that static objects live in a third region belonging to neither stack nor heap, so they are misclassified; and the memory layout it depends on is not universal. There is no portable way to answer the question at all, which makes redesigning so you never ask it the only reliable move.
- Don't set a flag in the allocation function and test it in the constructor. Allocating an array calls the allocation function once and the constructor once per element, so every element after the first sees a cleared flag; and where one construction is nested inside another, implementations are free to perform both allocations before either construction, which hands the flag to the wrong object.
- Don't put the single shared object in a class static rather than a function static. A class static is constructed whether or not the program ever uses it, and its construction order relative to statics in other translation units is undefined.

## Checklist
- Which specific instantiation does this class need to prevent, stated as a sentence?
- Which single special member, made non-public, prevents exactly that?
- If the destructor is non-public, how does a client end an object's life?
- If instances are counted, are the base-subobject and member contexts excluded by construction rather than by hope?
- Does any code here try to ask whether an address is on the heap?

## Notes
The reason to prefer access control over a runtime check is that the two fail differently. An access violation is a compile-time diagnostic at the offending line; a count that throws reports the problem at run time, at whatever unrelated location happened to trip it, with no indication of which of the three construction contexts was responsible.

Function-local statics carry an initialization property that is the point rather than a detail. They are constructed the first time control reaches them, so an unused one is never built, and their construction order relative to each other follows the order of use rather than the undefined cross-translation-unit ordering that afflicts statics at namespace scope. The cost is a check on each call to see whether construction has happened yet.

One caution attached to this technique has since expired. Meyers warned against inline non-member functions containing local statics, because internal linkage could leave a program holding several copies of an object there was meant to be one of. The default linkage of inline functions was changed to external shortly after, and the hazard went with it.

Where a class destroys itself when its last user goes away, releasing through the object's own pointer is only defined if the object came from the matching allocation — so a class that does that has to control its own creation anyway, which is the same constraint arriving from the other direction.
