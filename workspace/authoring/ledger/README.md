# ledger/

status: active
owner: docs/domains/corpus
last_reviewed: 2026-07-29

The run record. One folder per source, tracked in git.

```
ledger/<source_id>/
  SOURCE.md      what the source is, its sha256, how it was divided
  UNITS.md       the work queue: one row per unit, with status
  units/
    <unit_id>.md one row per candidate, with disposition and grounding
```

Formats are specified in `docs/PASS/PASS_LEDGER.md`.

This is the half of a PASS run that is safe to commit: small, diffable, and enough
to know exactly what was read and what came out of it. The books themselves live
in `sources/` and are gitignored.
