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
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u02, p. 20
  evidence_type: text
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

## Don't
- Don't buy into any single methodology 100 percent. The cost is not that the methodology is wrong — it is that you will see the whole world in terms of it and miss opportunities to use methods better suited to the current problem.
- Don't take a consultant's or an author's exclusivity claim at face value. The recommendation to adopt one approach to the exclusion of others is common and is the specific thing to resist.
- Don't stretch a single approach past where it fits. Extended too far or in the wrong direction, the frame that was guiding you starts misleading you instead, and the more powerful it is the further it can carry you off.

## Checklist
- Can you name the alternative you rejected and the reason?
- Did the problem select the approach, or did the approach select what you noticed about the problem?
- Are you still inside the range where this approach fits, or have you extended it past it?
- If two approaches both apply, is there a reason you are using only one?

## Notes
The failure here is perceptual rather than technical, which is what makes it hard to catch from the inside. A method you have fully adopted stops presenting itself as a decision and starts functioning as the description of the problem space, so the alternatives are not rejected — they are never generated. That is why the check has to be procedural: name an alternative out loud, every time, rather than waiting to notice that you should have.

McConnell's framing for the alternative is a toolbox of analytical tools, and the word *analytical* is doing work. These are not rules to comply with; they are instruments that tell you how to look for an answer rather than what the answer is. That property is also why they combine — two instruments pointed at the same problem do not conflict the way two rules would.

The same shape shows up narrowly in testing, where adopting a methodology such as TDD wholesale is the version of this trap most engineers meet first. This card is the general case; the testing-specific route carries the practices worth taking from those methodologies even when their headline rule is skipped.
