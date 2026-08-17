---
object_id: PAT_estimate_by_decomposition_and_cross_check
object_type: pattern
name: Estimate by Decomposing and Cross-Checking, Never by Feel
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- estimation
- planning
- calibration
- scheduling
cross_links:
- rel: related_to
  target_object_id: PAT_scope_construction_beyond_writing_the_code
- rel: related_to
  target_object_id: PAT_price_a_requirements_change_instead_of_absorbing_it
- rel: related_to
  target_object_id: AP_assess_construction_prerequisites_before_building
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Estimate by Decomposing and Cross-Checking, Never by Feel

## Pattern Rule
**IF** you are asked how long a piece of work will take
**THEN** break it into small pieces, total them, and check the total against a second technique that works differently — rather than producing a number from your sense of the size of the job
**ELSE** where the thing has not been defined yet, say that instead of estimating, because an undefined scope has no size to estimate.

## Do
- Refuse the off-the-cuff answer. Estimates given on the spot are commonly wrong by a factor of two or more, and the number you say first is the one that gets remembered and planned against whatever you attach to it afterwards.
- Expect your own optimism as a standing bias rather than a mood. Surveys of estimated against actual schedules put developers' estimates about 20 to 30 percent optimistic, which is a correction to apply to yourself even when this particular estimate feels different.
- Estimate small pieces and add them up. On one large piece a 10 percent error stays a 10 percent error; across fifty small ones, some estimates run high and some run low and the errors substantially cancel. The gain comes from the number of pieces, not from thinking harder about any one.
- Check the total with a genuinely different technique. Agreement between two methods that could not have made the same mistake is real evidence; divergence tells you which assumption to go dig at. An eyeball estimate of 250 to 300 pages for a book, against a detailed estimate of 873 and a second technique's 828, settles the question — and it settles it against the eyeball.
- Refuse to estimate an undefined thing. Nobody can price "a pretty big house", and the honest response to "roughly how long for something like this?" is to define it first or to plan a short exploration whose only deliverable is a better estimate.
- Give the estimate time. A rushed estimate is an inaccurate estimate, and on anything substantial the estimate deserves planning as a small task in its own right.
- Re-estimate as you learn, and expect the range to narrow rather than the number to hold. Early estimates span roughly four times to a quarter of the truth; that spread closes as the work reveals itself, so an estimate is a thing you maintain rather than a thing you produce once.

## Don't
- Don't plan to make up lost time later. Across more than three hundred projects, delays and overruns grow toward the end rather than shrinking — a schedule that is behind at the midpoint finishes further behind, so "we will catch up during coding" is a wish with evidence against it.
- Don't quietly widen an estimate to cover unstated risk. Say what the risk is and what it would cost, so the person deciding sees the same thing you do.
- Don't treat an estimate as a commitment you made. It is a prediction about work, and confusing the two turns every subsequent discovery into a personal failure rather than information.
- Don't estimate only the coding. What the work includes is a separate question from how long it takes, and getting it wrong makes an otherwise sound estimate useless.

## Checklist
- Did you give a number before you had decomposed anything?
- How many pieces did you estimate, and did you add them up rather than judging the whole?
- What was the second technique, and did it agree?
- Is the thing being estimated actually defined?
- When did you last re-estimate, and did the range narrow?

## Notes
The two moves at the centre of this — decompose, then cross-check — work for the same underlying reason, which is that they attack error rather than ignorance. Decomposition does not make you better at judging how long a task takes; it exploits the fact that independent errors partly cancel, so it converts one large unknown into many small ones whose mistakes work against each other. Cross-checking does not make either estimate more accurate on its own; it detects the case where a whole method was wrong, which is exactly the failure a single careful estimate cannot see from the inside. Neither is a substitute for the other, and each is nearly useless against the failure the other catches.

The optimism figure deserves to be treated as a property of the estimator rather than of the estimate. Twenty to thirty percent is close enough to universal that reading it as "other people are optimistic" is itself the bias operating. The practical form is to make the correction explicit and visible rather than to try to feel less optimistic, because the feeling is not under your control and the arithmetic is.

Where this ends is worth naming, because estimation gets asked to carry more than it can. The accuracy of an initial estimate matters much less than what happens afterwards: once a date and a scope exist, the useful question becomes what to control to hit them. And when a project is behind, the levers are real but few — hoping is measurably the worst of them, adding people works only where the remaining tasks genuinely partition, and reducing scope is the one that is both reliable and routinely overlooked. Cutting a feature removes its design, coding, debugging, testing, documentation, and every interface it would have had. Short of cutting it, ask what version of it exists at two hours, two days, and two weeks, and what the extra time actually buys.
