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
  - `art/`, `game-design/`, `writing/`, `software-engineering/` — independent domains
  - `metaskills/` — craft-neutral process knowledge every release bundles
- `workspace/release-recipes/` — named products
- `archive/` — retired material, excluded from validation and builds
- `docs/` — human operational guides
- `tests/` — architecture and release tests
- `.agents/skills/`, `.claude/skills/` — repo-local skill discovery wrappers

The release is the product. The repo is the factory.

## Domains are independent

Every package below `library/` other than `metaskills` is an independent domain.
An agent never needs to inspect, synchronize with, or modify another domain to
author its own. Domains share a **library**, not an authoring process. Cards may
reference other cards in their own domain, plus `metaskills`; anything else fails
validation.

## Context-efficient authoring

Root instructions and repo skills route before loading: metaskills is the small
default baseline, while PASS documents, cards, and memory are opened only for
the current operation and phase. Retrieve a small ranked set from metaskills and
the active domain instead of printing a whole index:

```bash
python PASS/tools/find_relevant.py --package metaskills --cues "<task cues>" --limit 5
python PASS/tools/find_relevant.py --package writing --cues "<task cues>" --limit 8
```

Extract only the PDF pages needed for the current unit. The output is disposable
workspace input; low-text pages are reported for visual inspection or OCR:

```bash
python workspace/tools/extract_pdf_text.py book.pdf workspace/authoring/book-unit.txt --pages 20-48
```

Build a pruned archive for one Project-chat domain. An extracted source can be
placed at top-level `SOURCE_INPUT/` without copying it into the repository:

```bash
python workspace/tools/build_project_snapshot.py workspace/releases/writing-project.zip --domain writing --source-text workspace/authoring/book-unit.txt
```

The snapshot includes PASS, metaskills, the selected domain, its memory, and its
matching agent skills. It excludes `.git`, retired material, source PDFs, nested
ZIPs, unrelated domains, tests, and workspace scratch by default.

### Choose the smallest working set

- **Claude Code or Codex in the repository:** let `CLAUDE.md` or `AGENTS.md`
  select the operation first. Load the matching repo skill, retrieve bounded
  metaskills and domain cards, and open PASS documentation only for the active
  authoring phase.
- **GPT Project chat:** upload a domain-scoped snapshot rather than the complete
  checkout. Attach extracted text through `--source-text`; do not include the
  PDF archive, `.git`, or unrelated domains.
- **Installed or shared skill:** build a named release. Its compact `SKILL.md`
  routes into the bundled domain and the mandatory metaskills baseline. Runtime
  profiles and execution barriers are deferred until productive work needs them.

### Add another skill domain

Create `library/<domain>/` and a matching discovery skill under both
`.agents/skills/<domain>/` and `.claude/skills/<domain>/`. Keep those two skill
wrappers identical. Optional empirical history belongs in `memory/<domain>/`.
The root instructions do not enumerate domains, and the retrieval and snapshot
tools discover library packages automatically, so adding a domain does not grow
every agent's cold-start context. Every release continues to include
`metaskills` automatically.

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
