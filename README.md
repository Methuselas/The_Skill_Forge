# SkillForge

SkillForge is the distribution repository for finished AI skillsets built and
validated in [PASS](https://github.com/Methuselas/PASS). Each release is a
self-contained package: install one skill, then let its root `SKILL.md` route the
model into only the knowledge needed for the current task.

## Skills

| Skill | Best for | Documentation | Download |
|---|---|---|---|
| Art | Drawing, painting, visual development, critique, composition, comics, animation, and production art | [Readme](skills/art/README.md) | [ZIP](releases/SkillForge-Art.zip) |
| Game Design | Mechanics, characters, adversaries, adventures, worlds, critique, and playtesting | [Readme](skills/game-design/README.md) | [ZIP](releases/SkillForge-Game-Design.zip) |
| Software Engineering | Design, implementation, review, refactoring, testing, maintainability, and C++ | [Readme](skills/software-engineering/README.md) | [ZIP](releases/SkillForge-Software-Engineering.zip) |
| State Protocol | Compact session continuity, local-model memory, scoped user adaptation, and isolated multi-model work | [Readme](skills/state-protocol/README.md) | [ZIP](releases/SkillForge-State-Protocol.zip) |
| Writing | Fiction, poetry, creative nonfiction, essays, career documents, revision, and feedback | [Readme](skills/writing/README.md) | [ZIP](releases/SkillForge-Writing.zip) |

## Install a skill

1. Download the skill's ZIP.
2. Install or upload it where Agent Skills are supported. On a host that expects
   files or folders, extract the ZIP and add the extracted skill directory.
3. Begin with the root `SKILL.md` inside the package.

Python helpers are included where deterministic routing, drill administration,
or local persistence benefits from them. The craft knowledge itself remains
readable Markdown and does not require Python.

## Repository layout

```text
skills/<skill-name>/README.md   browsable product documentation
releases/SkillForge-*.zip      stable current-download paths
```

The documentation paths and ZIP filenames stay stable. A release's
`RELEASE_MANIFEST.json` records the PASS factory version that produced it, and
[`releases/README.md`](releases/README.md) records its checksum. SkillForge does
not yet assign independent product versions; historical releases remain
available through Git history and repository tags instead of accumulating
renamed copies beside the current download.

## Source boundary

Do not edit generated archives here. Change cards, recipes, profiles, or tools
in PASS, rebuild and verify the release there, then replace the corresponding
ZIP in SkillForge. Source books and the PASS authoring environment are not
runtime dependencies.
