---
name: game-design
description: >-
  Use for designing, revising, critiquing, playtesting, or practising game
  mechanics, characters, adversaries, adventures, and playable worlds with
  SkillForge's game-design library. Do not use it for PASS source extraction.
---

# Game Design

Use the accepted Game Design cards as craft guidance. Source books are authoring
material, not runtime dependencies; never reopen one to apply a finished card.

## Targeted retrieval

Do not preload the Game Design master index or every category. Restate the play
experience and current design decision, use `metaskills` as the default skill
baseline, then retrieve a bounded set from both packages with a few task cues.
Resolve the closest applicable AP first. Load only the Patterns that its flow
reaches, plus declared foundations and prerequisites.

```bash
python PASS/tools/find_relevant.py --package metaskills --cues "<task cues>" --limit 5
python PASS/tools/find_relevant.py --package game-design --cues "<task cues>" --limit 8
```

Query `memory/game-design/` after canon and only with bounded cues from the task:

```bash
python PASS/tools/memory.py query --domain game-design --cues "<short,cues>"
```

For a Drill, read the applicable administration mode in
`PASS/docs/PASS_CONSUMPTION.md`; do not confuse describing an artifact with
producing it. Use the PASS-authoring skill instead when studying a source or
changing cards, modules, schema, or releases.
