---
object_id: PAT_dont_add_a_default_constructor_a_class_cannot_honor
object_type: pattern
name: Don't Add a Default Constructor a Class Cannot Honor
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
- initialization
- class_design
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_initialize_members_with_init_list
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Don't Add a Default Constructor a Class Cannot Honor

## Pattern Rule
**IF** a class needs outside information before an object of it means anything, and leaving out the argument-free constructor is restricting how clients may use the class
**THEN** leave it out and let the restrictions stand, because the alternative moves a validity question out of construction and into every other member function
**ELSE** where the class genuinely has a meaningful argument-free value — something number-like initialized to zero, something pointer-like initialized to null, an empty container — the constructor is honest and belongs there.

## Do
- Price the restriction concretely before trading it away. Arrays of the class cannot be created without supplying arguments for each element; templates that internally build an array of their parameter type will reject it; and a virtual base without one obliges every class derived from it, however indirectly, to know and supply its constructor arguments.
- Supply the arguments in the initializer when a non-heap array is what you need. For a heap array, either hold an array of pointers, or allocate the raw memory and construct the objects in place — accepting that in-place construction obliges you to invoke each destructor by hand and release the raw memory separately afterward.
- Let the restriction steer you toward the facility that does not impose it, since careful template design usually removes the requirement entirely and the standard growable array imposes no argument-free constructor on its element type.

## Don't
- Don't restore the argument-free constructor by admitting a magic "unspecified" value for the mandatory field. Every member function then has to ask whether the field was really set, and the usual answers when it was not — throw, or terminate — leave the software no better off than refusing to build the object did.
- Don't file the sentinel value under correctness alone. Clients pay for those tests in runtime, in the code size of the tests themselves, and in the code that handles the cases where they fail, on every call to every function that checks.
- Don't adopt the array-of-pointers workaround without counting what it adds: each object now has to be released individually or it leaks, and the pointers occupy memory over and above the objects they locate.
- Don't apply ordinary array deletion to memory you obtained as raw storage and populated by in-place construction. Releasing a pointer that never came from the corresponding allocation is undefined.

## Checklist
- Is there information without which an object of this class is meaningless?
- If the argument-free constructor existed, what would the mandatory fields hold?
- Would other member functions have to test whether those fields hold anything real?
- Does anything in the codebase actually need arrays of this type, or a template that builds one internally?
- Is a virtual base involved, and if so, does every derived class down the hierarchy know what it would have to supply?

## Notes
The trade is a genuine one, which is why the wrong answer is tempting. What you buy by refusing is a guarantee that holds everywhere else: any object of the class that exists at all is fully and meaningfully initialized, so no function has to defend against half-built ones. What you pay is that the class becomes harder to store in bulk and harder to pass through templates written without this case in mind.

The argument that "some people believe every class should have one" is worth answering rather than dismissing, because it is a response to real friction. The answer is that the friction is localized to array creation and a few template requirements, while the sentinel value spreads a question across the whole class interface and never removes it.

Templates that require the argument-free constructor almost always do so because they build an array of the parameter type internally. That is a defect in those templates rather than a property of the language, and as template design has improved the requirement has become rarer.
