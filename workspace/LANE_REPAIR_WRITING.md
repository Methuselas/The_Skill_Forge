# Lane repair — Writing — COMPLETE

Written 2026-08-23 as a handoff. Superseded the same day: the Writing lane did
the repair in commits `13fddfc`, `845887f`, and `cfa1ab9` while it was being
written. This file is kept as the record rather than deleted, because the
before/after numbers are the only trace the work leaves.

## What the handoff found

Not one of the 22 Writing APs claimed a single Pattern. Every `supports` edge in
the lane originated on a Pattern or a Drill, never on an AP. `related_to` was 92%
of all edges — the highest of the three lanes, an almost pure undirected
adjacency graph.

It was never a content problem. All 22 APs already listed the right Patterns —
168 edges — typed `related_to`, which cannot express authority.

## Result

| | before | after |
|---|---|---|
| patterns claimed by an AP | 0 of 131 (0%) | **100 of 134 (75%)** |
| `supports` edges | 24 (none from an AP) | **176** |
| APs naming owners in step prose | 0 of 22 | **22 of 22** |

75% is the highest of the three lanes, and every AP names its owners in prose.
This lane is now the reference implementation of the convention in
`PASS/docs/PASS_RUN.md` §2.8, ahead of both software-engineering (29%) and art.

## For comparison, at the same date

```
writing                22 APs   134 patterns    75% claimed   22/22 APs name owners
software-engineering   26 APs   462 patterns    29% claimed   24/26 APs name owners
art                    35 APs   222 patterns    27% claimed   25/35 APs name owners
```

The remaining 34 unclaimed Writing patterns are the honest residue the handoff
predicted: local decisions that fire on their own IF clause and need no
sequencing, plus any genuine AP coverage gap. Neither needs manufacturing an AP
to fix.

---

# Second pass — 2026-09-03 — residue classified

The 2026-08-23 record asserted that the unclaimed remainder was "local decisions
plus any genuine AP coverage gap" without saying which was which. PASS_RUN.md
§2.8 says recording that distinction is the point, so this pass made it. The lane
had grown to 30 APs / 169 patterns / 83% claimed by then.

## Defects found and fixed

Three genuine omissions, not residue. Every one was a step that already delegated
a decision the Pattern owns while carrying no edge to it.

| AP | step | missing owner |
|---|---|---|
| Draft and Revise a Dialogue Scene | 4 — prose already read `activate writing_make_nonstandard_language_deliberate` | `writing_make_nonstandard_language_deliberate` |
| Finalize and Submit a Resume | 4 — prose deferred to "the applicable keyword owners" without naming one | `writing_use_recognizable_job_language_for_resume_discovery` |
| Draft and Revise Short Creative Nonfiction | 3 — prose **restated the Pattern's rule** instead of delegating to it | `writing_creative_nonfiction_separate_experiencing_self_from_reflective_narrator` |

The third is the interesting failure mode. An AP that restates a Pattern's rule in
its own prose reads as complete, passes validation, satisfies "names an owner in
prose" on every other step, and still leaves the Pattern unclaimed. A percentage
cannot see it. Worth checking for in the other lanes.

After the fixes: **143 of 169 (84%)**, 242 `supports` edges, 30/30 APs naming
owners, and **zero** Patterns named in AP step prose without a carrying edge.

## The 26 remaining, classified

**AP coverage gap — one missing protocol, 5 patterns.** Nothing in the lane drafts
a resume from an established work history. Graduate and school-leaver drafting APs
both exist and are fully wired; `Finalize and Submit a Resume` audits content and
step 3 explicitly routes a failure "back to the Pattern that owns it" while
claiming none of them. The orphaned owner set is coherent enough to be the missing
AP's step list:

- `writing_scale_work_history_detail_by_role_relevance`
- `writing_account_for_career_interruptions_without_distorting_dates`
- `writing_preserve_employer_continuity_through_name_changes`
- `writing_show_current_readiness_after_extended_career_break`
- `writing_state_neutral_departure_context_when_it_resolves_concern`

**Smaller coverage gaps — 3.** Real actions with no protocol, each too small to
justify an AP on its own: `writing_control_online_resume_visibility_and_currency`
(no AP posts a resume to a searchable job service),
`writing_use_academic_cv_for_comprehensive_professional_evidence` (no CV AP),
`writing_poetry_make_performance_language_stand_alone` (no performance-poetry AP).

**Needs an owning-AP read before repair — 4.** Each looks like a missed edge from
the Pattern side, but the candidate owner's steps were not read this pass. Do not
add these edges without reading the AP first.

- `writing_creative_nonfiction_move_across_time_with_concrete_summary_and_brief_scenes` → Organize a Short Essay, step 3 chronology branch
- `writing_creative_nonfiction_portray_real_people_through_selective_behavioral_detail` → Draft and Revise Short CNF, step 7 (currently reached only through a drill)
- `writing_choose_truth_contract_before_shaping_real_material` → Design and Stress-Test a Life-Writing Project Contract
- `writing_shape_sentence_rhythm_through_length_structure_and_punctuation` → Revise a Creative Draft, editing stage

**Local decisions — 14, genuine residue.** These fire on their own IF clause and
nothing has to sequence them. Do not manufacture an AP for any of them.

The `poetry/forms` trio — `ground_haiku_in_present_sensory_perception`,
`make_refrains_and_repeated_words_accumulate_meaning`, `turn_sonnet_before_closure`
— sit in the same folder as `Design and Revise a Poem's Governing Form`, which is
the shape most likely to look like a defect. It is not. That AP is form-general by
design and claims `writing_poetry_learn_form_before_varying_its_rules`; the
per-form rules fire beneath that one. Linking them would turn the AP into a
catalogue of forms.

