# Viewpoints PASS Validation Report

**Validation ID:** `val-frantz-crannell-viewpoints-perspective-math-audit-1`  
**Candidate set:** `cand-frantz-crannell-viewpoints-perspective-math-audit-1`  
**Candidate hash:** `c53a5c47db10e85c20d634a876dac1b704b8639b455093e0a143db63f5751441`  
**Baseline snapshot:** `2fc94d3112bb585c3821619269fe9f1fdd11768072c91aeacc29d18b088b6f5c`  
**Ready to commit:** **NO** — intentionally held for cross-book Perspective reconciliation.

## Checks

- **PASS — `intake_session_schema`:** intake_session.json validates against intake_session.schema.json.
- **PASS — `gate1_schema`:** gate1_report.json validates against gate1_report.schema.json.
- **PASS — `gate2_schema`:** gate2_report.json validates against gate2_report.schema.json.
- **PASS — `delta_map_schema`:** delta_map_viewpoints.json validates against delta_map.schema.json.
- **PASS — `candidate_set_schema`:** candidate_change_set_viewpoints.json validates against candidate_change_set.schema.json.
- **PASS — `candidate_card_frontmatter`:** All 2 candidate frontmatters validate: {'pattern': 2}.
- **PASS — `candidate_card_body_contract`:** All candidate bodies use the exact Pattern heading contract in the required order.
- **PASS — `artifact_delta_links`:** All change artifacts exist; every delta and provenance reference resolves.
- **PASS — `candidate_hash`:** Candidate artifact SHA-256 = c53a5c47db10e85c20d634a876dac1b704b8639b455093e0a143db63f5751441.
- **PASS — `source_hash`:** Viewpoints PDF SHA-256 = e2e33af95f587a29624c111f8839583a2796e458795ecc7197af808860a9ec45.
- **PASS — `prior_cumulative_repo_hash`:** Prior five-book cumulative repo ZIP SHA-256 = c025da0f064c01b0715d31a9efcd9ceac1f0b22d18c7b8f3440b2d7087f77bcb.
- **PASS — `golden_repo_hash`:** Original golden repo ZIP SHA-256 = 373420fb1ec0c92f46991630b37424b74eb14ed69b9699088f89d610ec2b54eb.
- **PASS — `prior_candidate_baseline_unchanged`:** All 30 candidate cards from the five-book Perspective stack match the Viewpoints context-load baseline snapshot.
- **PASS — `prior_repo_byte_identity`:** All 1206 files from the prior five-book cumulative repo archive are byte-identical; Viewpoints intake is additive only.
- **PASS — `source_text_scope_complete`:** Deep source read covers Chapters 1-7 and the movie interlude / printed perspective pp. 1-138; the source changes subject at Chapter 8 to fractal geometry, which is intentionally outside this Perspective audit.
- **PASS — `source_visuals_complete`:** Physical PDF pp. 16-153 were rendered and visually scanned for the perspective half; physical pp. 154-165 color plates were also visually scanned. The theorem, station-point, skyscraper, spherical-perspective, and anamorphic sequences received close review.
- **PASS — `step3_architecture_tests`:** PASS vNext Step 3 test suite: 15 passed.
- **PASS — `root_unit_tests`:** Scoped root unit suite with repository on PYTHONPATH: 78 passed, 4 Pillow deprecation warnings.
- **PASS — `root_library_validation`:** tools/validate.py: PASS, 268 canonical objects validated.
- **PASS — `surgical_scope_control`:** Viewpoints produced one foundation supersession candidate, one new triggered three-point validator, three finalizing patches, and bounded theory/reference records; basic perspective and fractal chapters were not duplicated into new cards.
- **PASS — `cov_resolution`:** No universal 50°/60° cone-of-vision theorem was promoted; fixed numbers remain source-specific heuristics while station point, viewing distance, support/frame, and projection model carry the durable logic.
- **PASS — `ellipse_hold_resolution`:** Viewpoints does not establish the projected-circle minor-axis theorem. Robertson remains a bounded practical minor-axis/axle heuristic and D’Amelio remains the exact constructed-circle fallback; no universal theorem is promoted.
- **WARN — `perspective_reconciliation_pending`:** The mathematical audit is complete, but the agreed cross-book patch/supersession reconciliation has not yet been applied to canon. ready_to_commit remains false.

## Result

There are **no blocking validation failures**. The sole warning is intentional: the mathematical audit is complete, but the agreed cross-book patch/supersession reconciliation has not yet been applied to canon.
