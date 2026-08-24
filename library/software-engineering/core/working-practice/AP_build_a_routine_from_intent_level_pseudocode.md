---
object_id: AP_build_a_routine_from_intent_level_pseudocode
object_type: ap
name: Build a Routine From Intent-Level Pseudocode
library_path:
- software-engineering
- core
- working-practice
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- construction
- pseudocode
- routines
- detailed_design
- iteration
cross_links:
- rel: related_to
  target_object_id: AP_assess_construction_prerequisites_before_building
- rel: supports
  target_object_id: PAT_write_design_notation_at_the_level_of_intent
- rel: supports
  target_object_id: PAT_understand_the_routine_before_the_compiler_sees_it
- rel: supports
  target_object_id: PAT_extract_a_routine_even_when_it_seems_too_small
- rel: supports
  target_object_id: PAT_let_an_awkward_name_expose_the_design_fault
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Build a Routine From Intent-Level Pseudocode

## Objective

Take one nontrivial routine from an informal spec to finished code by designing it in English first and then growing the code underneath that design — so that the design gets checked while changing it still costs a line rather than a page, and so that it survives into the shipped routine as its comments instead of decaying in a separate document.

Reach for this on the routines that are actually hard. Accessors, pass-throughs to another object's routines, and the like do not need it and are slower for the ceremony. Four symptoms say afterwards that you should have used it: you coded yourself into a corner and had to restart, you lost your train of thought partway through a routine, you simply forgot to write part of a class, or you sat looking at the screen with no idea where to start.

## Steps / Flow

1. **Confirm the routine is called for, then state what it must do.** Check that its job is well defined and fits the overall design — that it is required, at least indirectly, by the project's requirements. Then pin down five things the high-level design should already imply: what the routine hides, its inputs, its outputs, the preconditions guaranteed true before it is called, and the postconditions it guarantees before returning. For an error-reporting routine those come out as: it hides the message text and whether processing is interactive or command-line; no preconditions; an error code in; a message and a status out; and a guarantee that the status is one of exactly two values.

2. **Name it, and settle testing, reuse, errors, and efficiency before writing anything.** Each of these is cheaper to decide now than to retrofit. If a clear, unambiguous name will not come, stop and improve the design rather than accepting a vague one. Plan the test cases while the routine is still an idea — all valid codes and a variety of invalid ones, in the example. Search the standard library, your platform, and your own organization's code before designing something that may already exist, and check an algorithms reference before writing anything complicated from scratch. Decide how errors are handled, following the architecture's strategy if it has one. On efficiency, most routines need only a well-abstracted interface and readable code so that a slow implementation can be swapped later without touching callers; design to a number only where the architecture gave this routine a resource or speed budget. `PAT_let_an_awkward_name_expose_the_design_fault` owns what to do when the name will not come.

3. **Write the header comment before the steps.** One concise statement of what the routine is supposed to do — the most general thing about it. This is a probe as much as a product: difficulty summarizing the routine's role is a warning that you do not yet understand its place in the program well enough to design it.

4. **Write the pseudocode, general first, then refined downward.** Precise English, no constructs from the target language, describing what the design accomplishes rather than how it will be spelled. Refine and decompose until writing the code instead would feel like a waste of time. If you are not sure how you would code something, that part is not refined enough yet. `PAT_write_design_notation_at_the_level_of_intent` owns the level it is written at.

5. **Design the data where data is the point.** For a routine whose logic dominates, the data falls out. Where manipulation of data is a prominent part of the job, work out the major pieces before the logic — having the key type definitions in hand is what makes the logic designable.

6. **Get the design read before it is code.** Back away from it and think about how you would explain it; then have someone actually look at it or listen to you. The economics here are the whole point and they are easy to miss: people will read a dozen lines of English and will not read a page of C++ or Java, and assumptions and high-level mistakes are more visible in the English than in the code. A design nobody reviews at this stage will not be reviewed at all.

7. **Try several versions in pseudocode and keep the best.** Do this before any code exists, because once you start coding you become emotionally involved with what you wrote and throwing away a bad design gets harder.

8. **Write the declaration, and turn every pseudocode line into a comment.** The interface statement in whatever form your language takes, the header turned into a language comment above it, the opening and closing braces, and the design lines commented out between them. At this point the routine has no executable content and its character is already evident — you should be able to sense how it works. If converting the remaining comments to code does not feel mechanical and natural, go back to step 4; that feeling is the exit test for the design.

9. **Fill in code below each comment, watching the expansion.** Each comment heads a block the way an outline heading precedes a paragraph, and each should normally grow to about two to ten lines. Declare and define each variable close to its first use. Where one comment produces far more code than expected, stop and choose: pull that block into its own routine — whose name is already written, it is the comment — or go back and decompose that one design line into several and fill in code beneath each.

10. **Check the code yourself, then compile, then step it, then test it.** Mentally execute every path, including endpoints and every exception condition, alone and then with someone else. Only then compile, with warnings at the pickiest level and every message's cause eliminated. Then step each line in the debugger and confirm it does what you expected. Then run the test cases from step 2, building scaffolding if the routine needs a harness or stubs to be exercised. A routine that is unusually buggy at this point should be redesigned rather than patched — the buggy ones tend to stay buggy. `PAT_understand_the_routine_before_the_compiler_sees_it` owns the self-check.

11. **Clean up the leftovers.** Confirm every parameter is used and all input and output is accounted for; that the routine does one thing, is loosely coupled, and is defensive; that variables are named accurately, declared, and initialized; that the logic has no off-by-one, no unterminated loop, no leak; that white space shows the structure; and that the comments still describe what the code below them now does. Delete the design comments that turned out to be redundant — typically the ones sitting above a call to a well-named routine after the process was applied recursively. `PAT_extract_a_routine_even_when_it_seems_too_small` owns what is worth pulling out.

12. **Loop back rather than pushing through.** If the routine's quality is poor, return to the pseudocode. None of the earlier steps is a gate you pass once; each stage can send you back to an earlier one, and the diagrams for this process draw a return path out of every single stage for that reason.

## Notes

The economic claim underneath this is that a few lines of pseudocode are easier to change than a page of code — the difference between moving a line on a blueprint and ripping out a wall to nail the studs somewhere else. Catching an error at the least-value stage, the stage where the least effort has been invested, is what the whole sequence is arranged to buy. That is also why steps 6 and 7 come before step 8 and not after it.

The second payoff is the one people abandon the method without noticing they have lost. The design statements do not get thrown away when coding starts; they become the comments, which is why step 11 removes comments rather than adding them. Writing the design in English and then deleting it before coding gives up half the return.

Three details decide whether this works in practice. The routine declaration is written *after* the pseudocode, not before, so the interface follows from the design rather than constraining it. The expansion ratio in step 9 is a live measurement, not a style rule — it is the earliest available signal that one design statement was carrying two jobs. And the process applies to itself: a block factored out in step 9 is a new routine, and it starts again at step 1.

Two limits worth stating. Applying this to trivial routines is waste, and the accessor case is the clearest example. And the flow is drawn as an ordered sequence only because something has to be drawn first — the source's own diagrams put back-edges on every stage and caption them as not necessarily happening in any particular order, so treat the numbering as a default route rather than a required one.
