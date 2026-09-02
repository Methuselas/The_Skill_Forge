---
object_id: PAT_price_character_options_by_mechanical_leverage_and_constraint
object_type: pattern
name: Price Character Options by Mechanical Leverage and Effective Constraint
library_path:
- game-design
- characters
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- balance
- characters
- costs
- point-economy
cross_links:
- rel: related_to
  target_object_id: PAT_derive_character_capabilities_from_expected_play
- rel: related_to
  target_object_id: PAT_keep_persistent_capability_dependencies_local_and_explicit
- rel: related_to
  target_object_id: DRILL_stress_test_mechanical_constraints_under_composition
reference:
  source_title: GURPS Basic Set, Fourth Edition and GURPS Compendium I
  author: Steve Jackson, David L. Pulver, Sean M. Punch, and contributors
confidence: high
references: []
variants: []
---

# Price Character Options by Mechanical Leverage and Effective Constraint

## Pattern Rule
**IF** character options share a build currency or can substitute economically for one another
**THEN** price them by the breadth, frequency, downstream effects, configurability, and actual constraint they create in play rather than by conceptual symmetry or dramatic wording
**ELSE** do not force nominally similar traits into equal prices when they do not buy or surrender comparable capability.

## Do
- Audit the leverage of broad traits. Count which skills, defenses, resources, derived values, defaults, future purchases, or other persistent capabilities change when the trait changes.
- Compare a broad purchase against representative narrower purchases that could produce the same intended concept. Reprice, narrow, or split the bundle when the broad option routinely dominates those alternatives.
- Provide intermediate bundles when the design needs a useful middle ground between one narrow capability and a very broad parent trait.
- Price drawbacks by the constraint they actually impose: frequency, severity, controllability, lost choices, social exposure, recovery difficulty, and how easily play can avoid the consequence.
- If drawbacks grant positive build currency, test whether rational players are pushed toward filling the allowed negative budget even when additional flaws do not strengthen the intended concept.
- Reprice a drawback when another broadly useful purchase can reliably neutralize it; do not let players retain the refund after the meaningful constraint has disappeared.
- Treat flexible configuration as capability. If one character can selectively enable, disable, retarget, or reshape a purchased effect while another cannot, account for that difference where it materially expands choices.
- Re-run the economic comparison when new supplements, traits, modifiers, or advancement options expand what a broad purchase can influence.
- Keep the price of the same persistent capability consistent across character creation and advancement unless timing, scarcity, or acquisition opportunity is itself an intentional source of play. Solve an underpriced option by repricing the option, not by imposing a lifecycle surcharge after play begins.

## Don't
- Price foundational attributes equally merely because their names are equally fundamental to the fiction.
- Assume a disadvantage is worth more because its label sounds severe when its actual trigger is rare, avoidable, or easily resisted.
- Treat a cap on negative points as proof that drawback incentives are solved; a cap limits magnitude but can still make filling the cap feel optimal.
- Let a general-purpose attribute or advantage cheaply erase a drawback while preserving the points the drawback financed.
- Force every concept to choose between dozens of narrow purchases and one giant bundle when a thematic middle layer would create better differentiation.
- Preserve legacy prices after the dependency network changes enough that an option now buys substantially more or less than it did when first costed.
- Charge a different point price for the same persistent capability solely because it was purchased after character creation when that timing difference has no intended fictional or strategic meaning.

## Checklist
- Each broad option has an identified set of downstream capabilities and a representative comparison against buying those capabilities more narrowly.
- No general-purpose trait is the routine cheapest answer for several concepts that are intended to remain mechanically distinct.
- At least one test character uses an intermediate bundle when the design provides one, and its cost is compared with both the narrow and broad alternatives.
- Drawback value reflects how often and how strongly the drawback constrains actual play rather than the severity of its name alone.
- If drawbacks refund build currency, test characters are built both with and without deliberately filling the permitted negative budget to expose incentive pressure.
- Purchases that reduce or remove a drawback also reduce the drawback's economic value when appropriate.
- Selective or configurable versions of an effect are not silently priced as though they were identical to fixed versions when the flexibility creates additional agency.
- The price audit is repeated after major additions to the character option catalog or dependency graph.
- A capability bought during play is compared with the same capability bought at creation; any price difference names the intentional gameplay value of timing rather than acting as a patch for an imbalanced base price.

## Notes
Point economies compare unlike fictional traits through one currency, so symmetry in description is not evidence of equal value. A broad attribute can be underpriced even when its number looks reasonable if it raises many skills, defenses, defaults, and future purchases at once. Conversely, a disadvantage can be overvalued if its supposed severity rarely removes meaningful choices. Incentives matter independently of intent: when flaws finance positive abilities, players may feel pressure to consume the entire allowed negative budget even if the final flaws are weakly connected to the character concept. Caps control the maximum distortion but do not remove that pressure. Intermediate bundles can relieve the opposite problem by giving players a priced thematic aptitude between one narrow skill and an attribute that improves almost everything in a domain. The durable test is economic leverage: what does this purchase actually change, how often does that matter, how much choice does it create or remove, and what other legal purchase would accomplish the same goal? Lifecycle pricing belongs to the same audit. If an attribute is too efficient, charging double to improve it later does not repair its creation price; it merely makes build order part of optimization. A different acquisition-time price is defensible only when timing, scarcity, or access is itself intended gameplay rather than compensation for a mispriced trait.
