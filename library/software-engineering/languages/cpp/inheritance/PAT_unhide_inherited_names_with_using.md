---
object_id: PAT_unhide_inherited_names_with_using
object_type: pattern
name: Unhide Inherited Overloads with using Declarations
library_path:
- software-engineering
- languages
- cpp
- inheritance
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- inheritance
- name_hiding
- overloading
cross_links:
- rel: related_to
  target_object_id: PAT_use_public_inheritance_only_for_is_a
- rel: related_to
  target_object_id: AP_choose_the_relationship_between_two_types
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Unhide Inherited Overloads with using Declarations

## Pattern Rule
**IF** a derived class declares a function whose name matches one that has overloads in the base class
**THEN** restore the hidden base overloads with a `using` declaration (or, under private inheritance, a forwarding function), because a name in a derived scope hides every base overload of that name.

## Do
- Add `using Base::name;` in the derived class for each inherited name you would otherwise hide, so all base overloads stay visible alongside the derived ones.
- Put those using declarations in the same access section they had in the base — public names stay public under public inheritance.
- Under private inheritance, when you want only one specific overload, write a small forwarding function that calls the base version instead of a using declaration.

## Don't
- Don't assume declaring one overload in the derived class keeps the others; name lookup hides all base overloads of that name, even ones with different parameter types and regardless of virtual-ness.
- Don't leave overloads hidden under public inheritance — losing them violates the is-a relationship, since a base call that should work no longer compiles.

## Checklist
- Does a derived declaration share a name with base overloads I still want callable?
- Is there a `using` declaration (or forwarding function) making the base overloads visible?
- Under public inheritance, can every base overload still be called on a derived object?

## Notes
Name hiding is a scope rule, not an inheritance rule: a derived `mf3()` hides `Base::mf3()` and `Base::mf3(double)` alike, just as a local variable hides a global of the same name regardless of type. The default protects against accidentally inheriting overloads from distant bases, but under public inheritance you almost always want them, so a `using` declaration is the fix. Private inheritance is the one case where selectively exposing a single overload — via a forwarding function — is legitimate.
