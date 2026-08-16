# PASS / The Skill Forge

PASS (Pattern Analysis Skill System) is a universal skill-card system. Sources are studied to create
self-contained Patterns, Drills, and APs. Cards live in independent skill domains
and are validated before entering the universal library. Source material and
authoring scratch state are not runtime dependencies.

```text
SOURCE MATERIAL (book / course / document / human instruction)
        ↓  an agent studies it
SELF-CONTAINED CARDS in ONE assigned skill domain
        ↓  PASS validates them
THE UNIVERSAL LIBRARY
```

The source is how the knowledge is learned. **The finished card is the durable
knowledge artifact.** Delete every research PDF and the library still validates,
still builds, and still works.

## Layout

- `PASS/` — the portable authoring package: schema, docs, tools, runtime
- `library/` — the universal library, one folder per skill domain
  - `art/`, `writing/`, `software-engineering/` — independent domains
  - `metaskills/` — craft-neutral process knowledge every release bundles
- `workspace/release-recipes/` — named products
- `archive/` — retired material, excluded from validation and builds
- `docs/` — human operational guides
- `tests/` — architecture and release tests
- `.agents/skills/`, `.claude/skills/` — repo-local skill discovery wrappers

The release is the product. The repo is the factory.

## Domains are independent

An Art agent never needs to inspect, synchronize with, or modify Writing or
Software Engineering in order to author Art. The same holds for each domain. They
share a **library**, not an authoring process. Cards may reference other cards in
their own domain, plus `metaskills`; anything else fails validation.

## Validate

Everything below runs on a clean clone with no source material present.

```bash
python -m pip install -r PASS/requirements.txt
python PASS/tools/validate.py
python PASS/tools/verify_references.py
python PASS/tools/build_index.py --check
python -m unittest discover -s tests -p "test_*.py"
```

Validate a single domain:

```bash
python PASS/tools/validate.py --package art
```

## Build a named skill

```bash
python PASS/tools/build_release.py build workspace/release-recipes/Animal_Anatomy.yaml ../releases/Animal_Anatomy
```

The release preserves `library/...` paths, includes `metaskills` plus the full
prerequisite closure, carries Agent Skills-compatible `SKILL.md` metadata, and
fails closed if schema, visual-reference, asset-resolution, or portability checks
do not pass. A domain release packages that domain without loading any other.

The builder refuses to write inside or above the repository, so give it an output
path outside the checkout.

## Author a card

See `PASS/docs/PASS_RUN.md`. Preflight the source first — subject, units, and
what each unit is likely to yield. Then per unit: read it deeply without naming
cards, raise anything the evidence cannot settle, read it again in full and
extract there, place each candidate against your own domain, present the delta,
validate, land it.
