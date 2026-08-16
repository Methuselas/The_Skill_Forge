---
object_id: PAT_never_let_exceptions_leave_a_destructor
object_type: pattern
name: Never Let Exceptions Escape a Destructor
library_path:
- software-engineering
- languages
- cpp
- destructors
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- destructors
- exceptions
- resource_management
cross_links:
- rel: related_to
  target_object_id: PAT_dont_hide_errors
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Never Let Exceptions Escape a Destructor

## Pattern Rule
**IF** a destructor performs an operation that might throw — closing a connection, flushing a buffer
**THEN** catch the exception inside the destructor and either swallow it or abort, and better still give clients a normal function that performs the operation so they can handle failure themselves.

## Do
- Wrap the risky call in a try/catch inside the destructor; log and call abort to forestall undefined behavior, or log and swallow when the program can safely continue.
- Provide a normal function such as `close` that does the work and reports errors, keeping a backup call in the destructor for clients who do not invoke it.

## Don't
- Don't let an exception propagate out of a destructor: during stack unwinding a second active exception is one too many, and the program terminates or becomes undefined.

## Checklist
- Can anything this destructor calls throw, and if so is it caught so nothing escapes?
- Is there a non-destructor function clients can call to handle the failure themselves?

## Notes
When a container of objects is destroyed and two destructors throw during the same unwinding, C++ has two simultaneously active exceptions and terminates. So a destructor must contain any exception. Swallowing and aborting both discard the client's chance to react, which is why the better design exposes a normal `close`-style function (the `DBConn`/`DBConnection` example) and keeps the destructor call only as a backup — this cooperates with the general rule against hiding errors rather than violating it.
