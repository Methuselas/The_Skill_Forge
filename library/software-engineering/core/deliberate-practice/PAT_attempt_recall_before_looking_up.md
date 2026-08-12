---
object_id: PAT_attempt_recall_before_looking_up
object_type: pattern
name: Attempt Recall Before Looking Syntax Up
library_path:
- software-engineering
- core
- deliberate-practice
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- retrieval_practice
- memory
- syntax
- deliberate_practice
cross_links:
- rel: related_to
  target_object_id: PAT_diagnose_weak_recall_as_storage_or_retrieval
- rel: teaches
  target_object_id: DRILL_practice_syntax_with_flashcards
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u03, pp. 40-42
  evidence_type: text
confidence: high
references: []
variants: []
---

# Attempt Recall Before Looking Syntax Up

## Pattern Rule
**IF** you are about to search for a piece of syntax you have written before
**THEN** produce your best attempt from memory first and only then verify it against the reference
**ELSE** searching immediately leaves the concept exactly as hard to recall next time

## Do
- Treat the impulse to search as a diagnosis, not just a need: it marks this concept as one whose retrieval is unreliable, which is the information worth acting on.
- Write the attempt down or type it into the editor rather than deciding you "sort of know it"; a half-formed answer you commit to still counts as an attempt.
- Verify against the real reference afterward and correct the attempt. A wrong attempt that gets corrected still strengthens the memory.
- Capture the concept for later practice at the moment you reach for the search, because that moment is the most reliable signal you will get about what you do not yet hold.

## Don't
- Don't count repeated exposure as practice. Ballard's students recalled roughly 10% *more* of a memorized poem two days later having done no further study, purely from being asked to recall it — re-reading code you have seen a dozen times produces no equivalent gain.
- Don't let the cheapness of searching make the decision. Because lookup is easy and habitual, the brain concludes the syntax need not be retained, retrieval stays weak, and the next lookup is guaranteed.
- Don't skip the attempt because you expect it to fail; failing to retrieve something you have tried to retrieve before is still easier than retrieving it cold.

## Checklist
- Did you commit to an attempt before opening the reference?
- Did you correct the attempt against what the reference actually said?
- Is the concept now captured somewhere you will practice it, or did you just move on?

## Notes
The cost of the lookup is measurable. Parnin recorded 10,000 programming sessions by 85 programmers and found it typically takes about a quarter of an hour to get back to editing after an interruption; programmers interrupted mid-edit resumed in under a minute in only 10% of cases. Opening a browser also invites the unrelated tab.

The benefit side rests on Bjork's distinction between storage and retrieval strength. The syntax is usually already stored — the recognition "of course it's `rbegin()`/`rend()`" proves it — so what has failed is access, and attempted access is the only thing that repairs access. Hermans calls the alternative a vicious cycle: because we do not remember it we look it up, and because we look it up instead of trying to remember it, we never build the strength that would let us stop.
