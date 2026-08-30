---
object_id: PAT_treat_conditionally_compiled_code_as_untested
object_type: pattern
name: A Branch Your Build Does Not Select Is Untested by Construction
library_path:
- software-engineering
- core
- testing
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- testing
- portability
- build
- contracts
- maintenance
cross_links:
- rel: related_to
  target_object_id: PAT_design_for_testability
- rel: related_to
  target_object_id: PAT_combine_detection_techniques_rather_than_perfecting_one
- rel: related_to
  target_object_id: PAT_convey_usage_through_names_and_types
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted sources
confidence: medium
references: []
variants: []
---

# A Branch Your Build Does Not Select Is Untested by Construction

## Pattern Rule
**IF** a body of code is chosen by a build-time condition — a platform branch, a feature-detection fallback, a substitute standing in for something this toolchain lacks
**THEN** treat it as untested until the configuration that selects it has actually been built and exercised, because the configuration you develop on is precisely the one where that code is absent
**ELSE** where the branch is selected by a build somebody actually runs, it is ordinary code and gets the ordinary treatment.

## Do
- Name the configuration each branch serves, and say whether anything builds it. A branch nobody compiles is not low-risk code that has quietly worked for years; it is code with no evidence behind it at all, and its age is not evidence, because nothing has been running it.
- Treat a substitute for a facility the toolchain usually supplies as the most dangerous instance of this. Every call site was written against the real contract and reads correctly against it, so a substitute that behaves differently produces failures no amount of inspection at the call sites will find. The substitute's whole job is to be indistinguishable from the thing it replaces.
- Check the substitute against the contract it is impersonating, not against the calls that happen to exist here. A comparison helper standing in for a standard one has a definition independent of your uses, and a handful of inputs run against both is a minute's work and the only thing that establishes agreement. A substitute verified only through today's call sites is verified against today's call sites.
- Get the fallback compiled somewhere even if it never ships — a job on the older configuration, or a local build with the feature forced off. That converts a branch nobody can test into a branch that is merely rarely run, which is a different and much smaller problem.
- Prefer your own differently named helper to a substitute occupying the expected name, wherever the language allows the choice. A wrong helper under a name of your own invites a reader to check it; a wrong one under the name everybody already knows does not, because nobody verifies what they recognise.
- Establish that the substitution is permitted, not merely that it compiles. Some namespaces are closed to additions and some symbols are reserved, and a substitute placed there can work on the toolchain that needed it and break on the next one without anything in the code changing.

## Don't
- Don't count "it builds here" as coverage of a branch your build does not select. The compiler did not check that code; it skipped it.
- Don't infer that a fallback was tested because somebody wrote it. A fallback is usually written by whoever could not run the configuration that needs it, which is what made the fallback necessary.
- Don't leave the selecting condition unexplained. Without knowing which configuration a branch serves, a reader cannot tell whether it is live, historical, or already dead, and so cannot safely change or delete it.
- Don't let a substitute drift once the real facility arrives. A fallback that is no longer selected anywhere is dead code that still reads as load-bearing, and it will be maintained by people who assume it runs.

## Checklist
- Which configuration selects this branch, and does anything at all build that configuration?
- If this stands in for a facility normally supplied by the toolchain, has it been compared against that facility's specification rather than against the way it is used here?
- Would a defect in this branch be visible at any call site, or do the call sites read correctly whichever version is selected?
- Is this substitution permitted by the language, or does it only happen to work on the toolchain that motivated it?
- What would have to change for this branch to become dead, and would anybody notice when it did?

## Notes
The reason this needs stating is that conditional code inverts the usual relationship between confidence and exposure. Ordinary code earns trust by being run: it is exercised on every build, and defects surface early and near their cause. A branch selected by a condition your build does not meet accumulates the appearance of that trust without any of the substance, because it sits in the same file, passes the same review, and ages alongside code that has been running the whole time. Nothing distinguishes it on the page, and the one thing that would — that it has never been compiled here — is invisible.

The substitute case deserves separating from platform branches generally, because its failure mode is worse. A platform branch does something this platform needs, and if it is wrong the failure is usually loud on that platform. A substitute impersonating a known facility is written to be interchangeable with it, and every caller has been written against the original's contract. When the two disagree, the calls are all correct with respect to what they meant, the substitute is doing what it says, and the defect exists only in the gap between them. That is why checking it against the specification rather than against local usage is not pedantry: local usage was written assuming the specification, so it cannot detect a departure from it.

Naming is the cheap defence and it is available more often than it is taken. A substitute placed under the expected name inherits every assumption readers hold about that name, which is exactly the property that makes a wrong one undetectable. The same code under a name belonging to this project announces itself as something to look at, and a reader who looks will check it against what it claims to do. Where the language forces the real name — because existing calls must resolve to it — the obligation moves to testing it against the contract instead, since the reader-side defence has been given up.
