---
object_id: PAT_balance_adaptability_without_predicting_future
object_type: pattern
name: Make Code Adaptable Without Predicting Specific Changes
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- adaptability
- code_quality
- over_engineering
- requirements_change
cross_links: []
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_isolate_the_categories_that_are_historically_volatile
  variant_name: Isolate the Categories That Are Historically Volatile
  variant_basis: method_sequence
  difference_from_foundation: The foundation applies general adaptability techniques and explicitly declines to predict which change will arrive. This variant supplies a middle route — predict the *category* rather than the specific change. It names areas that are volatile on almost any project (business rules, hardware dependencies, input and output formats, nonstandard language features, difficult design and construction areas, status variables, data-size constraints) and runs a three-step procedure over them — identify items likely to change, separate each volatile item into its own class or into a class with items that change at the same time, then isolate it behind an interface insensitive to the change so callers cannot tell it happened. It adds a proportionality rule the foundation lacks — make the scope of a change proportional to its likelihood, and factor in how cheap the change is to plan for, so an unlikely but easily anticipated change still earns preparation.
  when_to_use: Use when a component sits in one of the named volatile categories, where the evidence is historical rather than speculative. Also use its two concrete moves wherever status is represented — prefer an enumerated type over a boolean so adding a state is a recompile rather than a sweep, and read state through an access routine so a more sophisticated test can replace a simple one later.
  when_not_to_use: Do not let it license predicting specific future requirements, which is what the foundation rules out and what turns into speculative generality. Only extremely unlikely changes should be allowed to have drastic consequences across more than one class, so a category membership alone does not justify unlimited insulation.
  absorbed_from_object_id: none
---

# Make Code Adaptable Without Predicting Specific Changes

## Pattern Rule
**IF** you know a piece of code's requirements will change but not exactly how, and you must decide how much adaptability to build in
**THEN** aim for a point between two failure extremes — apply generally-applicable adaptability techniques that do not require knowing the specific future change.
**ELSE** for a small, run-once-then-throw-away utility, put no effort into adaptability at all.

## Do
- Recognize the cost of over-preparing (scenario A): days or weeks mapping speculative futures, deliberating every minutia, shipping a year late, and usually guessing the future wrong anyway.
- Recognize the cost of under-preparing (scenario B): brittle assumptions baked in everywhere and subproblems bundled into inseparable chunks, so a small requirement change forces throwing everything away and rewriting.
- Choose where on the spectrum to sit based on the specific project and the culture of the organization — there is no single optimal point.

## Don't
- Don't try to predict exactly how requirements will evolve and pre-engineer support for every branch you imagine.
- Don't swing the other way and ignore that requirements *will* evolve just because you cannot predict how.

## Checklist
- Are subproblems kept separable, or bundled into one inseparable chunk?
- Would a small but likely requirement change force a rewrite rather than a local edit?
- Did you add adaptability machinery for a specific future nobody has asked for?

## Notes
Long presents two extreme scenarios — exhaustively engineering for predicted change versus ignoring change entirely — and shows both lose to a competitor, one by shipping a year late and one by needing repeated three-month rewrites. The durable lesson is that adaptability is achievable without prophecy: general techniques (developed through the rest of the book) keep code flexible without committing to guesses about which change will actually arrive.

`VAR_isolate_the_categories_that_are_historically_volatile` supplies a genuinely different route to the same decision, and the two sources disagree in an instructive way. Long declines to predict; McConnell predicts the *category* and not the instance. His claim is that certain areas are volatile on nearly every project regardless of domain — business rules, hardware interfaces, input and output formats, nonstandard language extensions, the parts that were hard to design and may need redoing, status variables, and data-size constraints — so treating them as volatile is reading history rather than forecasting. Where the two agree is on the failure mode: he also holds that only extremely unlikely changes should be allowed drastic consequences across more than one class, which is the same anti-speculation instinct arriving from the other side. His proportionality rule is the useful addition — scope the preparation to the likelihood of the change, adjusted for how cheap it is to prepare for, so a change that is unlikely but trivially anticipated still earns its insulation while a likely one that would cost a rewrite to anticipate may not. His two status-variable moves are worth taking on their own: prefer an enumerated type to a boolean, and read state through an access routine rather than testing the variable directly.
