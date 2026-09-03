---
object_id: DRILL_replace_hard_coded_dependency_with_injection
object_type: drill
name: Replace a Hard-Coded Dependency With Injection
library_path:
- software-engineering
- core
- modularity
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- dependency_injection
- modularity
- refactoring
- interfaces
cross_links:
- rel: teaches
  target_object_id: PAT_use_dependency_injection
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: converting a hard-coded concrete dependency into an injected interface dependency
references: []
variants: []
---

# Replace a Hard-Coded Dependency With Injection

## Practice Task
Take a class that constructs a concrete dependency internally and refactor it to inject that dependency as an interface, then keep construction easy with a factory.

## Target Skill
Turning a hard-coded, unconfigurable dependency into an injected, interface-typed one.

## Setup
No special setup required.

## Instructions
1. Start from a class that builds a specific implementation in its constructor — a route planner that constructs a North America road map.
2. Note what the hard-coding prevents: using the class in any other region, and swapping the dependency in a test.
3. Change the constructor to accept the dependency as a parameter, typed as the interface it implements (a road map), and store that. Name a second implementation of that interface concretely, even if you do not write it.
4. Search the class for any surviving mention of a concrete implementation, including inside its methods, and state the search you ran.
5. Add a factory function that constructs the class with a sensible default implementation, so the common case stays a one-liner. Confirm it is not the only route to construction.
6. Construct the class with a different implementation and exercise it.
7. Write a test that supplies a fake and asserts on something the fake makes observable.

## Success Check
- The class is searched for any surviving mention of a concrete implementation and the search is stated. A constructor cleaned while a method still builds one directly passes a reading of the constructor.
- The parameter is typed as the interface, and a second implementation is named concretely even if it is not written. An interface with exactly one implementation forever is a rename, and saying so is part of passing rather than an admission of failure.
- The class is actually constructed with a different implementation and exercised. That it could be is the claim under test.
- The factory is checked against the defect it invites: it must not become the only route to construction, or the concrete dependency has moved out one level while every caller still receives it with no way to say otherwise.
- A test supplies a fake and asserts on something the fake makes observable, so injectability is demonstrated by use rather than by shape.

## Common Failures
- Injecting the concrete class instead of its interface, which restores construction flexibility but not reconfiguration.
- Leaving the dependency as static functions, which cannot be injected at all.

## Notes
This drills Long's `RoutePlanner`/`RoadMap` refactor. The habit is to treat a `new ConcreteThing()` inside a constructor as a modularity smell, and to lift it out to an injected interface — which simultaneously unlocks reconfiguration and test doubles.
