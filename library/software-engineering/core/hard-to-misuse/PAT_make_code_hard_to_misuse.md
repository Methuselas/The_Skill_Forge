---
object_id: PAT_make_code_hard_to_misuse
object_type: pattern
name: Make Wrong Usage Hard or Impossible
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- hard_to_misuse
- api_design
- error_prevention
- interfaces
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_prefer_immutable_objects
- rel: prerequisite_for
  target_object_id: PAT_keep_immutable_with_builder_or_copy_on_write
- rel: prerequisite_for
  target_object_id: PAT_make_immutability_deep
- rel: prerequisite_for
  target_object_id: PAT_use_dedicated_types_over_general_ones
- rel: prerequisite_for
  target_object_id: PAT_use_dedicated_time_types
- rel: prerequisite_for
  target_object_id: PAT_single_source_of_truth_for_data
- rel: prerequisite_for
  target_object_id: PAT_single_source_of_truth_for_logic
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Make Wrong Usage Hard or Impossible

## Pattern Rule
**IF** other code must "plug into" yours by passing arguments or putting the system into a required state before calling
**THEN** shape the interface so plugging the wrong thing in is hard or impossible — the way differently-shaped TV sockets stop a power cord from entering the HDMI port.

## Do
- Identify exactly what callers must supply and what state they must set up beforehand, then design the API so an incorrect combination physically won't fit.
- Weigh the blast radius of misuse: some wrong usage merely fails, but some corrupts a database, loses data, or crashes the system — like plugging power into the HDMI socket and blowing things up.

## Don't
- Don't leave every "socket" the same shape, so a caller can silently pass the wrong argument or invoke the code in the wrong state.
- Don't assume misuse that "doesn't blow up" is harmless — it may skip the important task the code was called to do, or misbehave in a way nobody notices.

## Checklist
- Can a caller pass arguments in the wrong order or of the wrong type without the interface stopping them?
- Does the API require the correct state to exist before it can even be called?
- For each misuse you can imagine, is the worst case a clean failure or silent corruption?

## Notes
The TV-socket analogy makes the principle physical: the manufacturer prevents a whole class of mistakes by making the wrong plug not fit. Long stresses that misused code need not crash to be a problem — it can quietly fail to perform the task it was called for. This is the "hard to misuse" pillar's foundation; chapter 7's techniques (immutability, dedicated types, single sources of truth) are specializations of making invalid use structurally impossible.
