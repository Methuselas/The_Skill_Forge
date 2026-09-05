---
object_id: PAT_agree_on_a_small_set_of_name_molds
object_type: pattern
name: Agree on a Few Name Molds and Reuse Them
library_path:
- software-engineering
- core
- readability
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- conventions
- consistency
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_invest_in_names_early_in_a_project
- rel: related_to
  target_object_id: PAT_follow_a_consistent_coding_style
- rel: supports
  target_object_id: AP_choose_a_name_with_feitelsons_three_steps
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants:
- variant_id: VAR_take_the_molds_off_the_shelf
  variant_name: Take the Molds Off the Shelf Instead of Deriving Them
  variant_basis: method_sequence
  difference_from_foundation: The foundation supplies a process — find the molds already in the codebase, agree a small set, keep the key concept in a predictable slot — and deliberately leaves the content local. This variant supplies the content, a set of prescribed molds that work across projects. Computed-value qualifiers go at the end, so `revenueTotal` and `expenseAverage` rather than `totalRevenue` and `averageExpense`; the most meaningful part of the name then sits at the front where it is read first, and a set of such names acquires a symmetry that a mixed set does not. `Num` is retired on both ends because it means a total at the front and an index at the back, replaced by `Count` for the total and `Index` for the position. Opposites are drawn from a fixed list — begin/end, first/last, locked/unlocked, min/max, next/previous, old/new, opened/closed, visible/invisible, source/target, source/destination, up/down — because pairs that depart from common-language opposites are hard to remember. And boundary words are given exact, non-overlapping meanings, which is where the payoff concentrates — `first` and `last` are relative to the operation in hand, `min` and `max` to the container itself, and `lim` is a noninclusive upper bound equal to `last` plus one and never a valid index.
  when_to_use: Use when starting fresh, when the existing molds are inconsistent enough that there is nothing to standardise on, or when a team is spending real time negotiating conventions that carry no local stakes. The boundary vocabulary is worth taking on its own even in a codebase with settled molds elsewhere, because ambiguity about whether a bound is inclusive is where off-by-one defects live, and a name that fixes it removes the ambiguity at every use site.
  when_not_to_use: Do not import these over molds a codebase already uses consistently — the foundation is right that standardising on what is there beats introducing a better scheme, since the gain is consistency rather than the particular choice. The specific vocabulary is also of its period, and a project whose language or libraries have already settled a boundary convention should adopt that convention rather than a second one alongside it.
  absorbed_from_object_id: none
---

# Agree on a Few Name Molds and Reuse Them

## Pattern Rule
**IF** a codebase names many values that share a shape — a maximum of something, a count of something per period
**THEN** agree on a small set of name molds and put every such name into one of them, because the cost of mixed molds is paid on every read, not on the one occasion the name is written.

## Do
- Recognise the mold as the thing being chosen. For "the maximum benefit per month," Feitelson's participants produced `max_benefit`, `max_benefit_per_month`, `max_monthly_benefit`, `benefits_per_month`, `max_num_of_benefit`, `benefit_max_num`, `monthly_benefit_limit` and more — all conceptually the same value, differing only in mold.
- Keep the key concept in a predictable position. Hunting for `benefit` in a different slot each time is extraneous cognitive load, and the energy spent locating the concept is not available for understanding it.
- Choose molds so that similar values end up with similar names. `max_benefit_amount` will remind you of `max_interest_amount`; it will not remind you of `interest_maximum`, even when the calculation is the same.
- On an existing codebase, extract the current variable names first, see which molds are already in use, and standardise on those rather than importing new ones.
- On a new project, agree the molds up front — this is one of the concrete decisions the early-naming pattern is asking you to make.

## Don't
- Don't treat mold variation as harmless stylistic freedom. It is the main reason two developers rarely pick the same name, and within one codebase it costs the same retrieval effort repeatedly.
- Don't try to enumerate every mold. The point is a limited number, and a long approved list reproduces the problem it was meant to solve.
- Don't standardise a mold that reads backwards in the project's natural language — see the ordering consideration in the naming action plan.

## Checklist
- What mold does this name use, and is that mold already established here?
- Is the central concept in the same position it occupies in neighbouring names?
- Would a similar value elsewhere in the codebase produce a name that looks like this one?

## Notes
Name molds are Feitelson's term for the patterns in which elements of a name are typically combined. Fourteen molds were recorded among his participants for a single value, ordered most to least chosen, and normalised so that `max`/`maximum` and `benefit`/`benefits` count as the same element — which means the fourteen are genuine structural differences, not vocabulary differences.

`VAR_take_the_molds_off_the_shelf` fills in the content this card deliberately leaves open. Hermans says agree on molds and does not say which; McConnell prescribes a set — qualifiers such as Total, Sum, Average, Max and Min at the end of the name rather than the front, `Count` and `Index` in place of the ambiguous `Num`, opposites drawn from a fixed list of common-language pairs, and boundary words given exact meanings. The two do not conflict so much as answer different questions, and the ordering between them is the useful part: where a codebase already has consistent molds, the foundation wins and you standardise on what is there, because consistency is the benefit and the particular choice mostly is not. Where there is nothing to standardise on, a prescribed set saves a negotiation with no local stakes.

The boundary vocabulary is the piece worth taking even into a codebase with settled molds. `first` and `last` describe the elements this operation must deal with; `min` and `max` describe the absolute ends of the container itself; `lim` is a noninclusive upper bound, generally `last` plus one, and never a legal index. Most code uses two or three of these words interchangeably, and the ambiguity about whether a bound is inclusive is precisely where off-by-one defects come from — so this is a mold decision that buys correctness rather than only readability. A project whose language or standard library has already fixed a convention should follow that one instead; what matters is that the question has a settled answer, not that this vocabulary supplies it.

The two cognitive arguments are separate and both hold. Mold consistency lowers extraneous load, by putting the concept where the reader's eye already is. It also improves LTM retrieval, by making similar values produce similar names so that one reminds you of the other. Hermans is careful that no studies have been run on molds specifically, and reasons by analogy from the camel-case training results — people get better at recognising the styles they see often — so the mechanism is inference from adjacent evidence rather than a direct finding.
