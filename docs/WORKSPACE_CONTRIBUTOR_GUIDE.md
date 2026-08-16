# Workspace Contributor Guide

This guide applies to humans, GPT, Claude, Codex, and other agents working in SkillForge.

SkillForge is a workspace for manufacturing portable skillsets. The repository is not the product. PASS is the authoring skill. Finished self-contained releases are the product.

## Non-negotiable architecture rules

> Do not add a global registry, repo-wide index, permanent root-level tool, new architectural convention, or cross-domain dependency without explicit authorization.

> A hardcoded path created by a previous agent is technical debt, not an architectural requirement.

Also preserve these boundaries:

- PASS must remain portable outside SkillForge.
- A released skill must be self-contained.
- A clean chat or Project must not require the repo to understand a release.
- Tools required by a skill live with that skill.
- Workspace-only tools stay workspace-only.
- Generated files are output, not hand-maintained sources of truth.
- Source modules may be composable; released products must contain their complete dependency closure locally.
- Every released skillset includes `metaskills`.
- Hard prerequisites are followed across folder boundaries and must never be silently dropped.
- Art and Software Engineering must not contaminate one another merely because they share a workspace.

## Before adding or moving a file

Classify it by ownership:

1. PASS-owned
2. domain-owned (for example Art or Software Engineering)
3. truly shared
4. workspace-only
5. generated/obsolete

Its location should make that ownership obvious.

Do not create another management layer just to manage the management layer. Move, rewire, validate, and delete.

## Authoring modes

Respect the skill's training mode.

### Autonomous domains

Some domains, including much coding and writing material, may be authored efficiently by agents from source material with PASS grounding and validation.

### Human-guided domains

Some domains require formal teaching. Current Art knowledge was built through chapter-by-chapter source study plus human discussion and correction. Do not reinterpret that trained library as a simple autonomous extraction corpus.

For human-guided work, process one source-native unit at a time, discuss it with the teacher, ask only necessary questions, incorporate corrections, then validate the result.

Do not manufacture questions after the trained framework is already sufficient to understand a unit.

## Module and release discipline

Modules organize reusable source knowledge. They are not automatically shipping boundaries.

When adding a module:

- keep its metadata local;
- declare only genuine requirements;
- avoid modifying unrelated sibling modules;
- preserve object-level prerequisite relationships;
- verify a new module can be added without rewriting existing modules.

When building a release:

- start from the requested named product or entry module;
- add `metaskills` automatically;
- resolve module and object prerequisites recursively;
- fail closed on missing prerequisites or dependency cycles;
- materialize the closure locally;
- exclude workspace-only material.

## Source and training material

Sources, evidence, and training notes are yours and stay outside the library unless the released skill genuinely needs a distilled runtime resource. PASS does not track them.

Do not ship a source simply because PASS learned from it, and never record its identity on a card. A card must execute after the source is gone.

Do not invent a memcap subsystem because one may be useful later. Add memcaps only when a trained skill actually needs a defined fallback format and that architecture has been approved.

## Art-specific maintenance

Organize Art by durable knowledge boundaries rather than by book or historical cram folders. Shared drawing systems and subject knowledge may be separated physically as long as prerequisites remain explicit.

Current subject families include figure and animals; future subjects may include creatures, objects, vehicles, environments, and others when authored. Do not scaffold Comic, Manga, or other future variants before the teaching needed to define them has happened.

The staged-drawing process is intentionally preserved as trained material. Do not streamline or redesign the Stages unless that work is explicitly requested as a separate training/refinement task.

## Storage and archive discipline

Do not create downloadable archives for normal unit, chapter, commit, validation, or phase progress.

Keep working state inside the workspace and report progress in chat. Create a downloadable workspace archive only when explicitly requested. The expected snapshot name is:

```text
SkillForge_Rebuild.zip
```

A requested snapshot is a complete current workspace, not a patch archive.

Avoid emitting thousands of individual generated Markdown files into user-facing storage merely to report progress.

## Validation and change discipline

At each major architectural phase:

1. make the smallest necessary change;
2. validate the affected boundary;
3. report PASS/FAIL;
4. continue only if the architecture remains clean.

Do not preserve a bad path, duplicated skill definition, importer, index, or agent-specific convention solely because earlier code expects it. Rewire the code or remove the dependency.

Do not claim a platform compatibility test passed unless it was actually exercised in that platform environment.

## End state

A healthy SkillForge workspace should make these statements true:

- PASS can leave the repo and still author skills.
- A release can leave the repo and still work.
- One Software Engineering language can ship without every other language.
- Art can preserve formally taught knowledge without being forced into an autonomous-agent workflow.
- Prerequisite closure survives folder reorganization.
- The repo is replaceable infrastructure; the skillsets are portable products.

## Repo-local agent discovery

`.agents/skills/` (Codex/ChatGPT tooling) and `.claude/skills/` (Claude Code) are
allowed repo integration points. They are deliberately thin wrappers around the
canonical `PASS/` and `library/` content. Do not turn those folders into separate
sources of truth, and never make a release depend on them.

`AGENTS.md` (Codex/ChatGPT and other agents) and `CLAUDE.md` (Claude Code) carry the
same repository-wide working agreements, each written for the agent that loads it.
`ARCHITECTURE.md` is the canonical contract and decides any disagreement between
them; change a rule in one and change it in the other. These files belong to the
factory and are excluded from release products.
