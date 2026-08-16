# Art Authoring ↔ SkillForge Repo Reconciliation — 2026-08-15

## Inputs

- Repo snapshot: `SkillForge_Repo.zip` supplied by MaDin on 2026-08-15.
- Active Art authoring state: Creative Illustration committed through u06 before this reconciliation.
- Goal: bring the Art authoring archive onto the repo's current PASS contract/runtime format without discarding the in-flight Composition work.

## Art card cross-reference before u07 commit

The repo Art package contained 245 canonical object IDs. The active authoring package contained 251.

- 244 IDs were shared.
- Shared IDs had **zero path mismatches**.
- The active package had seven Composition-run objects not yet present in the repo snapshot.
- The repo had one object not present in the active package: `PAT_route_group_composition_through_directional_paths_and_accents`, which had already been intentionally generalized/replaced during Creative Illustration u04 by `PAT_route_viewer_attention_through_planned_visual_paths`.
- Nine shared cards differed in content. Inspection showed every difference was an expected Creative Illustration mutation: u02/u03/u04/u06 variants, notes, or cross-link updates. No unrelated Art-card drift was found.

This means the repo Art canon and the active Art authoring canon agree on the pre-Composition baseline; the active copy is the repo baseline plus the approved Composition delta.

## New-format assessment

Running the repo's current `PASS/tools/validate.py` against the pre-migration Art authoring state exposed seven compatibility issues:

1. Creative Illustration lacked `unit_ledger_contract: 3`.
2. u04 used ledger format 2 despite being read on 2026-08-15.
3. u05 used ledger format 2 despite being read on 2026-08-15.
4. u06 used ledger format 2 despite being read on 2026-08-15.
5. u07 used the legacy queue status `claimed` rather than the current `in-progress`/closed vocabulary.
6. The Hampton registry row still reported `in-progress`.
7. The Hampton registry row still reported `9/10` rather than the authoritative `10/10`.

No schema/card failure was found in the Art canon itself.

## Reconciliation applied

- Replaced PASS core/docs/templates/runtime/tests with the supplied repo versions.
- Synced the repo's matching pre-Composition Art source ledgers and attestations into the authoring workspace.
- Kept the active Art card tree, because card-level cross-reference showed it equals the repo baseline plus approved Creative Illustration changes.
- Added the repo top-level Teaching package to the authoring slice so contract-v3 Teaching routes can be duplicate-guarded locally.
- Added the Starkey source ledger needed to ground those shared Teaching objects.
- Upgraded Creative Illustration to `unit_ledger_contract: 3`.
- Grandfathered only historical u01-u03, matching the accepted repo policy.
- Converted u04-u06 to ledger format 3 with explicit completed Teaching-lane receipts. Their scans had already been performed and yielded no Teaching candidates.
- Repaired the Hampton registry state to `complete | 10/10`.
- Committed u07 under ledger format 3.

## u07 committed delta

- New: `DRILL_compare_same_subject_across_tonal_treatments`.
- Variant: `VAR_loomis_build_soft_first_then_recover_selected_edges` → `PAT_control_edge_hardness_from_form_light_and_focus`.
- Variant: `VAR_loomis_break_uniform_tonal_fields_without_losing_value_family` → `PAT_consolidate_resolved_form_with_tone`.
- Refinement: expanded `PAT_control_edge_hardness_from_form_light_and_focus` with cause-based soft/lost-edge diagnostics and an explicit all-soft failure mode.
- Teaching scan: one cross-domain candidate was duplicate-guarded against top-level Teaching and routed to `AP_teach_craft_from_orientation_to_generation`; no new Teaching object or variant was required.

## Post-u07 card cross-reference

- Art objects: 252.
- Repo Art objects: 245.
- Shared IDs: 244.
- Active-only IDs: 8, all from the approved Creative Illustration run.
- Repo-only IDs: 1, the intentionally superseded Hultgren group-route owner.
- Shared paths still have zero mismatches.
- Nine shared cards differ, all explained by approved Creative Illustration variants/refinements/cross-links.

## Gates

- Current PASS schema/ledger validation: PASS.
- PASS core unit tests: PASS, 14/14.
- Creative Illustration live grounding: PASS through 7 processed units.
- Creative Illustration quality attestation: refreshed from live verification and PASS.
- Visual-reference verification: PASS.

The repo's stricter release-attestation gate is a separate issue from schema/ledger compatibility. The supplied repo snapshot itself still contains pre-existing attestation drift in several older source contributions. Ongoing Composition edits also touch shared cards whose older attestations are intentionally not rewritten here without their source payloads. This is deferred to the planned full-repo reconciliation after the first Composition book rather than papered over with fabricated live verification.
