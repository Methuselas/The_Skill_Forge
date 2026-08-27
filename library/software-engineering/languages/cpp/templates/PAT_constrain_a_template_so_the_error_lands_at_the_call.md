---
object_id: PAT_constrain_a_template_so_the_error_lands_at_the_call
object_type: pattern
name: Constrain a Template So the Error Lands at the Call
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- concepts
- interface_design
cross_links:
- rel: related_to
  target_object_id: PAT_program_to_a_templates_implicit_interface
- rel: related_to
  target_object_id: PAT_publish_a_trait_for_what_you_cannot_detect
- rel: related_to
  target_object_id: PAT_use_traits_classes_for_type_info
- rel: related_to
  target_object_id: PAT_prefer_the_form_that_refuses_what_you_did_not_mean
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Constrain a Template So the Error Lands at the Call

## Pattern Rule
**IF** a template will compile for type arguments it was never meant to accept
**THEN** write the requirement down as a constraint on the template, so an unsuitable argument is refused where it was supplied and the refusal names what was missing
**ELSE** where every type that compiles is genuinely acceptable, leave the template unconstrained rather than adding a constraint that only restates the body.

## Do
- Reach for this because of wrong answers, not because of ugly error messages. A template that adds a number to its argument will accept a pointer and compile silently, because pointer arithmetic is valid — and it will produce a value that means nothing. The unconstrained template's real failure is not a bad diagnostic; it is the absence of any diagnostic at all.
- Treat the constraint as the interface you were already depending on, written down. The set of expressions the body requires exists whether or not it is named; naming it moves the check from instantiation, deep inside code the caller did not write, to the call the caller did write.
- Build constraints from anything that yields a compile-time boolean — a standard concept, a type trait, or a predicate of your own. A named constraint is reusable and composes; an unnamed one written inline is neither.
- Combine constraints with conjunction and disjunction, and know they short-circuit left to right. Put the cheap or more discriminating test first, exactly as you would in a runtime condition.
- Constrain on the capability the body actually exercises. A function that only adds and returns needs arithmetic, not membership of a named family of types you had in mind — over-constraining rejects types that would have worked and pushes callers into casts or specializations to get around you.

## Don't
- Don't read "it compiles" as "it was accepted." For a template, compiling means the expressions in the body happened to be valid for that argument, which is a much weaker statement than the argument being suitable.
- Don't restate the body as a constraint. A constraint that lists every expression the implementation uses re-couples the interface to the implementation and has to be edited every time the body changes; constrain the requirement, not the code.
- Don't constrain to a named category when a capability is what you need. The category is a proxy, and proxies exclude the types nobody thought of.
- Don't choose among the several ways of spelling a constraint on grounds of correctness. They express the same requirement; pick the one that puts the requirement where a reader of the declaration will see it.

## Checklist
- What does the body actually require of the type — which expressions must be valid?
- Would a plausible wrong argument compile and produce nonsense rather than an error?
- Is the constraint written against a capability, or against a category standing in for one?
- Is the requirement visible at the declaration, where a caller reads it?
- Does the constraint need editing whenever the implementation changes? If so, it is describing the body rather than the interface.

## Notes
The change this represents is smaller than it looks and more useful than it sounds. A template always had an interface — the set of expressions its parameters must support — and reasoning about that set was always the way to use templates correctly. What was missing was any way to state it, so the requirement lived in documentation, in the author's head, or nowhere, and was enforced only by instantiation failing somewhere the caller could not read.

Writing it down changes two things. The error moves to the call and names the unmet requirement instead of exposing the implementation. More importantly, the requirement becomes checkable at all in the case where instantiation *succeeds* on a type that should have been rejected — which is the case that produces wrong answers rather than build failures, and the case a better error message would never have caught.
