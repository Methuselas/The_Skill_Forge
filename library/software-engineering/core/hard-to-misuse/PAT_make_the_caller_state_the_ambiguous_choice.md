---
object_id: PAT_make_the_caller_state_the_ambiguous_choice
object_type: pattern
name: Make the Caller Write the Ambiguous Choice
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- api_design
- ownership
- explicitness
- hard_to_misuse
- call_site
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_unmistakable_over_small_print
- rel: related_to
  target_object_id: PAT_convey_usage_through_names_and_types
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
- rel: related_to
  target_object_id: AP_harden_a_code_contract
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Make the Caller Write the Ambiguous Choice

## Pattern Rule
**IF** a call could reasonably mean two different things and you are deciding which one it should mean
**THEN** require the caller to write which one, rather than picking the more common reading and applying it silently.
**ELSE** where one reading is genuinely the only sane one, pick it and say so in the name, so the call still reads as a decision rather than as a default.

## Do
- Choose a parameter type that only spells one meaning, so writing the call is what states the choice. A parameter whose type says the argument is being handed over cannot be confused with one that says it is only being read.
- Accept that the caller types more. The extra typing is the mechanism, not a cost of it — a reader of the call site learns the answer without opening the callee, and that is what was bought.
- Prefer a distinguishing type over a flag argument. A boolean at the call site restates the ambiguity rather than resolving it, since the reader still cannot tell which way round it goes.
- Where the ambiguity is about lifetime or ownership, resolve it here rather than in documentation. Ownership questions answered silently are answered again by every reader, and eventually one of them answers wrong.

## Don't
- Don't resolve it by picking the reading that is right most of the time. The remaining cases do not fail loudly; they compile, run, and do the other thing, and the call site records no evidence that a choice was made at all.
- Don't rely on the name alone where the types still permit both readings. A name is a claim about intent; a type is a constraint the compiler applies, and only the second one holds when someone edits the call later.
- Don't optimize the interface for how little the caller has to type. Fewer characters at the call site is worth having only where nothing ambiguous was elided to get there.
- Don't answer it in a comment above the function. The confusion happens at the call site, which does not show the comment, and this is the class of mistake that is not discovered by reading the callee.

## Checklist
- Could a competent reader of this call site come away with the wrong idea of what it does?
- Is the choice visible in what the caller writes, or only in what I implemented?
- If someone changes this call in a year, will the types stop them from changing its meaning by accident?
- Am I making the caller type more in exchange for something, or only out of caution?

## Notes
This runs against the usual instinct, which is to make an interface as terse as possible and settle ambiguities with a sensible default. The distinction that makes it worthwhile is between ambiguities of convenience and ambiguities of meaning: defaulting a page size or a timeout hides a number, while defaulting whether a call takes ownership of what it was passed, or copies it, hides which of two different programs you wrote.

The reason to spend a type on it rather than a name or a comment is that only the type is still enforcing anything after the code is edited. A name states an intention to the reader who is paying attention; a parameter type that admits one reading and rejects the other holds for every future caller, including the ones who never read the documentation and the ones editing under time pressure.

Libraries that get this wrong tend to be the ones that felt pleasant to use at first. Silent conversions and quietly assumed ownership make the early call sites short, and the cost arrives later, spread across the places where the assumption did not hold and nothing in the code says which assumption was made.
