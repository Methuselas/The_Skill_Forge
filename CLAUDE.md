# SkillForge — Claude Instructions

PASS is a universal skill-card system. Sources are studied to create self-contained
Patterns, Drills, and APs. Cards live in independent skill domains and are validated
before entering the universal library. **Source material and authoring scratch state
are not runtime dependencies.**

```text
library/          the universal library — the whole system of record
  art/ writing/ software-engineering/    independent domains
  metaskills/                            shared foundation, bundled into every release
PASS/             the portable authoring package: schema, docs, tools, runtime
workspace/        release recipes, plus your local scratch (nothing reads it)
archive/          retired material — nothing active may depend on it
```

## Hard rules

These prevent damage. `ARCHITECTURE.md` is the canonical contract; this is the
working summary.

Each rule's **bold lead sentence is shared verbatim with `AGENTS.md`** and a test
enforces that the two files state the same set. Edit a lead here, edit it there.
The prose after each lead is this file's own.

1. **A card must be valid and executable after its source is gone.** Never write a
   `source_id`, locator, page number, or hash onto a card. `reference` is optional
   attribution (`source_title`, `author`) and nothing reads it.
2. **Author in one domain per run.** Art, Writing, and Software Engineering are
   independent lanes. Do not read, sync with, or modify another domain to author
   yours. Duplicate-guard against your own domain only; card IDs are unique
   library-wide.
3. **Cards may reference their own package plus `metaskills`.** Any other
   cross-package reference fails validation (rule 26).
4. **Do not rebuild the retired authoring infrastructure.** Ledgers, source
   staging, provenance receipts, attestations, source projections, state sidecars,
   registries of read material, and a shared Teaching lane were all deleted
   2026-08-15; see `docs/CLEANUP_2026-08-15.md`. When something seems to need
   tracking — what was read, which pages, which candidates were rejected — do not
   add it. Prefer deletion over abstraction, plain files over state machinery.
5. **Never widen the schema to accommodate a card.** A card that disagrees with its
   template is the card's bug.
6. **Do not modify the Art Stages.** They are frozen unless the user explicitly
   starts the Stage-streamlining work.
7. **`.claude/` and `.agents/` are repo discovery only.** They must never ship as
   runtime dependencies of a release.
8. **Indexes are generated, never hand-edited.** Do not edit `INDEX.md`; run
   `build_index.py`. An index that cannot be deleted and regenerated from the
   cards has become a second database.
9. **`archive/` is retired material.** Nothing active may depend on it.
10. **Every release ships `metaskills` and its complete prerequisite closure.**
    A build that omits a referenced card is broken even when the source library
    validates.
11. **Do not add a global registry, repo-wide index, or new architectural
    convention without explicit authorization.** This is the shape the retired
    machinery grew back in last time.
12. **A hardcoded path left by an earlier agent is technical debt, not
    architecture.** Do not treat it as a constraint to preserve.
13. **Front matter may not set a source's subject.** A preface, foreword, or
    introduction is read for orientation only. The subject is what the
    instructional body teaches you to do. A preface addressed to instructors is
    metadata about the preface, not evidence that a craft book is pedagogy.
14. **A session boundary never creates a unit boundary.** Units are set by
    instruction; context exhaustion is a separate problem. When a unit does not
    fit the remaining window, checkpoint and resume the same unit — never split
    it to make it fit.
15. **Practice history must not enter cards.** What one attempt revealed about
    application, calibration, or failure is not itself canonical knowledge.
    Attribute a failure before authoring: a missing reusable decision may justify a
    Pattern, and a missing reusable action orchestration may justify an AP;
    retrieval, application, continuity, reference, tool, and interface failures
    do not.

## Commands

```bash
python PASS/tools/validate.py                    # card shape, links, domain isolation
python PASS/tools/validate.py --package art      # one domain
python PASS/tools/verify_references.py           # shipped image assets
python PASS/tools/build_index.py                 # regenerate INDEX.md navigation
python -m unittest discover -s tests -p "test_*.py"
```

Every tool reads the library and nothing else. They work on a clean clone with no
source material present — that is the point, and the tests enforce it.

Build a release (the output path must be outside the repo):

```bash
python PASS/tools/build_release.py build workspace/release-recipes/CPP_Development.yaml ../releases/cpp
```

## Where to go deeper

| Question | File |
|---|---|
| Architecture contract, what must not grow back | `ARCHITECTURE.md` |
| Preflight and the authoring loop — units, two reads, dispositions | `PASS/docs/PASS_RUN.md` |
| Card schema (closed contract) | `PASS/docs/PASS_SCHEMA.md` |
| Why PASS works this way | `PASS/docs/PASS_DOCTRINE.md` |
| Library layout, modules, releases | `PASS/docs/PASS_LIBRARY.md`, `PASS/docs/MODULE_RELEASES.md` |
| What the 2026-08-15 reset removed and why | `docs/CLEANUP_2026-08-15.md` |

Repo skills live under `.claude/skills/`; their canonical content is in `PASS/` and
`library/`. `AGENTS.md` carries the same rules for non-Claude agents — if you change
a rule here, change it there too, and `ARCHITECTURE.md` decides any disagreement.

## Working style

Commit only when the user asks. Run the validators after any change to cards,
schema, or tooling. If a change would add shared state between domains or force two
lanes to coordinate, that cost is currently decisive — say so before building it.
