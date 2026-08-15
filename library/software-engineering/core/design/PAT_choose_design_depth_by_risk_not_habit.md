---
object_id: PAT_choose_design_depth_by_risk_not_habit
object_type: pattern
name: Design Deepest Where the Work Looks Easiest
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- design
- planning
- risk
- documentation
cross_links:
- rel: related_to
  target_object_id: PAT_settle_load_bearing_decisions_before_finishes
- rel: related_to
  target_object_id: PAT_scale_formality_to_the_kind_of_software
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u05, pp. 106, 112, 115-117
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Design Deepest Where the Work Looks Easiest

## Pattern Rule
**IF** you are deciding how far to take a design before writing code
**THEN** go deeper than feels necessary on the parts that look easy, because the worst design failures come from areas judged simple enough to skip designing rather than from hard areas designed badly.
**ELSE** stop designing when the work descends to a task you have done before, or to a simple modification or extension of one.

## Do
- Decompose until coding the next level looks easier than decomposing it. Work until the design seems obvious to the point of impatience — if it is even slightly tricky for you now, it will be brutal for whoever meets it later.
- Set detail and formality as two independent dials, not one. An inexperienced team needs *medium-to-high* design detail but only *low-to-medium* documentation formality; a safety-critical application needs high on both; a small project or short-lived software needs low on both. Reading them as one dial is what produces heavily documented shallow designs.
- Weigh the factors against each other when they disagree, and err upward. An experienced team building safety-critical software should take the higher detail and formality, not average the two.
- Spend the effort on alternatives rather than on polish. Roughly 80 percent into creating and exploring design options and 20 percent into less polished documentation beats the reverse — mediocre alternatives written up beautifully.
- Enumerate how the thing could fail, rather than copying what has succeeded. Spectacular bridge failures came from attending to previous successes and not considering failure modes; the same reasoning applies directly to the security lapses of well-known systems.

## Don't
- Don't assume the areas you find difficult are where the risk is. The reverse is the documented pattern: problems arise from areas thought easy and therefore never designed at all.
- Don't rush the design so that time remains to fix the defects the rush caused. That trade is the one Myers named, and it does not pay.
- Don't polish a design description prematurely. Programmed activity drives out unprogrammed activity, so formatting work will quietly consume the thinking time it was supposed to record.
- Don't confuse a large document with a designed system. Nobody reads seventeen thousand pages, and projects suffering from too much design documentation are far rarer than projects suffering from too little design.

## Checklist
- Which parts of this did you skip designing because they looked obvious?
- Are detail and formality set separately, and can you say why each is where it is?
- For each part: what does failure look like, and did you design against it or around a past success?
- Is the design at the point where coding the next step is easier than decomposing it?
- What fraction of your effort so far went into alternatives versus into writing them up?

## Notes
The counterintuitive core is worth stating plainly because it inverts the natural allocation of attention. Effort flows toward what feels hard, and what feels hard has already been recognised as risky — so it gets designed, reviewed, and usually survives. The parts that feel easy get no design at all, and a wrong assumption there is discovered only in code, where it is far more expensive. Depth should therefore be allocated against *unrecognised* risk, which means deliberately spending some of it where your instinct says it is unnecessary.

McConnell's factor table is the calibration, and its useful surprise is the decoupling of the two dials. Team inexperience raises the need for design detail while *lowering* the need for documentation formality — the inexperienced team needs to have thought the thing through, not to have produced artifacts about it. Turnover raises detail with no formality recommendation at all. Safety-critical work is the only row where both go high together.

Top-down and bottom-up are not competing strategies here but two ways of reaching the required depth, and each has a failure mode worth knowing. Top-down starts easy but low-level complexity can ripple back up and make things more complicated than they needed to be. Bottom-up starts hard but surfaces that complexity early, which produces better high-level classes — unless the complexity sinks the design first. You cannot build an airplane from bricks, so sometimes the top must be settled before the pieces make sense.
