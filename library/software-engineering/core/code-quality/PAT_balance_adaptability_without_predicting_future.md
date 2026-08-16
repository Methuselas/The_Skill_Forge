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
- variant_id: VAR_choose_how_late_each_value_is_bound
  variant_name: Choose How Late Each Value Is Bound
  variant_basis: method_sequence
  difference_from_foundation: The foundation decides how much adaptability a component gets, and the volatile-categories variant decides it from what history says will change. This variant applies the same flexibility-against-complexity judgment to a single value, and supplies a named ladder to place it on — coding time (a literal written into the source), compile time (a named constant), load time (read from a settings file or a registry at startup), object instantiation time (read again each time the window is created), and just in time (read again each time the window is drawn). Every rung further down buys flexibility and pays for it in complexity and error-proneness. The rule it contributes is that the first step is free and the rest are not. Replacing a hard-coded literal with a named constant wins on readability and single-point-of-change grounds whether or not anyone wants flexibility, so ordinary good practice already puts you on the second rung; each rung after that has to be justified by a requirement that exists.
  when_to_use: Use at the moment you write a value into the code and are deciding where it comes from, which is a finer grain than the foundation works at and happens far more often. It is also the sharper tool when a disagreement is really about configurability — placing the two proposals on named rungs turns "should this be configurable?" into a question about which rung the requirements actually reach, and makes the complexity being purchased visible rather than implied.
  when_not_to_use: Do not read the ladder as an invitation to climb it. Past the named constant, later binding costs complexity and invites errors, and flexibility built beyond what the requirements ask for is exactly the over-preparation the foundation rules out. It also prices one value rather than a design, so it does not decide where a component's boundaries belong.
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
- Don't leave speculative code in the codebase where it cannot be told apart from code that is in use. Later programmers do not know it was written ahead of any requirement; they assume it was coded, tested, and reviewed to the same standard as everything around it, build on top of it, and discover only afterwards that it does not work.

## Checklist
- Are subproblems kept separable, or bundled into one inseparable chunk?
- Would a small but likely requirement change force a rewrite rather than a local edit?
- Did you add adaptability machinery for a specific future nobody has asked for?

## Notes
Long presents two extreme scenarios — exhaustively engineering for predicted change versus ignoring change entirely — and shows both lose to a competitor, one by shipping a year late and one by needing repeated three-month rewrites. The durable lesson is that adaptability is achievable without prophecy: general techniques (developed through the rest of the book) keep code flexible without committing to guesses about which change will actually arrive.

Designing ahead fails in four ways, and only the first is the one people expect. The requirements for the speculative code do not exist yet, so the guess is usually wrong and the work is thrown away. Even a close guess misses the intricacies of the real requirement, and those undermine the design assumptions, so the work is thrown away anyway. The third is the one worth carrying, because it is a cost paid by other people and it does not announce itself: future programmers cannot tell design-ahead code from working code, assume it has been coded, tested, and reviewed like everything else, build on it, and find out late that it does not do what it appears to. And the extra code carries the ordinary tax of any code — more to test, more to fix, a slower project. The positive form of the rule follows from all four: the best preparation for a future requirement is not speculative code but current code that is clear and straightforward enough that whoever arrives can see what it does and does not do.

`VAR_choose_how_late_each_value_is_bound` works the same tradeoff at the smallest possible grain — one value, at the moment you write it down. Its contribution is a ladder with named rungs, running from a literal in the source, through a named constant, through a value read at load time, to one read on every object creation and finally on every use. The reason the ladder is worth carrying is that it separates a step everyone should take from steps that have to be earned. Going from a magic number to a named constant is free — it pays for itself in readability and in having one place to change — so good practice lands on the second rung without anyone deciding to be flexible. Everything below that is a purchase, and what it costs is complexity and error-proneness in the code that supports it. That reframes the familiar argument about whether something "should be configurable" into a question with an answer — which rung do the requirements actually reach — and it exposes the complexity being bought, which the usual framing leaves implicit. Read alongside the volatile-categories variant, the two cover different grains of the same judgment: one asks which parts of a design deserve insulation, the other asks how late a single value should be pinned down.

`VAR_isolate_the_categories_that_are_historically_volatile` supplies a genuinely different route to the same decision, and the two sources disagree in an instructive way. Long declines to predict; McConnell predicts the *category* and not the instance. His claim is that certain areas are volatile on nearly every project regardless of domain — business rules, hardware interfaces, input and output formats, nonstandard language extensions, the parts that were hard to design and may need redoing, status variables, and data-size constraints — so treating them as volatile is reading history rather than forecasting. Where the two agree is on the failure mode: he also holds that only extremely unlikely changes should be allowed drastic consequences across more than one class, which is the same anti-speculation instinct arriving from the other side. His proportionality rule is the useful addition — scope the preparation to the likelihood of the change, adjusted for how cheap it is to prepare for, so a change that is unlikely but trivially anticipated still earns its insulation while a likely one that would cost a rewrite to anticipate may not. His two status-variable moves are worth taking on their own: prefer an enumerated type to a boolean, and read state through an access routine rather than testing the variable directly.
