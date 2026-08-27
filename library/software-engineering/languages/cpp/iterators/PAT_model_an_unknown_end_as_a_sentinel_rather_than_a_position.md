---
object_id: PAT_model_an_unknown_end_as_a_sentinel_rather_than_a_position
object_type: pattern
name: Model an Unknown End as a Sentinel Rather Than a Position
library_path:
- software-engineering
- languages
- cpp
- iterators
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- iterators
- sentinel
- streams
cross_links:
- rel: related_to
  target_object_id: PAT_publish_the_traits_an_iterator_claims_not_just_its_operators
- rel: related_to
  target_object_id: PAT_read_characters_with_a_streambuf_iterator_not_a_formatted_one
- rel: related_to
  target_object_id: PAT_choose_index_types_the_compiler_can_assume_do_not_wrap
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Model an Unknown End as a Sentinel Rather Than a Position

## Pattern Rule
**IF** a sequence ends on a condition discovered while traversing it rather than at a position known beforehand — a stream that runs dry, a buffer closed by a terminator, a series computed until some count is reached
**THEN** represent the end as a sentinel that the traversing position is compared against, rather than as an end position you must produce before iterating
**ELSE** where the extent is known up front, an ordinary end position is simpler and supports arithmetic that a sentinel cannot.

## Do
- Notice when producing an end position would cost the traversal you were about to perform. Finding a buffer's terminator means walking to it, so computing the end first walks the sequence twice; for a stream it is worse, because the end cannot be known without consuming the stream, and consuming it is the thing you were trying to do.
- Let the comparison test the position's own state rather than compare two positions. The sentinel frequently needs to carry nothing at all — the question is whether this position has hit the terminator, exhausted the stream, or reached its count, and that is answerable from the position alone.
- Allow the sentinel to be a different type from the position. It is not a place in the sequence and does not need to behave like one; its whole obligation is to be comparable with the thing traversing, and freeing it from being the same type is what lets it be a plain value or an empty type.
- Reach for it when a type has no underlying container to point into. A generated series has no storage and therefore no last element to address, so an end position would have to be invented; a sentinel gives the traversal a place to stop without inventing one.
- Keep the comparison free of side effects even though it is testing a live condition. It will be evaluated once per step and may be evaluated more than the loop's shape suggests, so a comparison that consumes input or advances state produces a traversal that skips or loops depending on how it was called.

## Don't
- Don't reach for it when the extent is known. A sentinel gives up distance arithmetic and the ability to work backwards from the end, and where the length was available all along that is a loss for nothing.
- Don't expect to compute a distance by subtracting it. It marks a condition, not a location, so the number of steps remaining is unknown until they have been taken — which is the property you accepted when the end became a condition.
- Don't let the sentinel comparison decide two things at once. When the condition is compound — terminator reached *or* count exhausted — say so explicitly, because a comparison that quietly stops on whichever arrives first has made a policy decision the caller cannot see.

## Checklist
- Is the end of this sequence a position, or a condition discovered by traversing?
- Would producing an end position require walking the sequence, or consuming it?
- Does the comparison read only the traversing position's state, or does it mutate something?
- Is distance arithmetic needed anywhere here? If so, is a sentinel actually the right model?
- Where the stopping condition is compound, is it written down as such?

## Notes
The ordinary end position is a special case of this rather than the general one. Where a sequence sits in storage of known extent, the position one past the last element is a perfectly good stopping condition and happens to be expressible as a position — so the two ideas coincide and there is no reason to distinguish them. They come apart as soon as the extent is not known, and then the position model has to fabricate something the sequence does not have.

Worth noticing that this is what lets a stream be iterated at all. A stream has no last element to address and no length to ask for; the only honest statement about its end is "when reading stops working," which is a condition and cannot be a position. The same shape covers a null-terminated buffer, where the terminator is present in the data rather than known from outside, and a generated series, where nothing has been stored and the end is whatever the generator was told to count to. In each case the traversal is comparing itself against a condition, and calling the thing it compares against a sentinel rather than an end is what keeps the model honest.
