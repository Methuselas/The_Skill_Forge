---
name: pass-authoring
description: >-
  Use when studying sources or maintaining PASS APs, Patterns, Drills, modules,
  ledgers, grounding, references, prerequisites, release recipes, validation, or
  skill packaging in this SkillForge repository.
---

# PASS Authoring

Use the canonical portable PASS package in `PASS/`; this repo skill is only a
discovery wrapper for agents working inside SkillForge.

## Load order

1. `PASS/SKILL.md`
2. `PASS/docs/PASS_DOCTRINE.md`
3. `PASS/docs/PASS_RUN.md`
4. `PASS/docs/PASS_GROUNDING.md`
5. `PASS/docs/PASS_SCHEMA.md`
6. `PASS/docs/PASS_LEDGER.md`
7. `PASS/docs/PASS_LIBRARY.md`
8. `PASS/docs/MODULE_RELEASES.md` when packaging or changing dependencies

Use `workspace/authoring/ledger/` for authoring state and `library/` for canonical
knowledge. Do not make released skills depend on this repo, its ledger, `.agents/`,
or `.claude/`.

Art may require a human-guided chapter/unit discussion before commit. Software
Engineering may be authored autonomously when the source and task support it.
Never invent questions as ceremony, but stop for real ambiguity, contradiction,
or teacher-dependent interpretation.

Before publishing or attesting changed knowledge, run the applicable tools under
`PASS/tools/`. Release building must not bypass the quality gates.
