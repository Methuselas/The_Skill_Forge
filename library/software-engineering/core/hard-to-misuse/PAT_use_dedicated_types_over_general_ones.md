---
object_id: PAT_use_dedicated_types_over_general_ones
object_type: pattern
name: Use a Dedicated Type Instead of an Overly General One
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- types
- hard_to_misuse
- type_safety
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_replace_primitives_with_descriptive_types
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_alias_the_type_when_a_class_is_too_big_a_step
  variant_name: Alias the Type When a Class Is Too Big a Step
  variant_basis: method_sequence
  difference_from_foundation: The foundation answers the how-specific-should-this-type-be question with a dedicated class, which buys compiler-enforced shape at the cost of designing, constructing, and testing a new type. This variant supplies the rung below it — a one-line type alias, declaring a name such as `Coordinate` for what is currently a float, and then declaring every latitude, longitude, and elevation with that name instead of the primitive. What it buys is different from what the class buys. Changing the representation from single to double precision becomes one edit in one place rather than a sweep. The declarations document themselves, since a name that says `Coordinate` tells a reader more than one that says float. And the data-typing decision stops being distributed through the program. What it does not buy is enforcement — in most languages an alias is figurative information hiding, and nothing stops a caller from looking up the underlying type or assigning across aliases, where a language with genuinely private types makes the hiding literal.
  when_to_use: Use when the value is a scalar rather than a structure, when the representation is genuinely uncertain and may change, and above all when the honest alternative is not a class but a bare primitive. The friction argument is the real one — the step from a one-line alias to a class is a large one, so a rule that only offers the class tends to produce neither, and the alias is the version that actually gets written.
  when_not_to_use: Do not use it where the concept has parts that can be swapped or miscounted; that is the foundation's territory and an alias gives no protection there. Do not redefine a name the language already predefines, which leaves readers assuming the standard meaning. And where the type needs to enforce a range or an invariant rather than merely name a representation, step up to the class.
  absorbed_from_object_id: none
---

# Use a Dedicated Type Instead of an Overly General One

## Pattern Rule
**IF** you need to represent a specific structured concept — a latitude-longitude pair, say
**THEN** define a small dedicated type (class or struct) for it rather than reaching for a general type like a list or a pair, so the type is self-describing and the compiler enforces its shape.

## Do
- Create a purpose type: a `LatLong` class with named `latitude` and `longitude` fields takes minutes to write and makes a parameter self-explanatory, needing no documentation.
- Get real type safety: a dedicated type fixes the field count and names, so latitude and longitude cannot be swapped and a wrong number of values cannot compile.
- Head off the spread: an overly general representation forces every neighbouring class to adopt it too, so a dedicated type stops a hacky paradigm from becoming pervasive.

## Don't
- Don't represent a location as a list of doubles (or a list of lists of doubles); nothing explains the type, latitude and longitude are easily reversed, and a list with too few or too many values still compiles and fails only at runtime.
- Don't settle for a pair type as the fix; a pair of two doubles enforces exactly two values but still does not name them or say which is latitude, so misuse remains easy.

## Checklist
- Does the type name the concept it represents, or is it a bare general container?
- Can the compiler reject a wrong shape (wrong count, swapped fields), or does that surface only at runtime?
- Would a neighbouring class be forced to adopt a hacky representation to interoperate?

## Notes
The map-location example runs the full ladder: a list of doubles is unlabeled and permissive, a pair fixes the count but not the naming or order, and only a dedicated `LatLong` class removes the documentation and the ambiguity entirely. This is the shortcut lesson in miniature — a few minutes defining a type saves head-scratching and bugs, and prevents the general representation from spreading through the codebase. This is the misuse-focused sibling of the readability-focused descriptive types.

`VAR_alias_the_type_when_a_class_is_too_big_a_step` adds the cheaper rung beneath the class, and its justification is about human behaviour rather than about types. A one-line alias — naming `Coordinate` for what is presently a float, then declaring every coordinate with that name — buys three of the things a class buys: a single edit point when the representation changes, declarations that document themselves, and the typing decision held in one place instead of spread through the program. It does not buy enforcement, and McConnell is direct that in a language like C++ this is figurative rather than literal information hiding; nothing prevents a reader looking up the underlying type or a caller assigning across aliases. The reason to keep it anyway is the friction observation: the step from writing one line to designing, constructing, and testing a class is a big one, and a programmer who would happily write the alias will often write nothing at all rather than write the class. Offering only the stronger remedy tends to produce the bare primitive. Use the class where parts can be swapped or an invariant needs enforcing, and the alias where a scalar simply needs a name and a single point of change.
