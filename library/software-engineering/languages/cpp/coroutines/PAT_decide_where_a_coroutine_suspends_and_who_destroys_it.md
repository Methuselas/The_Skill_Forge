---
object_id: PAT_decide_where_a_coroutine_suspends_and_who_destroys_it
object_type: pattern
name: Decide Where a Coroutine Suspends and Who Destroys It
library_path:
- software-engineering
- languages
- cpp
- coroutines
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- coroutines
- lifetime
- resource_management
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_expect_one_keyword_to_convert_the_whole_function
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: PAT_choose_lazy_or_eager_by_how_often_the_result_is_needed
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: medium
references: []
variants: []
---

# Decide Where a Coroutine Suspends and Who Destroys It

## Pattern Rule
**IF** you are writing the resumable type that a coroutine returns
**THEN** make two decisions deliberately — whether it suspends before running its first statement, and whether it suspends after its last — because the first decides lazy against eager and the second decides whether the frame survives long enough to be read from and who is then responsible for freeing it
**ELSE** where you are using a resumable type somebody else wrote, these were decided for you and what you need is to know which way, since it determines whether calling the factory has already run the body.

## Do
- Read the initial suspension as the lazy-or-eager switch. Suspending immediately means nothing runs until something resumes the coroutine, so the factory call merely constructs; not suspending means the body runs up to its first internal suspension as part of the call.
- Read the final suspension as the lifetime switch, which is the less obvious of the two. Not suspending at the end lets the coroutine finish and destroy its own frame; suspending at the end leaves the frame intact after the body has completed, which is what allows a result to be retrieved afterwards — and transfers the obligation to destroy it to whoever holds the handle.
- Make the resumable type own that obligation rather than leaving it to callers. If the frame must be destroyed explicitly, the type holding the handle should do it in its destructor, for the same reason any other resource should.
- Keep in view what the handle can actually do, because it is a small interface: resume the coroutine, destroy it, and ask whether it has reached its final suspension. Everything a client does goes through those.
- Expect the frame to be a separate allocation. It holds the promise object, the copied parameters, the encoding of where execution has reached, and every local whose lifetime crosses a suspension — and while implementations may sometimes elide the allocation, that is an optimization with conditions rather than a guarantee.

## Don't
- Don't leave the final suspension at "never" and then try to read a result. The coroutine destroys its own frame on completion, so the promise object holding the value is gone by the time the caller looks — and the read is of freed memory rather than a diagnosable error.
- Don't suspend at the end and then forget the destruction. The frame stays allocated until something destroys it through the handle, so a type that suspends finally and has no destructor leaks one allocation per coroutine created.
- Don't assume calling the factory has done any work. Whether the body has begun depends entirely on the initial suspension choice, and a caller reasoning about side effects that happen "when I call it" is reasoning about a decision made in a different file.

## Checklist
- Does the factory call run the body, or only construct the object?
- Does the coroutine suspend at its end, and if so what destroys the frame?
- Does the resumable type's destructor destroy the handle when it needs to?
- Is a result read after completion, and does the frame still exist at that point?
- Do any locals crossing a suspension hold resources that the frame's destruction must release?

## Notes
The two suspension points look symmetric and are not. The initial one is a behavioural choice with an obvious consequence — the work either starts or it does not. The final one is a lifetime choice disguised as the same kind of switch, and it decides whether the coroutine cleans up after itself or hands you something you must clean up.

That asymmetry is why the pairing to watch for is suspending at the end together with a resumable type that has no destructor. Both halves look reasonable in isolation: suspending finally is required if the caller is to retrieve anything, and a small wrapper holding a handle looks like it needs no destructor. Together they leak.

Confidence on this card is deliberately lower than its neighbours. The coroutine machinery has more than twenty customization points, the interactions between the promise object's members are intricate, and the summary above covers the two decisions that most often matter rather than the full contract. Check the specific members against current documentation before writing a resumable type from scratch — or, better, use one somebody has already got right.
