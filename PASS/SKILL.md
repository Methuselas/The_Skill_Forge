---
name: pass-authoring
description: >-
  Use when studying a source to extract, review, validate, organize, revise, or
  publish PASS APs, Patterns, Drills, ledgers, source units, modules, or portable
  releases. Also use for PASS schema, grounding, provenance, and library
  maintenance work. Human-guided teaching may be required when source material alone is insufficient.
---

# PASS Authoring

This skill governs creation and maintenance of grounded PASS knowledge objects.
It is separate from the domain skills that consume those objects.

## Canonical load order

1. `docs/PASS_DOCTRINE.md`
2. `docs/PASS_RUN.md`
3. `docs/PASS_GROUNDING.md`
4. `docs/PASS_SCHEMA.md`
5. `docs/PASS_LEDGER.md`
6. `docs/PASS_LIBRARY.md`

Use the source material named by the user as the evidentiary basis. Preserve its
terminology and scope. Do not silently fill unsupported gaps with general
knowledge. Mark inference, uncertainty, and deferred review explicitly.

After edits, run the applicable validation, grounding, prerequisite, and release-boundary checks under `tools/` before publishing a release. Indexes are optional generated navigation, not canonical dependency state.
