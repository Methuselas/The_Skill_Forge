# Handoff — Bring the Art drill Success Checks up to schema

**For:** the Art project (GPT), authoring against `.agents/skills/visual-art/SKILL.md`
**Scope:** the `## Success Check` section of the 119 drills under `library/art/`. Nothing else.
**Status of the other lanes:** software-engineering (71 drills) and writing (73 drills) have already had this pass. Art is the last one.

---

## 1. What changed, and why this is now a schema matter

`PASS/docs/PASS_SCHEMA.md` previously constrained drill body sections by **name and order only**. It said nothing about what a Success Check had to contain, and `PASS/templates/DRILL_OBJECT_TEMPLATE.md` offered a single bullet reading `<specific observable outcome>`.

The predictable result, across all three lanes, was a library of checks that **any completed attempt satisfies**. A drill whose check cannot fail is not measuring anything — it is a description of the exercise with a tick beside it.

The schema now specifies the contract. This is the text to work against:

> `Success Check` is a closed list of conditions a reader other than the runner can
> check after the fact. The section as a whole has to be able to fail; one that any
> completed attempt satisfies is the bug rather than the drill. Three requirements
> make it able to fail:
>
> - **The property under test may not serve as its own evidence.** Where a drill
>   turns on a test that would fail, an interference that would occur, or a change
>   that would leave something intact, the check requires that it was run, produced,
>   or applied. A prediction recorded in place of an observation reads as complete
>   and establishes nothing.
> - **At least one bullet excludes a named plausible near-miss** that would otherwise
>   satisfy the section. The working form is to state the cheap answer and say what
>   it demonstrates, rather than to describe the correct answer more emphatically.
> - **Where the drill ends in a choice, the check asks for the reason rather than
>   the selection**, so the run produces a defensible decision instead of a
>   preference.
>
> A bullet requiring an output the work alone does not produce satisfies the second
> requirement by a different mechanism — a name that would have been accepted had it
> been read in place, a model not previously made explicit, a rejected candidate with
> the observation that disqualified it. These resist fabrication because performing
> the exercise does not hand them over.
>
> Length is not the contract and is a poor proxy for it. A compressed check can
> discriminate better than a long one, and padding a section that already
> discriminates dilutes the bullets doing the work. Register belongs to the package:
> a procedural lane and a critical lane phrase the same requirement differently and
> both are correct.

---

## 2. Where the Art lane currently stands

Measured across all 119 art drills:

| | |
|---|---|
| drills | 119 |
| median Success Check | 64 words |
| shortest | 12 words |
| longest | 117 words |
| carrying an exclusion clause | 88 |
| carrying a required-output bullet | 13 |
| **carrying neither mechanism** | **30** |

By family: `subjects` 69, `foundations` 12, `composition` 9, `rendering` 8, `color` 8, `perspective` 7, `drawing` 5, `painting` 1.

The lane is **not uniformly weak**. 88 of 119 already carry an exclusion clause, and many of those are good. The work is concentrated in the 30 listed in section 5, plus a judgement pass over the rest.

---

## 3. The standard comes from inside the Art lane

Do **not** import the phrasing from the software-engineering or writing lanes. Their register is wrong here — one is procedural, the other is compressed-critical. Art's own strongest checks already define the target: **five to seven bullets, roughly 100–120 words, each bullet naming a property the artifact must exhibit and excluding the plausible substitute, phrased in the lane's construction vocabulary.**

These three are the exemplars. Match what they do.

### `rendering/DRILL_compare_same_subject_across_medium_behaviors` (105w)

```
- The calibration strip reveals each candidate route's usable intensity, controllable range, layering behavior, and ground interaction before the subject comparison begins.
- The three studies differ because of medium behavior, not because the underlying animal mass changed.
- At least one soft or irregular treatment uses controlled surrender of edge precision rather than accidental mess.
- The chosen final route implies the target coat or skin quality with fewer literal marks than a hair-by-hair or crack-by-crack copy.
- You can explain why the selected process offers the right tradeoff between control, speed, freshness, texture character, and line-weight range when line behavior is being tested.
```

