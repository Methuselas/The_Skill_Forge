---
object_id: PAT_check_whether_a_second_model_composes_or_conflicts
object_type: pattern
name: Check Whether a Second Model Composes With the One You Already Use
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- problem_solving
- notional_machine
- mental_model
- abstraction
cross_links:
- rel: related_to
  target_object_id: PAT_reason_with_a_notional_machine_at_a_chosen_level
- rel: related_to
  target_object_id: PAT_guard_against_an_outdated_mental_model_under_load
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u06, pp. 106-107
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Check Whether a Second Model Composes With the One You Already Use

## Pattern Rule
**IF** you are adopting a second way of thinking about a language concept on top of one you already reason with
**THEN** work out whether the two compose into one picture or contradict each other, and if they contradict, pick one deliberately instead of letting both stay live.

## Do
- Expect a set of overlapping models rather than one all-encompassing one; a language does not come with a single notional machine, and the ones you hold accumulate as you learn.
- Look for the composable case and build on it. A variable as a box extends cleanly to an array as a stack of boxes, and a parameterless function as a package of lines extends to a traveler carrying values in a backpack, then to a traveler that brings a value back.
- When two models cannot be merged, name the tradeoff on each side before choosing. Variable-as-box makes simple assignment easy to grasp; variable-as-name-tag makes it structurally obvious that only one value can be attached at a time.
- Choose the model whose failure mode you can least afford in the code you are actually reading.

## Don't
- Don't try to hold a conflicting pair simultaneously and hope context will select the right one — "we either think of a variable as one or the other," and under load the wrong one surfaces.
- Don't assume a model that extended well once will keep extending; composability is a property of a specific pair, not a general feature of good models.
- Don't drop a model merely because it is imperfect. The box carries a real misconception risk and is still the better on-ramp for a first assignment.

## Checklist
- Does the new model add a layer to the one I have, or replace a claim it makes?
- If they conflict, which one have I actually committed to for this codebase?
- What does my chosen model make it easy to get wrong, and is that error visible here?

## Notes
Figures 6.5 and 6.6 carry this more directly than the prose. Figure 6.5 puts a single labeled box beside a vertical stack of indexed boxes, so the extension from variable to array is visible as literally the same object repeated. Figure 6.6 sets two hand-drawn function machines side by side — on the left `print_square(5)` with a figure carrying a 5 in, on the right `square(5)` with a second figure carrying 25 back out — which is what makes "input parameters only" versus "input and output parameters" an extension rather than a replacement.

The conflicting case is the variable as box against the variable as name tag or sticker. The box implies a container that could hold several things, "like a box can hold multiple coins or candies," and a sticker cannot be placed on more than one thing, so the second model rules out a misconception the first invites. Chapter 6 pairs this with the finding from Hermans's own NEMO study that the two framings produce measurably different errors, which is developed separately under metaphor selection.
