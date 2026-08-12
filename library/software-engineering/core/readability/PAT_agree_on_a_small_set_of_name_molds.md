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
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u08, pp. 142-144
  evidence_type: mixed
confidence: high
references: []
variants: []
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
Name molds are Feitelson's term for the patterns in which elements of a name are typically combined. Table 8.4 lists fourteen molds his participants used for a single value, ordered most to least chosen, and normalised so that `max`/`maximum` and `benefit`/`benefits` count as the same element — which means the fourteen are genuine structural differences, not vocabulary differences.

The two cognitive arguments are separate and both hold. Mold consistency lowers extraneous load, by putting the concept where the reader's eye already is. It also improves LTM retrieval, by making similar values produce similar names so that one reminds you of the other. Hermans is careful that no studies have been run on molds specifically, and reasons by analogy from the camel-case training results — people get better at recognising the styles they see often — so the mechanism is inference from adjacent evidence rather than a direct finding.
