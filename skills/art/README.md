# SkillForge Art

SkillForge Art is a production-oriented visual-art skillset for models that
draw, generate images, plan visual work, or critique an existing artifact. It
turns broad art requests into bounded decisions, staged execution, and visible
checks instead of loading one enormous art prompt.

[Download the current release](../../releases/SkillForge-Art.zip) ·
[Release details and checksum](../../releases/README.md)

## Use it for

- drawing, painting, rendering, composition, layout, and perspective;
- figures, heads, hands, anatomy, animals, gesture, and locomotion;
- comics, covers, inking, page construction, storyboarding, and animation;
- color development, publication design, ideation, critique, and repair;
- structured practice through blind Drills.

## How it works

The root `SKILL.md` routes the model into a compact execution contract and only
the relevant cards. Action Procedures organize multi-step work, Patterns guide
individual decisions, and Drills provide exercises with explicit success
checks. The bundled `metaskills` package supplies shared planning, creative
search, and verification behavior.

Some workflows include approval gates so a model does not silently carry an
unapproved sketch or composition into expensive finish work. Image generation
or drawing tools still come from the host; this package supplies the art
judgment and workflow.

## Install

Install or upload the ZIP as one skill. If the host expects a directory, extract
the archive and point it at the extracted `SkillForge_Art` folder. The entry
point is `SKILL.md`.

Python is optional. When available, the bundled helpers can resolve runtime
requirements and administer blind Drills without becoming the source of art
judgment.

## Persistence boundary

The release may include a read-only snapshot of Art Skillset Memory: empirical
observations from earlier tests. It never overrides the bundled cards and is not
a target for user or project memory. Rebuilds and changes originate in PASS.
