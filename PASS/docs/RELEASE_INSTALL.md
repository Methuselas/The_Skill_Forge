# Using a SkillForge Release

A finished release is one self-contained Agent Skills-compatible directory. It has
`SKILL.md`, `RELEASE_MANIFEST.json`, and a local `library/` containing the complete
metaskill + prerequisite closure.

## ChatGPT / Codex skills

Where standalone Agent Skills are supported, install or upload the release
directory/ZIP as a skill. The root `SKILL.md` carries the required `name` and
`description` metadata.

For repository-local Codex discovery, place a released skill directory beneath:

```text
.agents/skills/<skill-name>/
```

SkillForge itself keeps repo-only discovery wrappers under `.agents/skills/`; those
wrappers are factory integration and are not copied into released skillsets.

## Claude Code

For project-local Claude Code discovery, place the release directory beneath:

```text
.claude/skills/<skill-name>/
```

SkillForge keeps matching repo-only discovery wrappers under `.claude/skills/` for
working on the factory itself. They are not runtime dependencies of releases.

## Archive/context use

A release remains a normal self-contained directory/ZIP even when a host does not
install it as a native skill. The consumer may inspect `SKILL.md` and the bundled
`library/` directly. No SkillForge repository path is required.

## Execution contract and deployment profiles

Portable releases vendor the canonical SkillForge resolver as
`scripts/skillforge_runtime.py` and a declarative `runtime/profile.yaml`.

`runtime/profile.yaml` is the release's **execution contract**: it declares the
execution modes, routing, risk checks, and completion requirements the consuming
skill is expected to honor. The vendored script is an optional deterministic
helper that resolves a request against that contract and can audit a completion
record afterward. It does not run by itself, hold state, or gate anything — a
host that never invokes it still has a complete, usable release. Honoring the
contract is the consuming skill's responsibility. See `EXECUTION_CONTRACT.md`.

A release recipe may also name a target-specific `deployment_profile`. Package
size is then measured at release build/check time against that profile. No recipe
currently names one and `PASS/runtime/deployment_profiles/` does not yet exist;
it is an available extension point. This does not change canonical authoring
validation or library organization.
