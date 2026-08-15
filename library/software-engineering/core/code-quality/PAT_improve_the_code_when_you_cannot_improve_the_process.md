---
object_id: PAT_improve_the_code_when_you_cannot_improve_the_process
object_type: pattern
name: Fix the Code When You Cannot Fix the Process
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- construction
- prioritization
- code_quality
- documentation
- process_improvement
cross_links:
- rel: related_to
  target_object_id: PAT_evaluate_code_against_quality_goals
- rel: related_to
  target_object_id: PAT_invest_in_quality_over_hacky_shortcut
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u01, pp. 6-8
  evidence_type: text
confidence: high
references: []
variants: []
---

# Fix the Code When You Cannot Fix the Process

## Pattern Rule
**IF** you are asked to improve something and the surrounding process is visibly broken — no written requirements, no architecture, testing dropped
**THEN** put the effort into the construction-level work you can do right now, because that is the part that will actually happen.
**ELSE** name the missing process step once, in one line, and then go do the code work anyway.

## Do
- Spend the effort where the code is: the naming, the control structures, the routine boundaries, the tests you can add without permission. These land whether or not anyone restores the phases around them.
- Apply source-code improvement techniques consistently rather than occasionally. Consistency is what separates a detailed, correct, informative program from a Rube Goldberg contraption; scattered application separates nothing.
- Write the code as though it is the documentation, because on many projects it is the only documentation available to programmers. Requirements specs and design documents go out of date; the source is always current.
- When you do have room to change one thing about how the work runs, change something inside construction. Requirements and architecture exist so construction can be done effectively and independent system testing exists to verify it was done correctly — improving the middle improves the project regardless of what surrounds it.

## Don't
- Don't make the code work conditional on the process work. Real projects skip requirements and design to jump straight into building, and drop testing once they have too many defects and too little time — and they still ship whatever gets built.
- Don't answer a request to improve code with a proposal to improve process. The proposal needs someone else's agreement and a schedule; the code change needs neither.
- Don't assume a rushed project has no room for technique. The spread among individual programmers during construction ran a factor of 10 to 20 in Sackman, Erikson, and Grant's study and has been confirmed repeatedly since, and none of that spread depends on the process being fixed first.

## Checklist
- Is the improvement you picked something you can finish without anyone restoring a phase?
- Did you state the missing process step once and move on, or are you still arguing for it?
- If every document on this project went stale tomorrow, would the code still say what the system does?
- Is the technique being applied across the change, or in the one spot that was easy?

## Notes
The instinct this corrects is a strong one: seeing a project with no requirements work, no architecture, and abandoned testing, the natural move is to try to put those back. McConnell's counter is availability rather than value. The ideal project does careful requirements development and architectural design first, then comprehensive system testing afterwards; imperfect real ones skip both ends. What no project skips is the part where the rubber meets the road — so that is the part where effort is certain to land, and it is also 30 to 80 percent of total project time depending on project size.

None of this argues that the missing phases do not matter. They do, and each affects a project's success as much as construction. The claim is narrower and about sequencing your own effort: the phases are someone else's to restore and may never be restored, while the construction work is in your hands today.

One thread here gets its full treatment much later. That code outlives every other artifact's accuracy is a reason to care about clarity now; the concrete commenting and naming techniques that follow from it arrive in the self-documenting-code material, and this card should not be read as a substitute for them.
