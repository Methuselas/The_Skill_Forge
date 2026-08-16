---
object_id: PAT_program_into_the_language_not_in_it
object_type: pattern
name: Decide What to Express First, Then Find How the Language Can Carry It
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- language_choice
- conventions
- abstraction
- design
- construction
cross_links:
- rel: related_to
  target_object_id: PAT_write_the_language_you_are_in_not_the_one_you_know
- rel: related_to
  target_object_id: PAT_follow_a_consistent_coding_style
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Decide What to Express First, Then Find How the Language Can Carry It

## Pattern Rule
**IF** the language, framework, or toolchain you are working in has no direct support for a structure you want
**THEN** settle what you want to express first and then work out how to express it with what you have — inventing a convention, a standard, or a small library to carry the missing structure.
**ELSE** when the language does support it directly, use the language's own construct rather than a convention that shadows it.

## Do
- Write the constraint down as a rule that can be checked, not as an intention. A convention only compensates for a missing construct if a reader can tell at a glance whether a file obeys it.
- Prefer a rule that makes every instance identical over one that is merely sensible. When every unit of a kind works exactly the same way, you never have to re-derive what a given call means.
- Give the convention a single narrow interface. McConnell's example allowed his form files to do only two things — read from and write to the database — and exposed exactly one public routine so callers had one question they could ask and one answer to interpret.
- Watch for the workaround shapes the missing structure would otherwise force, and treat them as the signal to introduce a convention: loading something you do not need just to reach a routine buried inside it, or copying logic out and then maintaining parallel copies.
- Expect the environment to push against you. A language that lacks the structure often actively encourages the opposite, so the convention has to be maintained deliberately rather than falling out of normal use.

## Don't
- Don't let the toolset bound what you consider. Limiting your thoughts to constructs the language directly supports means primitive tools produce primitive designs, and the limit is in the thinking rather than in the language.
- Don't treat a missing feature as permission to give up on the structure. The structure is a decision about the program; the language is only how it gets written down.
- Don't build an elaborate framework where a convention will do. The value of the example convention was that it was simple enough to hold in mind while working.

## Checklist
- Can you state what you want to express independently of how this language would say it?
- If the language cannot say it, what convention or small library would, and is it checkable by reading?
- Does every instance of the convention behave identically, or does each need interpreting?
- Are you about to write a workaround — a hidden load, a copied block — that a convention would remove?

## Notes
The distinction is Gries's, and it is the one McConnell says matters most for reading his book: most important programming principles do not depend on specific languages but on how you use them. Programming *in* a language takes the available constructs as the boundary of the thinkable. Programming *into* one starts from the thought and treats the language as the medium it has to survive.

What makes this more than an attitude is that the compensation is cheap and local. The worked example is a single rule — form files may only move data to and from the database, all other logic lives elsewhere, and one public routine reports completion — adopted because the language of the day encouraged putting everything in the form file and made calling out awkward. The rule cost nothing to state and removed a class of convoluted code that would otherwise have accumulated across the project.

The ELSE clause matters as much as the rule. A convention that duplicates something the language already expresses is worse than nothing: it adds a second, weaker way to say the same thing, and readers now have to know both. Reach for this only where the gap is real.
