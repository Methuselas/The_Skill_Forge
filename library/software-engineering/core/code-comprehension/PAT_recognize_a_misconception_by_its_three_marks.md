---
object_id: PAT_recognize_a_misconception_by_its_three_marks
object_type: pattern
name: Tell a Misconception From a Slip Before Trying to Fix It
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- misconceptions
- debugging
- mental_model
- defects
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_replace_a_misconception_with_a_new_model
- rel: related_to
  target_object_id: PAT_diagnose_source_of_code_confusion
- rel: related_to
  target_object_id: PAT_expect_negative_transfer_between_similar_languages
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Tell a Misconception From a Slip Before Trying to Fix It

## Pattern Rule
**IF** a bug came from your reasoning rather than your typing
**THEN** test the belief behind it against three marks — faulty, held consistently across situations, held with confidence — because only a belief carrying all three needs the expensive repair.

## Do
- Apply all three marks, not one. A belief that is merely wrong is an error; a belief that is wrong, applied the same way everywhere, and trusted enough to act on is a misconception, and the difference determines what fixing it costs.
- Use the confidence itself as the diagnostic signal. When you were sure the code would work and it failed anyway, that combination is the symptom — as distinct from the case where you already suspected the line.
- Separate the slip cases out first. Forgetting to close a file, a typo in a filename, selecting the wrong method, an off-by-one in a boundary calculation: these are sloppiness and need nothing more than the fix.
- Look for the belief's origin once you have identified one, because that usually shows where else it is operating. The chapter traces "a variable holds only one value" to mathematics, where a variable genuinely does not change within a proof, and separately to filesystems, where a folder allows only one file of a given name.

## Don't
- Don't treat every wrong assumption as a misconception. Most bugs are slips, and applying conceptual-change effort to a typo wastes it.
- Don't dismiss a misconception as absurd because it is obviously wrong to you now. The book's examples are all *reasonable* — assuming a variable holds one value follows correctly from mathematics, and the reasonableness is why the belief survived.
- Don't stop at the instance. Consistency across situations is one of the three marks, so a misconception found in one place is by definition already at work elsewhere.

## Checklist
- Is this belief actually false, or merely different from how I would have written it?
- Would I apply it the same way in a different file, language, or project?
- Was I confident enough to act on it without checking?

## Notes
The formal definition matters because everyday usage blurs it. In ordinary conversation "misconception" means roughly a mistake or being confused; Hermans requires all three properties together, and the third is what makes the condition expensive to clear.

Her non-programming illustration carries the structure cleanly: many people believe chilli seeds are the spiciest part, which is false; they generalize it from one kind of chilli to all chillies, which is consistency; and they act on it by deseeding before cooking, which is confidence. The searing-meat case shows the same shape arriving through negative transfer instead of folklore — other foods such as eggs solidify when heated, so heat is assumed to form an impenetrable shield sealing in juices, when searing in fact produces a greater net loss of moisture.

Bugs from misconceptions look different from bugs from slips at the moment of discovery. A slip is recognized immediately once pointed out. A misconception produces the reaction that the code should work, which is the state this pattern exists to name.
