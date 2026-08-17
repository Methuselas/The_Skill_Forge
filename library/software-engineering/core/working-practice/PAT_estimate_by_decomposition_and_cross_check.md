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
- Pick the unit to carry the accuracy you actually have. "About six months" and "130 working days" name the same duration and promise very different things; quote in days below about three weeks, in weeks up to two months, in months beyond that, and treat anything past about thirty weeks as a number to think hard before saying aloud at all.
- State the scope inside the answer rather than refusing to answer. "Twenty minutes, assuming no accidents and there is fuel in the car" is both honest and usable, where either a bare number or a refusal is not.
- Look for someone who has already done it before building any model. It is the cheapest estimate available and it is routinely better than a careful derivation from first principles.
- Keep a log of what you estimated against what happened, and when one misses, find out which part was wrong — the model, or a parameter in it. A standing bias cannot be corrected by anyone who is not measuring it.
- Hold the number when it is challenged, and move the conversation to what is actually negotiable. You cannot negotiate how long the work takes any more than you can negotiate how many feet are in a mile — but features, performance targets, delivery in increments, and people against calendar time are all genuinely on the table. Change one of those, then re-estimate and quote the new number.

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

Producing a good estimate and defending one are different skills, and the second is where technical people more often fail — IBM's Bill Weimer reported exactly that pattern, that his engineers estimated well and then could not hold their ground. The defence rests on a distinction worth making explicit: an estimate is a *prediction about the work*, not an *offer*. Revise it whenever new information changes the prediction; never revise it because someone wants to hear a different number. The clean formulation is a division of authority — how long it takes is your judgment to give, whether it is worth that price is theirs to make. That framing keeps you from arguing about the number and moves the discussion to the scope, which is the only place agreement can actually be found.

Shading an estimate downward to secure approval is worse than it looks, because it is not optimism but a quiet transfer of somebody else's decision to yourself. If a capability is worth 250 thousand and would cost 750 thousand to build, the right outcome is that it does not get built, and that call belongs to whoever holds the budget. Underestimating to get a project started removes their ability to make it. The arithmetic does not favour it either: promising four months and delivering six earns nothing that promising six and delivering six would not have earned, and it costs the credibility that makes the next estimate believable.

Where this ends is worth naming, because estimation gets asked to carry more than it can. The accuracy of an initial estimate matters much less than what happens afterwards: once a date and a scope exist, the useful question becomes what to control to hit them. And when a project is behind, the levers are real but few — hoping is measurably the worst of them, adding people works only where the remaining tasks genuinely partition, and reducing scope is the one that is both reliable and routinely overlooked. Cutting a feature removes its design, coding, debugging, testing, documentation, and every interface it would have had. Short of cutting it, ask what version of it exists at two hours, two days, and two weeks, and what the extra time actually buys.
