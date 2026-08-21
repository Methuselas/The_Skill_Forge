---
object_id: PAT_reach_for_a_named_algorithm_before_writing_the_loop
object_type: pattern
name: Reach for a Named Algorithm Before Writing the Loop
library_path:
- software-engineering
- languages
- cpp
- algorithms
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- algorithms
- readability
- abstraction
- loops
cross_links:
- rel: related_to
  target_object_id: PAT_pick_the_search_that_fits_the_container_and_the_range
- rel: related_to
  target_object_id: PAT_prefer_range_member_functions_to_repeated_single_element_calls
- rel: related_to
  target_object_id: PAT_design_a_callable_for_the_copies_an_algorithm_will_make
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Reach for a Named Algorithm Before Writing the Loop

## Pattern Rule
**IF** you are about to write a loop over a range
**THEN** check first whether a named library operation already does that job, because the name states the intent where a bare loop only states that iteration is happening, and the library's version has had its boundary conditions worked out already
**ELSE** where the body does something the library has no name for, and expressing it would take more machinery than the loop itself, write the loop — the balance genuinely tips both ways.

## Do
- Treat the algorithm names as a shared vocabulary rather than a catalogue to memorize. A reader meeting a call that transforms, or partitions, or replaces-if, knows the shape of what happens before reading a single argument; a reader meeting a `for` knows only that something repeats.
- Let the named operation own the boundary conditions. Iteration bugs cluster at the ends of ranges and around elements being removed or inserted mid-traversal, which is exactly the code you are not writing when you call something that already handles it.
- Move a long or complicated body into its own function even when you end up keeping the loop. Once it is a function, passing it to a per-element operation is usually a small further step, and the result reads better than either starting point.
- Prefer the range-based loop over an iterator-driven one when no named operation fits. It removes the iterator bookkeeping that most loop bugs live in, without pretending to a name the library does not have.

## Don't
- Don't force a named operation onto a condition it cannot express cleanly. Meyers's own example — finding the first element strictly between two bounds — needed a composition of three adapters to avoid a loop, and he concedes the loop is clearer. That objection has since largely evaporated, because a lambda states the condition inline, but the underlying judgment stands: if saying it through the library takes more machinery than saying it directly, say it directly.
- Don't read this as a prohibition on loops. The claim is that a program using the library well contains fewer of them, not none, and the reason is that each one replaced raises the level the code is written at.

## Checklist
- Does a named operation already do what this loop's body amounts to?
- If not, can the body be stated as a small callable that one would accept?
- Is the loop doing iterator bookkeeping that a range-based loop would remove?
- Would a reader learn more from the call's name than from reading the loop?

## Notes
Meyers gives three reasons — efficiency, correctness, and maintainability — and the third is the one that has held up unchanged. The efficiency argument was partly about library implementers knowing tricks you do not, which remains true but is rarely decisive. The correctness argument is really about boundary conditions, and it is strong. The maintainability argument is the durable one: a name that says what is happening beats a construct that says only that something repeats.

Where the balance sits has moved considerably since this was written, in the direction of algorithms on one side and of simple loops on the other. Meyers's strongest objection was structural rather than stylistic: expressing a custom condition meant either an unreadable stack of adapters or a separate functor class, and a functor class could not be declared inside the function that used it, because neither templates nor local classes could serve. Lambdas removed that objection completely. In the other direction, the range-based loop made the simplest traversals cheap enough that reaching for a per-element algorithm to visit every element is now often the more roundabout spelling.

So the modern form of the question is narrower and easier than the one the item poses. It is no longer "algorithm or loop" but "does the library have a name for this?" If it does, use it. If it does not, a range-based loop says what is happening with very little ceremony, and the elaborate middle ground the item spends its length negotiating has mostly disappeared.
