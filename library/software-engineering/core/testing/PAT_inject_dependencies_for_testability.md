---
object_id: PAT_inject_dependencies_for_testability
object_type: pattern
name: Inject Dependencies to Make Code Testable
library_path:
- software-engineering
- core
- testing
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- unit_testing
- dependency_injection
- test_doubles
- testability
cross_links:
- rel: related_to
  target_object_id: PAT_use_dependency_injection
- rel: related_to
  target_object_id: PAT_design_for_testability
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Inject Dependencies to Make Code Testable

## Pattern Rule
**IF** a class constructs its own dependencies internally, making it impossible for a test to substitute test doubles
**THEN** inject those dependencies through the constructor, so tests can supply fakes while real callers still get real dependencies via a factory.

## Do
- Take dependencies as constructor parameters: an invoice reminder that receives its address book and email sender can be tested, where one that builds them itself cannot.
- Keep easy real-world construction with a static factory that wires the real dependencies, so injection does not burden ordinary callers.
- Let tests pass doubles: with injection, a test constructs the class with a fake address book and fake email sender, avoiding real customer data and real emails.

## Don't
- Don't hard-code dependency construction in the constructor; a class that builds a real database-backed address book and a real email sender cannot be tested without hitting the database and sending real emails.
- Don't conclude a behavior is untestable when the real fix is to make its dependencies injectable.

## Checklist
- Can a test construct this class with test doubles in place of its real dependencies?
- Are dependencies supplied from outside rather than created inside the constructor?
- Is there still a factory so real callers construct it easily?

## Notes
Testability is the fourth reason to use dependency injection, alongside the modularity motives of earlier chapters. Long's `InvoiceReminder` that calls a data store and instantiates a real email sender is effectively untestable — tests would touch real customer data and send real emails, and often lack database permissions. Injecting the address book and email sender lets tests supply fakes, which is why the chapter frames testability as tightly related to the modularity that dependency injection provides.
