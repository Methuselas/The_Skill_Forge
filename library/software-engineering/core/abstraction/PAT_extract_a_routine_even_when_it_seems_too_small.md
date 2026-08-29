---
object_id: PAT_extract_a_routine_even_when_it_seems_too_small
object_type: pattern
name: Two Lines Are Enough to Justify a Routine
library_path:
- software-engineering
- core
- abstraction
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- extraction
- abstraction
- routines
- information_hiding
cross_links:
- rel: related_to
  target_object_id: PAT_write_functions_as_single_sentences
- rel: related_to
  target_object_id: PAT_ask_what_should_be_hidden
- rel: related_to
  target_object_id: AP_build_a_routine_from_intent_level_pseudocode
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants:
- variant_id: VAR_ppp_split_where_one_design_line_explodes
  variant_name: Split Where One Design Line Explodes Into Code
  variant_basis: method_sequence
  difference_from_foundation: The foundation starts from a run of finished code and asks whether pulling it out would hide something worth hiding — an order, a formula, a condition, a representation. This variant supplies a signal that arrives earlier and needs no judgment about hiding, namely the ratio between one line of intent-level design and the code that appears beneath it. Two to ten lines is the expected expansion; a couple of dozen means that one design statement was carrying more than one job. It also offers a repair the foundation does not have. Rather than extracting the code, you can go back and decompose that single design line into several and fill in code beneath each — the split happens in the design, and no extraction is performed at all. When you do extract, the naming problem is already solved, because the new routine's name is the design line you wrote before the code existed.
  when_to_use: Use while constructing a routine from a written design, where the expansion ratio is observable as it happens. It is the cheaper detection of the two — the foundation's test requires reading finished code and forming a judgment, whereas this one is a count you cannot help noticing. It also catches the case the foundation is weakest on, since a block that grew unexpectedly large may hide nothing in particular and still be two jobs.
  when_not_to_use: It needs a design pass to exist, so it is unavailable when reading code somebody else already wrote or code you wrote without designing it first. There the foundation's hiding test is the tool you have. Do not read the two-to-ten-line figure as a size limit either — it is a calibration for spotting a surprise, not a target to refactor toward.
  absorbed_from_object_id: none
- variant_id: VAR_name_the_sub_conditions_in_local_booleans
  variant_name: Name the Sub-Conditions in Local Booleans
  variant_basis: method_sequence
  difference_from_foundation: The foundation's remedy for a complicated boolean test is to pull it into a named function. This variant supplies a lighter one for the same decision — assign each sub-condition to a named local boolean and let the test read as those names. A condition combining an index below zero, an index above the maximum, and an index equal to the previous one becomes `finished` and `repeatedEntry`, and the test becomes those two words. A longer test combining end-of-stream, an error flag, a line count within bounds, and an error-processing check becomes `allDataRead` and `legalLineCount` alongside the remaining call. The tradeoff runs both ways. The local booleans add no interface, need no name that will read well from elsewhere, and can be written without leaving the routine — but they are not reusable, they do not shorten the routine, and they add variables whose live time has to be kept short.
  when_to_use: Use when the complexity is in the *condition* rather than in the work, and when the named pieces have no meaning outside this routine. It is the right move for a test that took several attempts to get right, since the names record what the attempts were trying to express and make the later modification tractable. It is also the version that gets written under time pressure, where extracting a function would not.
  when_not_to_use: Do not use it where the test itself is worth reusing or worth testing independently — that is what the extracted function is for. Do not let it become a way of keeping an over-long routine, since it leaves the routine the same length. And where the sub-conditions need the routine's local state to be computed, check the resulting variables against the usual live-time discipline rather than letting them sit from the top of the routine.
  absorbed_from_object_id: none
---

# Two Lines Are Enough to Justify a Routine

## Pattern Rule
**IF** you are looking at a short run of code and dismissing extraction because it seems too small to be worth a routine
**THEN** extract it anyway when it hides something — a sequence, a calculation, a condition, a representation — because the value is the hiding, not the line count saved.
**ELSE** leave it inline when the extracted routine would need a name no clearer than the code it replaces.

## Do
- Extract to hide an order dependency. Reading the top of a stack and decrementing the stack pointer are two lines that must happen in that order; a `PopStack()` routine holds that assumption in one place instead of baking it in from one end of the system to the other.
- Extract a repeated calculation even when it is one line. A unit conversion appearing in a dozen places is a dozen chances to get it subtly wrong, and one well-named routine makes the intent visible where the arithmetic was not.
- Extract a complicated boolean test into a named function. Understanding a test in detail is rarely necessary to follow the flow, so moving the detail out of the way and letting the name summarize the purpose makes both the flow and the test clearer.
- Treat deep nesting as an extraction signal. An inner loop or conditional nested several levels down is a candidate to pull out whole — the containing routine loses the complexity, and the extracted part gains a name.
- Extract to introduce an abstraction that is missing. Eight lines walking a list to its end become `leafName = GetLeafName(node)`, and the routine is then so short that a good name is nearly all the documentation it needs.
- Extract to isolate what is not portable, and what is error-prone by nature. Nonstandard language features, platform dependencies, and pointer manipulation all get easier to find, verify, and later replace once they live in one named place.
- Dismiss the performance objection rather than trading against it. Modern machines impose virtually no penalty for calling a routine, and measurements of inlining a routine by hand run from a few percent gained to ten percent *lost* — you are about as likely to slow the program down as speed it up.
- Take a routine that needs two levels of comment as a routine that wants splitting. A routine should be logically flat, with its activities sitting at one level; if you find yourself marking some comments as major and others as subordinate to them, the unevenness is the finding, and extracting the major operation gives you two flat routines instead of one lumpy one.
- Check what your own conventions charge for a new routine. A house style that demands a heavy prolog on every routine — purpose, algorithm, inputs, outputs, assumptions, author, revision history — prices extraction so high that people quietly create fewer routines, which is the opposite of what the convention was meant to encourage.

