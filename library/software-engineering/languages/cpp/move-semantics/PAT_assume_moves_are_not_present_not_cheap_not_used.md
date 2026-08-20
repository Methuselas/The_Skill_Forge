---
object_id: PAT_assume_moves_are_not_present_not_cheap_not_used
object_type: pattern
name: Assume Moves Are Not Present, Not Cheap, and Not Used
library_path:
- software-engineering
- languages
- cpp
- move-semantics
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- move_semantics
- performance
- templates
- measurement
cross_links:
- rel: related_to
  target_object_id: PAT_understand_special_member_generation
- rel: related_to
  target_object_id: PAT_state_the_guarantees_a_function_can_honor
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_tell_a_universal_reference_from_an_rvalue_reference
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Assume Moves Are Not Present, Not Cheap, and Not Used

## Pattern Rule
**IF** you are writing code whose types you do not control — a template, a library, anything generic — and are tempted to reason about how fast it will be because moving exists
**THEN** assume the types have no move operations, that moving them costs what copying costs, and that the operations will not be selected anyway
**ELSE** where the types are known and their move support is established, reason about them specifically; this conservatism is for the case where you cannot.

## Do
- Separate the three failures, because they have different causes and different remedies. A type may have no move operations at all — every C++98 class that has not been revised, and any class whose declared destructor or copy operation suppressed the generated ones. A type may have them and gain nothing from them. And a type may have cheap ones that the library declines to use.
- Recognize the containers where moving cannot help. A fixed-size array holds its elements directly rather than behind a pointer, so there is no pointer to steal — moving it moves every element, and both copying and moving are linear in the number of elements. The saving over copying is whatever moving one element saves over copying one, which for many element types is nothing.
- Recognize the strings where moving does not help either. Implementations commonly store short contents inside the string object rather than in separate storage, on the well-supported grounds that short strings are the common case. Moving such a string copies those characters exactly as copying would.
- Remember that a cheap move operation is not used unless it promises not to throw. Library code that must leave its argument intact on failure will only move where moving cannot fail, and it determines that from the declaration. A movable type that never declared its moves non-throwing is a type the library copies.
- Reason specifically the moment you can. Where the types are yours, their move support is known, and a profile says the operation matters, the conservatism goes away — it is a rule about unknown types, not a claim that moving rarely helps.

## Don't
- Don't assume recompiling C++98 code with a modern compiler makes it faster. The standard library was overhauled to support moving and your own types were not; a class with a declared destructor gained nothing, and may have lost the moves it would otherwise have been given.
- Don't assume compilation proves a move happened. An unmovable type binds to the copy operation and the code is correct, so the only evidence of the difference is in a measurement.
- Don't design an interface around a saving you have not established. Passing by value on the assumption that moves are cheap is the common form of this, and for a type without cheap moves it costs a copy that passing by reference would not have.
- Don't treat this as an argument against move semantics. It is an argument against assuming them in code that cannot see the types, which is exactly where the assumption is most tempting because there is nothing concrete to check.

## Checklist
- Do you control the types this code operates on?
- For each type: does it declare a destructor or a copy operation that would have suppressed its move operations?
- Does moving this type actually avoid work, or does it hold its data directly?
- Are the move operations declared non-throwing, so library code will use them?
- Is any design decision here resting on an assumed saving rather than a measured one?

## Notes
This is the counterweight to the rest of the move-semantics material, and it belongs beside it rather than after it. The feature is genuinely valuable and every mechanism around it is worth learning; what does not follow is that any particular piece of code benefits. Three independent conditions have to hold — the operations exist, they save real work, and the context selects them — and generic code can verify none of them.

The last of the three is the one most often missed, because it looks like a technicality about exception specifications and is really about which operation runs. A container relocating its elements has to be able to undo a partial relocation if something fails; moving cannot be undone, so it moves only when moving is guaranteed not to fail. That guarantee comes from a declaration nobody is required to write.

The practical shape of the advice is narrow rather than pessimistic. In code with known types and known move support, reason normally. In templates, in interfaces, and in anything published for others to instantiate, be as conservative about copying as you would have been before move semantics existed — which is not a claim that nothing has improved, but a recognition that in generic code you cannot tell whether it has.
