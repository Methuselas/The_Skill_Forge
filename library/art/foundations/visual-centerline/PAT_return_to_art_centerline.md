---
object_id: PAT_return_to_art_centerline
object_type: pattern
name: Return to the Art Centerline
library_path:
- art
- foundations
- visual-centerline
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
- visual_art
- drawing_process
- image_generation
- staged_construction
- visual_continuity
- wu_sao
cross_links:
- rel: related_to
  target_object_id: AP_progress_artifact_through_ratified_steps
- rel: prerequisite_for
  target_object_id: AP_draw_a_figure_through_onion_skinned_stages
- rel: prerequisite_for
  target_object_id: AP_gate_staged_visual_work_by_approval
- rel: prerequisite_for
  target_object_id: PAT_calibrate_stage_information_density_against_precedent
reference:
  source_title: 'Guided Art Centerline: Registered Crescendo Construction'
  author: Blu + Admin
confidence: high
references: []
variants: []
---

# Return to the Art Centerline

## Pattern Rule
**IF** a task begins or resumes the creation, development, correction, or finishing of visual art
**THEN** distinguish internal stage reasoning from explicit staged production, and when visible staged artifacts exist recover the actual latest approved image in the conversation plus a compact textual carry before generating the next revision
**ELSE** when no approved visual artifact exists, establish the picture proposition before claiming staged continuity

## Do
- Treat **direct render** and **explicit staged production** as different delivery modes. Unless the user asks to see stages, use Drawing Stages 0–3 internally and surface the Stage 4 finished-pencil drawing when the requested artifact is a drawing; do not invent labels for intermediate images that were never generated.
- In explicit staged production, give every actually generated artifact a simple conversational stage/revision label such as `S0-r1`, `S1-r2`, or `S3-r1`. The label identifies the real image that appears beside it in the current conversation; it is not a filename, tool ID, database record, or claim of generator lineage.
- When a revision is approved, mark that exact conversational image as `APPROVED` and use it as the visual authority for the next stage. Rejected same-stage attempts increment the revision number.
- Carry two visual anchors after Stage 0: the **approved Stage 0 root**, which guards picture identity across cumulative drift, and the **latest approved stage**, which guards the current geometry and relationships.
- Carry a short text anchor beside those images. Record only load-bearing intent and permissions: what must remain true, what the current stage may change, what it may not change, and any major inventory that may not silently appear or disappear. The image carries geometry; the text disambiguates intent.
- Normalize ambiguous selection language once. If a four-option sheet is labeled A–D and the user says `#4/D`, resolve it to one canonical choice such as `D` and carry only that identifier forward.
- At Stage 0, ratify the **picture proposition**: camera/viewpoint, framing/crop, composition, major subject placement and apparent scale, dominant action read, large negative-space arrangement, broad value/light proposition, scene inventory, focal hierarchy, and story intent. A thumbnail may leave local anatomy, exact joints, precise surface shape, and fine design unresolved.
- At Stage 1, resolve a scene-wide structural skeleton inside that approved picture proposition: action lines, axes, joints, contacts, sparse object frames, perspective guides, and hidden paths for every important scene element. Improve structure without changing the selected picture or adding mass/rendering.
- At Stage 2, ratify complete minimum mass: silhouette, mass distribution, overlap, depth order, connected volume, and a structural placeholder for every major element intended for Stage 3.
- At Stage 3, realize specific form, design, anatomy, edge logic, intended detail hierarchy, and working light direction without changing the picture or exceeding the stage information ceiling.
- At Drawing Stage 4, finish the pencils. Stage 4 adds no new structural freeze and may not redesign an earlier commitment. Ink, Color, Paint, Manga/B&W finish, and other medium-specific operations are downstream workflows, not hidden Stage 4 permissions.
- Before recommending advancement, compare the current candidate against both anchors. Ask: does it prove the current stage's job, does it preserve the latest approved image, and does the accumulated result still reduce to the approved Stage 0 proposition?
- Distinguish repair classes. A **local current-stage defect** may be repaired as the next revision of that stage. A **centerline/composition defect** rolls back to the latest approved upstream stage that owns the violated property before retrying.
- When the host genuinely exposes the exact approved predecessor as an edit/continuation target, use it. For a registered-successor operation that requires exact image continuity, canonical identity alone is insufficient: if the exact accepted artifact is not available to the native tool, fail closed and recover/re-upload that artifact rather than regenerate a near-match. A re-upload restores the same canonical predecessor and lockset without reapproval. Never simulate or claim tool-level parentage that the host does not expose.

## Don't
- Do not generate each stage as a fresh interpretation of the original verbal prompt and call resemblance continuity.
- Do not treat conversational labels such as `S2-r1` as if they were persistent runtime IDs, tool parent IDs, hashes, filenames, or hidden state.
- Do not claim verified lineage, registered editing, or parent metadata unless the host actually exposes it.
- Do not let the original prompt override geometry already accepted in the approved visual anchors. The original prompt owns intent and explicit requirements; approved images own the developed picture.
- Do not let a later pass silently redesign camera, crop, subject scale/placement, dominant action, major negative spaces, hierarchy, or inventory already ratified at Stage 0.
- Do not use anatomy, texture, lighting, atmosphere, or polish to disguise a failure owned by an earlier stage.
- Do not advance because an image is attractive. A beautiful image that changes the approved picture is a failed stage.
- Do not overload the text carry with every descriptive preference. Keep only constraints that protect picture identity, stage purity, and the user's explicit requirements.

## Checklist
- Delivery mode is explicit: internal-stage direct render or visible staged production.
- Every visible staged artifact has an honest conversational `S#-r#` label; nonexistent internal stages have none.
- The exact approved Stage 0 root and latest approved stage are identifiable in the conversation.
- The compact carry states preserved properties, current-stage permissions, current-stage prohibitions, and major inventory when relevant.
- Stage 0 owns picture proposition; Stage 1 owns readable construction; Stage 2 owns complete minimum mass; Stage 3 owns specific rough/developed pencils; Stage 4 owns finished pencils.
- The newest candidate preserves the immediate approved anchor and still reduces to the approved Stage 0 proposition.
- Any drift is classified as local-stage repair or rollback to the owning upstream stage.
- No statement claims tool lineage beyond what the host actually exposes.

## Notes
Wu Sao remains the mnemonic: return to center before extending. In visible staged production, the practical centerline is not a simulated registry. It is the **actual approved image(s) still present in the conversation plus a compact prompt carry**.

The root and immediate-anchor distinction protects against two different failures. Comparing only with the latest stage can allow small changes to accumulate until the final no longer matches the chosen composition. Comparing only with Stage 0 can preserve the concept while allowing current geometry to wander. Use both.

The portable short form is: **user intent → approved Stage 0 root → latest approved stage → current-stage permissions.**
