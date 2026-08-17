---
object_id: PAT_scale_formality_to_the_kind_of_software
object_type: pattern
name: Set Ceremony by What Failure Costs, Not by Habit
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- process
- formality
- risk
- reviews
- change_control
cross_links:
- rel: related_to
  target_object_id: PAT_do_prerequisites_per_increment_when_iterating
- rel: related_to
  target_object_id: PAT_keep_a_toolbox_instead_of_adopting_one_methodology
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Set Ceremony by What Failure Costs, Not by Habit

## Pattern Rule
**IF** you are deciding how much process to put around a piece of work — reviews, change control, specification formality, check-in procedure
**THEN** set each one from what failure costs in this particular system, so that a business system gets informal handling, a mission-critical system semiformal, and a life-critical embedded system formal inspection at every stage.

## Do
- Grade specification formality by consequence: informal requirements specification for a business system, semiformal plus as-needed reviews for a mission-critical one, formal specification plus formal inspections for embedded life-critical work.
- Grade the review mechanism the same way. As-needed code reviews suit mission-critical work; life-critical work gets formal code inspections; business systems can often run on neither.
- Grade change control from informal, through formal, to rigorous, along the same axis. This is the control that most often gets copied from the wrong column.
- Let design and coding merge where the stakes allow it. On business systems that combination is the listed good practice, not a corner being cut; mission-critical work separates architectural from detailed design, and life-critical work inspects both formally.
- Keep two things constant no matter which column you are in: developers test their own code, and test-first development. Those appear in every category, which is what marks them as baseline rather than ceremony.
- Scale a small method up rather than scaling a large one down. Starting from an all-inclusive method and paring it back reliably leaves ceremony nobody can justify but nobody dares remove; starting small and adding what the project demonstrably needs arrives at a defensible set. The target is neither lightweight nor heavyweight but right-weight for this project's size and type.
- Read project size as the second axis alongside failure cost. A method that fits three people does not fit thirty, because the formality is buying coordination rather than safety at that point — paperwork runs about 7 percent of effort on a thousand-line project and about 26 percent on a hundred-thousand-line one, and that growth is a response to communication load, not a lapse in discipline.

## Don't
- Don't carry one project's process to the next because it worked there. Twenty years of survey work found 40 different requirements-gathering methods, 50 variations on design work, and 30 kinds of testing across more than 700 languages — the spread is the point, and no single configuration is correct across it.
- Don't apply life-critical ceremony to a business system as a safety margin. The cost is real and the benefit is not, and it is the reliable way to make the process the thing people work around.
- Don't apply business-system informality to something whose failure hurts people. Requirements stability is part of what buys ultrahigh reliability, and it is not available without the formality that produces it.
- Don't treat the three categories as a taxonomy to place a project in exactly. Real projects vary infinitely around them; the columns are for calibrating individual controls, not for assigning an identity.

## Checklist
- For this system, what does a defect that reaches production actually cost?
- Which controls did you choose deliberately, and which arrived by habit from the last project?
- Are the two constants — developers testing their own code, test-first — in place regardless of which column you picked?
- Is any control here more formal than its neighbours for no stated reason?

## Notes
The observation that makes this actionable is that the practices do not move together as a bundle. Formality is not a single dial from "agile" to "waterfall"; it is a set of independent controls — planning, test and QA planning, change control, requirements formality, design separation, check-in procedure, review mechanism, deployment procedure — each of which can be set separately. Most process arguments happen because people are arguing about the bundle when the disagreement is actually about two or three of the controls.

Life-cycle model choice follows the same axis. Business systems tend to sit with agile approaches and evolutionary prototyping; mission-critical and life-critical systems tend toward staged delivery, spiral development, and evolutionary delivery. The direction of travel is that business systems benefit from highly iterative approaches with planning, requirements and architecture interleaved with construction and testing, while life-critical systems need more sequential ones.

The size axis has its own invariants, and they are worth naming beside the failure-cost ones. Regardless of how big a project is, four things stay valuable and become more so as it grows: disciplined coding practices, design and code inspections by other developers, good tool support, and working in a high-level language. Those are the practices to reach for first when scaling a method up, because they are already justified at every size and only get cheaper relative to what they prevent.

What makes documentation grow is worth understanding, because it decides whether a given document is worth writing. Communication paths multiply roughly with the square of the number of people, so formal documents are what a project substitutes for everyone talking to everyone. That gives a test for any document: it exists to force someone to think a decision through and then to convey it to people who were not there. A configuration-management plan earns its place by making somebody actually settle configuration management. If writing one feels like going through the motions and producing generic prose, that is evidence the document is not doing either job, and the response is to question the document rather than to write it more carefully.

The two invariants deserve their own emphasis because they are the ones most often mistaken for ceremony and dropped when a project decides to move fast. Developers testing their own code and test-first development appear in the informal column exactly as they appear in the formal one. Whatever else is being scaled down, those two are not part of what scales.
