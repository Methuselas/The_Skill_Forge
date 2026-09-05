---
object_id: PAT_use_dependency_injection
object_type: pattern
name: Inject Dependencies Instead of Hard-Coding Them
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
- dependency_injection
- modularity
- configurability
- testability
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
- rel: related_to
  target_object_id: AP_refactor_monolithic_class_into_layers
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Inject Dependencies Instead of Hard-Coding Them

## Pattern Rule
**IF** a class, module, or function depends on something that could have alternative implementations
**THEN** hand that dependency in from outside instead of constructing a specific implementation inside — through the constructor where there is one, otherwise as a parameter or as a table of function pointers supplied at creation — so it can be reconfigured with any implementation.

## Do
- Take the dependency as a constructor parameter: a `RoutePlanner` given a `RoadMap` can plan routes anywhere, where one that builds a `NorthAmericaRoadMap` internally is useless outside North America.
- Keep the easy-construction convenience with factory functions (or a dependency injection framework) that supply sensible defaults, so the default case stays a one-liner while other cases stay possible.
- Write reconfigurable subproblems as instantiable objects, not static functions; static functions cannot be injected and block test doubles (static cling), whereas an injected instance can be swapped in tests.

## Don't
- Don't construct a concrete dependency in the constructor; that hard-codes not only the implementation but its configuration, forcing arbitrary choices (online map, no seasonal roads) onto every user.
- Don't lean on a dependency injection framework without care; misconfigured, it makes it hard to tell which configuration applies where.

## Checklist
- Is each swappable dependency supplied from outside rather than built inside?
- Can a caller construct the class with an alternative implementation for a different use case or a test?
- Is a default configuration still available through a factory so construction stays easy?

## Notes
Dependency injection is the foundational modularity move and the mechanism the refactoring AP previewed. The `RoutePlanner`/`RoadMap` example shows both the win (any region's map works) and the cost it manages (construction gets harder, softened by factory functions). The static-function trap is the subtle failure: writing the road map as static methods makes injection impossible even in hindsight, which is why designing for injectability — instantiable classes behind interfaces — matters before the need arises.
