---
object_id: PAT_put_review_effort_into_preparation_not_the_meeting
object_type: pattern
name: Put Review Effort Into Preparation, Not the Meeting
library_path:
- software-engineering
- core
- testing
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- reviews
- inspections
- defect_detection
- code_reading
cross_links:
- rel: related_to
  target_object_id: PAT_combine_detection_techniques_rather_than_perfecting_one
- rel: related_to
  target_object_id: PAT_review_to_detect_not_to_correct
- rel: related_to
  target_object_id: PAT_understand_the_routine_before_the_compiler_sees_it
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Put Review Effort Into Preparation, Not the Meeting

## Pattern Rule
**IF** you are organizing a review of someone's design or code
**THEN** spend the effort on individual reading beforehand and treat the meeting as the smaller part, because that is where the defects are actually found.
**ELSE** where a meeting genuinely earns its place — a large group, reviewers from outside the team, or people who have never inspected before — structure it formally, since an informal one costs the same and finds less.

## Do
- Weight the schedule toward reading. Across thirteen reviews at one company, ninety percent of the defects were found in preparation and only about ten percent during the meeting itself. Anything that trades preparation time for meeting time is trading the productive part for the ceremonial one.
- Give each reviewer a distinct lens instead of asking everyone to review. Assigning perspectives — the maintenance programmer, the customer, the designer — or specific questions and scenarios appears to surface more than a general request does, and it is the deliberate version of the finding that two reviewers overlap on only about a fifth of what they catch.
- Budget reading time from a rate rather than a guess. Around five hundred lines an hour suits application code and a hundred and twenty-five suits system code; a meeting, if you hold one, runs at roughly a hundred and fifty to two hundred non-blank non-comment statements an hour. Record your own numbers, because the effective rates vary by environment and by material.
- Drop the meeting entirely where scheduling it is the expensive part. Code reading — reviewers read independently, then discuss only what they found — detected about 3.3 defects per hour against testing's 1.8 and turned up twenty to sixty percent more errors over a project's life. The meeting is not strictly necessary, which makes this the technique of choice when reviewers are scattered.
- Apply the overhead test before scheduling anything. A review is a meeting and meetings are expensive; if the work justifies that overhead, structure it as a formal inspection, and if it does not, it does not justify a meeting at all — hand the document out and have people read it.
- Treat the choice between pairing and inspecting as a style question. The two produce broadly similar results on quality, cost, and schedule, so it can be settled by how the people involved prefer to work rather than by argument about which is technically superior.

## Don't
- Don't convene when people have not prepared. The property separating an inspection from an ordinary review is that it does not go ahead unless everyone has done the reading — without it, the meeting becomes the review, which is the arrangement that finds ten percent.
- Don't keep adding reviewers. Past two or three the defect count generally stops climbing; the gain comes from the second reader, not the sixth.
- Don't let a presentation stand in for reading. Walking the group through the material glosses over exactly the unclear points the exercise exists to find, and the work should speak for itself.
- Don't run past two hours or hold two in a day. Concentration does not survive either, and what gets missed afterwards outweighs what gets found.
- Don't read informal review as the cheap option. Bad experiences with technical review are nearly always with the informal kinds, which carry the full cost of a meeting and a fraction of the yield.

## Checklist
- What fraction of the total effort here is individual reading, and what fraction is sitting in a room?
- Does each reviewer have a distinct perspective or question assigned?
- Is preparation time budgeted from a rate, and does anyone know what the rate is here?
- Could this be done as independent reading with no meeting at all?
- Has everyone prepared — and if not, why is the meeting still going ahead?

## Notes
The ninety-ten split is the number that should reorganize how a review is run. Most review effort is scheduled around the meeting, with preparation treated as something people fit in beforehand if they can. The measurement says the meeting is where a tenth of the value appears, and that the reading is the activity. Once that is believed, the natural design changes — protect preparation time, allow the meeting to be short or skipped, and stop treating attendance as the marker that a review happened.

The perspective assignment is the operational consequence of a fact established elsewhere in this package, that reviewers overlap on only about a fifth of what they find. If different people reliably notice different things, then handing five reviewers the same undifferentiated request wastes most of the redundancy. Naming a lens for each one turns accidental variation into deliberate coverage, and it costs a sentence in the invitation.

An anecdote worth carrying, because it is about material that had every reason to be clean. The first edition of this book was self-reviewed after a cooling-off period, circulated to about a dozen peers, revised again, then passed through a copy editor, a technical editor, and a proofreader, and was in print for over a decade collecting around two hundred reader corrections. Formal inspections run against that text for the second edition still found several hundred previously undetected errors. Prior review effort, even substantial and varied prior review effort, does not saturate the defect supply.