The rest: `poetry_sustain_intensity_beyond_meter_and_lineation`,
`poetry_use_white_space_to_weight_language`,
`balance_symbols_between_cliche_and_obscurity`,
`control_irony_to_preserve_reader_trust`,
`use_working_title_as_temporary_attention_cue`,
`use_cultural_memory_to_complicate_personal_recollection`,
`build_sustainable_writing_practice_around_real_constraints`,
`synthesize_literary_influences_into_voice`,
`preserve_exploratory_draft_variants_with_lightweight_labels`,
`decide_whether_and_how_to_seek_literary_representation`,
`creative_nonfiction_move_between_conversational_exploration_and_formal_argument`.

## Lane comparison at this date

```
metaskills              3 APs     2 patterns   100% claimed    3/3 APs name owners
writing                30 APs   169 patterns    84% claimed   30/30 APs name owners
art                    58 APs   370 patterns    45% claimed   41/58 APs name owners
software-engineering   31 APs   506 patterns    33% claimed   29/31 APs name owners
game-design             1 AP     30 patterns     0% claimed    0/1  AP names owners
```

---

# Third pass — 2026-09-03 — paraphrased delegations

The second pass proved two link-integrity properties (no edge without a naming
step, no named Pattern without an edge) and left a third unproven: an AP that
**paraphrases** a Pattern's decision instead of naming it satisfies both checks
and still leaves the Pattern unclaimed. One instance had been found by accident.
This pass went looking.

## Method, and what it was worth

A containment sweep — how much of each unclaimed Pattern's THEN vocabulary
appears in each of the lane's 254 AP steps — over every unclaimed Pattern.
It surfaced **one** of the five real delegations found this pass, plus one false
positive it still reports. Reading the candidate owner APs found the other four.

Record that honestly: the sweep is a weak instrument, because a paraphrase that
uses different words is exactly the case it cannot see, and that is the normal
case. It is worth running as a cheap first pass and worth nothing as an
assurance. The property is only established by reading the AP.

## Fixed — five paraphrased delegations

| AP | step | owner it was performing without naming |
|---|---|---|
| Design and Stress-Test a Life-Writing Project Contract | 4 "Set the truth contract" | `writing_choose_truth_contract_before_shaping_real_material` |
| Organize a Short Essay from Discovered Material | 3 chronology branch | `writing_creative_nonfiction_move_across_time_with_concrete_summary_and_brief_scenes` |
| Draft and Revise Short Creative Nonfiction | 7 portrayal audit — reached the decision through a **drill** rather than its Pattern | `writing_creative_nonfiction_portray_real_people_through_selective_behavioral_detail` |
| Revise a Creative Draft from Diagnosis to Final Proof | 8 editing gate | `writing_shape_sentence_rhythm_through_length_structure_and_punctuation` |
| Use a Writer's Notebook from Capture to Draft | 8 "only enough labeling to retrieve useful entries" | `writing_preserve_exploratory_draft_variants_with_lightweight_labels` |

The last is the clearest example of the class. Step 8 read "retain only enough
separation, labeling, or indexing to retrieve useful entries" against a Pattern
whose THEN reads "add only enough naming, grouping, summary, and version order to
retrieve and compare them." Same decision, different words, no edge — and below
the sweep's threshold precisely because the words differ.

**Lane now: 148 of 169 (87%), 247 `supports` edges, 30/30 APs naming owners.**

## The 21 remaining, reclassified

Every candidate owner AP named below was read this pass. The second pass's
"needs a read" category is now empty.

- **AP coverage gap, 5 patterns** — the missing experienced-work-history resume
  drafting AP. Unchanged from the second pass.
- **Smaller coverage gaps, 4** — job-board resume visibility, academic CV,
  performance poetry, and `writing_decide_whether_and_how_to_seek_literary_representation`.
  The last is **reclassified from local**: neither Research and Shortlist
  Publication Outlets nor Prepare and Send a Creative-Writing Submission Package
  has any step touching representation, and the Pattern's THEN is a procedure
  (verify fit, then compare candidates on sales, terms, relationship, conflicts)
  rather than a single decision. It is protocol-shaped and unowned.
- **Local decisions, 12** — the `poetry/forms` trio plus
  `poetry_sustain_intensity_beyond_meter_and_lineation`,
  `poetry_use_white_space_to_weight_language`,
  `balance_symbols_between_cliche_and_obscurity`,
  `control_irony_to_preserve_reader_trust`,
  `use_working_title_as_temporary_attention_cue`,
  `use_cultural_memory_to_complicate_personal_recollection`,
  `build_sustainable_writing_practice_around_real_constraints`,
  `synthesize_literary_influences_into_voice`, and
  `creative_nonfiction_move_between_conversational_exploration_and_formal_argument`.

  Two were confirmed against the specific AP most likely to own them and do not:
  `use_white_space_to_weight_language` against Revise Poetic Rhythm step 5, which
  delegates lineation to `break_lines_to_control_pace_and_expectation` — pace and
  pause, not the weighting of blank space; and
  `build_sustainable_writing_practice_around_real_constraints` against Use a
  Writer's Notebook step 1, whose gate is capture speed, not a practice contract
  fitted to obligations and energy.

## Not checked

`art` and `software-engineering` have never been swept for this class at all.

