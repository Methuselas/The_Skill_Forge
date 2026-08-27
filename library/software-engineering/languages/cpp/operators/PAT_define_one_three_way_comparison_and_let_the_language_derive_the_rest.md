---
object_id: PAT_define_one_three_way_comparison_and_let_the_language_derive_the_rest
object_type: pattern
name: Define One Three-Way Comparison and Let the Language Derive the Rest
library_path:
- software-engineering
- languages
- cpp
- operators
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- operators
- comparison
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_implement_the_standalone_operator_from_the_compound
- rel: related_to
  target_object_id: PAT_make_operator_nonmember_for_conversions
- rel: related_to
  target_object_id: PAT_dont_redefine_a_standard_comparison_to_mean_something_else
- rel: related_to
  target_object_id: PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Define One Three-Way Comparison and Let the Language Derive the Rest

## Pattern Rule
**IF** a type needs relational comparison and clients will expect every spelling of it to exist and to agree
**THEN** define a single three-way comparison operator — defaulted where memberwise order is the order you want, written out where it is not — and let the compiler rewrite the relational spellings against it, defining equality yourself whenever the three-way operator is user-written
**ELSE** where the type carries no order worth exposing, define equality alone and leave the relational operators undeclared rather than inventing an order to fill them.

## Do
- Default it when memberwise comparison in declaration order is the order you actually mean. One defaulted line then supplies all four relational spellings plus equality, and it works for a class whose members are several different scalar types.
- Write the operator out when the members are the representation rather than the value. A fraction stored as a numerator and a denominator does not compare correctly member by member — the comparison belongs on the value those members encode, and the operator is where you say so.
- Define equality yourself whenever you write the three-way operator rather than defaulting it. The rewrite rules cover the relational spellings and deliberately exclude equality, because equality is frequently cheaper to answer than ordering and the language will not assume otherwise. Once equality exists, inequality is derived from it.
- Choose the ordering category as a claim about the type, not as a formality. The strongest one says equal values are interchangeable everywhere; the weakest admits pairs that are neither less, greater, nor equal, which is what floating-point comparison against a not-a-number requires. Callers must handle whatever the category admits, so claiming a weaker order than the type has costs every caller, and claiming a stronger one is false.
- Let a member operator handle mixed-mode comparison. The compiler synthesizes the reversed form when the literal is on the left, which places the convertible operand where a member call can convert it — so comparison does not need the non-member treatment that mixed-mode arithmetic does.

## Don't
- Don't hand-write the six overloads when one line generates them. Six independent definitions are six chances for one of them to disagree with the others, and the disagreement is invisible until a caller compares two objects in the one spelling you got wrong.
- Don't default the operator on a type whose members are an implementation detail. Defaulting compares what is stored, which is only correct when what is stored is the value.
- Don't assume equality arrived with the three-way operator you wrote. It did not, and the symptom is not a wrong answer but a failure to compile at some distant call site that only ever needed `==`.
- Don't reach for the weakest ordering category to avoid thinking about it. It forces every caller to handle an unordered outcome that your type may never produce.

## Checklist
- Is memberwise comparison in declaration order the order clients expect, or is the value something the members merely encode?
- If the three-way operator is user-written, is equality defined as well?
- Is the ordering category the strongest one the type honestly supports?
- Are there pairs that must compare as unordered, and does the chosen category admit them?

## Notes
The interesting thing about this operator is not that it shortens a class, though it does. It is that the language now relates the comparison spellings to one another, which is exactly the opposite of the situation for arithmetic operators and their compound-assignment counterparts, where nothing is related and every consistency between them is one the author wrote and maintains by hand. A reader who has internalised that older lesson will expect to keep the six comparison overloads in sync themselves, and that expectation is now wrong in a way that costs real work.

The exclusion of equality from the rewrite rules looks arbitrary and is not. Ordering two objects can be considerably more expensive than deciding whether they are equal — comparing sizes first will settle inequality for two strings that ordering would have to walk. Leaving equality to be defined separately is what lets a type answer the cheap question cheaply. The cost of that design is a trap with no diagnostic at the point of the mistake: a user-written three-way operator with no equality beside it produces a class that supports every comparison except the one most callers reach for first.
