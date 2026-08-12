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
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u06, pp. 151-156
  evidence_type: text
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
- The function either no longer causes the side effect or names it unmistakably.
- Callers that inherit the effect also name it, so no reader is misled.
- Each of the three original failure modes is visibly addressed.

## Common Failures
- Renaming the leaf function but leaving inheriting callers with innocent-looking names.
- Keeping an unnecessary side effect and only documenting it in a comment instead of removing it.

## Notes
This drills Long's `getPixel`/`captureScreenshot` cascade, where one hidden redraw causes a 47-minute freeze, a privacy leak, and a threading bug. The reflex it builds is to treat a getter that mutates as a defect and to fix it at the name, so the caller's mental model can no longer be wrong.
