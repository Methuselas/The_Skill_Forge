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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Don't Leak Implementation Details in Exceptions

## Pattern Rule
**IF** a layer can propagate an error raised by a lower layer — thrown or returned — that a caller might want to recover from
**THEN** translate it into a failure appropriate to this layer — an exception type where the language has them, this layer's own error value where it does not — preserving the original as the cause either way, rather than letting an implementation-specific failure escape through your interface.

## Do
- Define an error type for your layer and wrap lower-layer errors in it: a text summarizer should throw a `TextSummarizerException` that wraps whatever a scorer threw, so callers handle one predictable error type.
- Let the interface dictate the error types of the layer: declare the scorer interface's method as throwing a `TextImportanceScorerException`, so every implementation conforms and no implementation-specific exception leaks.
- Publish the small set of failures callers are allowed to branch on, as values this layer defines and names. That set is the contract: a caller testing for this layer's own not-found or out-of-order condition keeps working across any reimplementation, because the thing it names belongs to the interface rather than to whatever currently sits behind it. Without such a set a caller who needs to distinguish two failures has no supported way to do it and will reach past you for one that is not supported.
- Treat an attached cause as diagnostic rather than contractual, and say so. Wrapping does not hide the inner failure in any language whose cause chain can be inspected at run time, and most can be — the chain is exactly as reachable to a caller's branching as an unwrapped error was. Wrapping converts an unavoidable leak into a documented one; it does not close it. What closes it is having published an alternative worth using, so the supported answer is easier to reach than unwrapping.
- Attach a cause only where there is one. A layer originates a large share of its own failures — an unsupported option, a count that disagrees with itself, a value outside the range this layer defines — and those have nothing beneath them to preserve. Reading the wrap rule as universal produces either an invented cause or a chain repeating one condition at every level.
- Prefer an explicit signaling technique (checked exception, result, outcome) so the layer-appropriate error type is enforced rather than merely documented.

## Don't
- Don't let an implementation's exception surface through a higher layer; a caller catching a `PredictionModelException` from a summarizer has learned it uses a model, and their catch breaks the moment a different scorer implementation is configured.
- Don't rely on unchecked exceptions to carry cross-layer errors silently; unmentioned in the contract, they leak implementation details especially easily.

## Checklist
- Does any exception escaping this class name a lower layer's implementation?
- Would a caller's error handling still work if you swapped the internal implementation?
- Is the layer's error type enforced by the interface, or left to each implementation's whim?
- Which failures may a caller branch on, and are they named by this layer rather than
  reached by unwrapping to something underneath it?
- Does this failure have an underlying cause at all, or did this layer originate it?

## Notes
Wrapping is necessary here and is not sufficient, and the gap between those two is where
this card is most often applied and still defeated. The reasoning that fails is that
putting a lower error inside your own type has contained it, when a cause chain that any
caller can walk leaves the inner failure exactly as reachable as before — now with a
documented route to it. A caller who needs to tell two failures apart, and who has been
given no vocabulary of yours for doing so, will find the inner one and branch on it, and
the coupling the card warns about is back with the wrapping still in place. The wrap
governs what escapes by default; it settles nothing about what a determined caller can
still depend on.

What actually closes it is supplying the thing that caller needed. A layer that names its
own small set of branchable failures gives the supported answer, and the supported answer
being available is what makes reaching past it rare rather than routine. The two halves
work together: the named set is the contract and stays stable across reimplementation, and
the chain underneath carries whatever a human needs when reading a log, which is a real
job and a different one. Marking the chain as diagnostic is worth doing explicitly, because
nothing in the language distinguishes a cause that is part of the interface from one that
happens to be visible, and a caller cannot tell which you meant.

Exceptions are the sneakier leak because unchecked ones sit in the small print or nowhere at all. Long's `TextSummarizer` leaking a `PredictionModelException` couples callers to the model implementation and makes their catch fragile against reconfiguration; wrapping lower-layer errors into a `TextSummarizerException` (with the interface declaring a `TextImportanceScorerException`) gives callers one stable error type. It is the return-type leak rule applied to the error channel, and it leans on chapter 4's explicit-signaling techniques to make the layer-appropriate type enforceable.
