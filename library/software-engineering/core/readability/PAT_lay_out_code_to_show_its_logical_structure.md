---
object_id: PAT_lay_out_code_to_show_its_logical_structure
object_type: pattern
name: Lay Out Code to Show Its Logical Structure, Not to Look Pretty
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
- layout
- readability
- formatting
- maintainability
cross_links:
- rel: related_to
  target_object_id: PAT_follow_a_consistent_coding_style
- rel: related_to
  target_object_id: PAT_make_code_readable
- rel: related_to
  target_object_id: PAT_write_boolean_expressions_to_be_read_not_decoded
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Lay Out Code to Show Its Logical Structure, Not to Look Pretty

## Pattern Rule
**IF** you are choosing how to arrange code on the page — indentation, blank lines, line breaks, alignment
**THEN** take the arrangement that most accurately shows the logical structure, and where an arrangement that looks better conflicts with one that shows structure better, take the one that shows structure
**ELSE** where two arrangements represent the structure equally well, the difference is aesthetic and belongs to whatever convention is already in force.

## Do
- Judge a scheme against four criteria rather than against taste: does it represent the logical structure *accurately*, can it be applied *consistently* without a pile of exceptions, does it make the code easier to *read*, and does it *survive modification*.
- Prefer a scheme that makes good code look good and bad code look bad over one that makes all code look good. A scheme that beautifies everything has destroyed the signal you were formatting to produce, and in practice prioritising structure rarely produces ugly code — unless the logic is ugly, which is the point.
- Never let whitespace claim a structure the language does not have. Three statements indented under an unbraced loop tell a human that all three repeat and tell the compiler that one does; `x = 3+4 * 2+7` spaced that way reads as 63 and evaluates as 18. Layout that tells the reader a different story than it tells the machine is a defect waiting for a maintainer, not a style preference.
- Give each statement its own line so that complexity stays visible. Statements that are complex should look complex and statements that are simple should look simple — packing several onto one line hides how much is happening and makes the line count lie about the work.
- Reject any scheme in which changing one line forces you to change its neighbours. That is what condemns layouts aligned to the width of a preceding token: lengthen the first line and every aligned line below it has to move, so the scheme fights every edit and decays the moment someone is in a hurry.
- Settle a disagreement by naming which criterion each side is weighting. Most layout arguments are two people optimising different things without saying so, and stating the criteria converts an argument about taste into one about tradeoffs that can actually be resolved.

## Don't
- Don't trust that what looks best reads best. Given the same code at two, four, and six spaces of indentation, readers scored *worse* on comprehension at six — and many of them reported that six felt easier. Aesthetic appeal and measured readability come apart, and when they do the measurement is what matters.
- Don't treat layout as decoration applied after the work. The information in a program is denser than the information in a book, so it needs more organisational cues than a book, not fewer — and the cues have to be there from the start because retrofitting them is nobody's idea of a scheduled task.
- Don't conclude that good names and good comments will carry poorly laid-out code. They will not: the same routine with identical names and identical comments is unreadable at bad layout and clear at good layout, because the layout is what lets the rest of the effort become visible.

## Checklist
- Does the indentation match what the compiler will actually do?
- Would changing one line here force you to reformat several others?
- Does this arrangement make a complicated statement look complicated?
- If you are arguing about this, which of the four criteria is each side weighting?
- Is the scheme one you could apply to the whole file without exceptions?

## Notes
The organising claim is McConnell's Fundamental Theorem of Formatting: good visual layout shows the logical structure of a program. Everything else here is a consequence. Prettiness is worth something and it is worth less than structure, so it loses every time the two conflict.

The demonstration that makes the case is a single routine printed three times. The first is a wall of text, the second is broken into lines but crowded and structureless, the third is laid out properly. The code is identical in all three. The comments are identical. The variable names are identical and they are good. Only the whitespace differs — and in the first two versions the good names and the careful comments are simply invisible, doing nothing for the reader at all. That is the argument for treating layout as load-bearing rather than cosmetic: it gates the value of every other readability investment already made.

The maintenance criterion deserves more weight than it usually gets, because it is the one that predicts which schemes survive contact with a real codebase. Any layout that aligns code to the width of something above it is making every line depend on its neighbours' lengths, so ordinary edits produce either cascading reformatting or a layout that quietly stops being aligned. Schemes that indent by a fixed amount have no such coupling. This is also why the question is worth settling before construction rather than during it — the cost of a bad choice is paid on every subsequent edit.

What is *not* worth arguing about is which of several structurally accurate conventions to adopt. The one study comparing two common brace styles found no statistically significant difference in understandability, and the consistency of whatever you pick matters more than the pick — a convention followed inconsistently can read worse than no convention at all. That question belongs to [PAT_follow_a_consistent_coding_style](PAT_follow_a_consistent_coding_style.md); this card governs only the cases where one arrangement genuinely represents the code better than another.
