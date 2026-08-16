---
object_id: PAT_write_design_notation_at_the_level_of_intent
object_type: pattern
name: Write Design Notation at the Level of Intent
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
- pseudocode
- detailed_design
- design_notation
- intent
- comments
cross_links:
- rel: related_to
  target_object_id: AP_build_a_routine_from_intent_level_pseudocode
- rel: related_to
  target_object_id: PAT_comment_why_not_what
- rel: related_to
  target_object_id: PAT_choose_design_depth_by_risk_not_habit
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Write Design Notation at the Level of Intent

## Pattern Rule
**IF** you are writing down a design for a piece of code before the code exists
**THEN** state each step in precise English describing what it accomplishes, borrow nothing from the target language's syntax, and refine downward until turning a line into code would require no decision you have not already made.
**ELSE** stop refining when writing the code instead would be a waste of time — that is the floor, and going below it produces a transcription rather than a design.

## Do
- Test any line by asking which languages it could be implemented in. `allocate a dlg struct using malloc` and `*hRsrcPtr = resource number` could only ever have become C; `Allocate a dialog box structure` and `Store the resource number at the location provided by the caller` could become anything.
- Say what the outcome means rather than what the mechanism does. `Keep track of current number of resources in use` carries a purpose; `increment resource number by 1` carries an operation whose purpose you now have to reconstruct.
- Describe returns by what they signify. `Return true if a new resource was created; else return false` survives a change of convention that `return 1` and `return 0` do not.
- Write the one-paragraph statement of purpose before the step list, and treat trouble writing it as a finding about your understanding rather than about your prose.
- Refine unevenly. Some lines from the first pass are already at the floor; others are high enough to hide a decision, and those are the ones to decompose. Any line you are unsure how to code is not finished.

## Don't
- Don't reach for the target language's constructs because they are precise. They drop the design to the level of the code, which throws away the reason for designing above it, and they impose syntactic restrictions you had no need to accept yet.
- Don't get into coding details such as which numeric status a routine hands back. Those are decisions the design should still be free to change.
- Don't leave a line high enough to gloss over a problematic detail. The details you skipped are still there and will be met later, at the level where they cost the most.
- Don't assume any English-like description will do. The intuition that collecting your thoughts in prose is enough is exactly what produces the version that reads fluently and helps with nothing.

## Checklist
- Could each line be implemented in a language other than the one you have in mind?
- Does any line name a function, operator, or notation belonging to that language?
- Does each line say what it achieves rather than what statement it will become?
- Is there a line you could not turn into code right now without deciding something new?
- Read as a comment above the code it produced, would each line still be telling a reader something?

## Notes
The two failure directions are asymmetric in how they feel. Writing too low feels productive, because language-specific notation is precise and looks like progress; what it costs is invisible, since the design silently becomes single-language and the reviewer is now reading code. Writing too high feels efficient and defers the same work to the point where it is most expensive to do. The floor and ceiling given here are the only two constraints that matter, and they are stated as tests rather than as a style guide because the failure is a level error, not a formatting one.

There is a downstream consequence that makes the level worth getting right beyond the design itself. These lines are not scratch work — in this method they become the finished code's comments. A line written at the level of intent becomes a comment that says something the code below it cannot; a line written at the coding level becomes a comment that restates its own code, which is the standard argument against commenting, arrived at by writing the design at the wrong altitude.

The reason this needs a card rather than being obvious is the natural assumption that any English-like description that collects your thoughts is as good as any other. Both bad versions are legible, orderly, and written by someone who was genuinely thinking. Legibility is not the variable being controlled.
