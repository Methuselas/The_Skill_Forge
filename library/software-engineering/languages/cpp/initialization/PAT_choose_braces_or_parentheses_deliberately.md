---
object_id: PAT_choose_braces_or_parentheses_deliberately
object_type: pattern
name: Choose Braces or Parentheses Deliberately
library_path:
- software-engineering
- languages
- cpp
- initialization
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- initialization
- overloading
- class_design
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_manually_initialize_builtin_objects
- rel: related_to
  target_object_id: PAT_prefer_auto_for_local_variables
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Choose Braces or Parentheses Deliberately

## Pattern Rule
**IF** you are creating an object and choosing how to delimit its initializer
**THEN** pick one delimiter as your default, apply it consistently, and use the other only where it is required — because for some classes the two select different constructors
**ELSE** where the class has no initializer-list constructor, the two forms mean the same thing and the choice is style.

## Do
- Know what braces buy, since it is the case for making them the default. They are the only form usable everywhere — including default values for non-static data members, which parentheses cannot express, and uncopyable objects, which an equals sign cannot. They prohibit narrowing conversions among built-in types, so summing three doubles into an int is an error rather than a silent truncation. And they are immune to the most vexing parse: a declaration with empty parentheses declares a function, while one with empty braces default-constructs an object.
- Know what parentheses buy, since it is the case for the other default. They never divert a call to an initializer-list constructor, and they avoid deducing an initializer list where `auto` is involved.
- Understand the rule that makes the choice matter: when any constructor takes an initializer list, a braced call prefers it *strongly*. If there is any way to construe the braced arguments as that list, the compiler will, even when another constructor is an exact match on every argument and the list constructor requires conversions on all of them.
- Follow how far that preference goes, because it is further than "prefers." Braced copy and move construction can be diverted to an initializer-list constructor if the source object converts to the element type. And the preference holds even when it produces an error: if the elements would require narrowing, the call is rejected rather than falling back on the other constructors. Only when no conversion to the element type exists at all does normal overload resolution resume.
- Design your own classes so the delimiter does not change which constructor runs. The canonical failure is the standard vector: two arguments in parentheses give a sized container of repeated values, and the same two in braces give a two-element container. Meyers names that an error in its interface, not a quirk to imitate.
- Treat adding an initializer-list constructor to an existing class as a breaking change. Braced calls that resolved to other constructors may silently start calling the new one — an overload that overshadows rather than competes.
- Remember that empty braces mean no arguments, not an empty list. To pass an empty initializer list, the empty braces have to be an argument, nested inside the outer delimiters.

## Don't
- Don't switch delimiters case by case according to what looks right. The whole benefit is that a reader can predict which constructor a call selects, and that requires a rule applied consistently.
- Don't add an initializer-list constructor casually. It competes with nothing and displaces everything, so it belongs in a class only where taking a list of values is the primary way the class is built.
- Don't use braces inside a template to construct an object of a deduced type. The template author cannot know which delimiter the caller wanted, and the two produce different objects — which is why the standard's own factory functions use parentheses and say so in their documentation.
- Don't read narrowing prohibition as a reason to brace everything. It is a real benefit and it is not free of the interaction above.

## Checklist
- Does this class have a constructor taking an initializer list?
- If so, would a braced call select it, and is that what you want?
- Are you adding a list constructor to a class that already has clients using braces?
- Inside a template, is the delimiter choice being made by code that cannot know the caller's intent?
- Is your default delimiter applied consistently across this codebase?

## Notes
There is no consensus on which default is better and this card does not invent one. The braces-by-default position rests on breadth, narrowing prohibition, and vexing-parse immunity; the parentheses-by-default position rests on never being diverted to a list constructor and on interacting predictably with `auto`. Both concede cases where the other is required. What is not defensible is choosing per site, because then nothing about a call site tells a reader which constructor runs.

The interaction with type deduction is worth holding alongside this decision rather than separately. A variable declared `auto` with a braced initializer deduces an initializer list, so the more a codebase leans on `auto`, the more friction braced initialization creates — the two modern habits pull against each other, and that tension is a genuine input to the choice rather than an argument against either.

For a class author the takeaway is sharper than for a client, and it is the one that outlasts a style preference: the strength of the list-constructor preference means that adding one changes the meaning of existing braced calls at every client. That is an ABI-stable, silent, compile-clean change of behaviour, which puts it in the category of interface decisions to make once and early.
