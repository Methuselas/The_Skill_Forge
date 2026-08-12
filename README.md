# SkillForge

A workspace for authoring portable, self-contained AI skillsets.

- `PASS/` — portable authoring package
- `library/` — canonical reusable knowledge modules
- `workspace/authoring/` — sources, ledgers, attestations, and training-only state
- `workspace/release-recipes/` — named products
- `.agents/skills/` — repo-local Codex/ChatGPT skill discovery wrappers
- `.claude/skills/` — repo-local Claude Code skill discovery wrappers
- `docs/` — human operational guides
- `tests/` — architecture, quality-gate, discovery, asset, and release tests

The ZIP is the product. The repo is the factory.

## Validate the workspace

```bash
python -m pip install -r PASS/requirements.txt
python PASS/tools/validate.py
python PASS/tools/verify_references.py
python PASS/tools/quality_attestation.py verify --all
python -m unittest discover -s tests -p "test_*.py"
```

## Build a named skill

```bash
python PASS/tools/build_release.py build \
  workspace/release-recipes/Animal_Anatomy.yaml \
  workspace/releases/Animal_Anatomy
```

The release preserves `library/...` paths, includes `metaskills` plus the full
prerequisite closure, carries Agent Skills-compatible `SKILL.md` metadata, and
fails closed if required quality/asset/portability checks do not pass.
