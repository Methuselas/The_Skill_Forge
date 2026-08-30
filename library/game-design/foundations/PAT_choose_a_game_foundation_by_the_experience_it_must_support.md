---
object_id: PAT_choose_a_game_foundation_by_the_experience_it_must_support
object_type: pattern
name: Choose a Game Foundation by the Experience It Must Support
library_path:
- game-design
- foundations
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- framework
- architecture
- adaptation
- novelty
cross_links:
- rel: related_to
  target_object_id: PAT_use_the_defining_affordances_of_an_adopted_game_system
- rel: related_to
  target_object_id: PAT_account_for_the_intended_play_environment_before_freezing_the_design
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Choose a Game Foundation by the Experience It Must Support

## Pattern Rule
**IF** an established rules framework, engine, genre structure, or other foundation can produce the intended player experience without fighting the design
**THEN** prefer adapting that foundation and spend new-design effort only where the intended experience requires behavior the foundation cannot support cleanly
**ELSE** justify a new foundation and budget for the additional validation, onboarding, implementation, and audience-building burden created by novelty.

## Do
- Start by stating what players should experience or be able to do, then test candidate foundations against that requirement.
- Count the benefits of reuse as real design assets: tested procedures, familiar interaction patterns, tooling, existing audiences, and known failure modes.
- When novelty is necessary, identify which requirement actually forces it so the project does not redesign unrelated parts by accident.
- Increase playtesting and implementation scrutiny when unfamiliar mechanics, components, or interaction methods are introduced.

## Don't
- Treat originality as a quality metric by itself.
- Keep an inherited framework when major portions of the design require exceptions, workarounds, or avoidance of the framework’s central behavior.
- Build a new system merely because designing one sounds more impressive than adapting a suitable existing one.

## Checklist
- The intended experience is written independently of any candidate framework.
- At least one existing foundation has been tested for fit before starting from zero.
- Any rejected foundation has a concrete mismatch, not merely a preference for novelty.
- Novel mechanics have an explicit validation plan proportional to how unfamiliar they are.

## Notes
Reuse and invention are both legitimate. The decision turns on fit. Existing foundations reduce uncertainty and can provide a ready-made mechanical language, but they become liabilities when the desired experience depends on behavior they were not built to express. Novelty therefore carries both opportunity and verification cost.
