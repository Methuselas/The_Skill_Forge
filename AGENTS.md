# SkillForge Agent Instructions

SkillForge turns studied sources into self-contained PASS cards. `PASS/` is the
portable authoring skill; `library/` is the universal library of finished cards;
releases must be self-contained.

Read `ARCHITECTURE.md` for the contract and `PASS/docs/PASS_RUN.md` for the
authoring loop.

## Non-negotiable boundaries

- **A card must be valid and executable after its source is gone.** No card
  carries a source id, locator, page number, hash, receipt, or attestation.
- **Author in one domain.** `art`, `writing`, and `software-engineering` are
  independent. Do not inspect, synchronize with, or modify another domain in
  order to author yours.
- Cards may reference cards in their own domain plus `metaskills`. Any other
  cross-package reference fails validation.
- Duplicate-guard against your own domain only. Card IDs are unique library-wide.
- Every release includes `library/metaskills` and the complete prerequisite
  closure.
- Do not add a global registry, repo-wide index, permanent root-level tool, or new
  architectural convention without explicit authorization.
- Do not rebuild the retired authoring infrastructure — ledgers, source staging,
  provenance receipts, attestations, source projections, state sidecars, or a
  shared Teaching lane. See the end of `ARCHITECTURE.md`.
- A hardcoded path created by an earlier agent is technical debt, not
  architecture.
- `.agents/` and `.claude/` are repo discovery/integration only; they must never
  ship as runtime dependencies of a release.
- `archive/` is retired material. Nothing active may depend on it.
- Art's staged-drawing material is frozen until the user explicitly asks to
  revise it.
- **Front matter may not set a source's subject.** A preface, foreword, or
  introduction is read for orientation only. The subject is what the
  instructional body teaches you to do. A preface addressed to instructors is
  metadata about the preface, not evidence that a craft book is pedagogy.
- **A session boundary never creates a unit boundary.** Units are set by
  instruction; context exhaustion is a separate problem. When a unit does not fit
  the remaining window, checkpoint and resume the same unit — never split it to
  make it fit.
- **Practice history must not enter cards.** What one attempt revealed about
  application, calibration, or failure is not a Pattern. Attribute a failure
  before writing a card about it: missing knowledge justifies a card, while
  retrieval, application, continuity, reference, tool, and interface failures do
  not.

## Validation

Use the tools in `PASS/tools/`. They read the library and nothing else.

```bash
python PASS/tools/validate.py
python PASS/tools/validate.py --package art
python PASS/tools/verify_references.py
python PASS/tools/build_index.py            # regenerate INDEX.md navigation
python -m unittest discover -s tests -p "test_*.py"
```

A release build is publishable only when schema, visual-reference,
asset-resolution, and portability gates pass. Run the test suite after
architecture changes.
