---
name: pass-authoring
description: >-
  Use when studying a source to extract, review, validate, organize, revise, or
  publish PASS APs, Patterns, Drills, modules, or portable releases. Also use for
  PASS schema and library maintenance work. Human-guided teaching may be required
  when source material alone is insufficient.
---

# PASS Authoring

This skill governs creation and maintenance of PASS knowledge objects. It is
separate from the domain skills that consume those objects.

A finished card is the durable artifact. It must be valid and executable after
the source it was learned from is gone, so it carries no source id, locator,
page, hash, or receipt.

## Canonical references by phase

Do not preload every PASS document. Open the reference that owns the current
decision:

- purpose, admissibility, and extraction judgment: the relevant section of
  `docs/PASS_DOCTRINE.md`;
- preflight, source reading, reconciliation, third read, and closure: the
  relevant section of `docs/PASS_RUN.md`;
- object creation or review: the frontmatter contract and applicable Pattern,
  Drill, or AP section of `docs/PASS_SCHEMA.md`;
- placement and module ownership: `docs/PASS_LIBRARY.md`;
- packaging and dependencies: `docs/MODULE_RELEASES.md`;
- runtime profile routing, vendoring, or completion contracts:
  `docs/EXECUTION_CONTRACT.md`;
- skill consumption or drill administration: `docs/PASS_CONSUMPTION.md`;
- Skillset Memory: `docs/MEMORY_SCHEMA.md`.

Read a complete document only when the task genuinely spans its complete
contract. Load later-phase references when that phase begins, not in anticipation.

## Working rules

Use the source material named by the user as the evidentiary basis. Preserve its
terminology and scope. Do not silently fill unsupported gaps with general
knowledge. Mark inference, uncertainty, and deferred review explicitly.

Author in **one** domain per run. Duplicate-guard against that domain only; do not
search or modify another. Cards may reference their own domain plus `metaskills`.

Treat AP authoring as **orchestration authoring**, not merely another extraction
shape. A source may teach an AP directly, but a stable AP may also be synthesized
from accepted Patterns when a recurring action needs dependable ordering, gates,
recovery, and completion. See `docs/PASS_RUN.md` §2.8. During execution, productive
actions resolve AP-first; Pattern-first assembly is the fallback when coverage is
missing.

Every run ends with a **third read**: the cards it just produced, read cold
against the schema, before the delta is presented. See `docs/PASS_RUN.md` §2.6.
The validator is the floor of that pass, not the pass — a Success Check nothing
can fail, a graded artifact no instruction asks for, and a universal IF with a
mechanism-specific THEN all pass `validate.py` and have each cost a lane-wide
repair.

After edits, run the validation and release-boundary checks under `tools/` before
publishing a release:

```bash
python tools/validate.py
python tools/verify_references.py
python tools/build_index.py
```

Indexes are optional generated navigation, not canonical dependency state.
