---
object_id: PAT_choose_the_loop_by_where_it_tests
object_type: pattern
name: Choose the Loop by Where It Tests
library_path:
- software-engineering
- core
- control-flow
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- loops
- control_flow
- iteration
- construct_selection
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_control_construct_that_fits_the_data
- rel: related_to
  target_object_id: PAT_keep_a_loops_control_outside_its_body
- rel: related_to
  target_object_id: PAT_treat_floating_point_arithmetic_as_approximate
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Choose the Loop by Where It Tests

## Pattern Rule
**IF** you are picking which looping construct to write
**THEN** decide it on two axes before reaching for a familiar one — whether the number of repetitions is known in advance, and where the completion test belongs, since the test's position is what determines whether the body runs at all.
**ELSE** when the repetition is over the members of a collection and the language offers a construct for exactly that, take it, because it removes the index arithmetic and with it every error the arithmetic could contain.

## Do
- Settle the count question first. A repetition performed a specified number of times wants the rigid, counted form; one that discovers on each pass whether it is finished wants the flexible form, and forcing either into the other's shape is where loop-control damage starts.
- Then place the test, knowing what each position guarantees. Testing at the start means the body may never run. Testing at the end means it runs at least once. Testing in the middle means everything before the test runs at least once and everything after it may not — which is a real third option, not a degenerate case.
- Reach for the middle test when the alternative is duplicated code. Where a start-tested loop forces you to run the first part of the body once before entering and again at the bottom of each pass, those duplicated lines will drift apart under maintenance, and nobody modifying one will realize the other exists. Testing in the middle removes the duplicate rather than managing it.
- Prefer a collection-iterating construct where the language has one. It eliminates the loop-housekeeping arithmetic entirely, and arithmetic that does not exist cannot be wrong.
- Write a genuinely endless loop as an explicit unconditional loop. A fake bound like counting to 99999 muddies the intent, may collide with a legitimate value, and breaks down when someone later takes the bound seriously.

## Don't
- Don't use the counted form for anything needing internal control. Its whole value is that you set it up once at the top and then leave it alone; if execution has to jump out partway, or the index has to be nudged to make it stop, the flexible form was the right choice and the counted one is now lying about what governs it.
- Don't index a loop with a floating-point value. Beyond a certain magnitude, adding one to a floating-point number returns the same number — an increment that does nothing, and a loop that never ends. Counters want ordinal or enumerated types.
- Don't decide by habit. The counted form is the one most reached for automatically, and a large share of loop defects come from a repetition that was never actually counted being expressed as though it were.

## Checklist
- Is the number of repetitions known before the loop starts, or discovered during it?
- Must the body run at least once, and does the chosen construct guarantee that?
- Is anything before the test duplicated above the loop?
- Does the language offer a construct that iterates the collection directly?
- Is the counter an ordinal type?

## Notes
Reducing the choice to two axes is what makes it a decision rather than a habit. Most programmers pick a loop by recall — the counted form for anything numeric, the flexible one for anything else — and the two questions cut across that: how the repetition is bounded, and where the test sits. Together they identify which construct fits, and the second question is the one that gets skipped, even though it is the one that determines whether the body executes at all.

The middle-tested loop deserves its awkward reputation and is still worth knowing. There is evidence for it — student programmers scored substantially higher on comprehension of loops written that way, and the researchers concluded it models how people actually think about iteration better than testing at either end. It also remains uncommon enough that using it will surprise readers, and the source is candid that opinion has not settled. The case where it clearly earns its place is the duplicated-prologue problem, because there the alternative is not a stylistic preference but two copies of the same lines waiting to diverge.

The collection-iterating form is the quiet winner of the whole section, and its argument is different from the others. Every other choice here trades one kind of clarity for another; that one removes a category of defect outright. There is no index to get wrong, no bound to be off by one, no advance step to forget. Where the repetition really is over the members of a collection, reaching past it for a counted loop is choosing to hand-maintain arithmetic the language was prepared to do correctly.
