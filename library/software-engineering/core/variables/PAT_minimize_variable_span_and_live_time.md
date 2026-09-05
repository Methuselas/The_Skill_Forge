---
object_id: PAT_minimize_variable_span_and_live_time
object_type: pattern
name: Keep a Variable's References Close and Its Life Short
library_path:
- software-engineering
- core
- variables
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- variables
- scope
- span
- live_time
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_declare_and_initialize_at_first_use
- rel: related_to
  target_object_id: PAT_start_a_variable_at_the_narrowest_scope
- rel: related_to
  target_object_id: PAT_avoid_global_state_inject_shared_state
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Keep a Variable's References Close and Its Life Short

## Pattern Rule
**IF** you are arranging the statements that read and write a variable
**THEN** shorten both distances — the gap between consecutive references, and the total stretch from the first reference to the last — because every line in between is a line where the value can be changed, or where a reader can lose track of what it holds.
**ELSE** when the references cannot be brought together at all, the finding is about visibility rather than layout — a variable reachable from everywhere has enormous values for both by construction.

## Do
- Measure when the argument is worth settling. The gap is the count of lines between one reference and the next; the life is the last referencing line minus the first, plus one. In one worked contrast, three variables initialized in a block at the top of a routine score lives of 27, 67 and 67 — an average of 54 — and moving each initialization down to just above the loop that uses it gives 4, 8 and 8, for an average of 7.
- Do not infer a short life from tight clustering. A variable touched on every line from 1 to 25 has an average gap of zero and still lives for 25 statements. The two measures are independent, and only the second bounds how much code a reader has to hold at once.
- Reorder statements so each block needs fewer variables in play. A routine that interleaves the old-data and new-data sequences forces six variables to be tracked at once; running the old-data sequence to completion before starting the new one leaves three per block — and those blocks are then clean candidates for extraction, because their references are already grouped.
- Put a loop's initialization immediately above the loop rather than at the top of the routine, so that when somebody later wraps a second loop around the first, the initialization runs on every pass instead of only the first one.
- Poison a variable whose life is genuinely over. Setting a pointer to null once it has been deleted turns a silent stale read into an immediate, locatable failure.

## Don't
- Don't treat the space between two references as neutral. A value assigned on line 10 and not used until line 45 tells every reader that something in between depends on it; assigning it on line 44 tells them nothing does. Both messages get read whether or not you meant to send one.
- Don't leave a variable live across code you are about to change. The gap between references is exactly where new code lands, and new code is what alters the value or forgets what it was supposed to contain.
- Don't chase a threshold. No research has produced a number separating a good figure from a bad one, so this is a direction to move in, not a target to hit or a metric to report.

## Checklist
- Where is this variable first referenced and where last, and how many lines is that?
- Is there anything between those two points with no business touching it?
- How many distinct variables does this block require a reader to hold at once?
- Is the initialization inside every loop that needs it to be?
- If this routine were split in two tomorrow, are the references already grouped for the split?

## Notes
The unifying idea is the window of vulnerability. Every line between two references is an opportunity for code to be inserted that alters the value, and an opportunity for whoever is reading to forget what the variable is supposed to hold. Both measures are proxies for the size of that window, approached from different directions — one asks how far apart consecutive touches are, the other how long the variable is exposed at all.

Four consequences follow from a short life, and they are worth knowing separately because they fail separately. The code gives an accurate picture of itself, since the distance between references implies dependence and a short distance implies none. Initialization errors get rarer, because straight-line code turns into loops as a program is modified and a nearby initialization travels with the loop. Reading gets easier, because fewer lines have to be held at once. And extraction gets easier, which is the one people miss — a variable whose references already sit together does not have to be untangled before the block around it can become a routine.

The measures also settle an argument that otherwise runs on taste. When someone defends a widely visible variable on grounds of convenience, computing its life produces a number that is large by construction, and the discussion moves from preference to arithmetic.
