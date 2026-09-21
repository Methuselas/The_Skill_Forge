# SkillForge

SkillForge is the distribution repository for finished AI skillsets built and
validated in [PASS](https://github.com/Methuselas/PASS).

## Releases

Each release has its own folder with its ZIP and a README. Sizes, hashes and
build versions are in [`releases/README.md`](releases/README.md).

- [SkillForge Agent Kit](releases/skills/agent-kit/) — coordinates several AI
  agents in one project: claims, file and resource scopes, reviews, evidence.
  Ships a standard-library runtime; its state lives in the project.
- [SkillForge Art](releases/skills/art/) — drawing, painting, comics and
  illustration craft.
- [SkillForge Game Design](releases/skills/game-design/) — mechanics, characters,
  adversaries, adventures and playable worlds.
- [SkillForge Software Engineering](releases/skills/software-engineering/) —
  design, implementation, review, testing, C++, Unreal Engine editor tooling
  and Blueprints visual scripting.
- [SkillForge Writing](releases/skills/writing/) — fiction, poetry, nonfiction,
  admission essays and career documents.

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

## Model Tools

- [Bionic Memory](releases/models/bionic/) — persistent cross-session memory for
  AI agents. Local Markdown files, Python CLI, works with any Agent Skills–compatible
  host. Not built by PASS; it carries its own version.
