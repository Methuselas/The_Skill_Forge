---
object_id: AP_run_an_evidence_driven_playtest_revision_cycle
object_type: ap
name: Run an Evidence-Driven Playtest Revision Cycle
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
- playtesting
- evidence
- revision
- feedback
cross_links:
- rel: related_to
  target_object_id: PAT_define_the_intended_player_before_designing_for_them
- rel: related_to
  target_object_id: PAT_make_the_game_operable_without_hidden_designer_knowledge
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: DRILL_stress_test_the_core_resolution_grammar
- rel: related_to
  target_object_id: DRILL_stress_test_mechanical_constraints_under_composition
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Run an Evidence-Driven Playtest Revision Cycle

## Objective
Run completed-game playtesting as an evidence-producing revision cycle: begin with a specific question, preserve the test conditions long enough to observe the game honestly, distinguish symptoms from diagnoses and proposed fixes, decompose mixed evidence when a test build changed several things at once, revise or revert only as strongly as the evidence supports, retest every changed behavior, and stop the current cycle when its defined completion criteria are satisfied.

## Steps / Flow
1. **Enter with a testable build and an intended behavior.** Preserve the matching game version, design specification, GDD state, or other recoverable statement of what the tested version is supposed to do.
2. **Name the test question.** State what this session is primarily trying to learn. Avoid using “is the game fun?” as the only question when a more diagnostic question can be asked.
3. **Choose appropriate testers.** Include people representative of the intended audience, and when useful vary experience, play style, or familiarity within that audience so one regular group is not mistaken for the whole market of intended players.
4. **State the test conditions.** Tell participants what kind of play or content is being tested, what the session is focusing on, and what table or safety procedures apply.
5. **Preserve the test environment.** Do not silently repair, reinterpret, or explain the game while it is being tested. Intervene when continuing would otherwise be impossible or inappropriate, but record the intervention as part of the evidence.
6. **Observe behavior, not only opinions.** Record confusion, lookup time, repeated questions, skipped options, dominant strategies, stalls, unexpected solutions, pacing changes, referee improvisations, emotional reactions, and other observable effects relevant to the test question.
7. **Collect independent feedback before open discussion when practical.** Written or private responses reduce the chance that the first or loudest opinion rewrites everyone else's memory of the session.
8. **Separate observations from proposed fixes.** Preserve the symptom as evidence. Treat any suggested cause or repair — including the designer's own — as a hypothesis requiring diagnosis and testing.
9. **Classify evidence strength.** Mark each important finding as ambiguous or group-specific, recurring, severe but uncertain, or a conclusive/reproducible defect.
10. **Branch on evidence strength.**
    - If a finding is ambiguous or plausibly group-specific, repeat it with another group, scenario, or test condition when the question matters enough to resolve; otherwise leave it explicitly unresolved rather than treating it as proof.
    - If a finding is recurring or severe but still uncertain, run a targeted reproduction that changes as few unrelated conditions as practical.
    - If a failure is already conclusive and reproducible — such as a demonstrably missing required rule or a reproducible infinite-action exploit — repair it without ceremonial repetition merely to satisfy a test-count ritual.
11. **Decompose mixed-result bundles.** If the tested build changed several things and the package is rejected while some components are clearly supported, do not label every included change a failure. Separate the changed components, preserve the observations for each, revert or isolate the rejected pieces, and retest retained pieces independently when their value matters.
12. **Make an unvalidated revision or revert.** Prefer the smallest justified repair when the defect is local, but redesign or remove the underlying rule when the architecture itself is wrong. Returning to a known-working prior state is a legitimate result when the replacement has not earned its migration or regression cost.
13. **Regression test the change.** Rerun the changed behavior and nearby dependencies. A repair, retained component, or partial reversion does not become trusted merely because it sounds cleaner on paper.
14. **Preserve history.** Keep prior versions, change records, matching specifications, and test records long enough to compare outcomes, reverse a bad repair, distinguish newly introduced regressions from older defects, and identify what each tested build was supposed to implement.
15. **Apply the completion gate.** Continue the cycle while required fundamentals remain unsupported, material unresolved defects remain, or an implemented repair has not survived retesting. When the current version's defined design and release gates are satisfied and no material unresolved defect remains for this cycle, stop. Further ideas become later revisions, enhancements, expansions, optional modules, or next-version work rather than proof that the current cycle never finished.

## Notes
Completed-game playtesting is not an approval ritual. It is an empirical revision loop. Different groups can expose different truths about the same design, so uncertain findings often need reproduction; recurrence is an evidence tool rather than a ceremonial threshold. Testers are excellent sensors for what happened to them, but their repair suggestions remain design proposals. Preserve observations, diagnose causes, and version revisions so the design can learn without being whipsawed by noise.

The durable rule is: **repeat uncertainty, decompose mixed evidence, repair or revert proof, retest change.** A rejected test build can contain a useful component; package-level failure is not evidence that every bundled change failed. When a GDD or equivalent specification exists, preserve the specification state with the tested build and use its completion gates to decide when testing has done enough for the current version.
