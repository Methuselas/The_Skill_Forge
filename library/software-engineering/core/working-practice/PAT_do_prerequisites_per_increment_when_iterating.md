---
object_id: PAT_do_prerequisites_per_increment_when_iterating
object_type: pattern
name: Iterating Does Not Buy You Out of the Upfront Work
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
- iterative_development
- prerequisites
- requirements
- architecture
- rework
cross_links:
- rel: related_to
  target_object_id: AP_assess_construction_prerequisites_before_building
- rel: related_to
  target_object_id: AP_grow_a_system_from_a_running_skeleton
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Iterating Does Not Buy You Out of the Upfront Work

## Pattern Rule
**IF** you are working iteratively and about to skip requirements or architecture work on the grounds that the approach absorbs change anyway
**THEN** identify the critical requirements and architectural elements for the piece you are about to build, before you build it — iteration reduces the cost of missing upstream work, it does not remove it.

## Do
- Scope the upfront work to the increment rather than to the system. A builder starting a housing development does not need every detail of every house, but does survey the site and map the sewer and electrical lines — otherwise a sewer line has to be dug under a house that is already standing.
- Pick a completeness target and hold it. One workable rule is to specify about 80 percent of the requirements upfront, reserve time for the rest, and run systematic change control on new ones; another is to specify the most important 20 percent and develop the rest in small increments as you go. Both beat deciding case by case.
- Lean further toward upfront work when the requirements are fairly stable, the design is straightforward and well understood, you know the application area, risk is low, long-term predictability matters, or downstream change looks expensive. Lean toward as-you-go work when those are reversed.
- Notice the failure on both sides. Too little upfront work exposes construction to a stream of destabilizing changes and stops consistent progress; too much produces doggedly defended requirements and plans that downstream discoveries have already invalidated.

## Don't
- Don't read "requirements will change anyway" as "requirements work has no value." The change rate is an argument for cheap revision, not for skipping the first version.
- Don't take the smoothness of iterative rework as evidence it is cheap. Costs get absorbed piecemeal across the project instead of landing at the end, so the total never presents itself as a number anyone reacts to — it is paid in small installments rather than one bill.
- Don't assume defects found within an iteration are found early. They are still found late *in that iteration*, and correcting them still means parts of the software get redesigned, recoded, and retested.
- Don't aim for 100 percent of requirements or design upfront either. It is not practical, and most projects find their value in identifying the most critical requirements and architectural elements rather than all of them.

## Checklist
- For the increment in front of you: which requirements and which structural elements does it depend on, and are they settled?
- Is there anything in this increment that a later increment will have to dig up to reach?
- Which of the six conditions — requirement stability, design clarity, domain familiarity, risk, predictability, downstream change cost — actually hold here?
- Are you defending a plan that a recent discovery has already invalidated?

## Notes
The illustrative arithmetic is what makes this concrete, and the striking comparison is not the one people expect. On a project of the same size: sequential without prerequisites totals $1,000,000; iterative without prerequisites totals $875,000; sequential *with* prerequisites totals $600,000; iterative with prerequisites totals $550,000. Iteration is worth something — $125,000 in this illustration. Prerequisites are worth roughly three times that. And the crossing case is the one that settles the argument: an iterative project that ignores prerequisites costs substantially more than a sequential project that attends to them.

The claim being resisted here is a specific one — that iterative techniques make upstream focus unnecessary — and it is not a straw man; it is asserted in print. What is true is the weaker version: iterative approaches reduce the impact of inadequate upstream work, because defects are detected nearer the time they were introduced and the cost curve is steep in elapsed time. That is a real benefit and it is why iterative approaches suit most software. It is not immunity.

In practice almost nothing is purely one or the other. Activities overlap on even highly sequential projects, and on many projects they overlap for the entire duration. The useful question is therefore not which camp a project belongs to but how completely the prerequisites have been satisfied for the specific piece about to be built, and adjusting accordingly.
