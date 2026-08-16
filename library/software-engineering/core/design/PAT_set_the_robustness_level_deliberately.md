---
object_id: PAT_set_the_robustness_level_deliberately
object_type: pattern
name: State How Robust to Build Before Anyone Builds It
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
- robustness
- overengineering
- architecture
- consistency
- simplicity
cross_links:
- rel: related_to
  target_object_id: PAT_judge_an_architecture_before_building_on_it
- rel: related_to
  target_object_id: PAT_settle_one_error_handling_strategy_systemwide
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# State How Robust to Build Before Anyone Builds It

## Pattern Rule
**IF** you are about to write a component and no one has said how much hardening it should carry
**THEN** get the expectation stated — err toward robustness, or toward the simplest thing that works — because left unstated each author picks their own and the system ends up robust in patches.

## Do
- Ask for the instruction in exactly those terms, as a direction to err in rather than a level to hit. It is a tie-breaker for the many small judgment calls nobody will review, not a specification.
- Expect the system-level requirement to exceed the sum of the component requirements. A system assembled from many minimally robust parts can be less robust than required overall, so the components may need to be hardened past what any of them needs alone.
- Watch for the reflex in yourself. Programmers routinely overengineer their classes automatically, out of professional pride, which means the default is not neutral and will not stay consistent across a codebase without an explicit instruction.
- Where the instruction is toward simplicity, take it as licence rather than as a compromise. Building the simplest thing that works, deliberately, is a decision the design made — not a corner you cut.

## Don't
- Don't reason about system reliability as a weakest-link problem. In software the chain is not as strong as its weakest link; it is as weak as all the weak links multiplied together, so several individually acceptable components can compound into an unacceptable whole.
- Don't harden a component past its stated level because you happen to be the one writing it. The cost is not the extra code — it is the unevenness, where some classes are exceptionally robust and others barely adequate and nobody can predict which is which.
- Don't confuse this with error handling policy. That decides how a detected error is treated; this decides how much effort goes into surviving one at all.

## Checklist
- Do you know which way this component is supposed to err, and who said so?
- If every component were built to this level, would the assembled system meet its reliability requirement?
- Are you adding hardening because the design asked for it, or because it felt unprofessional not to?
- Would another author working on a sibling component make the same call you just made?

## Notes
Robustness here means the ability to keep running after detecting an error, and the interesting property is that it does not aggregate the way intuition suggests. The weakest-link model says a system is as reliable as its worst part, which would make it enough to find and fix the worst part. The multiplicative model says otherwise: five components that each work 99 percent of the time do not give you a system that works 99 percent of the time. That is why an architecture may reasonably demand more robustness from parts than the requirements demand of the whole.

The failure this prevents is not any individual over- or under-built component but the variance between them. A codebase where the hardening level is unpredictable is one where nobody can reason about what happens under failure without reading everything, and where defensive code accumulates in the places written by cautious authors while the paths written under deadline stay bare. Consistency is the deliverable; the level chosen matters less than that the same level was chosen everywhere.

Professional pride is named explicitly as the mechanism, and it is worth taking seriously rather than as a joke. The impulse to make the thing you personally are writing more solid than strictly required is a good instinct in isolation and a source of inconsistency in aggregate — which is precisely why the decision has to be made above the level of the person writing the component.
