# SkillForge Agent Instructions

SkillForge is a factory for portable skillsets. `PASS/` is the portable authoring
skill; `library/` is canonical reusable knowledge; `workspace/authoring/` is
factory state; finished releases must be self-contained.

## Non-negotiable boundaries

- Every release includes `library/metaskills` and the complete prerequisite closure.
- Do not create cross-domain dependencies without explicit authorization.
- Do not add a global registry, repo-wide index, permanent root-level tool, or new
  architectural convention without explicit authorization.
- A hardcoded path created by an earlier agent is technical debt, not architecture.
- `.agents/` and `.claude/` are repo discovery/integration only; they must never ship
  as runtime dependencies of a release.
- Art's staged-drawing material is frozen until the user explicitly asks to revise it.

## Validation

Use the tools in `PASS/tools/`. A release build is publishable only when schema,
visual-reference, grounding-attestation, asset-resolution, and portability gates pass.
Run `python -m unittest discover -s tests -p "test_*.py"` after architecture changes.
