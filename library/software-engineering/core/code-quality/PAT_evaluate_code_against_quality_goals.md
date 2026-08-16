---
object_id: PAT_evaluate_code_against_quality_goals
object_type: pattern
name: Judge Code Against the Four Quality Goals
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_quality
- requirements
- maintainability
- engineering_judgment
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_balance_adaptability_without_predicting_future
- rel: prerequisite_for
  target_object_id: PAT_reuse_before_reinventing
- rel: prerequisite_for
  target_object_id: PAT_invest_in_quality_over_hacky_shortcut
- rel: prerequisite_for
  target_object_id: PAT_make_code_readable
- rel: prerequisite_for
  target_object_id: PAT_match_caller_mental_model
- rel: prerequisite_for
  target_object_id: PAT_make_code_hard_to_misuse
- rel: prerequisite_for
  target_object_id: PAT_design_modular_interfaces
- rel: prerequisite_for
  target_object_id: PAT_make_code_reusable_and_generalizable
- rel: prerequisite_for
  target_object_id: PAT_design_for_testability
- rel: prerequisite_for
  target_object_id: PAT_decompose_into_layers_of_abstraction
- rel: prerequisite_for
  target_object_id: PAT_define_your_code_contract_explicitly
- rel: prerequisite_for
  target_object_id: PAT_classify_error_recoverability_by_caller
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_hermans_judge_a_codebase_on_cognitive_dimensions
  variant_name: Judge a Codebase by What It Does to Its Readers
  variant_basis: method_sequence
  difference_from_foundation: The foundation evaluates code against four goals that are properties of the software — it works, keeps working, adapts, and does not reinvent. This variant evaluates the same thing against thirteen properties of the *experience of using it*, asking what the codebase does to a reader's brain rather than what it does to a computer. The dimensions are error proneness, consistency, diffuseness, hidden dependencies, provisionality, viscosity, progressive evaluation, role expressiveness, closeness of mapping, hard mental operations, secondary notation, abstraction and visibility. Answers questions the four goals cannot reach, such as whether people will find this code easy to change or easy to find information in.
  when_to_use: Use for libraries, frameworks and modules that other programmers call rather than modify, where the cost of poor design is borne by people you never meet. It is also the right frame for the questions that decide a codebase's future — whether contributors will attempt structural changes or only patch around them, and whether anyone will volunteer to maintain it.
  when_not_to_use: Do not substitute it for the four goals on a single function or class under review; the dimensions are codebase-scale properties and most of them are meaningless at that granularity. It also does not judge correctness, so it complements the first quality goal rather than covering it.
  absorbed_from_object_id: none
---

# Judge Code Against the Four Quality Goals

## Pattern Rule
**IF** you are deciding whether a piece of code is actually good — while writing it, reviewing it, or before submitting it
**THEN** judge it against four concrete goals instead of a gut reaction: (1) it works and meets *all* requirements; (2) it keeps working as surrounding code and requirements change; (3) it is adaptable to changing requirements; (4) it does not reinvent the wheel.

## Do
- Fold non-functional requirements — latency, CPU usage, privacy, security — into goal 1: code that implements the feature but blows the latency budget does not "work."
- Treat "keeps working" as its own design concern, because code depends on other code that will be modified, updated, and changed around it.
- When code triggers a "yuck" or "this is excellent" reaction, trace the reaction to which of the four goals it helps or harms, turning a subjective feeling into an objective call.

## Don't
- Don't equate code quality with nit-picky advice about trivial things; the goals exist to create better software, not to police style trivia.
- Don't assume code that runs today will still run tomorrow — a dependency change, a new feature, or an evolving problem can break it.

## Checklist
- Can you name which of the four goals a given change advances?
- Are performance, security, and privacy requirements included in your definition of "working"?
- Have you asked how this code behaves when the code around it changes?

## Notes
`VAR_hermans_judge_a_codebase_on_cognitive_dimensions` retains **Judge a Codebase by What It Does to Its Readers** as a second evaluation route at a scale the four goals do not reach. Where Long's goals are properties of the software, the cognitive dimensions of codebases are properties of using it — thirteen of them, from error proneness and consistency through viscosity and closeness of mapping to secondary notation and visibility. The framework is Green, Blackwell and Petre's cognitive dimensions of notation, built for flowcharts, extended to programming languages, and generalised by Hermans to codebases. What it buys is the ability to ask whether people will find this code easy to change or easy to search, and the failure modes it predicts are social rather than technical — high viscosity produces contributors who patch around problems instead of fixing them, and a codebase demanding hard mental operations struggles to attract maintainers. Reach for it on libraries and frameworks others call rather than modify, and keep the four goals for judging a function or a class, where most of the dimensions do not apply.

Long frames code quality as inherently subjective — "yuck" versus "excellent" gut reactions — and makes it objective by stepping back to what he is really trying to achieve: work, keep working, adapt, and not reinvent the wheel. The goals deliberately absorb concerns engineers sometimes file separately: performance and security are part of "working," and durability under change ("keep working") is called out because code does not live in isolation. This is the evaluative foundation the book's six pillars and later chapters build specific techniques on.
