# The Programmer's Brain

source_id:    programmers_brain
title:        "The Programmer's Brain: What Every Programmer Needs to Know About Cognition"
author:       Felienne Hermans
publish_date: 2021
media_type:   PDF
payload_path: sources/programmers_brain/The_Programmers_Brain.pdf
sha256:       52063e7300c1f52095b594da93ee75d42fe4b2cd4991be55f0305a0e39cbaa0b
pdf_page_offset: 26
added:        2026-08-01
status:       complete

## Unit scheme

One source-native chapter per unit (13 chapters across four parts). Each chapter
develops a coherent cognitive concept and its programming applications, and the
first two chapters fit comfortably within the required two-read grounding cycle.
Chapter boundaries use the book's printed pagination and must be verified from
the chapter text when each unit is claimed.

Page numbers in locators are the book's printed page numbers. PDF page = printed
page + 26. The offset was verified at the Chapter 1 opening (printed p. 3 / PDF
p. 29) and the Chapter 2 opening (printed p. 13 / PDF p. 39).

## Summary

**All 13 units are processed.** Source reconciliation per `PASS_RUN.md` §8 is due
and is not yet complete — see "Closure status" below.

- **Units:** 13 processed / 0 empty / 0 blocked, of 13.
- **Objects added:** 66 — 23 under `foundations/code-comprehension` (10 from
  u01-u02, 5 from u04, 3 from u05, 1 from u06, 3 from u07, 1 from u09), 8 under
  `foundations/problem-solving` (7 from u06, 1 from u10), 14 under
  `foundations/deliberate-practice` (5 from u03, 1 from u06, 4 from u07, 4 from
  u10), 8 under `foundations/readability` (7 from u08, 1 from u09), 9 under
  `foundations/working-practice` (4 from u11, 5 from u13), 4 under
  `foundations/code-quality` (1 from u09, 3 from u12).
- **Variants absorbed:** 19 — 4 into gcbc readability/naming foundations (u01-u02),
  1 into `PAT_calibrate_code_reading_scope_to_reader_knowledge` (u03), 1 into
  `DRILL_practice_syntax_with_flashcards` (u04), from u05 one into
  `DRILL_annotate_a_dependency_graph_over_code` and one into
  `PAT_use_descriptive_names`, from u06 one into
  `PAT_externalize_intermediate_state_when_tracing`, and from u07 one into
  `PAT_guard_against_an_outdated_mental_model_under_load` and one into
  `PAT_choose_explanatory_metaphors_by_audience_schemata`, and from u08 one into
  `PAT_use_descriptive_names` and one into `PAT_follow_a_consistent_coding_style`,
  from u09 one into `PAT_treat_bad_names_as_a_defect_search_heuristic`, and from
  u10 one into `PAT_separate_intrinsic_from_extraneous_load` and one into
  `PAT_expect_negative_transfer_between_similar_languages`, from u11 one into
  `PAT_comment_why_not_what`, from u12 one into
  `PAT_evaluate_code_against_quality_goals`, and from u13 one into
  `DRILL_read_code_with_text_comprehension_strategies`.
- **Objects replaced:** 0. u08 was expected to produce the source's first
  `replace` and did not; see `units/u08.md` Notes for why the naming chapter
  corroborates `PAT_use_descriptive_names` rather than superseding it.
- **Candidates rejected:** 159, of 244 raised across the 13 units.

The arithmetic reconciles: 66 new + 19 variants + 0 replaced + 159 rejected = 244,
and each unit's disposition rows sum to its own declared `candidate_count`.

## Closure status

All 13 units are `processed` and the library-side work of `PASS_RUN.md` §8 is
done. Three items remain, each deliberately left rather than overlooked:

- **`ledger/REGISTRY.md`** — this source's row has been updated in the working
  tree to `complete`, 13/13, 66 objects, but is **not committed**. The file is
  shared state whose pending diff is mostly art-lane rows, and git cannot stage
  part of a file. It should be committed alongside the art lane's own registry
  changes.
- **The root `library/INDEX.md`** — not regenerated. `build_index.py --package`
  deliberately skips it so a lane-scoped run cannot bake the other lane's
  in-flight state into the shared index. Regenerate it unscoped immediately
  before a commit that covers both lanes.
- **Payload retirement** — `sources/programmers_brain/The_Programmers_Brain.pdf`
  (9.6 MB, sha256 `52063e7300c1…`) has **not** been moved to
  `trash/sources/programmers_brain/`. §8 calls for the move; it is left to the
  user because it relocates a file that `verify_grounding.py` depends on, and
  because a stale `payload_path` is exactly the failure mode that made seven art
  sources permanently unverifiable. When the move happens, update `payload_path`
  and `status` here in the same commit.

Cross-links were checked as part of closure: `validate.py` resolves every
`cross_links` target and every `variant_id` mention across all 268 objects in the
package, so no link points at a candidate that was later rejected or absorbed. No
object ids are source-prefixed — all 66 use semantic filenames — so there is
nothing to reconcile there.

### What this source contributed

Two new topics were opened. u06 opened `foundations/problem-solving` for choosing
how to represent a problem before solving it. u11 opened
`foundations/working-practice` for how a working session is organised and how it
survives contact with other people; u13 more than doubled it.

The variants are the part worth noting. Nineteen landed, and they are the reason
this source was chosen — it applies external pressure to cards extracted from
other books. Six went onto gcbc foundations, and several revised rather than
merely extended them: u10's germane-load variant contradicted a sentence in
`PAT_separate_intrinsic_from_extraneous_load` and the foundation's Notes were
amended rather than left standing. Four went onto this source's own earlier
objects, which is the chapter structure showing through — chapter 7 reopens
chapter 6's snowman puzzle, chapter 13 reruns chapter 5's reading strategies with
a team.

Three of the thirteen TOC page ranges were wrong — u04, u07 and u13, each long by
one page or more, with u13's overrun reaching into the epilogue. Bounds were
verified from chapter text on every unit, which is the only reason none of that
propagated into a locator.

u06 opened `foundations/problem-solving`. The chapter concerns choosing how to
represent a problem before solving it, which is neither reading code already in
front of you (`code-comprehension`) nor building knowledge for later
(`deliberate-practice`).

u11 opened `foundations/working-practice` for material about how a working session
is organised and how it survives contact with other people — programming
activities and the memory each taxes, interruptions from both sides, and
multitasking. u12 and u13 are likely to add to it.

Both u07 variants land on u06 objects. Chapter 7 explicitly reopens chapter 6's
snowman puzzle and supplies the inhibition mechanism chapter 6 left unexplained,
so the sharper method was absorbed rather than restated as a second pattern.

**TOC page ranges are unreliable in this source.** u04's was long by one page and
u07's was long by one page; u06's happened to be correct. Verify every remaining
range against the chapter text before extracting.

**Figure counts per unit are not reliable and must be checked when each unit is
claimed.** This summary previously asserted that u08 and every remaining chapter
carried no figures; u08 in fact had four figures and four tables, and figure 8.4
materially qualified the prose it accompanied. Do not plan a unit's visual work
from this file — count the figures in the chapter text first. u10 is known to
carry at least 6. Poppler `pdftoppm` is absent from this environment;
`tools/render_pdf.py` falls back to pypdfium2, which is what u03, u06 and u07 were
rendered with.
