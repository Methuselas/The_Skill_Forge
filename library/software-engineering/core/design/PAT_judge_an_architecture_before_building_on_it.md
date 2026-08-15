---
object_id: PAT_judge_an_architecture_before_building_on_it
object_type: pattern
name: Refuse to Implement an Architecture You Cannot Follow
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- architecture
- design_review
- prerequisites
- conceptual_integrity
cross_links:
- rel: related_to
  target_object_id: AP_assess_construction_prerequisites_before_building
- rel: related_to
  target_object_id: PAT_settle_load_bearing_decisions_before_finishes
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u03, pp. 43-54
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Refuse to Implement an Architecture You Cannot Follow

## Pattern Rule
**IF** you are about to write code against an architecture or high-level design someone else produced
**THEN** check it for the things a builder needs — a comprehensible overview, building blocks with single responsibilities and stated communication rules, coverage of every requirement, and recorded reasons — and raise what is missing before implementing, not after.
**ELSE** if any part of it does not make sense to you, say so; you are the one who has to implement it, and code written against a design you do not understand will encode your guess instead.

## Do
- Start at the overview. If the description does not let you assemble a coherent picture of the whole from a dozen or so subsystems, you will not be able to tell how the class you are writing contributes to the system.
- Check each building block has one area of responsibility and knows as little as possible about the others' — and that the description says which blocks it may use directly, which indirectly, and which not at all.
- Map requirements to blocks in both directions. Every feature in the requirements should be covered by at least one block, and where two blocks claim the same function, their claims should cooperate rather than conflict.
- Hunt for the rationale, not just the decision. The architecture should record the alternatives considered and why the chosen organization beat them — for the system's organization, for the major classes, and for data design, where the reasoning behind picking a sequential-access list over a hash table is what makes maintenance possible later.
- Expect the major classes to be specified but not all of them. Aim for the 20 percent of classes that make up 80 percent of the system's behaviour.
- Treat unease as data. If you are uncomfortable with a part of it, that part is a defect in the design or in its explanation — the design should look natural and easy for the problem, not like the problem and the solution were forced together with duct tape.

## Don't
- Don't accept "we've always done it that way" as a recorded reason. That is the recipe that cuts both ends off the roast because the pan was too small two generations ago.
- Don't start coding around a gap and plan to raise it later. An architecture error costs about what a requirements error costs to fix — far more than a coding error — and the cost climbs with every line written against the wrong structure.
- Don't accept a design that only works on one machine or in one language when the program's purpose is not to exercise that machine or language. Environment coupling in the top-level design is usually over-architecture, doing badly at design time a job that construction would do better.
- Don't confuse thoroughness with quality. A part that receives more attention than it deserves is a defect in the same way an underspecified part is, and gold-plating — elements nothing required — is not a bonus.

## Checklist
- Can you draw the whole system from the overview without reading the details?
- For the block you are about to write: what is its single responsibility, and which blocks may it talk to?
- Is there a requirement with no block, or a block with no requirement?
- Are the risky areas named, with what was done to reduce them?
- Are the objectives stated, so you can tell whether this design optimizes for modifiability or for performance when the two collide?
- Is there anything here you do not understand or are uneasy about?

## Notes
The reason architecture is a prerequisite rather than a nicety is conceptual integrity — it is what keeps a system coherent from the top level down, and Brooks's central argument in *The Mythical Man-Month* is that maintaining it is the essential problem of large systems. A design that has drifted shows the drift as accumulated ad hoc additions, each of which fitted a local need and none of which fits the whole; the recognizable shape is a bill with a rider attached for every constituency.

The last item on the checklist is the one to take most seriously, and it is the one most easily talked out of. Discomfort with part of a design is usually read as inexperience, and sometimes it is. But the person who has to turn the description into working code is the one whose comprehension actually gates the outcome, and a design that cannot be explained to its implementer has failed at the only job that matters at that moment. Raising it costs a conversation; not raising it costs code that encodes a guess and looks finished.

Two shapes of failure sit either side of the good case. Underspecification leaves you inventing structure at the keyboard that should have been decided once, centrally. Overspecification burns effort on decisions that were cheap and, worse, makes the design brittle to the discoveries construction will inevitably produce. The architecture should tread between them, and knowing which side a given document errs on tells you which failure to prepare for.
