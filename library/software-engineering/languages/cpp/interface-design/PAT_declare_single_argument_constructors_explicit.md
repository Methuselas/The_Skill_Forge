---
object_id: PAT_declare_single_argument_constructors_explicit
object_type: pattern
name: Declare Single-Argument Constructors Explicit
library_path:
- software-engineering
- languages
- cpp
- interface-design
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- interface_design
- type_conversion
- class_design
- explicit
cross_links:
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
- rel: related_to
  target_object_id: PAT_make_operator_nonmember_for_conversions
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Declare Single-Argument Constructors Explicit

## Pattern Rule
**IF** you are adding a constructor to a class that can be called with one argument, or a conversion operator that turns the class into some other type
**THEN** mark the constructor so it cannot be used for conversion, and give the conversion operator an ordinary name instead, unless you have positively decided you want compilers inserting this conversion at call sites where no source code shows it happening
**ELSE** where the conversion really is the point — a wrapper meant to be interchangeable with what it wraps at every call — the implicit form is the design, and what you owe is a reason recorded next to it.

## Do
- Count the constructors correctly. A constructor qualifies as a conversion whenever it *can* be called with one argument, which includes constructors declaring several parameters where everything after the first carries a default.
- Replace a conversion operator with a named member function that does the same job, and require clients to call it. The standard string type takes exactly this route for its character-pointer form rather than declaring the operator, which is why printing a string never silently prints something else.
- Where you must keep the conversion available for genuine construction while blocking it for argument matching, note that no legal conversion sequence contains more than one user-defined step — a fact you can build against deliberately, and the mechanism the pre-keyword workarounds all relied on.

## Don't
- Don't assume a missing overload gives you a compile error. Faced with a call that does not match, compilers go looking for a conversion sequence that makes it match, and a one-argument constructor is exactly such a sequence; the call then succeeds and does something you never wrote.
- Don't treat the resulting bug as rare because the conversion looks implausible. The classic instance is a dropped subscript — comparing a container to an element instead of element to element — which compiles into a comparison against a temporary container built from the element's value, constructed and destroyed once per loop iteration.
- Don't leave a conversion operator in place on the grounds that no current call site abuses it. The abusive call site is the one nobody wrote yet, and its symptom is a wrong answer rather than a diagnostic.

## Checklist
- Which constructors of this class can be called with exactly one argument, counting defaulted trailing parameters?
- Does the class declare any conversion operator, and would a named function serve the same clients?
- For each conversion left implicit, is there a recorded reason it should happen without appearing in the source?
- If an argument of the wrong type were passed to a function taking this class, would that be a diagnostic or a silent temporary?

## Notes
The reason this is worth a decision rather than a habit is that both mechanisms are invisible at the call site. A conversion inserted by the compiler leaves nothing in the source to grep for, so when the resulting behavior is wrong there is no line to look at — which is what makes the failures so expensive to diagnose relative to how simple they are.

Experience tends to push in one direction here. The more C++ a programmer has written, the more likely they are to have stopped writing conversion operators altogether, and the committee members who designed the standard library largely did the same.

Before the language offered a keyword for this, the workaround was to introduce a small intermediate type and have the constructor take that instead, so reaching the class from the original argument type would require two user-defined conversions and therefore fail. That workaround is obsolete as a technique but not as an idea: it is the same interposed-object move that proxy classes are built on, applied to conversion rather than to access.
