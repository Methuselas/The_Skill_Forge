---
name: pass-authoring
description: >-
  Use when studying sources or maintaining PASS APs, Patterns, Drills, modules,
  variants, references, prerequisites, release recipes, validation, or skill
  packaging in this SkillForge repository.
---

# PASS Authoring

Use the canonical portable PASS package in `PASS/`; this repo skill is only a
discovery wrapper for agents working inside SkillForge.

## Load order

1. `PASS/SKILL.md`
2. `PASS/docs/PASS_DOCTRINE.md`
3. `PASS/docs/PASS_RUN.md`
4. `PASS/docs/PASS_SCHEMA.md`
5. `PASS/docs/PASS_LIBRARY.md`
6. `PASS/docs/MODULE_RELEASES.md` when packaging or changing dependencies

## Rules that decide most questions here

`library/` holds finished knowledge. There is no authoring state to maintain
beside it — no ledger, no source registry, no reading receipts, no provenance
records. Do not create any.

A card must be valid and executable after its source is gone. Never write a
`source_id`, locator, page number, or hash onto a card. `reference` is optional
attribution (title and author) and nothing reads it.

Author in one domain per run. Duplicate-guard against that domain only. Cards may
reference their own domain plus `metaskills`; any other cross-package reference
fails validation.

Do not make released skills depend on this repo, `.agents/`, or `.claude/`.
Nothing may depend on `archive/`.

Art may require a human-guided chapter discussion before commit. Software
Engineering may be authored autonomously when the source and task support it.
Never invent questions as ceremony, but stop for real ambiguity, contradiction,
or teacher-dependent interpretation.

## Skillset Memory

`memory/<domain>/` is a separate store with its own contract in
`PASS/docs/MEMORY_SCHEMA.md`. Read that before touching it.

Memory records what happened when canon was used. It is never canon, never
overrides a card, and is never copied into one — an entry that seems important
enough to apply on every turn has earned promotion review, not a paste, because
pasting creates a second write site and lets the real owner decay unobserved.
`tests/test_memory.py` enforces this.

An observation is evidence about a capability only if the run that produced it
was a valid test of that capability. A run that failed before the capability was
exercised stays in `training_history.jsonl` and never counts toward a craft
weakness; attribute it to the tool, controller, or package that actually failed.

```bash
python PASS/tools/memory.py validate
python PASS/tools/memory.py review --domain <domain>
python PASS/tools/memory.py compact --domain <domain>
```

The card tools read `library/` and the memory tool reads `memory/`. Keep them
apart; neither store is an input to the other.

Before publishing changed knowledge, run the tools under `PASS/tools/`:

```bash
python PASS/tools/validate.py
python PASS/tools/verify_references.py
python PASS/tools/build_index.py
```

Release building must not bypass the quality gates.
