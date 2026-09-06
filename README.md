# SkillForge

SkillForge is the distribution repository for finished AI skillsets built and
validated in [PASS](https://github.com/Methuselas/PASS).

## Releases

- [SkillForge Art](releases/SkillForge-Art.zip)
- [SkillForge Game Design](releases/SkillForge-Game-Design.zip)
- [SkillForge Software Engineering](releases/SkillForge-Software-Engineering.zip)
- [SkillForge Writing](releases/SkillForge-Writing.zip)

Each ZIP is a self-contained Agent Skills-compatible release with a compact
`SKILL.md`, its complete domain knowledge, the mandatory `metaskills` baseline,
its prerequisite closure, runtime profile, and validated Skillset Memory when
that domain has one. Source books and the PASS authoring environment are not
runtime dependencies.

## Use a release

Install or upload the ZIP as a skill where Agent Skills are supported. On other
hosts, extract it and begin with its root `SKILL.md`. The release routes into the
smallest relevant portion of its bundled library instead of requiring the whole
skillset in context at once.

Do not edit generated releases here. Change cards, recipes, or tooling in PASS,
rebuild the release, run the release check, and replace the corresponding ZIP.
