---
object_id: PAT_depend_on_interfaces_not_concrete_classes
object_type: pattern
name: Depend on Interfaces, Not Concrete Classes
library_path:
- software-engineering
- core
- modularity
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- interfaces
- dependency_inversion
- modularity
- adaptability
cross_links:
- rel: related_to
  target_object_id: PAT_use_interfaces_for_swappable_layers
- rel: related_to
  target_object_id: PAT_use_dependency_injection
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u08, pp. 213-215
  evidence_type: text
confidence: high
references: []
variants: []
---

# Depend on Interfaces, Not Concrete Classes

## Pattern Rule
**IF** you depend on a class that implements an interface, and that interface captures the functionality you actually need
**THEN** declare the dependency on the interface rather than the concrete class, so any implementation of it can be supplied.

## Do
- Type the dependency as the abstraction: a `RoutePlanner` that holds a `RoadMap` interface accepts every regional map, where one that holds a `NorthAmericaRoadMap` accepts only that one.
- Treat depending on the interface as the payoff of injection — injecting a concrete class still hides its construction, but only depending on the interface unlocks reconfiguration.
- Read an implemented interface that captures what you need as a strong hint that other engineers will want to supply different implementations.

## Don't
- Don't depend directly on a concrete implementation when an interface would do; it needlessly ties your code to one solution and forfeits adaptability.
- Don't assume the interface costs effort — depending on it is rarely more work than depending on the class, for a large gain in modularity.

## Checklist
- Does your field or parameter type name an interface or a concrete class?
- Would swapping in a different implementation require editing this class?
- Does the interface you depend on expose only what you need from the dependency?

## Notes
This is the dependency inversion principle — depend on abstractions, not concretions — applied to everyday code, and it is what makes injection pay off. Long contrasts a `RoutePlanner` depending on the `RoadMap` interface with one depending on `NorthAmericaRoadMap`: both inject, but only the interface version works with a European map. It builds directly on chapter 2's advice to define an interface whenever a subproblem has more than one plausible solution; here the rule is to then depend on that interface rather than any one class behind it.
