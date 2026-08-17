---
object_id: PAT_keep_a_toolbox_instead_of_adopting_one_methodology
object_type: pattern
name: Pick the Method Per Problem Instead of Committing to One
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
- methodology
- technique_selection
- construction
- judgment
cross_links:
- rel: related_to
  target_object_id: PAT_pick_and_choose_testing_philosophies
- rel: related_to
  target_object_id: PAT_settle_load_bearing_decisions_before_finishes
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Pick the Method Per Problem Instead of Committing to One

## Pattern Rule
**IF** you are about to apply a development method, design approach, or technique because it is the one you use
**THEN** treat it as one analytical tool among several and choose against the problem in front of you, since a method you have committed to becomes the only one you can see.

## Do
- Notice the reflex. The moment to check is when you reach for an approach without having considered another — that is the signature of a method that has stopped being a choice.
- Name at least one alternative before proceeding, and say why the problem fits the one you picked. Techniques are not rules; they are analytical tools, and a tool is selected against a job.
- Treat accumulated technique as inventory. Effective developers spend years collecting dozens of techniques, tricks, and magic incantations, and the value is in knowing when to use each and how to use it correctly — not in having a favourite.
- Combine freely. Because these approaches guide how to look rather than dictating what to find, they are not mutually exclusive; using two together is normal, not a compromise.
- Budget for the dip when you do adopt something. Across a range of studied technologies — fourth-generation languages, structured techniques, CASE tools, formal methods, clean room, process models, object orientation — whatever benefit arrives shows up only after a real drop in productivity and quality while people learn the thing. Plan the first project using it as a learning exercise and price it that way, rather than being surprised by the trough and concluding the method does not work.
- Judge a method by what it does for your team's output, not by the volume or polish of what it produces. An acre of diagrams is still somebody's fallible interpretation of the requirements, and what a tool cost is not evidence about the quality of its output.

## Don't
- Don't buy into any single methodology 100 percent. The cost is not that the methodology is wrong — it is that you will see the whole world in terms of it and miss opportunities to use methods better suited to the current problem.
- Don't take a consultant's or an author's exclusivity claim at face value. The recommendation to adopt one approach to the exclusion of others is common and is the specific thing to resist.
- Don't stretch a single approach past where it fits. Extended too far or in the wrong direction, the frame that was guiding you starts misleading you instead, and the more powerful it is the further it can carry you off.
- Don't evaluate a newly adopted method while your team is still climbing its learning curve. Measured during the trough, everything looks like a failure; measured only after, everything looks like a triumph. Neither reading is about the method.
- Don't accept a method's own artifacts as authority. Class diagrams, use-case counts, and generated documentation describe what somebody understood, not what is true — and a team that has begun treating the diagram as the application has stopped checking either.

## Checklist
- Can you name the alternative you rejected and the reason?
- Did the problem select the approach, or did the approach select what you noticed about the problem?
- Are you still inside the range where this approach fits, or have you extended it past it?
- If two approaches both apply, is there a reason you are using only one?
- If you are adopting something new, has the cost of learning it been budgeted rather than absorbed?

## Notes
The failure here is perceptual rather than technical, which is what makes it hard to catch from the inside. A method you have fully adopted stops presenting itself as a decision and starts functioning as the description of the problem space, so the alternatives are not rejected — they are never generated. That is why the check has to be procedural: name an alternative out loud, every time, rather than waiting to notice that you should have.

McConnell's framing for the alternative is a toolbox of analytical tools, and the word *analytical* is doing work. These are not rules to comply with; they are instruments that tell you how to look for an answer rather than what the answer is. That property is also why they combine — two instruments pointed at the same problem do not conflict the way two rules would.

The same shape shows up narrowly in testing, where adopting a methodology such as TDD wholesale is the version of this trap most engineers meet first. This card is the general case; the testing-specific route carries the practices worth taking from those methodologies even when their headline rule is skipped.

The adoption cost is the part that gets left out of the decision, and leaving it out corrupts the evaluation as well as the plan. Reviews of the productivity and quality claims made for a long succession of development technologies found the same pattern each time: the initial enthusiasm was overblown, some of them did eventually deliver, and the benefit only became visible after a genuine decline while the team learned to use the thing. A team that has not budgeted for that decline reads it as evidence the method is bad and abandons it just before the return; a team that has committed publicly reads the eventual recovery as vindication and stops asking. Both are reading the learning curve rather than the method.

The false-authority problem is worth naming separately because it survives the toolbox stance. Choosing an approach deliberately still leaves you sitting in a meeting with a large quantity of formal-looking output, and volume reads as rigour. It is not: every diagram is somebody's interpretation, subject to the same errors as the prose it replaced, and expensive tools do not produce better designs than cheap ones. The tell that a team has crossed from using a method to serving one is when the artifacts stop being checked against the system and start being treated as the system, with the remaining work described as mechanical.
