---
object_id: PAT_use_maintenance_to_trade_present_effort_for_future_reliability
object_type: pattern
name: Use Maintenance to Trade Present Effort for Future Reliability
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
- maintenance
- reliability
- risk
- downtime
- resources
- equipment
cross_links:
- rel: related_to
  target_object_id: PAT_use_time_to_structure_opportunity
- rel: related_to
  target_object_id: PAT_compress_resource_contents_without_erasing_resource_constraints
reference:
  source_title: "Twilight: 2000 (1st Edition) and Twilight: 2000 Version 2.2"
  author: "Frank Chadwick; David Nilsen, Loren Wiseman, and Lester Smith"
confidence: high
references: []
variants: []
---

# Use Maintenance to Trade Present Effort for Future Reliability

## Pattern Rule
**IF** equipment wear or neglect is meant to create planning rather than merely punish ownership
**THEN** let players trade present time, labor, tools, or parts for reduced future failure risk while retaining the option to defer maintenance and accept that risk
**ELSE** omit routine maintenance when it does not alter future reliability or other decisions.

## Do
- Make maintenance change future breakdown probability, severity, warning state, or another reliability variable the players can plan around.
- Allow prudent extra maintenance to buy additional reliability when downtime itself is scarce and valuable.
- Let neglected equipment continue operating when plausible so the choice becomes push now versus pay risk later.
- Use warning states to create stop-or-continue decisions before total failure.
- Connect maintenance to the same time, labor, tools, parts, and mobility economy used elsewhere rather than isolating it as a separate tax.

## Don't
- Require maintenance as pure ritual bookkeeping with no change to future risk.
- Make equipment fail automatically the instant a maintenance interval is missed when the intended play is risk management.
- Hide the reliability consequence so completely that players cannot make informed tradeoffs.
- Add component-level maintenance state when one aggregate wear state already produces the intended decisions.

## Checklist
- Performing maintenance measurably changes a future risk or capability.
- Skipping maintenance remains a legal choice with a legible consequence.
- At least one competing use of the same time, labor, tools, or parts makes the maintenance decision nontrivial.
- Warning or degradation state can create a meaningful push-versus-stop decision when appropriate.
- Tracking depth is no finer than the reliability decisions require.

## Notes
Maintenance becomes gameplay when it is a reliability investment rather than a periodic fee. The key choice is not whether the owner remembered to tick a box; it is whether spending scarce effort now is worth the reduction in future failure risk. This works especially well when safe downtime is itself valuable and when pushing damaged or neglected equipment may preserve immediate mobility at the cost of later breakdown.
