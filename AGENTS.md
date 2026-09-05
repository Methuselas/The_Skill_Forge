# SkillForge Agent Instructions

SkillForge turns studied sources into self-contained PASS cards. `PASS/` is the
portable authoring skill; `library/` is the universal library of finished cards;
releases must be self-contained.

## Route before reading

Do not preload `ARCHITECTURE.md`, PASS documentation, master indexes, domain
cards, or memory merely because the repository is open. First identify the
operation, then use the matching skill description under `.agents/skills/`:

- source study, card or module maintenance, validation, and release packaging
  use the PASS-authoring skill and only the references for the active phase;
- domain practice, evaluation, or production uses the matching domain skill,
  the default `metaskills` baseline, and a bounded set of relevant domain cards;
- repository code, tests, tooling, and architecture use the
  software-engineering skill and targeted implementation files.

Skill descriptions own discovery, so this file does not enumerate domains. Read
`ARCHITECTURE.md` only for an architectural decision or conflict.

## Non-negotiable boundaries

Each rule's **bold lead sentence is shared verbatim with `CLAUDE.md`** and a test
enforces that the two files state the same set. Edit a lead here, edit it there.
The prose after each lead is this file's own.

- **A card must be valid and executable after its source is gone.** No card
  carries a source id, locator, page number, hash, receipt, or attestation.
- **Author in one domain per run.** Every package under `library/` other than
  `metaskills` is independent. Do not inspect, synchronize with, or modify
  another domain in order to author yours. Duplicate-guard against your own
  domain only; card IDs are unique library-wide.
- **Cards may reference their own package plus `metaskills`.** Any other
  cross-package reference fails validation.
- **Do not rebuild the retired authoring infrastructure.** Ledgers, source
  staging, provenance receipts, attestations, source projections, state sidecars,
  and a shared Teaching lane are all retired. See the end of `ARCHITECTURE.md`.
- **Never widen the schema to accommodate a card.** A card that disagrees with
  its template is the card's bug.
- **Do not modify the Art Stages.** Art's staged-drawing material is frozen until
  the user explicitly asks to revise it.
- **`.claude/` and `.agents/` are repo discovery only.** They must never ship as
  runtime dependencies of a release.
- **Indexes are generated, never hand-edited.** Run `build_index.py`. An index
  that cannot be deleted and regenerated from the cards has become a second
  database.
- **`archive/` is retired material.** Nothing active may depend on it.
- **Every release ships `metaskills` and its complete prerequisite closure.** A
  build that omits a referenced card is broken even when the source library
  validates.
- **Do not add a global registry, repo-wide index, or new architectural
  convention without explicit authorization.** Nor a permanent root-level tool.
- **A hardcoded path left by an earlier agent is technical debt, not
  architecture.** Do not treat it as a constraint to preserve.
- **Front matter may not set a source's subject.** A preface, foreword, or
  introduction is read for orientation only. The subject is what the
  instructional body teaches you to do. A preface addressed to instructors is
  metadata about the preface, not evidence that a craft book is pedagogy.
- **A session boundary never creates a unit boundary.** Units are set by
  instruction; context exhaustion is a separate problem. When a unit does not fit
  the remaining window, checkpoint and resume the same unit — never split it to
  make it fit.
- **Practice history must not enter cards.** What one attempt revealed about
  application, calibration, or failure is not itself canonical knowledge.
  Attribute a failure before authoring: a missing reusable decision may justify a
  Pattern, and a missing reusable action orchestration may justify an AP; retrieval,
  application, continuity, reference, tool, and interface failures do not.
- **Skillset Memory records what happened; it is never canon and is never copied
  into canon.** Empirical state lives in `memory/<domain>/`. Cards do not carry
  it and entrypoints do not inline it; an observation that appears to belong
  everywhere goes through promotion review instead.
- **An invalid run is never evidence about a capability.** If the run failed
  before the capability was exercised, record it in `training_history.jsonl` with
  a reason and attribute it to the tool, controller, or package that failed. It
  never counts toward a craft weakness. See `PASS/docs/MEMORY_SCHEMA.md`.

## Validation

Use the tools in `PASS/tools/`. They read the library and nothing else.

```bash
python PASS/tools/validate.py
python PASS/tools/validate.py --package art
python PASS/tools/verify_references.py
python PASS/tools/build_index.py            # regenerate INDEX.md navigation
python -m unittest discover -s tests -p "test_*.py"
```

Skillset Memory has its own tool, which reads `memory/` and nothing else:

```bash
python PASS/tools/memory.py validate
python PASS/tools/memory.py query --domain art --cues hand
python PASS/tools/memory.py append --domain art --task "..."
```

A release build is publishable only when schema, visual-reference,
asset-resolution, and portability gates pass. Run the test suite after
architecture changes.
