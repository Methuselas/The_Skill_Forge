# SkillForge Runtime Architecture State — 2026-08-14

Recovered and merged forward from the lost Art-authoring chat onto the Python-recovery golden truth.

## Runtime centerline

- Canonical kernel: `PASS/runtime/skillforge_runtime.py`
- Art profile: `PASS/runtime/profiles/art.yaml`
- Generic profile: `PASS/runtime/profiles/generic.yaml`
- Metaskill activation manifests: the three current metaskill submodules each carry `RUNTIME.yaml`.
- Runtime operations: `resolve`, `verify`, `doctor`.
- Normal Art generation defaults to **Stage-informed Direct Render**.
- Explicit stages/process, training, drills, or debugging route to **Staged Production**.
- Explicit mode override wins.
- Python requires task-specific risk checks but does not make the artistic judgment.
- Completion fails closed when required objective/instruction checks or routed risk checks are missing.

Boundary: scripts decide when thinking must happen; skills teach how to think about it; the model makes the judgment; verification checks what happened.

## Release integration

`PASS/tools/build_release.py` now vendors the canonical runtime kernel and recipe-selected runtime profile into each portable release. Current Art recipes declare `runtime_profile: art`.

The release builder also supports declarative deployment profiles. `chatgpt_skill` is currently configured as a hard 25,000,000-byte compressed-package limit. This gate runs only at release/check time and never during normal authoring validation.

Observed smoke results:

- Animal Anatomy compressed package: about 1.16 MB — PASS.
- Dynamic Figure Drawing compressed package: about 31.36 MB — FAIL against the 25 MB ChatGPT Skill profile.

No automatic sharding was implemented; architecture/package-family design remains a later task.

## Authoring cache lifecycle

`PASS/tools/cleanup_authoring_cache.py` deterministically preserves render caches for active/incomplete/unattested/stale sources and permits removal only for `complete` sources whose current quality attestation verifies. Use it against a handoff/staging copy to omit reproducible render caches without discarding ledger receipts.

The current closed-source handoff state has no `workspace/authoring/renders` cache. Marvel's completed render evidence was pruned only after its live grounding verification and quality attestation succeeded.

## Verification at checkpoint

- 246 canonical objects validate.
- 30/30 quality attestations verify.
- visual-reference review passes.
- runtime unit suite: 6/6 PASS.
- canonical Art runtime doctor: PASS.
- vendored Animal Anatomy runtime doctor: PASS.
- `marvel_how_to_draw_comics` is complete, live-grounded, and quality-attested; it no longer blocks quality-gated releases.
- Animal Anatomy safe release builds/checks successfully with Marvel in provenance closure.
- Dynamic Figure Drawing reaches the intended deployment-size blocker only: ~31.36 MB exceeds the 25 MB `chatgpt_skill` target.
