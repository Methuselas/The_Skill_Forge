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
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u07, pp. 164-168
  evidence_type: text
confidence: high
references: []
variants:
- variant_id: VAR_ppp_split_where_one_design_line_explodes
  variant_name: Split Where One Design Line Explodes Into Code
  variant_basis: method_sequence
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  locator: u09, pp. 229, 232
  difference_from_foundation: The foundation starts from a run of finished code and asks whether pulling it out would hide something worth hiding — an order, a formula, a condition, a representation. This variant supplies a signal that arrives earlier and needs no judgment about hiding, namely the ratio between one line of intent-level design and the code that appears beneath it. Two to ten lines is the expected expansion; a couple of dozen means that one design statement was carrying more than one job. It also offers a repair the foundation does not have. Rather than extracting the code, you can go back and decompose that single design line into several and fill in code beneath each — the split happens in the design, and no extraction is performed at all. When you do extract, the naming problem is already solved, because the new routine's name is the design line you wrote before the code existed.
  when_to_use: Use while constructing a routine from a written design, where the expansion ratio is observable as it happens. It is the cheaper detection of the two — the foundation's test requires reading finished code and forming a judgment, whereas this one is a count you cannot help noticing. It also catches the case the foundation is weakest on, since a block that grew unexpectedly large may hide nothing in particular and still be two jobs.
  when_not_to_use: It needs a design pass to exist, so it is unavailable when reading code somebody else already wrote or code you wrote without designing it first. There the foundation's hiding test is the tool you have. Do not read the two-to-ten-line figure as a size limit either — it is a calibration for spotting a surprise, not a target to refactor toward.
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

## Don't
- Don't require a routine to save lines to earn its place. The most common reason people cite for extracting — avoiding duplication — is real but is only one of many, and a routine called once can still be worth having.
- Don't let the smallness itself be the objection. Reluctance to write a simple routine for a simple purpose is a mental block rather than a judgment, and it is the specific block that keeps this technique unused.
- Don't extract to satisfy a size target. Some jobs really are done better in one larger routine, and shrinking routines is not a goal in itself.
- Don't extract when the name would restate the code. A routine whose name is no more informative than the two lines inside it has added a hop and hidden nothing.

## Checklist
- What does this extraction hide — an order, a formula, a condition, a representation?
- Could the name be more informative than the code it replaces?
- Is this run of code nested deep enough that pulling it out would flatten its container?
- Does anything else in the system depend on these operations happening in this order?
- If this appears once today, would a reader still be helped by the name?

## Notes
The reason this needs stating is that the usual justification for routines — avoiding duplicate code — sets the bar in the wrong place. Under that rule a run of code appearing once has no case, and a two-line run has no case at all. McConnell's list of reasons is much longer, and most entries have nothing to do with duplication: reducing complexity, introducing an abstraction, hiding sequences, hiding pointer operations, isolating nonportable capabilities, simplifying boolean tests, supporting subclassing, and enabling a single place to optimize.

Hiding a sequence is the entry most often missed and the one with the longest reach. An order dependency spread across call sites is a semantic assumption every caller has to know and none of them can check; the same dependency inside a named routine is a fact about one implementation. That converts something the compiler cannot enforce into something callers cannot get wrong.

The counterweight is that the routine must be genuinely more informative than what it replaces. The test is not size but whether the name says something the code did not. Where it does, two lines are plenty. Where it does not, the extraction has bought a level of indirection and sold nothing.

Variant `VAR_ppp_split_where_one_design_line_explodes` (Code Complete, ch. 9) attacks the same decision from the opposite end of the size range and at an earlier moment. The foundation looks at code that seems too small and argues for pulling it out anyway; this looks at code that came out unexpectedly large under a single line of written design and reads that surprise as the finding. Both are asking whether this run of code should become its own routine, but the evidence differs — one is a judgment about what would be hidden, the other is a count of lines against an expectation of two to ten. The count is available only if you wrote a design first, which is the variant's real precondition. Its second contribution is a repair the foundation has no version of: the fix for an over-large block may be to decompose the *design* line into several rather than to extract the code, which resolves the problem without adding an interface at all. Read the two together as covering different halves of the size distribution, and note that the variant's expected-expansion figure is a detector rather than a target.