### `subjects/animals/construction/DRILL_construct_contrasting_big_cat_poses_from_studied_anatomy` (106w)

```
- The crouch and stretch read as clearly different actions before fur, texture, or rendering is added.
- Trunk curvature organizes the pose instead of functioning as an outline drawn after the limbs.
- Shoulder/scapular placement and hindleg folding support the action rather than floating independently of the torso.
- Forearm rotation, paw fan, digit direction, and claw state remain consistent with the studied carnivore construction.
- Near forearm/paw enlargement strengthens recession without producing a disconnected oversized terminal form.
- The stretching pose remains nonthreatening when the intended head cues are added.
- A failed read is corrected in the block rather than hidden by finish.
```

### `subjects/figure/heads/DRILL_rebuild_complex_facial_features_from_support_to_cover` (117w)

```
- Each feature reads as a solid before shading or texture is added.
- The difficult views show believable changes in overlap, underplane exposure, and wrapping.
- Eye lids wrap a globe; nose parts belong to one wedge; lips ride a mouth/dental mass; the ear has a shell/bowl depth rather than a flat C symbol.
- A near-front nose can recover projection from light/shadow evidence without turning the shadow itself into a symbolic contour, and the inferred depth remains consistent with other available views.
- When transferred back to a head, the feature agrees with the head's turn and tilt.
- The memory redraw preserves the support relationship even if local contour details differ from the source.
```

**What makes these work.** Every bullet names something a second person can look at the drawing and check. Each one pairs the requirement with the substitute it rules out — *an outline drawn after the limbs*, *accidental mess*, *a flat C symbol*, *a hair-by-hair copy*, *hidden by finish*, *a disconnected oversized terminal form*. That pairing is the whole technique. The bullet is not "the pose reads well"; it is "the pose reads well **and here is the specific way it could look like it does without doing so**."

---

## 4. What a failing check looks like

The four weakest in the lane, verbatim:

```
- The final motion is more flexible without losing the main action.          (12w)
- The versions feel meaningfully different even though duration and
  endpoints are unchanged.                                                   (13w)
At least one correction makes edge forms more plausible without breaking
the shared vanishing structure.                                              (15w)
- The variants remain recognizable as the same underlying step structure
  but express different character.                                           (15w)
```

Each is a restatement of the drill's goal. Nobody who finished the exercise would conclude they had failed. "Feel meaningfully different" and "express different character" are judgements only the maker can render, which is exactly the property the schema now forbids.

The repair is to ask: **what could someone produce that satisfies this sentence while having done the exercise badly?** Then write that into the check as the excluded case. For the spacing drill, a person can produce two versions that differ because they secretly changed the endpoints, or that differ only in a way visible on the chart and not in playback. Both belong in the bullets.

---

## 5. Worklist — the 30 with neither mechanism

These are the priority. Paths are relative to `library/art/`.

