---
object_id: PAT_define_task_objective_before_judging_human_action_mechanics
object_type: pattern
name: Define Task Objective Before Judging Human Action Mechanics
library_path:
- art
- subjects
- animation
- motion
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_identify_causal_level_of_animated_movement_before_adding_performance
tags:
- animation
- action_analysis
- human_motion
- objective
- balance
- locomotion
- projection
- manipulation
- effort
cross_links:
- rel: related_to
  target_object_id: PAT_track_force_continuity_through_action
- rel: related_to
  target_object_id: PAT_scale_whole_body_effort_to_apparent_load
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Define Task Objective Before Judging Human Action Mechanics

## Pattern Rule
**IF** a human action looks generically plausible but its force, trajectory, precision, support, or body recruitment cannot be judged confidently
**THEN** define what the action must accomplish first, then evaluate the mechanics against that objective rather than against a generic symbol of the action
**ELSE** retain the simpler action when its objective and success condition are already unambiguous

## Do
- State the immediate job of the movement before refining it: maintain balance, travel, project something, manipulate something, exert effort, or combine several of these aims.
- Define what success means for the specific task, such as maximum distance, precise placement, controlled contact, sustained resistance, stable support, or efficient travel.
- Let the objective change the physical solution. A long-distance throw can recruit more range and force than a precision toss even though both are recognizably throws.
- Match tool handling to the result being sought. Similar hand-and-arm actions should change when the task shifts from a heavy strike to a delicate controlled contact.
- When several objectives overlap, decide which one dominates at each phase so balance, locomotion, manipulation, projection, and effort do not compete accidentally.
- Recheck the action after posing or timing changes to make sure the visible mechanics still serve the intended result.

## Don't
- Do not judge an action only by whether it resembles the generic category named in the brief.
- Do not use maximum force when the task requires accuracy, restraint, or fine control.
- Do not assume that two actions using the same tool, limb, or broad gesture should share the same force, timing, or body recruitment.
- Do not treat Webster's objective labels as mutually exclusive boxes; real actions can combine them and shift emphasis during the movement.

## Checklist
- The intended result of the action can be stated independently of the pose description.
- Force, trajectory, speed, support, and precision all make sense for that result.
- Similar-looking actions with different goals would produce visibly different mechanics where needed.
- Any change of dominant objective during the action is reflected in the body rather than only in the story description.

## Notes
Action analysis becomes more reliable when the animator asks what the movement is for before asking what it should look like. Balance, locomotion, projection, manipulation, and effort are useful starting categories because they expose different success conditions, but they often overlap. The durable decision is to judge mechanics against the task being accomplished rather than against a stock image of “throwing,” “hitting,” “cutting,” or another named action.
