<!-- Generated shape. The closed contract is docs/PASS_SCHEMA.md.
     If this file and the schema disagree, the SCHEMA wins and this file is the bug.
     Copy below the marker; delete every <angle_bracket> token before saving.

     A card must execute after its source is gone. Never add source_id, locator,
     page numbers, hashes, or any other source identity to a card. -->

---
object_id: <stable_id>
object_type: pattern
name: <semantic_skill_name>
library_path:
  - <package>
  - <topic>
stage_binding: <0 design | 1 skeleton | 2 block | 3 rough | 4 final>
lane_fit: <teach | skill | both>
foundation_role: <foundation | specialization>
routing_class: <general | specialized | teaching>
specialization_axis: <none | language | tool | framework | medium | style | genre | tradition | source | method | domain>
foundation_object_id: <object_id | none>
tags:
  - <tag>
cross_links: []
# Optional attribution. Nothing reads it; omit the whole block if you prefer.
reference:
  source_title: <source_title>
  author: <author>
confidence: <low | medium | high>
variants: []
---

# <semantic_skill_name>

## Pattern Rule
**IF** <the specific decision moment a practitioner recognizes>
**THEN** <the specific action, with enough detail to execute>
**ELSE** <specific fallback for THIS pattern — optional, omit if none>

## Do
- <source-derived HOW detail — not a restatement of the THEN>

## Don't
- <source-derived failure mode, misconception, or warning>

## Checklist
- <observable verification specific to this skill>

## Notes
<Synthesized prose: what the source demonstrated, what misconception it addresses,
what it builds on. Not an OCR dump. Do not open by restating the THEN.>