```
  12w  subjects/animation/motion/DRILL_build_flexible_action_with_successive_joint_and_phase_offsets.md
  13w  subjects/animation/timing/DRILL_hold_timing_constant_and_compare_spacing_profiles.md
  15w  perspective/DRILL_subdivide_a_plane_without_screen_space_guessing.md
  15w  subjects/animation/motion/DRILL_generate_walk_variants_from_fixed_contact_positions.md
  17w  foundations/mark-making/DRILL_copy_then_emulate_master_mark_language.md
  19w  perspective/DRILL_project_circles_and_cylinders_on_tilted_planes.md
  23w  composition/DRILL_generate_composition_variations_inside_fixed_frame.md
  23w  foundations/mark-making/DRILL_practice_deliberate_brush_line_control.md
  25w  composition/DRILL_isolate_and_recombine_depth_cues_on_one_scene.md
  25w  perspective/DRILL_aim_clean_perspective_construction_lines.md
  25w  perspective/DRILL_place_freehand_ellipses_on_minor_axes.md
  26w  foundations/observation/DRILL_train_observation_with_look_hold_draw_and_blind_bursts.md
  26w  subjects/figure/construction/DRILL_trace_underarm_curve_bent_and_extended.md
  32w  subjects/figure/construction/DRILL_block_connected_torso_masses_across_views.md
  35w  subjects/figure/construction/DRILL_build_overlap_sequences_from_complete_and_partial_forms.md
  37w  subjects/figure/construction/DRILL_unify_one_foreshortened_figure_three_ways.md
  38w  subjects/figure/construction/DRILL_trace_joint_connections_across_camera_angles.md
  42w  subjects/figure/heads/DRILL_rotate_cranial_ball_and_facial_wedge.md
  43w  drawing/rendering/DRILL_build_full_tonal_drawing_from_value_sketch_and_relational_checks.md
  44w  subjects/figure/hands/DRILL_contrast_hand_and_foot_wedge_construction.md
  45w  subjects/figure/construction/DRILL_classify_and_build_s_and_b_leg_rhythms.md
  45w  subjects/figure/construction/DRILL_solve_hidden_limb_with_minimum_construction.md
  46w  subjects/figure/construction/DRILL_diagnose_joint_interlock_by_reversing_depth.md
  50w  subjects/figure/gesture/DRILL_design_about_to_pose_from_support_shift.md
  52w  subjects/figure/construction/DRILL_rotate_one_limb_cylinder_while_holding_width.md
  62w  subjects/animals/anatomy/DRILL_build_animals_from_pivot_skeletons_to_main_forms.md
  62w  subjects/figure/heads/DRILL_compare_master_heads_for_invariant_structure.md
  65w  subjects/figure/heads/DRILL_map_facial_wrinkles_by_flow_and_cause.md
  68w  subjects/figure/heads/DRILL_build_living_head_over_constructed_skull.md
  74w  foundations/observation/DRILL_pair_sustained_studies_with_regular_quick_sketching.md
```

After those, pass over the remaining 89 and ask of each only: *can this fail?* Most will already be fine.

---

## 6. Method

For each drill:

1. Read its `## Practice Task` and `## Instructions` first. The check has to be about **this** exercise; a generic construction check could be pasted into forty of these files and would be worthless in all of them.
2. Ask what a bad-but-complete attempt would look like, and what its maker would honestly be able to claim.
3. Write four to seven bullets, each naming an observable property of the artifact **paired with the substitute it excludes**.
4. Where the drill ends in a selection — a chosen route, a chosen order, a chosen treatment — require the reason, not the choice.
5. Where the drill turns on a comparison or a test, require that it was actually performed. "The versions differ" becomes "both versions were played back at the same duration and the difference was visible in playback rather than only on the chart."

---

## 7. Do not

- **Do not target a word count.** This was got wrong twice during the software-engineering pass. Length is a symptom, not the goal. A tight 70-word check that excludes three real near-misses beats a 160-word one that restates the task at length.
- **Do not pad a check that already discriminates.** Several short ones in this lane are already doing their job. In the writing lane, ten checks between 73 and 78 words were deliberately left alone for exactly this reason, and inflating them would have diluted the bullets that were working.
- **Do not import another lane's voice.** Art's register is construction vocabulary about an artifact. Keep it.
- **Do not touch `## Practice Task`, `## Target Skill`, `## Setup`, `## Instructions`, `## Common Failures`, or `## Notes`.** This pass is the Success Check only. If a drill's instructions look wrong, note it separately rather than fixing it here.
- **Do not use angle brackets anywhere in a card body.** The validator rejects them outright (they are reserved for template placeholders). This bites when writing things like a range or a comparison — spell it in words.
- **Do not add or remove section headings.** The schema is closed and the heading set is fixed.

---

## 7b. A second, separate defect — conditions no single sitting can close

Found by sweeping all three lanes after this handoff was first written, so it is an addition
rather than part of the original brief.

Some Success Check bullets require something that cannot happen during the run: a later
repetition, a comparison across a cycle of days, a card that stays retired for weeks, a
distribution that shifts when the exercise is repeated in another context. Phrased plainly,
every honest single run scores them as a miss, forever. Phrased as deferred, they become
discriminating instead — because claiming them *on the day* is itself the failure. A run
reporting that a card stayed retired the same afternoon has measured nothing, and one
reporting that the distribution shifted without having worked in the second context has put
a prediction where the evidence goes.

