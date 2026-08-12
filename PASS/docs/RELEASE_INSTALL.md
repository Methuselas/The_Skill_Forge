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
