# PASS User Guide

PASS is a portable authoring skill for turning source material and, when needed, human teaching into grounded, reusable AI skillsets. The SkillForge repository is optional. A released PASS package must make sense in a clean chat, Project, or other compatible agent environment without SkillForge present.

## Load PASS

Use the complete `PASS/` package, not a repo-specific mirror.

At minimum, load `PASS/SKILL.md` and keep its local `docs/`, `templates/`, and `tools/` available beside it. If the host can execute Python, PASS may use its package-local tools for preflight, rendering, validation, grounding checks, and release building. If code execution is unavailable, follow the documented method directly; Python accelerates PASS but does not define the methodology.

## Provide source material

Give PASS the actual source files it should learn from: PDFs, text, images, code, or other supported material. A source is evidence for authoring; it is not a runtime dependency of the finished skill.

For PDFs, PASS should inspect the real unit content and any diagrams or layout that carry meaning. If a unit cannot actually be read or inspected well enough to ground claims, mark it blocked and stop rather than inventing output.

PASS works one source-native unit at a time. A chapter is the default unit, but a lesson or section may be used when that better matches the source.

## Choose the authoring mode

PASS supports two workflows.

### Autonomous authoring

Use this for domains where the source material is sufficient for an agent to work independently, such as much software-engineering or writing material.

1. Read one unit.
2. Extract reusable candidates.
3. Re-read the same unit against the candidates.
4. Place each candidate against the existing library: new object, variant, revision, replacement, duplicate, or reject.
5. Ground and validate retained objects.
6. Record the unit as processed or empty.
7. Continue to the next unit.

### Human-guided teaching

Use this when correct skill behavior depends on formal human teaching, interpretation, correction, or taste, as with the current Art workflow.

1. Read one unit.
2. Compare it with the already-trained library.
3. Discuss the unit with the human teacher.
4. Ask questions only where there is real ambiguity, contradiction, a new decision rule, a prerequisite implication, or a useful variant/drill to clarify.
5. Incorporate the teacher's corrections before publishing the unit's knowledge.
6. Validate and continue.

Questions are adaptive, not mandatory ceremony. Once the trained framework is strong enough that a unit fits cleanly, PASS should not manufacture questions just to satisfy a workflow.

## What PASS authors

PASS authors reusable skill objects and the relationships between them. The finished object must be usable without the original source in hand. Sources provide grounding and provenance; they are not shipped merely because they were studied.

The repository folder tree is navigation. Knowledge relationships and prerequisites must remain explicit in the authored material rather than being implied only by physical location.

## Export a skill

The normal human-facing request should be simple, for example:

- `Build Animal Anatomy.`
- `Build Dynamic Figure Drawing.`
- `Build C++ Development.`

A named release selects its entry module or modules. PASS then resolves the full dependency closure, adds the universal `metaskills` package automatically, and materializes every required module locally in the release.

The user should not have to remember prerequisite ingredient lists. If a required prerequisite cannot be resolved, export fails.

A finished release must be self-contained. It must not require SkillForge, a source PDF, a workspace ledger, Git, an agent coordination system, or a path outside the release.

## Export rule

The ZIP is the product; the workspace is the factory.

Do not create per-unit, per-chapter, per-commit, or per-phase download archives. Build a ZIP only when a downloadable release or explicit workspace snapshot is requested.