Six were repaired this way across the software-engineering and writing lanes. The fix is a
clause appended to the existing bullet, not a new bullet:

> Repeating the exercise in a less familiar language shifts the distribution, confirming the
> phases track the skill-in-context rather than you. **This is the condition a single session
> cannot close. Predicting the shift is not observing it, and a run reporting that the
> distribution moved without having worked in the second context has put the prediction where
> the evidence goes.**

**In the art lane a keyword sweep surfaced 20 candidate bullets, and most are false
positives.** `later`, `repeat`, and `repeated` are ordinary words there — "repeated generic
ovals", "one repeated template" — describing properties of a single drawing that are
perfectly checkable on the day. Only bullets naming something that happens *after this
sitting* qualify. From the wording alone these look like the real ones, but each needs
confirming against its own Practice Task before being touched:

```
trace_surface_paths_over_wrapped_forms             "improves later anatomy/contour placement"
infer_execution_sequence_from_unfinished_artwork   "improves future workflow inference"
keep_animators_sketchbook_of_transient_everyday_observation  (both bullets: a sketchbook accumulates)
sculpt_and_light_invented_form_for_rendering       "corrected in later imagination drawing"
make_many_observational_studies_of_your_own_hand   "easier to see through repetition"
calibrate_animal_proportion_from_measurement_to_estimation   "later estimated studies" (check: may be within-run)
```

The scan that produced them, to re-run after any edits — judge every hit by hand, because it
cannot tell a future sitting from an adjective:

```python
import io, re, glob, os
long_re  = re.compile(r"\b(later|a week|weeks|over time|repetition|repeat\w*|next time|"
                      r"subsequent\w*|eventually|across (?:several |multiple )?(?:sessions|entries|days)|"
                      r"stay retired|keep returning|revisit|periodic\w*|daily)\b", re.I)
defer_re = re.compile(r"single sitting|cannot close|deferred|on the day|in the same session|"
                      r"falls outside this sitting|waits on", re.I)
for f in glob.glob("library/art/**/DRILL_*.md", recursive=True):
    s = io.open(f, encoding="utf-8").read()
    m = re.search(r"^## Success Check\n(.*?)(?=^## )", s, re.S | re.M)
    if not m:
        continue
    for b in m.group(1).strip().split("\n- "):
        b = b.lstrip("- ").strip()
        if b and long_re.search(b) and not defer_re.search(b):
            print(os.path.basename(f)[6:-3]); print("   " + b[:130])
```

## 8. Verification

Structural check — must stay clean:

```bash
python PASS/tools/validate.py --package art
```

Progress measurement — re-run to see coverage move:

```bash
python - <<'PY'
import io,re,glob,os
excl=re.compile(r"rather than|not merely|without being|not mere|instead of|not only|does not|never|not the same",re.I)
req=re.compile(r"at least one|recorded|written down|is stated|is named|attempted|actually",re.I)
rows=[]
for f in glob.glob("library/art/**/DRILL_*.md",recursive=True):
    s=io.open(f,encoding="utf-8").read()
    m=re.search(r"^## Success Check\n(.*?)(?=^## )",s,re.S|re.M)
    if not m: continue
    sc=m.group(1).strip()
    rows.append((len(sc.split()), bool(excl.search(sc)) or bool(req.search(sc)),
                 os.path.relpath(f,"library/art").replace("\\","/")))
ws=sorted(r[0] for r in rows)
print(f"{len(rows)} drills | median {ws[len(ws)//2]}w | neither mechanism: {sum(1 for r in rows if not r[1])}")
for w,ok,r in sorted(rows):
    if not ok: print(f"  {w:>4}w  {r}")
PY
```

Target: **zero** drills reported with neither mechanism. Median will rise as a side effect; it is not the goal.

Full suite, if the repo is available:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

---

## 9. One caveat worth carrying

None of the rewritten checks in any lane has yet been run against. The software-engineering ones were graded blind before the rewrite — 8 clean, 3 short — and the rewrite was informed by exactly where the loose bullets let a mediocre answer through. Whether the new checks actually catch more is untested. If the Art project can run a few of these drills blind after the pass, answering to a file before opening the check, that is the measurement that would confirm the work.
