---
object_id: PAT_use_interfaces_for_swappable_layers
object_type: pattern
name: Represent a Layer With an Interface When It Earns Its Keep
library_path:
- software-engineering
- core
- abstraction
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- interfaces
- modularity
- dependency_inversion
- configurability
cross_links:
- rel: related_to
  target_object_id: PAT_decompose_into_layers_of_abstraction
- rel: related_to
  target_object_id: AP_refactor_monolithic_class_into_layers
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Represent a Layer With an Interface When It Earns Its Keep

## Pattern Rule
**IF** you are deciding whether a layer of abstraction should be represented by an interface
**THEN** define one when there are (or plausibly will be) multiple implementations to swap, and have higher layers depend only on the interface; for a single implementation, add an interface only where its benefits outweigh its costs, not reflexively.

## Do
- For the multi-implementation case, extract the subproblem to an interface (`TextImportanceScorer`) and let each approach implement it (`WordBasedScorer`, `ModelBasedScorer`), wiring the choice through factory functions or dependency injection so higher code never names a concrete class.
- For the single-implementation case, weigh the real benefits: a crisp public API, insurance against having guessed wrong about needing only one implementation, easier mocking or faking in tests, and the option for one class to satisfy two interfaces (a `LinkedList` serving both `List` and `Queue`).
- Weigh those against the costs: extra code and files, and harder navigation — a reader chasing the logic must go interface-then-implementation instead of straight to the class.

## Don't
- Don't hide every single class behind an interface as a reflex; taken to an extreme it makes code unnecessarily complex to understand and modify.
- Don't let a higher layer depend on a concrete implementation class when an interface is meant to be the layer's boundary.

## Checklist
- Is there more than one implementation to swap, now or plausibly soon? If so, an interface is warranted.
- For a lone implementation, can you name a concrete benefit (clear API, testing, future-proofing) the interface buys here?
- Do all higher layers depend on the interface rather than the concrete class?

## Notes
The scoring example carries the strong case: wanting to trial a machine-learning scorer alongside the word-based one without replacing it wholesale is exactly when an interface pays off, letting factory functions configure either summarizer. The "interfaces for everything?" discussion carries the judgment case — Long lists genuine benefits even for a single implementation but warns from experience that blanket interface-ing gets out of hand. His rule of thumb: keep layers clean enough that hiding a class behind an interface later would be trivial, but add the interface only where it provides an appreciable benefit.
