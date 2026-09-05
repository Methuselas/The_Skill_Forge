---
object_id: AP_test_animation_incrementally_before_polish
object_type: ap
name: Test Animation Incrementally Before Polish
library_path:
- art
- subjects
- animation
- timing
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- testing
- roughs
- workflow
cross_links:
- rel: related_to
  target_object_id: AP_review_completed_animation_from_intent_to_evidence_and_revision
- rel: supports
  target_object_id: PAT_judge_animation_as_moving_performance_not_isolated_drawings
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Test Animation Incrementally Before Polish

## Objective
Validate motion repeatedly while it is cheap to change, moving from structural tests to rough passes before cleanup or finish.

## Steps / Flow
1. Test story keys and, when useful, run a **key-pose timing test before in-betweens** by holding each key for its planned duration so gross timing errors surface cheaply.
2. Test extremes and breakdowns while keeping the work structurally rough; do not spend design/detail effort on motion that has not survived playback.
3. Test rough primary action. In CG, block with simplified geometry before adding complexity; in stop-motion, rehearse the action and verify the puppet's usable range before committing the final take.
4. Test added secondary/tertiary motion. Isolate elements temporarily when that clarifies a problem, but keep interacting elements together when their relationship is what must be judged.
5. **When a detailed production layout overwhelms the rough motion, derive a simplified registered test underlay.** Preserve the approved camera, perspective, important contacts, and environmental anchors; trace or identify the key animation poses to locate the path of action; suppress rendering and nonessential detail inside that movement corridor so the animation remains visually dominant; and retain enough information outside it to judge staging, depth, contacts, and scene relationship. Test against this simplified environment rather than against either a blank field or a visually overpowering final layout.
6. Adjust the **test presentation** when necessary for diagnosis: allow an opening state enough time to register, crop closer to expose subtle motion, or inspect a difficult element separately without confusing the temporary test with the final staging.
7. **Run a repair-economy check before forcing many valid drawings to fit one incompatible layout.** If a large amount of otherwise sound animation conflicts with a background or layout, reconsider whether the cheaper correction lies on the layout side while preserving the owning story, camera, geography, and approved staging. A beautiful drawing is not sufficient reason to preserve the more expensive mistake.
8. Rewatch the entire shot repeatedly; do not let easy digital local edits replace whole-shot evaluation.
9. Only polish after timing, spacing, path, and performance survive playback.

**Completion check**
- Major motion errors are found before cleanup.
- Polish never serves as the first motion test.

## Notes
- Keep early animation rough while solving timing, spacing, path, performance, and continuity. Rough states are for discovering motion; cleanup is for preserving a motion solution that already works.
- At sequence scale, test storyboards and animatics before detailed animation so editing, geography, duration, and staging problems are corrected at their cheapest representation.
- Webster extends the same economy principle across media: rough line tests, key-pose timing holds, simplified CG blocks, and stop-motion rehearsals are all valid when they expose expensive mistakes before finish or irreversible capture.
- Byrne adds a layout-specific diagnostic mode: derive a simplified registered environment from the production layout, keep camera/perspective/contacts authoritative, and reduce detail inside the character's movement corridor so rough animation can be judged against the real scene without being visually buried. He also adds a useful repair-economy check: when many otherwise valid drawings conflict with one layout, compare the cost and authority of both fixes before forcing the larger body of work to conform.
