---
object_id: DRILL_make_a_side_effect_obvious_or_remove_it
object_type: drill
name: Make a Hidden Side Effect Obvious or Remove It
library_path:
- software-engineering
- core
- avoiding-surprises
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- side_effects
- avoid_surprises
- naming
- refactoring
cross_links:
- rel: teaches
  target_object_id: PAT_avoid_unexpected_side_effects
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: detecting side effects hidden behind getter-like names and either removing or surfacing them
references: []
variants: []
---

# Make a Hidden Side Effect Obvious or Remove It

## Practice Task
Take a getter-like function that secretly modifies state, decide whether the side effect is needed, and either remove it or rename to surface it — then trace the fix through its callers.

## Target Skill
Finding side effects that a function's name hides and resolving them by deletion or honest naming.

## Setup
No special setup required.

## Instructions
1. Start from a read-style function that also mutates state — a `getPixel` that calls `canvas.redraw()` before returning a color.
2. List the ways the hidden effect can bite: an expensive loop (a screenshot calling it per pixel), a broken assumption (a redaction that assumes no redraw), and a concurrency hazard across threads.
3. Ask whether the side effect is actually necessary; if not, remove it and confirm the problems disappear.
4. If it is necessary, rename the function to name the effect (`redrawAndGetPixel`) and propagate honest names to callers that inherit it (`redrawAndCaptureScreenshot`).
5. Re-examine each caller and confirm the new name would make them reconsider the expensive loop, the broken assumption, and the threading risk.

## Success Check
- Each of the three failure modes is traced to a concrete consequence in the example — how many redraws an image-sized loop causes, the specific assumption the second caller makes, the interleaving that breaks across threads. Naming the three is the setup rather than the finding.
- Whether the effect is necessary is answered with a reason, and that answer decides which path the rest of the run takes. A run that renames without asking has skipped the only step that could have removed the problem instead of labelling it.
- Where the effect stays, callers inheriting it are found by searching and the search is stated, not recalled. The caller that is forgotten is the one whose name still lies.
- At least one caller is re-read under the new name and the decision it would now prompt is written down. A rename that changes no reader's decision has not been tested, only performed.
- The opposite failure is checked: a name honest enough that callers who do not want the effect have nowhere to go. Where no effect-free variant exists, that is recorded as an outstanding cost rather than left implied.

## Common Failures
- Renaming the leaf function but leaving inheriting callers with innocent-looking names.
- Keeping an unnecessary side effect and only documenting it in a comment instead of removing it.

## Notes
This drills Long's `getPixel`/`captureScreenshot` cascade, where one hidden redraw causes a 47-minute freeze, a privacy leak, and a threading bug. The reflex it builds is to treat a getter that mutates as a defect and to fix it at the name, so the caller's mental model can no longer be wrong.
