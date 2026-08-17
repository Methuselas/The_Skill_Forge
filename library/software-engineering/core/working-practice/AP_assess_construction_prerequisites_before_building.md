---
object_id: AP_assess_construction_prerequisites_before_building
object_type: ap
name: Assess the Groundwork You Inherited Before Writing Code
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
- prerequisites
- requirements
- architecture
- construction
- risk_reduction
cross_links:
- rel: related_to
  target_object_id: PAT_scope_construction_beyond_writing_the_code
- rel: prerequisite_for
  target_object_id: PAT_judge_an_architecture_before_building_on_it
- rel: prerequisite_for
  target_object_id: PAT_state_the_problem_before_the_solution
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Assess the Groundwork You Inherited Before Writing Code

## Objective

Find out, before committing code, whether the problem definition, requirements, and architecture handed to you are solid enough to build on — and adjust the approach, or stop, when they are not. You usually did not produce these artifacts and cannot fix them all, but you can determine how good your situation is and back up while backing up is still cheap.

## Steps / Flow

1. **Read the problem definition and check it is a problem.** It should be a short statement, one or two pages, in the user's language, describing what is wrong without naming a solution. If it names a solution instead, you do not yet know what you are solving.

2. **Run the requirements past the discriminating questions.** Not all of them, and formality scales with the project — but at construction time these are the ones that decide whether the ground holds: are the inputs specified with source, accuracy, range, and frequency; are the outputs specified with destination, accuracy, range, and format; is each requirement testable by an independent group; do the requirements avoid specifying the design; is each item traceable to its origin in the problem environment; and is the definition of success — and of failure — included.

3. **Stop and back up if they do not hold.** If the requirements are not good enough, stop work and make them right before proceeding. This feels like falling behind. Driving from Chicago to Los Angeles, stopping to check the map when you start seeing signs for New York is not a waste of time.

4. **Judge the architecture against what you will actually have to implement.** Look for the overview, the major building blocks with defined responsibilities and communication rules, coverage of every requirement by at least one block, and the rationale for the major decisions. One review of design practices found the design rationale is at least as important for maintenance as the design itself.

5. **Estimate only after the ground is known.** If requirements are unstable, treat requirements work as its own project and estimate the rest afterwards. Nobody can reasonably expect a schedule for a thing whose shape is undecided; a contractor asked to bid before being told what to build goes home.

6. **Choose the construction approach from what you found.** The point of the assessment is not a verdict but a calibration — how much to lean on the existing specifications, how much to expect churn, and how much to verify as you go.

## Notes

The framing that makes this worth doing is that you are at the end of the chain. The architect consumes the requirements, the designer consumes the architecture, and the coder consumes the design — so contaminated requirements contaminate the architecture, which contaminates everything you write. Nothing you do downstream recovers what was lost upstream; the best available outcome once construction starts on bad ground is keeping damage to a minimum.

The cost asymmetry is what makes stopping rational rather than pedantic. Purging an error before construction begins allows the rework to be done 10 to 100 times less expensively than during system test or after release, and the effect is graded rather than binary: a requirements defect caught at requirements time costs 1, at architecture 3, during construction 5–10, at system test 10, and post-release 10–100. An architecture defect costs 1 at architecture time and 15 at system test — the concrete version being that a $1,000 architecture fix becomes a $15,000 one.

Two calibration numbers. A well-run project spends about 10 to 20 percent of its effort and 20 to 30 percent of its schedule on requirements, architecture, and up-front planning, not counting detailed design, which belongs to construction. Read that range as a function of size rather than as a single target: the lowest-cost outcome for a ten-thousand-line project came from spending about 5 percent on architecture and requirements, while a hundred-thousand-line project did best at 15 to 20 percent. Applying the large-project figure to a small one is the overhead that makes people distrust prerequisites in the first place. And debugging plus associated rework takes roughly 50 percent of a typical development cycle — most of it spent on the expensive right-hand side of the curve, which is the room this assessment is trying to claim back.

Steps 1, 2, and 4 assess artifacts you may not own. That is the intended use: these are recognition procedures, not authoring ones. Knowing that a requirement is untestable is useful even when fixing it is someone else's job, because it tells you what to expect to churn.
