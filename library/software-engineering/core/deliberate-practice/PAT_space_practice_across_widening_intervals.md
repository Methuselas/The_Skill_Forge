---
object_id: PAT_space_practice_across_widening_intervals
object_type: pattern
name: Space Practice Across Widening Intervals
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
- spaced_repetition
- memory
- deliberate_practice
- onboarding
cross_links:
- rel: related_to
  target_object_id: PAT_attempt_recall_before_looking_up
- rel: teaches
  target_object_id: DRILL_practice_syntax_with_flashcards
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Space Practice Across Widening Intervals

## Pattern Rule
**IF** you are planning how to make new syntax or concepts stick
**THEN** spread a fixed number of repetitions across the longest interval you can sustain rather than concentrating them
**ELSE** the material will be available for the current task and gone within days

## Do
- Hold the repetition count roughly fixed and stretch the gaps; the gain comes from the spacing, not from adding study time. Ebbinghaus reliably learned a 12-item set with 75 total repetitions crammed across two days, or 38 spread over three — half the study time for the same result.
- Prefer intervals of weeks over intervals of days when the knowledge has to last. In Bahrick's study, the group drilled 26 times at 8-week spacing recalled 76% of 50 foreign words a year later; the 2-week spacing group recalled 56%.
- Schedule the revisit rather than waiting to feel rusty, since the feeling arrives well after the decay does.
- Accept a modest cadence. Hermans's practical floor is revisiting a flashcard set about once a month, which is low enough to actually keep doing.

## Don't
- Don't infer from a successful cram that the knowledge is retained. The forgetting curve is steepest immediately — roughly half of what you read is gone within the hour and about 25% remains after two days — so a session that felt complete predicts almost nothing about next week.
- Don't model a bootcamp or a single-semester course as sufficient. Knowledge acquired that way sticks only if repetition continues afterward, which is why so much of a degree evaporates.
- Don't read the curve as decaying to nothing; it flattens. The steep early loss is what spacing is aimed at, not a slow slide to zero.

## Checklist
- Are the gaps in your practice plan measured in weeks rather than within one sitting?
- Would the plan survive being run for a year, or does it depend on unusual effort this month?
- Are you adding study hours where you could instead widen intervals at the same cost?

## Notes
Ebbinghaus spent about a decade and 1,000 hours memorizing nonsense syllables — deliberately meaningless so that existing associations could not help — and published the forgetting formula in 1885; Murre's 2015 replication found it largely correct. The curve shows the shape the numbers alone do not: a steep early drop that levels off around a quarter of the material rather than continuing toward zero.

The counterintuitive part is that spacing is cheaper, not more expensive. The instinct when something has to be learned by Friday is to mass the practice, and that instinct optimizes for Friday at the cost of everything after it.
