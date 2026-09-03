---
object_id: DRILL_box_related_statements_to_find_overlap
object_type: drill
name: Box the Related Statements and Look for Overlap
target_skill: Organizing statements within a routine so that related work stays contiguous, and recognizing interleaved concerns before they harden
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
- statement_organization
- refactoring
- code_review
- readability
cross_links:
- rel: supports
  target_object_id: PAT_minimize_variable_span_and_live_time
- rel: supports
  target_object_id: PAT_make_order_dependencies_visible
- rel: related_to
  target_object_id: PAT_extract_a_routine_even_when_it_seems_too_small
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Box the Related Statements and Look for Overlap

## Practice Task
Take a routine of thirty lines or more that you wrote recently, mark up its statements into groups of related work, and use the shape of the markings — not your judgment about the code — to decide whether it needs reorganizing.

## Target Skill
Organizing statements within a routine so that related work stays contiguous, and recognizing interleaved concerns before they harden.

## Setup
Print the routine, or open it somewhere you can draw rectangles freely. Working on paper or in a drawing tool matters more than it sounds — the point of the exercise is to produce a picture you can judge at a glance rather than a verdict you argue yourself into.

## Instructions
1. Pick a routine you wrote in the last week or two. Long enough to have structure, short enough to see whole.
2. Read it once and identify the groups. Statements belong together when they work on the same data, when they perform similar tasks, or when they must happen in a given order.
3. Draw a rectangle around each group. Do not adjust the groups to make the drawing come out well — that inverts the exercise.
4. Name what each rectangle does in a short phrase, and note any phrase that needs an "and" to be complete.
5. Look at the resulting picture and classify it. Rectangles sitting one after another are fine. One rectangle wholly inside another is fine, and expected wherever a group has sub-structure.
6. Find every place where two rectangles cross without one containing the other, and record the count before changing anything. Each crossing is a pair of concerns that have been interleaved rather than sequenced.
7. Reorder the statements to remove one crossing, show the behaviour unchanged, and redraw. Where a crossing will not come out, name the dependency holding it in place and judge whether that dependency is real or accidental.
8. Place every variable in the routine in exactly one rectangle, or identify it as spanning several.
9. Where a rectangle now sits alone with no meaningful relationship to what precedes or follows it, consider lifting it into a routine of its own.

## Success Check
- The rectangles are drawn from the grouping decided before the picture was looked at, and are not redrawn to improve it. Adjusting the boxing after seeing the shape moves the measurement instead of the code, and it satisfies every bullet below without reorganizing anything.
- Every rectangle has a short phrase naming what it does, and any phrase needing an "and" is noted as two groups boxed as one.
- The crossings on the first drawing are counted and the count recorded before any reordering. That count is the finding; a run showing only the final picture cannot demonstrate it changed.
- At least one crossing is removed by reordering statements, with the behaviour shown unchanged and the routine redrawn. A crossing that survives passes only with the dependency holding it named and judged real or accidental — left unexamined it does not.
- Every variable is placed in exactly one rectangle, or is identified as spanning several. A variable living across boxes is the same interleaving seen from the other side, and skipping this reports the picture without the data flow that produced it.

## Common Failures
- Redrawing the boxes until the picture looks tidy, instead of reordering the code. The drawing is a measurement, and adjusting the measurement to get a better reading defeats the exercise.
- Treating nesting as a problem. Nested groups are normal and often correct; the failure shape is specifically partial overlap, where two groups share some statements and neither contains the other.
- Grouping by syntax rather than by relatedness — boxing each loop or each conditional rather than each piece of work — which produces a clean picture that says nothing.
- Stopping at the first crossing removed. Crossings tend to come in clusters, because one interleaved pair usually forced its neighbours apart as well.
- Concluding that overlapping boxes mean the routine is too long. Length is a separate question; a short routine can interleave two concerns and a long one can be perfectly sequenced.

## Notes
The value here is that it converts a vague question into a visible one. Asking whether related statements are grouped well invites the answer "well enough," particularly from whoever wrote them. Asking whether any two rectangles cross has an answer you cannot talk yourself out of, and it takes about a minute on a routine you already understand.

What the picture is really measuring is how many concerns a reader has to hold at once. Two crossing rectangles mean that somewhere in the overlap a reader is tracking both concerns simultaneously, and every statement in that region has to be checked against both. That is also why the fix is usually reordering rather than rewriting — the statements are fine and their sequence is what costs.

Run this on code you wrote rather than on code you inherited, at least the first few times. Reorganizing someone else's routine requires you to establish which dependencies are real before you can move anything, and that turns a one-minute diagnostic into an afternoon. On your own recent code you already know what depends on what, so the exercise stays cheap enough to become a habit — and the habit is worth more than any individual reorganization it produces.
