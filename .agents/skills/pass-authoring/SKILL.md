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

Before publishing changed knowledge, run the tools under `PASS/tools/`:

```bash
python PASS/tools/validate.py
python PASS/tools/verify_references.py
python PASS/tools/build_index.py
```

Release building must not bypass the quality gates.
