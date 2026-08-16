---
object_id: DRILL_replace_inheritance_with_composition
object_type: drill
name: Replace Inheritance With Composition
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
- composition
- inheritance
- refactoring
- interfaces
cross_links:
- rel: teaches
  target_object_id: PAT_prefer_composition_over_inheritance
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: converting an inheritance-for-reuse relationship into composition over an interface
references: []
variants: []
---

# Replace Inheritance With Composition

## Practice Task
Take a class that extends another purely to reuse it, and refactor it to compose an injected interface instead, then compare the public APIs.

## Target Skill
Recognizing inheritance-for-reuse and converting it to composition over an interface.

## Setup
No special setup required.

## Instructions
1. Start from a subclass that extends a utility class to reuse it — an integer reader extending a comma-separated file handler.
2. Write out the subclass's effective public API, including everything inherited, and note the strange functions it exposes (reading raw strings, writing values).
3. Identify the interface that captures only what you need from the superclass (a file value reader).
4. Refactor: have the class hold an injected instance of that interface instead of extending the class, and forward only the functions callers need (such as close).
5. Support a sibling requirement — a semicolon-separated format — by injecting a different implementation, and confirm no duplicate class was needed.

## Success Check
- The class's public API exposes only its own functions, not the whole superclass.
- The reused functionality is held as an injected interface and forwarded selectively.
- A new file format is supported by a different injected implementation, with no duplicated subclass.

## Common Failures
- Composing the concrete class instead of its interface, losing the reconfiguration benefit.
- Forwarding every function reflexively, which re-leaks the API composition was meant to hide.

## Notes
This drills Long's `IntFileReader` refactor from extending `CsvFileHandler` to composing a `FileValueReader`. The lesson is that inheritance couples you to a whole class and its API, while composition over an interface reuses just what you need and stays reconfigurable — reserve inheritance for genuine is-a relationships, and even then weigh its hazards.
