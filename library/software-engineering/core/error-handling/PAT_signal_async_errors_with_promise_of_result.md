---
object_id: PAT_signal_async_errors_with_promise_of_result
object_type: pattern
name: Make Async Error Signaling Explicit With a Promise of a Result
library_path:
- software-engineering
- core
- error-handling
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- async
- promises
- result_type
- error_handling
cross_links:
- rel: related_to
  target_object_id: PAT_return_result_type_to_convey_error_cause
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: medium
references: []
variants: []
---

# Make Async Error Signaling Explicit With a Promise of a Result

## Pattern Rule
**IF** you return a promise or future from an asynchronous function and it can carry an error
**THEN** recognize that a bare promise signals the error implicitly, and if you want it explicit, return a promise of a result type so the error possibility is visible in the return type.

## Do
- Understand the implicit default: a consumer can attach only a fulfilled-path callback (a promise's `then`) and never realize a rejection is possible, leaving the error to a higher handler or unnoticed entirely.
- Make it explicit by wrapping the payload — return a promise of a result-of-value-or-error — so a caller reading the type sees both the async nature and the error possibility.
- Accept the tradeoff consciously: the promise-of-result return type is clunkier to read and write, and not everyone finds it worth it.

## Don't
- Don't assume returning a plain promise makes callers aware of failure; knowing a rejection can happen requires reading the small print or the implementation.
- Don't leave an important recoverable async error implicit when callers must handle it — pay the clunkiness for the explicit signal.

## Checklist
- Can a consumer tell from the return type that the async operation might fail?
- If they only handle the success path, will the error surface or vanish?
- Have you judged whether the explicit promise-of-result is worth its added clumsiness here?

## Notes
Promises and futures are excellent for returning values from async work but poor at advertising errors: rejection is invisible unless the consumer already knows to add a rejection callback, which makes the plain promise an implicit technique. Long's remedy applies the same explicit/implicit logic as the synchronous case — wrap the value in a result type — while being candid that the resulting return type is verbose enough that reasonable engineers decline it. Use it when the async error is recoverable and must not be missed.
