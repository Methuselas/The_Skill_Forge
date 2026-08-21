---
object_id: PAT_read_characters_with_a_streambuf_iterator_not_a_formatted_one
object_type: pattern
name: Read Characters With a Streambuf Iterator, Not a Formatted One
library_path:
- software-engineering
- languages
- cpp
- iterators
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- iterators
- streams
- performance
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_convert_a_reverse_iterator_with_base_and_mind_the_offset
- rel: related_to
  target_object_id: PAT_choose_braces_or_parentheses_deliberately
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Read Characters With a Streambuf Iterator, Not a Formatted One

## Pattern Rule
**IF** you are moving a stream's characters one at a time into a container — slurping a file into a string, copying a stream verbatim — and do not need any interpretation of what those characters mean
**THEN** use the iterator that reads the stream's buffer directly rather than the one that performs formatted extraction, because the formatted one silently discards whitespace and pays for machinery you are not using
**ELSE** where you are reading values rather than characters — numbers, words, anything the extraction operators parse — formatted extraction is the whole point and the buffer iterator cannot do it.

## Do
- Notice the correctness half before the performance half, since it is the one that produces wrong output rather than slow output. Formatted extraction skips leading whitespace by default, so a file copied through it arrives with its spacing gone — and the fix people reach for, clearing the skip-whitespace flag on the stream, treats a symptom of using the wrong tool.
- Understand what the formatted version is doing on each character so the cost is not mysterious: constructing and destroying a guard object for the operation, consulting the stream's formatting flags, checking comprehensively for read errors, and consulting the exception mask to decide whether to throw. That is a reasonable amount of work to parse a value and a great deal of work to fetch a character.
- Use the buffer-reading iterator for output as well as input where you are writing characters verbatim, since the same asymmetry applies in that direction.
- Watch the declaration syntax when constructing a container from a pair of these. Two parenthesized temporaries in a declaration is exactly the shape that gets read as a function declaration, and this is the construct most likely to put you in front of it.

## Don't
- Don't clear the skip-whitespace flag and consider the matter closed. It restores the missing characters and leaves you paying formatted-extraction costs to read raw ones, which is the worse half of both options.
- Don't reach for this where the input has structure you want parsed. It hands you exactly the bytes in the buffer, with no notion of fields, separators, or values, which is a feature only when that is what you asked for.

## Checklist
- Is this reading characters, or reading values?
- If characters, has whitespace survived the round trip?
- Is the skip-whitespace flag being manipulated anywhere, and would the buffer iterator remove the need?
- Does the declaration constructing from two iterators risk being parsed as a function?

## Notes
The distinction is between two layers of the stream. Formatted extraction sits on top and exists to turn characters into values, with all the error checking and flag consultation that implies; the buffer iterator reaches past it and asks the stream's buffer for the next character. When the job is to move bytes, the upper layer is pure overhead and also actively wrong about whitespace.

Meyers measured up to a forty percent improvement in simple benchmarks and was careful to say it varied, noting that on one implementation he saw about five percent. The variance is the honest part of that report: this corner of the library has historically received less optimization attention than the mainstream containers, so the gap depends heavily on what you are compiling against. The correctness argument does not vary at all, which is why it belongs first.
