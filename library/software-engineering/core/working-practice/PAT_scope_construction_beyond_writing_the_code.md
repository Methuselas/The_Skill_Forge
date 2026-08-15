---
object_id: PAT_scope_construction_beyond_writing_the_code
object_type: pattern
name: Take On the Whole Construction Span, Not Just the Code
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- construction
- estimation
- planning
- scope
- software_process
cross_links:
- rel: related_to
  target_object_id: PAT_support_the_memory_system_the_activity_taxes
- rel: related_to
  target_object_id: PAT_design_for_testability
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u01, pp. 3-6
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Take On the Whole Construction Span, Not Just the Code

## Pattern Rule
**IF** you are picking up a request to build or change something and deciding what the work includes
**THEN** do the whole construction span — check the groundwork, settle how it will be tested, design the classes and routines, write it, review, integrate, format and comment, tune — and hand back anything that is really requirements, architecture, user-interface design, or system testing.
**ELSE** when the groundwork check fails, stop and report what is missing instead of building on it.

## Do
- Open by confirming the groundwork holds — the interfaces you will call exist and behave as documented, the data you need is actually available. McConnell puts this first in the task list, ahead of writing anything.
- Settle how the code will be tested before writing it, not after it works. The determination is part of the build, and made afterwards it gets shaped to fit whatever you happened to write.
- Do the small-scale work the list names and habit skips: creating and naming variables and named constants, selecting control structures and organizing blocks of statements, polishing by formatting and commenting.
- Integrate components that were built separately as part of the same task, rather than declaring the piece done when it compiles in isolation.
- Read the low-level design and code you are building against as you go — that review is your work, not an optional courtesy to whoever wrote it.
- Watch the straddling edges. Detailed design, unit testing, integration, and integration testing sit only partly inside construction; coding and debugging alone is squarely at the centre. On the straddling tasks, say which part you are doing rather than assuming the whole of it is yours or none of it is.

## Don't
- Don't let the word "coding" set the boundary. It implies mechanical translation of a preexisting design into a computer language; the work is not mechanical and takes substantial creativity and judgment.
- Don't collapse every activity into one undifferentiated "programming" blob. That is what informal and self-taught practice does, and the cost is losing track of which tasks belong to the thing in front of you.
- Don't quietly absorb requirements development, architecture, user-interface design, or system testing because they are adjacent and nobody else is doing them. Say they are missing and who they belong to.
- Don't leave formatting, commenting, integration, and tuning for a follow-up pass. They are enumerated construction tasks, and a follow-up pass is where they go to die.

## Checklist
- Did you verify the groundwork before writing, or assume it?
- Was the testing approach decided before the code existed?
- Are the components integrated, or does the piece only work in isolation?
- Is the formatting and commenting done now, or deferred?
- Is anything you are about to build actually requirements, architecture, or system testing that belongs to someone else?

## Notes
The everyday sense of the word — the hands-on part of building, with some planning, designing, and checking mixed in — carries over to software almost intact. What it drops is the surrounding map, and the map is the useful part: problem definition, requirements development, and architecture come before; system testing and corrective maintenance come after. Knowing where the edges are is what stops you from either building on absent groundwork or silently taking on work that was never yours.

The proportion is worth holding onto. Construction is 30 to 80 percent of total project time depending on project size, so where you draw this line moves a large number. Drawn too narrowly — code only — review, integration, and tuning surface later as overruns. Drawn too widely, you have taken on requirements and architecture nobody scheduled.

McConnell draws the activity set twice. The first drawing weights every activity equally. The second re-sizes each by how much of a construction handbook it deserves: coding and debugging swells to dominate, detailed design stays large, unit testing and integration hold the middle, and problem definition, requirements, architecture, system testing, and corrective maintenance shrink to the margins. In both drawings the activities overlap the construction boundary rather than sitting cleanly inside or outside it, which is the reason the straddling tasks need an explicit split rather than an assumption.
