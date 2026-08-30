---
object_id: PAT_treat_compiler_warnings_as_potential_bugs
object_type: pattern
name: Treat Compiler Warnings as Potential Bugs
library_path:
- software-engineering
- core
- error-handling
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- compiler_warnings
- error_prevention
- static_analysis
- code_review
cross_links:
- rel: related_to
  target_object_id: PAT_make_breakage_fail_compile_or_test
- rel: related_to
  target_object_id: AP_decide_how_to_signal_and_handle_an_error
- rel: related_to
  target_object_id: AP_refactor_working_code_safely
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_cpp_warnings_implementation_dependent
  variant_name: Heed C++ Warnings but Don't Depend on Them
  variant_basis: emphasis
  difference_from_foundation: Adds the C++-specific caveat that compiler warnings are implementation-dependent, so you should compile warning-free at the maximum level yet never rely on a particular warning to catch a bug, because another (widely used) compiler may stay silent about the same mistake.
  when_to_use: Writing portable C++ that must behave correctly across compilers and warning levels.
  when_not_to_use: A single-fixed-compiler context where warnings are already errors and portability is not a concern.
  absorbed_from_object_id: none
---

# Treat Compiler Warnings as Potential Bugs

## Pattern Rule
**IF** the compiler emits a warning about your code
**THEN** treat it as an early sign of a possible bug and act on it — fix the underlying issue, or suppress that specific warning with a documented reason — rather than dismissing it because the code still compiles.

## Do
- Read what the warning is really telling you: "private member `displayName` can be removed as the value assigned to it is never read" is the compiler pointing straight at a `getDisplayName()` that wrongly returns the real name.
- Configure warnings as errors where you can, so warnings cannot be silently ignored and every one must be addressed.
- When a warning is genuinely a false alarm, suppress just that warning with an explanation — a targeted `@Suppress("unused")` plus a comment and an issue link — never by turning warnings off wholesale.
- Check that a project-wide setting is actually one setting. A build supporting several toolchains configures each of them separately, and two flag sets chosen independently do not report the same defects — one may name a narrowing conversion that the other passes in silence, and neither list announces what it is missing relative to the other. Establish which supported build is weakest on the classes of defect you care about, because that is the one every contributor is really gated by, and a defect the strict build reports is not caught if the lenient one is what runs.
- Fix the warning level itself as a project-wide setting rather than a personal one. Where each author compiles at their own level, the warnings are clean for everyone individually and a flood appears the moment the parts are integrated, which is the worst time to meet them. A shared build script or make file makes the setting the default rather than a matter of discipline.

## Don't
- Don't dismiss warnings as unimportant because the build passed; an ignored one here hides a bug that leaks a user's real name in place of their display name.
- Don't silence warnings globally to make them go away; suppress the specific case and record why.

## Checklist
- Has every compiler warning been either fixed or explicitly suppressed with a reason?
- Does each suppression name why it is safe, ideally with a tracking link?
- Are warnings configured to fail the build so none slip through unnoticed?
- Is the warning level set by the project's build, or by whatever each person happens to have configured?
- If more than one toolchain is supported, do their settings catch the same classes of defect,
  and which of them is the weakest?

## Notes
Long's `UserInfo` example shows a warning catching a real, privacy-violating bug that tests might have missed: an unused-field warning is the visible symptom of a getter returning the wrong field. The rule extends the chapter-3 idea of making breakage fail at compile time — warnings are the compiler's softer signal of suspicious code, and the disciplined end state is a clean build where every warning has been fixed or suppressed with a documented, valid reason.

Variant `VAR_cpp_warnings_implementation_dependent` (Effective C++, Item 53) adds a C++-specific caveat: a compiler warning that "D::f() hides virtual B::f()" is really flagging a botched override (a const mismatch that hides rather than redefines the base function), so understand each warning before dismissing it — but because warnings are implementation-dependent, compile warning-free at the maximum level while never *depending* on a given warning to catch a mistake, since another compiler may accept the same code silently. Use this emphasis when writing portable C++ across compilers.
