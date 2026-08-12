---
object_id: PAT_dont_leak_implementation_details_in_exceptions
object_type: pattern
name: Don't Leak Implementation Details in Exceptions
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
- abstraction
- modularity
- exceptions
- error_handling
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_explicit_error_signaling_for_recoverable_errors
- rel: related_to
  target_object_id: PAT_dont_leak_implementation_details_in_return_types
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u08, pp. 234-239
  evidence_type: text
confidence: high
references: []
variants: []
---

# Don't Leak Implementation Details in Exceptions

## Pattern Rule
**IF** a layer can propagate an error thrown by a lower layer that a caller might want to recover from
**THEN** wrap it in an exception type appropriate to this layer — preserving the original as the cause — rather than letting an implementation-specific exception escape through your interface.

## Do
- Define an error type for your layer and wrap lower-layer errors in it: a text summarizer should throw a `TextSummarizerException` that wraps whatever a scorer threw, so callers handle one predictable error type.
- Let the interface dictate the error types of the layer: declare the scorer interface's method as throwing a `TextImportanceScorerException`, so every implementation conforms and no implementation-specific exception leaks.
- Prefer an explicit signaling technique (checked exception, result, outcome) so the layer-appropriate error type is enforced rather than merely documented.

## Don't
- Don't let an implementation's exception surface through a higher layer; a caller catching a `PredictionModelException` from a summarizer has learned it uses a model, and their catch breaks the moment a different scorer implementation is configured.
- Don't rely on unchecked exceptions to carry cross-layer errors silently; unmentioned in the contract, they leak implementation details especially easily.

## Checklist
- Does any exception escaping this class name a lower layer's implementation?
- Would a caller's error handling still work if you swapped the internal implementation?
- Is the layer's error type enforced by the interface, or left to each implementation's whim?

## Notes
Exceptions are the sneakier leak because unchecked ones sit in the small print or nowhere at all. Long's `TextSummarizer` leaking a `PredictionModelException` couples callers to the model implementation and makes their catch fragile against reconfiguration; wrapping lower-layer errors into a `TextSummarizerException` (with the interface declaring a `TextImportanceScorerException`) gives callers one stable error type. It is the return-type leak rule applied to the error channel, and it leans on chapter 4's explicit-signaling techniques to make the layer-appropriate type enforceable.
