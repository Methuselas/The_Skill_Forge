---
name: writing
description: >-
  Use for drafting, revising, critiquing, or practising fiction, creative
  nonfiction, poetry, college essays, and career documents with SkillForge's
  writing library. Do not use it for PASS source extraction or repository code.
---

# Writing

Use the accepted Writing cards as craft guidance. Source books are authoring
material, not runtime dependencies; never reopen one to apply a finished card.

## Targeted retrieval

Do not preload the Writing master index or every writing category. Restate the
deliverable and current craft decision, use `metaskills` as the default skill
baseline, then retrieve a bounded set from both packages with a few task cues.
Resolve the closest applicable AP first. Load only the Patterns that its flow
reaches, plus declared foundations and prerequisites.

```bash
python PASS/tools/find_relevant.py --package metaskills --cues "<task cues>" --limit 5
python PASS/tools/find_relevant.py --package writing --cues "<task cues>" --limit 8
```

Query `memory/writing/` after canon and only with bounded cues from the task:

```bash
python PASS/tools/memory.py query --domain writing --cues "<short,cues>"
```

For a Drill, read the applicable administration mode in
`PASS/docs/PASS_CONSUMPTION.md`; do not confuse describing an artifact with
producing it. Use the PASS-authoring skill instead when studying a source or
changing cards, modules, schema, or releases.
