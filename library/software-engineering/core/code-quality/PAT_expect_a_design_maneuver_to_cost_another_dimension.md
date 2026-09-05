---
object_id: PAT_expect_a_design_maneuver_to_cost_another_dimension
object_type: pattern
name: Every Design Maneuver Buys One Dimension and Charges Another
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
- api_design
- tradeoffs
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_evaluate_code_against_quality_goals
- rel: related_to
  target_object_id: PAT_optimize_a_codebase_for_its_likely_activities
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Every Design Maneuver Buys One Dimension and Charges Another

## Pattern Rule
**IF** you are about to change a codebase to improve some property of how people experience it
**THEN** name the dimension you are paying with before you start, because improvements to one cognitive dimension routinely come out of another and the bill arrives later than the benefit.

## Do
- State the maneuver as a trade rather than as an improvement. Adding types improves error proneness; renaming toward the domain improves closeness of mapping; each has a second effect you should be able to name.
- Watch these three tensions by name. **Error proneness against viscosity** — types let the compiler prevent mistakes, and they also mean casting to use a value the way you want, which is usually the real reason people resist type systems rather than dislike of safety.
- **Provisionality and progressive evaluation against error proneness** — a system that lets you sketch and run incomplete code helps thinking, and incomplete programs may never be deleted while imperfect ones may never be improved, leaving code that is hard to understand and therefore hard to debug.
- **Role expressiveness against diffuseness** — named parameters and type annotations both make roles visible and both make the code longer.
- Accept that how the dimensions interact depends heavily on the codebase. These three recur; they are not the complete set, and yours may have others.

## Don't
- Don't treat a dimension as a target to maximise. Every one of them has a use case where high is wrong — high consistency costs effort during transcription, and high abstraction harms exploration.
- Don't argue a maneuver purely on the dimension it improves. That is how a codebase ends up safe and unchangeable, or flexible and undebuggable.
- Don't assume the cost is theoretical. Slow compiles and slow test suites are viscosity, arriving from outside the code entirely, and they are usually the accumulated price of maneuvers nobody costed.

## Checklist
- Which dimension is this change buying?
- Which one is it spending, and have I said so out loud?
- Is the dimension I am spending one that matters for how this codebase is actually used?

## Notes
"Design maneuver" is the framework's term for a change made to a codebase to improve a dimension, and the reason it is worth a name is that it forces the question of side effects. The original exercise pairs each maneuver with two columns — impacts which dimensions positively, impacts which negatively — and the second column is the one that does the work.

The consequences of leaving dimensions unmanaged are stated in terms of people rather than code, which is the point of the framework. High viscosity makes future developers reluctant to change the codebase, which produces complicated patches instead of structural fixes. A codebase requiring hard mental operations makes people less likely to become maintainers of it. Those are the failure modes this pattern exists to price.
