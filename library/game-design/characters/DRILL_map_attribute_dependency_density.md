---
object_id: DRILL_map_attribute_dependency_density
object_type: drill
name: Map Attribute Dependency Density
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
- attributes
- balance
- dependencies
- optimization
- cadence
cross_links:
- rel: supports
  target_object_id: PAT_price_character_options_by_mechanical_leverage_and_constraint
- rel: related_to
  target_object_id: DRILL_trace_a_character_option_into_play
- rel: related_to
  target_object_id: PAT_keep_persistent_capability_dependencies_local_and_explicit
reference:
  source_title: Cyberpunk 2020 (2.0.2.0 Version)
  author: Mike Pondsmith and R. Talsorian Games contributors
confidence: high
references: []
variants: []
target_skill: Detect attributes whose value compounds through many high-cadence downstream systems even when the attribute bonus itself looks ordinary.
---

# Map Attribute Dependency Density

## Practice Task
Build a dependency graph for every broad attribute or foundational rating in one playable character architecture, then compare the marginal value of increasing each attribute by one step.

## Target Skill
Detect attributes whose value compounds through many high-cadence downstream systems even when the attribute bonus itself looks ordinary.

## Setup
Use a complete representative character sheet and the rules that derive skills, initiative, offense, defense, movement, resistance, resource pools, advancement currency, defaults, and other persistent values. Include at least one optimized and one non-optimized build.

## Instructions
1. List every direct task family that uses each attribute.
2. Add every derived value the attribute changes: initiative, **action quantity**, damage, defense, movement, resource generation, starting skill budget, advancement efficiency, thresholds, or other persistent state.
3. Mark each dependency by expected cadence and consequence. A dependency used every combat round weighs differently from one used once per campaign.
4. Mark multiplicative dependencies separately from additive ones. If an attribute increases the number of times full downstream procedures can be invoked, trace the multiplied attacks, defenses, state writes, and spotlight cost rather than recording only the initiative bonus.
5. Mark feedback loops. Note when acting first improves the chance to wound an opponent, which then reduces the opponent's future initiative or competence, or when one attribute also lowers future costs for skills that use the same attribute.
6. Mark **double-leverage dependencies** where one rating controls both resource capacity and spend potency, both a fixed bonus and the size of its random component, or both a specialist ceiling and the breadth/strength of options beneath that ceiling.
7. Record any free build resources, derived pools, caps, or advancement efficiencies generated from the attribute rather than only tests that roll it.
8. Compare a one-step increase in each attribute against representative narrower purchases that could produce similar outcomes.
9. Repeat the graph for at least two campaign ecologies, such as combat-heavy and social/investigative play, to expose environment-dependent value.
10. Identify counterweights such as encumbrance penalties, hard skill gates, opportunity costs, caps, resource dilution, or competing resources and test whether they materially reduce the leverage.

## Success Check
- Every foundational attribute has a named downstream dependency set rather than a skill-count total alone.
- Cadence and consequence are recorded for the major dependencies.
- At least one indirect or feedback dependency is included.
- Any action-quantity dependency is expanded through its downstream procedures rather than counted as one ordinary edge.
- An attribute with many low-value dependencies is distinguished from one with fewer but high-cadence/high-consequence dependencies.
- At least one counterweight is tested rather than merely listed.
- The final judgment distinguishes **optimization bottleneck** from **broken attribute**; high value alone does not prove failure.

## Common Failures
- Counting the number of linked skills while ignoring initiative, derived resources, advancement, or feedback loops.
- Calling two attributes equal because they share the same numeric range.
- Treating a campaign-specific dominance result as universal across all campaign ecologies.
- Ignoring skill gates or other costs that prevent the broad attribute from substituting for training.

## Notes
Attribute balance is a graph problem. Count resource-generation and ceiling effects as first-class dependencies: a rating that both creates more uses and makes each use stronger, or that both sets a specialist ceiling and improves the tests below it, can compound faster than a raw skill-link count suggests. The useful diagnostic is not raw bonus size but **dependency density × cadence × consequence**, adjusted for feedback and counterpressure. Action quantity is a multiplier edge because each extra action can invoke whole downstream procedures, and advancement economics can create another hidden edge when a broad attribute also lowers the future cost of linked expertise. A modest-looking attribute can dominate optimization when it simultaneously improves sequencing, action count, competence, resource generation, and the ability to exploit the first successful action.
