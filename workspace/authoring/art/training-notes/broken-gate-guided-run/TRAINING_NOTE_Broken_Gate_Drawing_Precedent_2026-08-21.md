# Training Note — Broken Gate Canonical Drawing Precedent Run

**Date:** 2026-08-21  
**Status:** guided authoring run closed; evidence integrated into the Art library.  
**Canonical authority:** the reviewed assets under `library/art/process/staged-drawing/assets/broken-gate/canonical/` and the accepted PASS cards that reference them.

This note preserves the guided-review reasoning for the next repository audit. It is practice history, not a runtime dependency.

## Canonical Drawing architecture established

Universal Drawing is now:

1. **Stage 0 — Search / Composition**
2. **Stage 1 — Framework / Scene Skeleton**
3. **Stage 2 — Complete Minimum Mass**
4. **Stage 3 — Specific Rough / Developed Pencils**
5. **Stage 4 — Finished Pencils**

Stage 4 closes the Drawing AP. It does not own universal color, materials, painted lighting, atmosphere, ink, manga tone, or another medium's final finish.

Future downstream crafts inherit the completed Drawing lockset rather than reopening upstream decisions. Likely downstream families include Ink, Color, Paint, Manga/B&W finish, and other medium-specific workflows, but this run deliberately does **not** invent their unfinished stage definitions.

## Canonical Broken Gate lineage

The accepted sequence is one image developed in place. The canonical files are:

- Stage 0: `broken_gate_stage0_canonical_composition.png`
- Stage 1: `broken_gate_stage1_canonical_scene_skeleton.png`
- Stage 2: `broken_gate_stage2_canonical_complete_mass.png`
- Stage 3: `broken_gate_stage3_canonical_specific_rough.png`
- Stage 4: `broken_gate_stage4_canonical_finished_pencils.png`

The canonical Stage 4 is the **first accepted** finished-pencil artifact. Its slightly soft / uniformly busy pencil finish is an accepted minor limitation.

The later tightening reconstruction is explicitly invalid as a canonical successor and is retained only as debug evidence.

## Guided corrections that mattered

### Stage 0

The first selected composition was compositionally strong but too much like a small finished sketch. The accepted correction preserved the camera, courier dominance, spear diagonal, wagon anchor, gate framing, pursuers, road flow, city depth, and negative spaces while lowering surface decision density. The key teaching correction was that a beautiful Stage 0 can still fail if it spends information that later stages need to own.

### Stage 1

The main repeated failure was figure-stage leakage. Environment scaffolding behaved structurally while humanoids drifted into mannequin mass. The canonical target is scene-wide structure: head direction, ribcage/pelvis primitives, axes, action/spine, limb paths, joints, hand/foot direction, and object/environment scaffolds. Stage 1 is not the mannequin stage.

### Stage 2

Stage 2 successfully added complete minimum mass scene-wide while preserving the exact registered Stage 1 relationships. This is the stage where mannequin/solid volume belongs.

### Stage 3

Two important failure classes were exposed:

1. mixed-stage development — environment advanced into late rendering while figures remained Stage 2 mannequins;
2. globally overcooked Stage 3 — figure specificity became correct, but masonry, rubble, road, wagon, and line finish consumed too much of the information budget.

The accepted Stage 3 made anatomy, clothing/gear, spear handling, pursuers, architecture, props, and environment specific while remaining visibly rough. Stage 3 is a design-specific working drawing, not a texture pass.

### Stage 4

Stage 4 was redefined through this run as **Finished Pencils**. The accepted Stage 4 cleaned and integrated the Stage 3 drawing without entering Ink/Color/Paint. A later request for local pencil tightening did not materially succeed because the exact accepted image was not reliably available to the native edit operation.

## Exact-predecessor accessibility finding

Registered-successor generation requires two separate truths:

- **A — canonical identity:** PASS knows which exact artifact is accepted;
- **B — tool accessibility:** the native image tool can actually use that exact artifact as an edit/reference source when the operation requires one.

If B fails, fail closed.

Do not reconstruct from prose, regenerate a near-match, substitute a rejected image, or use another stage merely because canonical identity is known. If the user re-uploads the exact accepted artifact, treat that as restoration of access to the **same** canonical predecessor with the **same** lockset; no new approval is required.

Core rule: **LOSS OF EDIT-TARGET ACCESS DOES NOT AUTHORIZE VISUAL REINTERPRETATION.**

The rejected Stage 4 tightening reconstruction demonstrates the failure mode: visually similar regeneration can introduce small differences without producing the requested local correction. Similarity is not an edit.

## Current Rendering / Color training question

The Art library already contains substantial Rendering/Color knowledge: value/color relationships, gamut, hue/value/chroma decisions, lighting, material response, edge control, atmosphere, multiple color drills, and several rendering APs. It does **not** yet have a formally reviewed universal downstream Color AP that should simply be invented as part of this Drawing migration.

The next audit should answer:

**Is the existing Rendering/Color training mature enough to synthesize a downstream Color AP from finished pencils now, or should additional source/drill training occur first—and how should Color, Lighting/Rendering, and Paint responsibilities be separated without duplicating ownership?**

Do not assume the answer is “four color stages” merely because a four-step color idea was discussed. Inspect the accepted Rendering/Color library, existing AP coverage, reading/training state, and old staged material first.

## Outstanding repository cleanup

The source checkpoint intentionally makes only the changes needed to preserve this run. A fresh cleanup chat should still audit the Art domain for older statements that may encode the prior “Stage 4 = active-medium final render” assumption, including staged-drawing support cards, direct-render language, old four-step/process references, and any release-facing help/routing text.

The legacy object id `AP_finish_stage4_final_presentation` is retained in this checkpoint for compatibility even though its active content/name now means Finished Pencils. Decide during the audit whether to rename the object id/file and update all links.

Do not build the final uploadable Skill from this checkpoint until that audit is complete.

## Next-chat restriction

**Do not resume Broken Gate image generation before repository review.** The authoring run is closed. The next operation is repository audit/cleanup and AP architecture work, not another visual revision.
