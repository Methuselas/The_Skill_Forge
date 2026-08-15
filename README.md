# The Skill Forge

A workspace for authoring portable, self-contained AI skillsets.

- `PASS/` — portable authoring package
- `library/` — canonical reusable knowledge modules
- `workspace/provenance/` — public provenance receipts, one per source
- `workspace/authoring/` — **local only, not in Git**: source payloads, ledgers, renders
- `workspace/release-recipes/` — named products
- `.agents/skills/` — repo-local Codex/ChatGPT skill discovery wrappers
- `.claude/skills/` — repo-local Claude Code skill discovery wrappers
- `docs/` — human operational guides
- `tests/` — architecture, quality-gate, discovery, asset, and release tests

The ZIP is the product. The repo is the factory.

## Validate the workspace

These work on a clean clone. The private authoring ledger is not published, so the
tools verify against `workspace/provenance/` instead; they detect which state is
present and need no flag.

```bash
python -m pip install -r PASS/requirements.txt
python PASS/tools/validate.py
python PASS/tools/verify_references.py
python PASS/tools/quality_attestation.py verify --all
python -m unittest discover -s tests -p "test_*.py"
```

Cloning gives you the library and the receipts proving it matches its accepted
grounding. Authoring against a source additionally needs its payload staged
locally — see `workspace/authoring/README.md`.

## Build a named skill

```bash
python PASS/tools/build_release.py build \
  workspace/release-recipes/Animal_Anatomy.yaml \
  workspace/releases/Animal_Anatomy
```

The release preserves `library/...` paths, includes `metaskills` plus the full
prerequisite closure, carries Agent Skills-compatible `SKILL.md` metadata, and
fails closed if required quality/asset/portability checks do not pass.
