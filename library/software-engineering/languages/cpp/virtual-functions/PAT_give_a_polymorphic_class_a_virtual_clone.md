---
object_id: PAT_give_a_polymorphic_class_a_virtual_clone
object_type: pattern
name: Give a Polymorphic Class a Virtual Clone
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
- copying
- polymorphism
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_copy_all_members_and_base_parts
- rel: related_to
  target_object_id: PAT_give_polymorphic_base_a_virtual_destructor
- rel: related_to
  target_object_id: PAT_use_unique_ptr_for_exclusive_ownership
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Give a Polymorphic Class a Virtual Clone

## Pattern Rule
**IF** you hold objects through base-class pointers and need to copy one without knowing its real type, or need to create an object whose type is decided by input data rather than by the code
**THEN** declare a virtual member that returns a new copy of whatever it was invoked on, and put the data-driven case in one static function that reads enough to decide which derived type to build
**ELSE** where the set of types is fixed, tiny, and closed by design, holding a discriminated union and copying it directly is simpler and does not require every type to participate.

## Do
- Make each override exactly one line: construct a new object of its own class from itself. The real copy constructor then defines what copying means, so whatever it does — shallow, deep, reference-counted, copy-on-write — the polymorphic version does automatically and cannot drift from it.
- Declare each override as returning a pointer to its own class rather than to the base. The language permits the narrowing, so callers holding a derived pointer get a derived pointer back and need no cast, while callers holding a base pointer are unaffected.
- Let the owning class's copy constructor become a walk over its members, asking each one to copy itself. That replaces the usual alternative — a type tag and a chain of tests inside the container — with code that never needs editing when a new element type appears.
- For the data-driven case, keep the decision in one place. A single static function that reads the input, determines the type, and returns a base pointer to the newly built object is the only code in the system obliged to know the full set of derived classes.

## Don't
- Don't attempt this by copying through a base-class object. Copying is performed by the copy constructor of the static type, so a derived object copied as a base loses its derived part entirely — the same slicing that afflicts passing by value, arriving here through a different door.
- Don't let the virtual version and the real copy constructor be written independently. Two definitions of what it means to copy this type will eventually disagree, and the one that gets used will depend on whether the caller happened to know the dynamic type.
- Don't assume a container of base pointers can be copied by the compiler-generated copy constructor. It duplicates the pointers, giving both containers the same objects, which is nearly never what "copy the container" was meant to mean.

## Checklist
- Does each override construct an object of its own class and nothing else?
- Does each override's return type name its own class rather than the base?
- Is there exactly one function that knows which derived type corresponds to which input?
- If a new derived class were added tomorrow, how many existing functions would need editing?
- Does the base declare a virtual destructor, so the copies can be released through base pointers?

## Notes
Constructors cannot be virtual, and the reason clarifies what this actually is. Virtual dispatch selects an implementation using an object that already exists and already has a dynamic type; a constructor runs precisely when neither is true. So what gets called a virtual constructor is not a constructor at all — it is an ordinary virtual function whose job is to create, which is why it can be dispatched normally.

The narrowing of return types in overrides was a relatively late relaxation of the rules, and this is the use case that motivated it. Without it the override would have to advertise a base pointer even though it always produces a derived object, so every caller that knew better would need a cast to recover what the function already knew.

The same shape answers a related problem: a free function that ought to behave virtually. Since a free function cannot be virtual and a member function would put the operands in the wrong order for operators like stream insertion, the working arrangement is a virtual member doing the work and a non-member — usually inline — that does nothing but call it.
