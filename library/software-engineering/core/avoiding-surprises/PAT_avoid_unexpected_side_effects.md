---
object_id: PAT_avoid_unexpected_side_effects
object_type: pattern
name: Avoid Unexpected Side Effects or Make Them Obvious
library_path:
- software-engineering
- core
- avoiding-surprises
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- side_effects
- avoid_surprises
- naming
- concurrency
cross_links:
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Avoid Unexpected Side Effects or Make Them Obvious

## Pattern Rule
**IF** a function would modify state outside itself — redrawing a display, writing a file, calling a system, touching a cache
**THEN** avoid the side effect if it is unnecessary, and if it is necessary make it unmistakable in the function's name, especially for a function that looks like a plain getter.

## Do
- First ask whether the side effect is needed at all; removing an unnecessary `canvas.redraw()` from a `getPixel` is the cleanest fix.
- If it must stay, name the function for it: `redrawAndGetPixel` warns callers a redraw happens, so no one calls it 280,000 times in a screenshot loop and freezes the app.
- Propagate the honesty upward — a caller that inherits the side effect (`captureScreenshot`) should name itself `redrawAndCaptureScreenshot` so the next caller knows too, including anyone running it across threads.

## Don't
- Don't hide a side effect behind a get/read name; engineers assume a value-reading function is free of them, so a redacting screenshot that secretly redraws leaks the personal data it was meant to erase.
- Don't ignore the multithreading cost of a hidden side effect; a getter that mutates shared canvas state corrupts reads from another thread, and such bugs are rare per call but near-certain at scale and brutal to debug.

## Checklist
- Is the side effect actually required, or leftover caution that can be deleted?
- Does the function's name make any remaining side effect impossible to miss?
- If two threads called this at once, would the shared-state change break either?

## Notes
A side effect is any change a function makes beyond its return value, and they are unavoidable in real software; the surprise comes when a function's name does not advertise one. Long's `getPixel`-redraws-canvas example cascades into three failures — a 47-minute screenshot freeze, a broken privacy redaction, and a multithreading corruption — all flowing from a getter that lies about being pure. The remedy is cheap: remove the effect, or rename so the caller's mental model matches reality. Chapter 7's immutability is the deeper defense against unwanted state change.
