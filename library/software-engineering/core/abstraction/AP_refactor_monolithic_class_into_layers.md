---
object_id: AP_refactor_monolithic_class_into_layers
object_type: ap
name: Refactor a Monolithic Class Into Clean Layered Abstractions
library_path:
- software-engineering
- core
- abstraction
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- refactoring
- abstraction
- dependency_injection
- interfaces
cross_links:
- rel: supports
  target_object_id: PAT_size_classes_by_pillars_not_lines
- rel: supports
  target_object_id: PAT_use_interfaces_for_swappable_layers
- rel: supports
  target_object_id: PAT_decompose_into_layers_of_abstraction
- rel: supports
  target_object_id: PAT_use_dependency_injection
- rel: supports
  target_object_id: PAT_tune_layer_thickness_err_thin
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Refactor a Monolithic Class Into Clean Layered Abstractions

## Objective
Transform a class that has grown to solve several subproblems into a set of cohesive, independently reusable and testable classes with clean layers of abstraction, without leaking implementation details.

## Steps / Flow
1. **Identify the subproblems.** Read the class and list every distinct subproblem it solves internally, including nested ones — for a text summarizer: splitting text into paragraphs, scoring importance, and beneath scoring, finding important nouns, verbs, and adjectives. `PAT_decompose_into_layers_of_abstraction` owns where one subproblem ends and the next begins.
2. **Diagnose against the pillars.** For each pillar (readable, modular, reusable, testable), name a concrete way the monolith fails it, to confirm the split is worth doing and to target where the seams belong. The pillar test itself belongs to `PAT_size_classes_by_pillars_not_lines`.
3. **Extract one class per concept.** Move each subproblem's logic into its own class with a single cohesive concern (a `ParagraphFinder`, a `TextImportanceScorer`), each exposing only the public functions its layer needs.
4. **Inject dependencies through the constructor.** Have the top class receive the extracted classes as constructor parameters rather than creating them internally, and provide a static factory (`createDefault`) so callers get a wired instance easily. `PAT_use_dependency_injection` owns how the dependency arrives.
5. **Extract an interface where implementations will vary.** If a subproblem has more than one plausible approach, turn its class into an interface with an implementation per approach (word-based vs model-based scoring), let the top class depend only on the interface, and configure the choice via factory functions. Whether an interface is warranted at all is `PAT_use_interfaces_for_swappable_layers`.
6. **Check layer thickness.** Confirm no extracted layer is so thin that its pieces only ever serve each other; if so, merge back. When unsure, leave layers slightly thin rather than thick, and expect a few iterations before the layering settles. `PAT_tune_layer_thickness_err_thin` owns the thickness judgement.

## Notes
This is the chapter's worked refactoring, generalized: the `TextSummarizer` moves from a monolith (everything in one class) to one-class-per-concept with constructor injection, then to an interface-backed scorer with factory wiring, while the too-thin `OffsetDetector` split marks the stopping point. Steps 4 and 5 name dependency injection and interface extraction, which chapter 8 develops in depth; here they are the mechanics that turn a diagnosed monolith into clean layers. Apply it both to code that arrived bloated and to a class you notice growing while you modify it.
