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

## Canonical load order

1. `docs/PASS_DOCTRINE.md`
2. `docs/PASS_RUN.md`
3. `docs/PASS_SCHEMA.md`
4. `docs/PASS_LIBRARY.md`
5. `docs/EXECUTION_CONTRACT.md` when changing profile routing, release vendoring,
   or the declared execution/completion contract.

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
