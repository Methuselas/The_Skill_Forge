---
object_id: PAT_name_a_two_argument_predicate_by_role
object_type: pattern
name: Name a Two-Argument Predicate So Its Order Reads
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- readability
- api_design
- argument_order
- predicates
cross_links:
- rel: related_to
  target_object_id: PAT_use_descriptive_names
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
- rel: related_to
  target_object_id: PAT_convey_usage_through_names_and_types
- rel: related_to
  target_object_id: AP_choose_a_name_with_feitelsons_three_steps
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Name a Two-Argument Predicate So Its Order Reads

## Pattern Rule
**IF** you are naming something that takes two arguments of the same kind and answers differently when they are swapped — a comparison, a containment test, a relationship check, a copy or transfer
**THEN** put both roles in the name in the order the parameters appear, so a reader at the call site can tell which argument is which without opening the definition.
**ELSE** where the name genuinely cannot carry both roles, make the argument types different so the wrong order will not compile.

## Do
- Say both roles rather than the relation alone. A name carrying two role words in position order tells the reader what the second argument is doing there; a name carrying only the relation leaves it to memory.
- Write a call with the arguments deliberately reversed and read it aloud. If the reversed call sounds equally plausible, the name is not carrying the order.
- Rename on evidence. Repeatedly checking your own definition to recall which way round it goes is the signal — that check costs every reader, not only you.
- Where the two arguments have distinct roles in the domain, prefer the type system: distinct types make the swapped call fail rather than quietly answering the other question.

## Don't
- Don't rely on a verb whose subject is ambiguous. A name built from a bare relation reads as a question about the pair rather than about one of them in particular, and a reader has no way to tell which end the verb attaches to.
- Don't settle the order in a comment or in parameter names visible only at the definition. The confusion happens at call sites, which show neither.
- Don't assume the convention is obvious from the domain. Whichever order feels natural to the author, roughly half of readers will guess the other one, and a wrong guess here returns a plausible answer rather than an error.
- Don't leave a confusing name in place because the code works. A predicate answering the opposite of what a reader assumed is a defect waiting for the first person who edits around it.

## Checklist
- Can I tell from a call alone which argument plays which role?
- Does the reversed call look obviously wrong, or merely different?
- Have I had to look up the order more than once?
- If the name cannot carry the order, can the types carry it instead?

## Notes
The failure mode here is quiet in a way most naming problems are not. A vague name for a value produces a reader who is unsure; a reversed predicate produces a reader who is confident and wrong, and the code compiles and returns an answer either way. Nothing surfaces until the answer matters.

The evidence for this rule is usually the author's own behavior. A library that shipped a relationship test named for the relation alone had its own author unable to remember which direction it ran, and the fix was a name stating both roles in argument order. That is worth noting because it inverts the usual assumption: familiarity with the code did not make the name workable, so no amount of documentation would have made it workable for anyone else.

The fallback is real and often better. Two arguments with genuinely different roles frequently deserve different types, and then the compiler enforces what a name could only suggest. Reach for the name when the arguments are the same kind of thing and the asymmetry is in the question rather than in the values.
