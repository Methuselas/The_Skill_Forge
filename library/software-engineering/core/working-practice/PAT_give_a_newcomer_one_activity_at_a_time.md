---
object_id: PAT_give_a_newcomer_one_activity_at_a_time
object_type: pattern
name: Give a Newcomer One Programming Activity, Not Four
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: teach
foundation_role: foundation
routing_class: teaching
specialization_axis: none
foundation_object_id: none
tags:
- onboarding
- teaching
- cognitive_load
- working_practice
cross_links:
- rel: related_to
  target_object_id: PAT_support_the_memory_system_the_activity_taxes
- rel: related_to
  target_object_id: PAT_account_for_the_curse_of_expertise_when_onboarding
- rel: supports
  target_object_id: AP_prepare_an_onboarding_for_all_three_memory_systems
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u13, pp. 213-214, 216
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Give a Newcomer One Programming Activity, Not Four

## Pattern Rule
**IF** you are setting a first task for someone new to a codebase
**THEN** choose a task that requires exactly one of the five programming activities, because the standard welcome task requires at least four and each taxes a different memory system.

## Do
- Count the activities in the task before setting it. "Fix this small bug" asks the newcomer to search for the right place, comprehend unfamiliar code, explore to orient, and increment with a change — four activities, before any of them is easy.
- Set single-activity tasks and let them build. Search for a class that implements a certain interface; write a natural-language summary of a specific method; implement a method from a plan you supply; browse the codebase for a general sense of it; add a feature to a class including planning it.
- Sequence them so they compound on related code — search for a class, then transcribe a method within it, then increment the same class in a more complex way.
- **Prefer understanding to building as a welcome task.** If you want a newcomer to understand a piece of code, ask them to understand it — summarise a class, or list every class involved in executing a feature — rather than handing them an implementation task and hoping understanding follows.
- If you do want a feature implemented, strip the other activities out of it. Prepare the relevant code beforehand, refactoring what is needed into one place so the newcomer does not have to search.
- Alternate the axis deliberately: some tasks focused on programming concepts, some on the domain, according to what prior knowledge the person already has.

## Don't
- Don't trust the "beginner-friendly" label, on your own issue tracker or an open-source project's. It usually marks small scope, not few activities, and small scope with four activities is the exact failure this pattern names.
- Don't count the code walkthrough as having removed the searching. A newcomer who has watched someone else click through the code still cannot navigate it, and will spend the task searching while trying to build.
- Don't optimise the first task for output. A good summary of code serves later newcomers as documentation better than another feature does, so the low-load choice is also the more valuable one.

## Checklist
- How many of the five activities does this task actually require?
- Is there a version of this task that is only comprehension?
- Have I removed the searching, or only assumed the walkthrough removed it?

## Notes
This applies chapter 11's five activities — searching, comprehension, transcription, incrementation, exploration — to the onboarding case, and the argument is the one that framework supplies: each activity places different demands on the programmer and the system, so switching between them is itself expensive. Asking a newcomer to switch between four while none is fluent is a load problem before it is a skill problem.

Table 13.3 supplies one worked example per activity, which is what makes the pattern usable rather than merely correct — the hard part in practice is inventing a single-activity task, not agreeing that one would be better.

The germane-load argument decides the priority between the two halves. A focused task leaves capacity for storing what was learned; a four-activity task consumes it all, so the newcomer completes the work and retains little of it. That is why "ask them to understand" beats "ask them to build" for a first task even when both are achievable.
