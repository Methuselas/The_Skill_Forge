---
object_id: PAT_let_an_awkward_name_expose_the_design_fault
object_type: pattern
name: Fix the Routine the Honest Name Exposes
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- routines
- side_effects
- design_signal
cross_links:
- rel: related_to
  target_object_id: PAT_use_descriptive_names
- rel: related_to
  target_object_id: PAT_write_functions_as_single_sentences
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Fix the Routine the Honest Name Exposes

## Pattern Rule
**IF** naming a routine honestly produces something long, awkward, or vague
**THEN** treat the name as a report on the routine and change the routine, not the name — an accurate name that reads badly is describing something that is built badly.

## Do
- Name every output and side effect, then read the result. A routine that computes report totals and opens an output file is honestly called `ComputeReportTotalsAndOpenOutputFile`, and the absurdity of that name is the finding: the cure is to stop causing things to happen as side effects, not to pick a shorter name.
- Read an `And` in a routine name as a split instruction. It is the cheapest available signal that the routine has more than one job.
- Treat a vague verb as one of two different faults. Sometimes only the name is weak and the routine is fine — `HandleOutput` becoming `FormatAndPrintOutput` tells you what it does. Sometimes the verb is vague because the purpose is, and then the fix is restructuring the routine and its neighbours until each has a purpose strong enough to name.
- Name a function for the value it returns, and name a procedure for what it does. That single convention removes most of the ambiguity about which one you are looking at.
- Let the name run as long as clarity needs. Around nine to fifteen characters is the researched optimum for variables, routines usually need more, and an object name often supplies part of the name for free — so the target is understandable rather than short.

## Don't
- Don't shorten a name to make it comfortable. The discomfort was information, and removing it leaves the design fault in place with the evidence deleted.
- Don't accept elastic verbs that fit anything. `HandleCalculation`, `PerformServices`, `ProcessInput`, `DealWithOutput` say only that the routine has something to do with a noun. The exception is `handle` in its precise technical sense, for an event handler.
- Don't distinguish routines by number. `OutputUser`, `OutputUser1`, `OutputUser2` give no indication of the different abstractions they represent, which is the same as saying nobody knows what the difference is.
- Don't let the same concept get several names across a codebase. When one class exposes `id.Get()`, another `GetId()`, another a default return value, and another the id object itself, everybody spends attention remembering which syntax applies where — a convention would have cost nothing.

## Checklist
- Does the name mention every output and every side effect?
- Is there an `And` in it, or would an honest name need one?
- Is the verb doing real work, or could it be swapped for any other verb?
- For a function: is it named for what it returns?
- Does this codebase already have a name for this concept, spelled differently somewhere else?

## Notes
The move here is to use naming as a diagnostic rather than as a finishing step. Most naming advice runs one way — the routine exists, now describe it well. This runs the other way: try to describe it accurately, and let the difficulty of doing so tell you what is wrong with it. A name that resists being written is reporting either that the routine does several things, or that nobody can say what its one thing is.

The side-effect case is the sharpest version and the one worth internalising. If a routine's honest name needs `And`, the usual response is to pick something shorter and vaguer, which trades an ugly name for an invisible problem. McConnell's inversion is that the long silly names are a symptom of programming with side effects, so the fix is to cause things to happen directly. The naming rule then enforces itself, because a routine that does one thing is easy to name.

Vagueness needs a second diagnosis before acting, since the same symptom has two causes. A well-built routine can carry a lazy name, and renaming genuinely fixes it. A routine with a weak purpose produces a weak name no matter how hard you try, and renaming just relabels it. Telling them apart is a matter of asking whether a strong name exists that you have not thought of yet.
