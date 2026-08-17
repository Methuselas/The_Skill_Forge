---
object_id: PAT_look_for_the_evidence_outside_the_code
object_type: pattern
name: Read the Record Around the Code, Not Only the Code
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_quality
- maintenance
- evidence
- legacy_code
- diagnosis
cross_links:
- rel: related_to
  target_object_id: PAT_diagnose_why_the_code_degraded_before_changing_it
- rel: related_to
  target_object_id: PAT_concentrate_effort_where_defects_concentrate
- rel: related_to
  target_object_id: PAT_watch_for_semantic_coupling
reference:
  source_title: 'Refactoring at Scale: Regaining Control of Your Codebase'
  author: Maude Lemaire
confidence: medium
references: []
variants: []
---

# Read the Record Around the Code, Not Only the Code

## Pattern Rule
**IF** you believe a region of the codebase is causing enough trouble to be worth changing, and your belief rests on having worked in it
**THEN** go looking for the trace that trouble left in the written record around it — the design documents, the incident write-ups, the question threads, the ticket history — before committing to the change
**ELSE** where the record turns out to be thin or absent, treat that as information too, since a region genuinely costing people time usually leaves marks somewhere.

## Do
- Read the limitations section of whatever design document covers the current implementation. Authors frequently name the exact condition under which their approach would stop working, and a surprising share of the time that condition is the one you are living in — which converts your hunch into a prediction the original designers wrote down.
- Read the alternatives that document rejected. Options set aside for reasons that no longer apply are candidate designs already partly worked through, and knowing why each was dropped tells you which constraint to check before picking it up.
- Search the incident write-ups for the region, and read the contributing-factors and what-went-badly sections specifically. Those are where the cost of a confusing implementation shows up as time-to-resolution, and a count of incidents naming the area is a harder number than any impression.
- Notice where the onboarding material and the style guidance spend their length. Disproportionate coverage marks the places enough people got lost that somebody wrote defences, and bold warnings about what not to do are usually scar tissue.
- Search the question threads and chat archives for the region's vocabulary. This is the cheapest test of whether your frustration is yours alone, and it frequently turns up the same question asked at intervals by people across several teams over years.
- Note who asked, not only what was asked. People who hit the problem before you understand it already, and their accounts will tell you which parts are genuinely hard and which merely look it.
- Use ticket history to bound the time already spent. Bugs traced to the region and changes that took longer than their size suggests both estimate the ongoing cost, coarsely but in units anyone can compare against the cost of fixing it.

## Don't
- Don't take the absence of a document as the absence of a record. Most of what a team knows about its own difficult code sits in conversations and issue threads rather than in anything anyone would call documentation.
- Don't collect only the material that agrees with you. Threads where somebody explains why the implementation is the way it is are the ones most worth reading, because they are the ones that can change the plan.
- Don't mistake a well-documented region for a healthy one. Volume of explanation tracks how much explanation people needed, which points the other way.
- Don't let evidence-gathering become the project. This bounds a decision that is otherwise made on feel; a decision you can already make on a document or two is made.

## Checklist
- Does a design document exist, and does its limitations section describe your situation?
- How many incident write-ups name this region in their contributing factors?
- Has anyone asked your question before, and how long ago was the first time?
- What does the ticket history say about time spent here relative to the size of the changes?
- Did you find anything that argues against the change, and what did you do with it?

## Notes
The reason to leave the code is that the code records what was built and nothing about what it cost. A region can read badly and cause very little trouble because nobody touches it, and another can read acceptably while quietly consuming an afternoon from every person who passes through. The difference is invisible in the source and thoroughly visible in the surrounding record, which is written by exactly the people who paid.

Design documents are the most undervalued item on the list because of what their limitations sections tend to contain. Authors under no pressure to sell anything to anyone will state plainly where their approach gives out, and that statement was made by people holding the full problem in mind. Finding your present difficulty described there is the strongest evidence available that the difficulty is structural rather than a matter of taste — and the rejected alternatives sitting a page later are the closest thing to a head start that exists.

Conversation archives do a different job, which is calibration. Working in code that resists you produces a conviction that it is bad, and that conviction is not reliable on its own, since the same feeling attends code that is merely unfamiliar. Discovering that the same confusion has recurred at intervals for years, among people with no connection to each other, separates a property of the code from a property of your acquaintance with it. It also identifies the people worth talking to, who are generally happy to be asked and have usually thought about it more than they have written down.
