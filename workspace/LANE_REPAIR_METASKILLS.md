# Lane repair — metaskills — COMPLETE

Done 2026-09-03. `metaskills` had **zero `supports` edges of any kind**: three
APs, two Patterns, and no ownership graph at all. Because rule 10 ships
`metaskills` and its closure in every release, that broken graph was the one
every consumer inherited.

## Result

| | before | after |
|---|---|---|
| patterns claimed by an AP | 0 of 2 (0%) | **2 of 2 (100%)** |
| `supports` edges | 0 | **5** |
| APs naming owners in step prose | 0 of 3 | **3 of 3** |

## The edges, and the step each was read from

| AP | step | owner |
|---|---|---|
| Alternate Search and Control Cycles | 2 Control the search | `PAT_verify_result_against_objective_after_production` |
| Alternate Search and Control Cycles | 3 reopen Search after broad rejection | `PAT_generate_novel_options_by_combining_distant_concepts` |
| Plan and Build Work From Thumbnail to Final | 9 read backward and inspect drift | `PAT_verify_result_against_objective_after_production` |
| Progress an Artifact Through Ratified Steps | 5 evaluate the returned candidate, 15 stop | `PAT_verify_result_against_objective_after_production` |
| Progress an Artifact Through Ratified Steps | 8 retire the failed search space | `PAT_generate_novel_options_by_combining_distant_concepts` |

`PAT_generate_novel_options_by_combining_distant_concepts` was deliberately *not*
attached to `AP_plan_and_build_work_from_thumbnail_to_final` step 1. Stage-0
probing is ordinary search; that Pattern fires only when search is returning the
familiar answer, and no step of that AP reaches that condition.

The pattern-side `related_to` from `PAT_generate_novel_options_by_combining_distant_concepts`
to `AP_alternate_search_and_control_cycles` was left in place. It is sibling
adjacency in the opposite direction and removing it is not part of the repair.

## Rule 3 violation, fixed 2026-09-03

`AP_plan_and_build_work_from_thumbnail_to_final` Notes names two **`art`** cards in
runtime prose — `PAT_return_to_art_centerline` and
`AP_gate_staged_visual_work_by_approval`. `validate.py` does not catch it because
the references are in Notes rather than `cross_links`, but it is a rule 3
violation with a rule 10 consequence: any release that ships `metaskills` without
`art` carries a metaskill that names two unresolvable identifiers. Fixing it means
rewriting that Notes paragraph, which is outside an additive ownership repair.

The Notes paragraph now describes the roles instead of naming the cards: the
domain supplies its own centerline Pattern and its own approval-gated stage AP
thread, and the metaskill says why it names neither.

A sweep of all 1487 cards found these two and no others. `validate.py` now
carries the check that would have caught them — `rule 26` is applied to card
bodies as well as `cross_links`, over object ids and variant ids alike — with a
regression test beside the existing cross_link case in
`tests/test_architecture.py`.
