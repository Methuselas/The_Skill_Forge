---
object_id: PAT_diagnose_weak_recall_as_storage_or_retrieval
object_type: pattern
name: Separate Storage Strength From Retrieval Strength
library_path:
- software-engineering
- core
- deliberate-practice
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- memory
- diagnosis
- retrieval_practice
- deliberate_practice
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_attempt_recall_before_looking_up
- rel: prerequisite_for
  target_object_id: PAT_space_practice_across_widening_intervals
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u03, pp. 41-42
  evidence_type: text
confidence: high
references: []
variants: []
---

# Separate Storage Strength From Retrieval Strength

## Pattern Rule
**IF** you cannot produce a concept you are confident you have learned before
**THEN** decide whether it was never durably stored or is stored but hard to reach, and pick the remedy that matches — study for the first, attempted recall for the second

## Do
- Test which one failed by looking at the answer: if seeing it produces "of course, I knew that," storage is fine and retrieval is what needs work.
- Route a retrieval failure to recall attempts and spacing rather than to re-reading, because re-reading raises the strength that was not the problem.
- Route a genuine storage failure — the answer means nothing when you see it — to actually learning the concept before drilling recall of it.
- Expect the two to diverge for material you encounter constantly but never produce: reading a construct often builds recognition without building the ability to write it.

## Don't
- Don't read "I've seen this a dozen times and still can't write it" as evidence that you are bad at the language. Hermans's six near-identical C++ reverse-iteration options are hard for experienced C++ programmers precisely because recognition and production are different capacities.
- Don't treat forgetting as loss. Storage strength is generally held to only increase — recent work indicates people never really lose memories — so what decays over the years is reach, not the record.

## Checklist
- When shown the answer, did it feel obvious or unfamiliar?
- Does your planned fix target the capacity that actually failed?
- Are you re-reading material whose problem is that you have never once produced it from memory?

## Notes
Robert and Elizabeth Bjork separated the two mechanisms: storage strength is how well something is held, retrieval strength is how easily it comes back. The tip-of-the-tongue state — certain you know a name, a phone number, the signature of `filter()` — is high storage with low retrieval, and it is the ordinary case for programming syntax.

This card exists mainly to stop a misdiagnosis. The intuitive response to "I can't remember this" is to study it again, which is the correct response only in the rarer case. Most syntax failures are access failures, and the remedies for access — attempted recall, spaced revisiting — look nothing like re-reading.
