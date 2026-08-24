---
object_id: PAT_keep_a_generic_accessor_out_of_the_type
object_type: pattern
name: Keep a Generic Accessor Out of the Type It Accesses
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- name_lookup
- api_design
- code_generation
cross_links:
- rel: related_to
  target_object_id: PAT_choose_scattered_or_chained_generation
- rel: related_to
  target_object_id: PAT_make_operator_nonmember_for_conversions
- rel: related_to
  target_object_id: PAT_unhide_inherited_names_with_using
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Keep a Generic Accessor Out of the Type It Accesses

## Pattern Rule
**IF** you are adding an accessor to a class assembled out of a template the user supplied — a generated aggregate, a mixin chain, a wrapper built over someone else's type
**THEN** make it a free function taking the object as a parameter rather than a member, because every member you add competes for a name in a scope whose other occupants the user chose and you cannot see.

## Do
- Put the accessor at namespace scope beside the type, where argument lookup will find it without the caller qualifying anything.
- Treat every name in the assembled type as belonging to whoever supplied the pieces. The generator owns the structure; it does not own the vocabulary.
- Pick names for anything you must add inside that are unlikely to collide and are clearly yours, and keep the count as small as the mechanism allows.
- Where the accessor needs something private, expose that through one deliberately obscure member rather than through the natural name a user would want.

## Don't
- Don't give a wrapper member functions where the thing it wraps has members of its own. A wrapper reached through arrow dereference puts two unrelated interfaces one character apart — an arrow call goes to the wrapped object and a dot call goes to the wrapper — and readers have no habit to catch the difference, because the raw thing being imitated has no members at all. Where both interfaces contain a similarly named operation, the two calls read almost identically and do entirely different things.
- Don't add a member accessor with the obvious name. The obvious name is exactly the one a user's own piece is likely to have used, and the member you add hides theirs — from calls that were written before your generator existed and never mentioned it.
- Don't judge safety by inspecting the pieces in front of you today. The point of taking the template as a parameter is that you do not know what will be passed tomorrow.
- Don't rely on a using declaration to unhide what you masked. That repairs the symptom for one name in one hierarchy and leaves the mechanism to collide again on the next.

## Checklist
- What names does this add to the assembled type, and would a user plausibly want each of them for their own piece?
- Does the accessor work through ordinary lookup at the call site, without the caller naming a namespace?
- If a supplied piece already defines a member with the same name, whose does a call reach?
- Could this accessor take the object as a parameter instead, and if so why has it not?

## Notes
This is a scoping problem rather than a style preference, and it is specific to code assembled from parts someone else wrote. An ordinary class owns its own names; a generated one is a shared scope where the library contributes structure and the user contributes members, and anything the library adds can shadow something the user is already calling.

What makes it costly is where the breakage lands. The collision does not appear where the generator is written, and it does not appear where the user's piece is written. It appears at a call site that predates both, whose author is now looking at a function they did not know existed, silently preferred over the one they meant.

The standard library reaches for the same shape whenever it must operate on types it does not own — the accessors for generic aggregates are free functions found by lookup, not members. That is not a stylistic preference either; a member could not have been added to types the library never declared.
