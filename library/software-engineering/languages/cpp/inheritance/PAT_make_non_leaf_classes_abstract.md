---
object_id: PAT_make_non_leaf_classes_abstract
object_type: pattern
name: Make Non-Leaf Classes Abstract
library_path:
- software-engineering
- languages
- cpp
- inheritance
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- inheritance
- abstraction
- class_design
- assignment
cross_links:
- rel: related_to
  target_object_id: PAT_use_public_inheritance_only_for_is_a
- rel: related_to
  target_object_id: PAT_copy_all_members_and_base_parts
- rel: related_to
  target_object_id: PAT_give_polymorphic_base_a_virtual_destructor
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Make Non-Leaf Classes Abstract

## Pattern Rule
**IF** you are about to derive one concrete class publicly from another concrete class
**THEN** turn the two-class hierarchy into a three-class one instead — invent an abstract class holding what they share and derive both from it — so that only leaves of the hierarchy can be instantiated
**ELSE** where the class you want to inherit from is concrete and lives in a library you cannot edit, you are choosing among damage-limitation options rather than applying this, and the choice should be made deliberately.

## Do
- Understand the defect precisely, because the fix looks disproportionate until you do. Assigning one derived object to another through base-class pointers calls the base's assignment operator, which copies the base part and stops — leaving the derived members holding their old values, in an assignment that reported no error.
- Reject the obvious repair rather than half-applying it. Making assignment virtual does not work, because a virtual function must take identical parameter types throughout the hierarchy, so each derived operator must accept any base object at all — which makes assigning one derived type to a different one legal, converting a partial assignment into a mixed-type one.
- Reject the next repair for a reason worth keeping. Restricting the base's assignment operator does stop the partial assignment, but a non-public one also stops derived operators from calling it, and stopping legitimate assignment between base objects requires that no base objects exist — which is what making the class abstract achieves and nothing weaker does.
- Where the new abstract class has no member that is naturally pure, make its destructor pure and then supply a definition for it anyway. Destructors of base classes are invoked whenever a derived object is destroyed, so this one has to exist; declaring it pure only obliges concrete derived classes to be concrete.

## Don't
- Don't extend this into a rule that every concept gets an abstract class and a concrete one. That doubles the hierarchy for no benefit and produces something harder to read, slower to compile, and more expensive to maintain than what it replaced.
- Don't excuse a concrete-from-concrete derivation on the grounds that the derived class adds no data. It adds none today; the whole problem reappears the moment somebody adds a member, and by then the inheritance relationship is established and the code depending on it is written.
- Don't invent the abstract class the first time a concept appears. You cannot design a good interface for a concept you have seen used once, and an abstraction that has to change later forces the recompilation it existed to prevent.
- Don't rely on a run-time type check inside a virtual assignment operator as the answer. It works, and it converts something the compiler could have refused into an exception that clients must catch at every assignment — which, in practice, they will not.

## Checklist
- Does any concrete class here inherit publicly from another concrete class?
- If two objects of a derived type were assigned through base-class pointers, which members would be copied?
- Does the shared abstract class have at least one pure virtual member?
- If that member is the destructor, does it also have a definition?
- Has this abstraction now been needed in two places, or only anticipated for a second?

## Notes
The assignment behavior is the concrete symptom, but the larger payoff is at the design level. Forcing the transformation means you must name what the two classes have in common and formalize it as a type with stated members and stated meaning — turning a vague sense that they are related into something the codebase can express.

That is also the answer to when a new abstraction is justified. Needing one in a single context is coincidence; needing one in two is evidence. The transformation triggers exactly when an existing concrete class is about to be reused in a new context, which is precisely the second appearance, so it mechanizes a judgment that would otherwise be made by taste.

It also removes the temptation that leads to treating arrays polymorphically. Passing an array of derived objects where an array of base objects is expected computes element addresses using the base's size, and deleting such an array through a base pointer is undefined for the same reason — hazards that only arise when a concrete class has a concrete base to be passed as.

When the base is a library class you cannot change, four options remain, none good: derive anyway and live with both the assignment and array hazards; look for an abstract class higher in that library's hierarchy and reimplement what the concrete one gave you; hold the library object as a member and forward to it, giving up the ability to override its virtual functions and taking on an update each time the vendor changes the class; or use the library class as it stands and add what you need as non-member functions.