## Don't
- Don't require a routine to save lines to earn its place. The most common reason people cite for extracting — avoiding duplication — is real but is only one of many, and a routine called once can still be worth having.
- Don't let the smallness itself be the objection. Reluctance to write a simple routine for a simple purpose is a mental block rather than a judgment, and it is the specific block that keeps this technique unused.
- Don't extract to satisfy a size target. Some jobs really are done better in one larger routine, and shrinking routines is not a goal in itself.
- Don't extract when the name would restate the code. A routine whose name is no more informative than the two lines inside it has added a hop and hidden nothing.
- Don't cut where mutable state crosses the cut. Where the run of code and the run beside it both read and update the same working state — a parse mode, a nesting depth, a running position, a flag saying which branch you are inside — the split does not divide the problem, it distributes one state machine across two scopes. Each half then reads correctly on its own while the pair is wrong, which is the hardest kind of defect to see in review because there is nothing wrong with either routine. This is a different objection from the two above: the name can be excellent and the extraction still wrong.

## Checklist
- What does this extraction hide — an order, a formula, a condition, a representation?
- Could the name be more informative than the code it replaces?
- Is this run of code nested deep enough that pulling it out would flatten its container?
- Does anything else in the system depend on these operations happening in this order?
- Do the runs of code on either side of the proposed cut read or write the same working state? The practical tell is a helper whose parameter list has to carry three or more values the caller still needs afterwards.
- If this appears once today, would a reader still be helped by the name?

## Notes
The reason this needs stating is that the usual justification for routines — avoiding duplicate code — sets the bar in the wrong place. Under that rule a run of code appearing once has no case, and a two-line run has no case at all. McConnell's list of reasons is much longer, and most entries have nothing to do with duplication: reducing complexity, introducing an abstraction, hiding sequences, hiding pointer operations, isolating nonportable capabilities, simplifying boolean tests, supporting subclassing, and enabling a single place to optimize.

Hiding a sequence is the entry most often missed and the one with the longest reach. An order dependency spread across call sites is a semantic assumption every caller has to know and none of them can check; the same dependency inside a named routine is a fact about one implementation. That converts something the compiler cannot enforce into something callers cannot get wrong.

The performance objection deserves burying because it is the most common reason people decline to extract, and it is empirically dead. Machines once charged heavily for a call — swapping the program out, a directory of routines in, the routine in, then all of it back — and the belief outlived the hardware by decades. Measured on anything you are likely to work on, hand-inlining a routine returns a few percent at best and can cost around ten percent, so the trade people think they are making is not on offer. The relationship runs the other way: good decomposition is one of the more powerful things you can do *for* performance work, because a hot routine can be tuned once and every caller benefits, and because a small routine is tractable to rewrite in a lower-level language while a long tortuous one is not.

The counterweight is that the routine must be genuinely more informative than what it replaces. The test is not size but whether the name says something the code did not. Where it does, two lines are plenty. Where it does not, the extraction has bought a level of indirection and sold nothing.

Variant `VAR_ppp_split_where_one_design_line_explodes` (Code Complete, ch. 9) attacks the same decision from the opposite end of the size range and at an earlier moment. The foundation looks at code that seems too small and argues for pulling it out anyway; this looks at code that came out unexpectedly large under a single line of written design and reads that surprise as the finding. Both are asking whether this run of code should become its own routine, but the evidence differs — one is a judgment about what would be hidden, the other is a count of lines against an expectation of two to ten. The count is available only if you wrote a design first, which is the variant's real precondition. Its second contribution is a repair the foundation has no version of: the fix for an over-large block may be to decompose the *design* line into several rather than to extract the code, which resolves the problem without adding an interface at all. Read the two together as covering different halves of the size distribution, and note that the variant's expected-expansion figure is a detector rather than a target.

`VAR_name_the_sub_conditions_in_local_booleans` offers a cheaper remedy for one entry in the Do list above — the complicated boolean test. Instead of extracting the test into a named function, assign its pieces to named local booleans and let the condition read as those names, so an `if` combining four clauses about streams, error flags, and line counts becomes `allDataRead` and `legalLineCount` beside the one remaining call. The honest comparison is that the two buy different things. The function is reusable, independently testable, and shortens the routine; the local booleans add no interface, need no name that must travel, and get written in situations where extracting a function would have been skipped entirely. McConnell's own framing of the failure is the useful part — faced with a dense four-clause condition most readers decide to work it out later if they really need to, and they never really need to, which is the same thing every reader of your code will do. The variables the remedy introduces are subject to the usual short-live-time discipline, so declare them immediately above the test rather than at the top of the routine.
