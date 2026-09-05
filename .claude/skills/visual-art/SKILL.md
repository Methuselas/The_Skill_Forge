---
name: visual-art
description: >-
  Use for drawing, illustration, visual composition, figure or animal drawing,
  gesture, construction, anatomy, heads, hands, perspective, rendering, art
  critique, and guided visual-art teaching in this repository.
---

# Visual Art

## User help command

Treat `Help Art` and clear variants such as `Help Art staged`, `Help Art modes`, `Help Art revisions`, `Help Art references`, or `Help Art approval` as non-productive help commands. Do not generate/edit an image, change mode, ratify/reject an artifact, advance/rollback the staged workflow, or otherwise mutate production state merely because help was requested. Read `docs/ART_HELP.md` and answer from that user-facing contract. If the user separately issues a production or mode command in the same turn, follow the explicit command after answering the requested help where practical.

Use the trained Art library as canonical knowledge. Books are study material;
the accepted PASS cards and teacher corrections are the working curriculum. The
cards stand on their own — never reach for a source book to apply one.

## Targeted retrieval

Do not preload the Art master index, every subject, or every drawing system.
Classify the operation and subject, use `metaskills` as the default skill
baseline, then retrieve a bounded set from both packages with a few task cues.
Load only the relevant metaskill cards. Resolve the closest applicable AP
first, then load only the Patterns its flow reaches, plus declared foundations
and prerequisites.

```bash
python PASS/tools/find_relevant.py --package metaskills --cues "<task cues>" --limit 5
python PASS/tools/find_relevant.py --package art --cues "<task cues>" --limit 8
```

For a Drill, read the applicable administration mode in
`PASS/docs/PASS_CONSUMPTION.md`; do not confuse describing an artifact with
producing it. Use the PASS-authoring skill when studying a source or changing
cards, modules, schema, or releases.

Classify the turn from meaning: discuss, inspect, or produce. Do not generate or
edit an image unless the user actually asks for production. During PASS training,
work one source chapter at a time, discuss after the read, and ask questions only
when genuine uncertainty remains.

## Skillset Memory

`memory/art/` is the empirical record of what happened when this canon was
actually used — known weak areas, recurring failures, and the boundary of what
has been verified. It is not canon and never overrides a card.

Canon resolves first; memory is retrieved second and bounded. Query it before
productive work, with short cues drawn from the subject and the operation:

```bash
python PASS/tools/memory.py query --domain art --cues "hand,contact,foreshortening"
```

Cues match as substrings of an entry's recorded cues, so prefer several short
terms over one long phrase. Read what comes back as an observation carrying a
stated confidence, not as an instruction. A recorded weak area is a reason to
inspect that region of the artifact more carefully after rendering; it is never
a reason to skip a risk check the routing contract already requires.

Never copy an entry's content into a card, an index, or this file. An entry that
seems to apply on every turn has earned promotion review, not a paste.

## Conditional production contract

For any request that may generate or edit an image, read
`references/production-routing.md` before the first productive call and retain
its mode, approval, continuity, risk-inspection, and completion gates for the
active production thread. Do not load that reference for discussion, critique,
source authoring, or a Drill that produces no image.
