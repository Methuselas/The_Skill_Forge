---
object_id: PAT_choose_a_randomizer_by_the_uncertainty_profile_it_must_produce
object_type: pattern
name: Choose a Randomizer by the Uncertainty Profile It Must Produce
library_path:
- game-design
- mechanics
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- mechanics
- probability
- randomizers
- resolution
cross_links:
- rel: related_to
  target_object_id: PAT_choose_a_game_foundation_by_the_experience_it_must_support
- rel: related_to
  target_object_id: PAT_evaluate_mechanics_by_the_decisions_and_agency_they_create
- rel: related_to
  target_object_id: PAT_account_for_the_intended_play_environment_before_freezing_the_design
reference:
  source_title: Designing TTRPGs For Dummies
  author: Martin Buinicki
confidence: high
references: []
variants: []
---

# Choose a Randomizer by the Uncertainty Profile It Must Produce

## Pattern Rule
**IF** a mechanic needs randomness
**THEN** define the uncertainty behavior the game needs before choosing dice, cards, or another randomizer, including distribution, granularity, degree-of-success information, how competence and circumstances alter the odds, execution burden, and the desired physical or emotional experience
**ELSE** do not introduce randomness merely because roleplaying games traditionally use a randomizer.

## Do
- Decide what outcomes must be possible and how frequently broad classes of outcomes should occur before selecting a die expression or other device.
- Separate result range from probability shape; a mechanic can have many possible values with a simple distribution or few values with a nonlinear distribution.
- Decide which information survives resolution: binary success, margin, number of successes, exceptional result, complication, or another usable output.
- Decide whether prior random results should alter future probabilities; independent rolls are memoryless, while finite decks, held cards, discards, depletion, and reshuffles can make uncertainty stateful.
- Consider whether the randomizer should carry content or rules payload in addition to probability, such as an event, trait, encounter, item, or instruction printed directly on a card.
- Choose how skill, difficulty, advantage, disadvantage, resources, or opposition modify the odds without assuming one manipulation method is inherently superior.
- Account for how the randomizer feels and operates at the table as well as what it does mathematically.
- Prefer established randomizer vocabulary when it already produces the needed behavior; novelty is not itself a design benefit.

## Don't
- Choose a randomizer first and then distort the rest of the game to justify it.
- Treat a large numerical range as automatically more complex or a small numerical range as automatically simpler.
- Assume two mechanics with similar average success rates create the same player experience.
- Invent an unfamiliar randomization procedure merely to make the game appear original.
- Preserve information from a roll that the game never uses just because the randomizer happens to produce it.
- Treat a finite deck as merely a die printed on cards when depletion, hands, discards, or reshuffling materially change what can happen next.

## Checklist
- The intended probability shape and ordinary success range can be described without naming a specific die mechanic.
- The game has a deliberate answer for how competence, difficulty, and situational changes affect the odds.
- The useful information produced by the roll or draw is identified explicitly.
- The design deliberately chooses independent or stateful uncertainty and specifies when the probability state resets.
- If the randomizer also carries content or rules text, that information density reduces or justifies the added handling burden.
- Physical handling, arithmetic, counting, lookup, and component requirements fit the intended play environment.
- The selected randomizer supports the intended tension, pacing, and player understanding better than at least one plausible alternative.
- Any unusual randomizer requirement has a concrete experiential or mechanical payoff beyond novelty.

## Notes
The randomizer determines what results can occur and how likely they are; the surrounding rules determine what those results mean. Percentile rolls, single-die targets, dice pools, step dice, advantage systems, cards, and other familiar structures are tools rather than markers of originality. Finite decks add an important axis because draws can change later odds, and a card can function simultaneously as randomizer, result, and rules payload. Mature design often innovates through integration, application, presentation, or refinement rather than by inventing a new way to generate uncertainty.
