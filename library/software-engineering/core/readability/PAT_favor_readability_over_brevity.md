---
object_id: PAT_favor_readability_over_brevity
object_type: pattern
name: Favor Readability Over Fewer Lines of Code
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- readability
- code_length
- maintainability
- single_source_of_truth
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 112-115
  evidence_type: text
confidence: high
references: []
variants: []
---

# Favor Readability Over Fewer Lines of Code

## Pattern Rule
**IF** compacting logic into fewer lines would make it harder to understand
**THEN** choose the more readable form even if it takes more lines, treating line count as a proxy signal rather than a target to minimize.

## Do
- Remember what the proxy stands for: code that is easy to understand, hard to misunderstand, and hard to break — one cryptic line can cost more quality than ten clear ones.
- Expand dense expressions into named helpers and constants: the one-line parity check `countSetBits(id & 0x7FFF) % 2 == ((id & 0x8000) >> 15)` becomes readable as `extractEncodedParity(id) == calculateParity(getIdValue(id))` with named masks.
- Use the expansion to also create a single source of truth — naming the parity-bit position once means encoder and validator cannot silently drift apart.

## Don't
- Don't pack multiple nonobvious assumptions (which bit is the parity bit, what each mask means) into one succinct line where readers must reverse-engineer them.
- Don't argue that a change is worse simply because it turned three lines into ten; judge by understandability, not length.

## Checklist
- Is the criterion or intent immediately obvious, or must a reader decode it?
- Are hidden assumptions named as constants/functions rather than inlined as literals?
- Did brevity create a fragile duplicate of an assumption defined elsewhere?

## Notes
The 16-bit parity-check example is the anchor: the succinct version hides six undocumented assumptions and is fragile because it silently depends on an encoding defined elsewhere, while the verbose version names each mask and conversion and is both readable and reusable. Long is explicit that fewer lines is still a useful warning sign for over-complexity or missed reuse, but it is a guiding heuristic, not a rule that overrides understandability.
