---
name: visual-art
description: >-
  Use for drawing, illustration, visual composition, figure or animal drawing,
  gesture, construction, anatomy, heads, hands, perspective, rendering, art
  critique, and guided visual-art teaching in this repository.
---

# Visual Art

## User help command

Treat `Help Art` and clear variants such as `Help Art staged`, `Help Art modes`, `Help Art revisions`, `Help Art references`, or `Help Art approval` as non-productive help commands. Do not generate/edit an image, change mode, ratify/reject an artifact, advance/rollback the staged workflow, or otherwise mutate production state merely because help was requested. Read `docs/ART_HELP.md` and answer from that user-facing contract. If the user separately issues a production or mode command in the same turn, follow the explicit command after answering the requested help where practical.

Use the trained Art library as canonical knowledge. Books are study material;
the accepted PASS cards and teacher corrections are the working curriculum. The
cards stand on their own — never reach for a source book to apply one.

## Load order

1. `library/metaskills/INDEX.md`
2. Relevant shared drawing systems under `library/art/drawing/`
3. Relevant subject under `library/art/subjects/`
4. Follow `foundation_object_id` and `prerequisite_for` relationships even when
   the prerequisite lives in a different folder.
5. For open-ended production, load the visual-centerline foundation under
   `library/art/foundations/visual-centerline/`. For explicit approval-gated production,
   load `AP_progress_artifact_through_ratified_steps`, then the owning domain adapter:
   `AP_gate_staged_visual_work_by_approval` for Drawing or
   `AP_gate_visible_color_development_by_approval` for approval-gated Color. Load only
   the Art AP that owns the current legal operation, and load
   `AP_prepare_artifact_only_image_generation_handoff` immediately before native image
   generation. PASS may reason in workflow terms, but do not restate controller,
   stage, approval, rollback, or future-operation terminology in the productive
   pre-generation context; orient the generator only toward the current artifact contract.

Classify the turn from meaning: discuss, inspect, or produce. Do not generate or
edit an image unless the user actually asks for production. During PASS training,
work one source chapter at a time, discuss after the read, and ask questions only
when genuine uncertainty remains.

## Art production routing contract

Resolve the latest explicit Art mode directive **before any productive image call**. `Mode: staged` and `Mode: direct` are preferred control language; also recognize equivalent clear intent such as “in stages,” “staged composition,” “start with thumbnails,” “thumbnail-first,” “direct render,” “single final,” or “one-shot final.” The latest explicit mode directive is sticky across later Art turns until the user changes it, explicitly exits the staged thread, or that thread completes.

**Routing priority is hard:** an active staged mode overrides the ordinary direct-render default. Merely acknowledging `Mode: staged` in prose is not sufficient. While staged mode is active, a normal direct/final image call is illegal. Resolve the owning domain thread before production. For Drawing, no explicitly ratified composition root means only `AP_run_stage0_rough_composition_search` is legal; an explicitly ratified Stage 0 permits only `AP_build_stage1_scene_skeleton`, then Stage 2, Stage 3, and Stage 4 in order. For an explicit approval-gated Color continuation from an authoritative Drawing, use `AP_gate_visible_color_development_by_approval`: with no approved Broad Color Direction only `AP_establish_broad_color_direction_from_authoritative_drawing` is legal, and approval of that exact artifact permits exactly one successor, `AP_develop_approved_color_direction_to_color_completion`. Do not infer that Drawing automatically enters Color after Stage 4, and do not impose either thread's operation count on another Art domain. Assistant preference, praise, silence, or revision instructions never manufacture ratification.

Mode and stage words are controller vocabulary for PASS. Consume them during routing; do not repeat them in the productive pre-generation context for native image generation.

Before any image call that depends on user-supplied **golden truth**, inspect the supplied reference package first. Resolve the relevant visual sheets plus explicit rules/specs and establish the immutable canon anchors before production. If the authoritative package cannot be read or its relevant contents cannot be resolved, do not generate and do not claim the character/design is locked. Low-information artifacts may withhold surface detail, but they may not redesign the authority they are withholding.

For every native image call in active staged mode, apply this call barrier in order: (1) confirm staged mode is still active; (2) confirm any required golden-truth preflight is complete; (3) determine the single legal current domain Art AP from explicit user ratification; (4) for any successor after the first approved artifact, register the exact predecessor with `PAT_develop_scene_through_registered_successors`; (5) when the authorized operation requires edit/reference continuity, confirm that the **exact canonical predecessor is actually accessible to the native image tool**. Canonical identity alone is not enough. If exact-source access fails, fail closed and recover/request a re-upload of that exact accepted artifact; do not reconstruct from prose, use a rejected image, or generate a near-match. A user re-upload restores access to the same canonical predecessor and lockset without reapproval; (6) compile only the current AP's Productive Image Contract through `AP_prepare_artifact_only_image_generation_handoff`; (7) make one current-artifact call and stop for the user gate. If any prerequisite is unresolved, do not fall through to direct render.

For productive Art requests in direct mode, keep the relevant visual development internal and return only the requested artifact. For a Drawing request, internalize Drawing Stages 0–4 with Stage 4 = Finished Pencils. If the user requests a downstream medium such as Ink, Color, Paint, or Manga/B&W finish, do not redefine Drawing Stage 4. When an approved Drawing predecessor exists, route only into a downstream AP whose entry contract is legal for that predecessor and can preserve its inherited lockset; subject similarity alone does not make an AP applicable. An owning downstream AP may still define a legitimate root or alternate entry that begins without manufacturing Finished Pencils. If no successor-safe AP exists, use an honest Pattern-chain fallback when coverage is sufficient or stop rather than route through an illegal root workflow. For general Color development from an authoritative Drawing predecessor, route to `AP_develop_approved_drawing_into_coherent_color_image`; its dependency gates preserve the inherited Drawing lockset while coordinating accepted Color and Rendering owners. This is one orchestration AP, not a ratified visible Color-stage thread. After rendering, inventory every visible instance named by the activated risk checks and inspect both the full image and each risk region at local/enlarged scale. Checking one representative hand, foot, prop contact, or joint does not clear the other visible instances. Any materially represented articulated limb in a pose/action context activates `AP_audit_articulated_limb_identity_and_joint_mechanics`. Resolve the expected limb-chain topology from explicit prompt/specification, authoritative visual reference, accepted construction, or established character/body-plan continuity before judging the artifact; do not hardcode a two-arm/two-leg count when the subject establishes another topology. Record anatomical or body-plan identity separately from screen location, trace every audited chain from its declared parent origin through ordered joints to the expected endpoint type, inspect visible joint mechanics locally, and record expected versus observed origin/endpoint types plus a range class of `ordinary`, `extreme_but_plausible`, or `impossible`. A connected limb is not sufficient evidence: endpoint substitution, chain exchange through overlap, shared joint/endpoint ownership, a reversed visible human hinge, impossible range, or materially visible mechanics that remain indeterminate forbids completion. Rebuild the entire affected chain from parent origin through each joint to the endpoint rather than repainting only the terminal form or joint, then re-audit all materially represented limb chains because regeneration can disturb another chain. Any materially visible human or humanoid hand activates `AP_construct_hand_from_function_contact_and_articulated_form`. Resolve the expected hand topology from explicit prompt/specification, authoritative visual reference, or established character continuity before constructing digits. If authoritative sources disagree about a numeric topology contract, normalize only unambiguously equivalent wording; otherwise fail closed instead of choosing one count. If none of those establishes a different anatomy and the subject is otherwise humanlike, use a provisional humanlike fallback of four long fingers plus one thumb; never let that fallback override known nonhuman, stylized, altered-digit, or altered-joint anatomy. Apply the AP's topology, root-chain, mechanical-attainability, and rendering-preservation gates to each hand independently before accepting the render. For every materially visible hand at a stage/resolution where full digit topology is legal, create a separate evidence record: identify the hand and location, record expected and observed topology/count, inspect a local/enlarged view, and trace every observed digit branch to one unique palm root. `uncertain`, insufficient evidence, any extra/missing/fused/untraceable branch, or any unrecorded visible hand forbids completion. A global boolean such as `all hands valid = true` is never sufficient. When overlap or foreshortening makes digit identity risky, prefer the palm-wedge owner's deepest-to-nearest digit-construction variant so hidden chains are solved before nearer contours occlude them. When a rigid object constrains a hand, additionally load the hand function/contact owner and verify the object axis, palm facing, topology-appropriate opposable digit behavior, active/support digit roles, palm contact, wrist axis, and forearm chain before accepting the render.

## Staged Art routing contract

Treat `Mode: staged` and `Mode: direct` as explicit Art routing commands. The latest explicit mode remains active across subsequent Art turns until the user changes it or the active visible thread is completed/exited. While staged mode is active, ordinary direct-render routing is illegal. The active domain supplies the legal operation thread: Drawing uses its ratified Stage 0–4 sequence; approval-gated Color uses Broad Color Direction → Color Development / Completion. Rejection remains at the owning current operation unless an upstream commitment must be reopened.

Before each productive staged image call, resolve golden-truth references first when supplied, identify the single legal current Art AP, classify any pending rejection, and use `AP_prepare_artifact_only_image_generation_handoff` so the native image task describes only the current artifact. Do not repair rejected pose/composition/stage-density decisions by increasing polish. After approval, use `PAT_develop_scene_through_registered_successors` so figures, weapons, props, architecture, terrain, signs, pipes, cables, and other important scene objects develop from the exact accepted predecessor when the host exposes edit/reference continuity.

Keep mode/stage/process vocabulary on the PASS side. Native image generation should receive only the artifact form, preserved properties, permitted visual vocabulary, withheld information, identity visibility, layout constraints, and stop condition.

Art is an independent lane. Authoring Art never requires inspecting or modifying
Writing or Software Engineering.

The numbered visual Stages remain the **Drawing-specific** thread: rough composition proposition →
scene skeleton → complete mass block → specific rough / developed pencils → finished pencils.
Approval-gated **Color** supplies a separate named thread: Broad Color Direction → Color Development / Completion.
Search/Control is an operating mode, not a replacement for either domain thread. In
interactive approval-gated production, only explicit user approval may ratify the current artifact or
unlock the next operation. After surfacing any artifact, explicitly prompt the user
with that operation's legal next actions rather than a generic invitation to continue. At terminal Color completion, a bare `Continue` closes Color; it does not invent Painting, Ink, Manga/B&W, watercolor, or another successor medium.

When visible approval-gated production is active, ordinary direct-render routing is illegal until the active domain thread is explicitly exited or completed. Only the first legal operation of that domain thread may run before ratification. After an artifact is ratified, apply `PAT_develop_scene_through_registered_successors`: every later visible artifact develops from the exact approved predecessor whenever the host exposes that predecessor as an edit/reference target, and continuity applies to figures, weapons, props, architecture, terrain, signs, pipes, cables, Color direction, and other important approved visual commitments. For Color, once Broad Color Direction is approved, the required predecessor for Color Development is that exact Color artifact rather than the original Drawing. The prose brief remains a constraint source, not a substitute visual source. Do not independently restart later artifacts from an earlier prompt or predecessor.

For registered-successor operations, distinguish **canonical state** from **native edit-target availability**. If the exact accepted predecessor is not exposed to the native image tool and the requested operation depends on editing/reference continuity, generation is illegal until that exact artifact is recovered or re-uploaded. Loss of edit-target access never authorizes visual reinterpretation.

For native image generation, workflow vocabulary is controller-only. After resolving
the current visual operation, do not echo terms such as numbered stages, staged
production, process progression, Search/Control, approval, rollback, or future steps
in the productive pre-generation context. Use the current AP's Productive Image
Contract and describe only the artifact that should visibly exist now.


The final visual operation of the universal **Drawing** AP is finish-only **finished pencils**: clean and resolve the exact approved Stage 3 predecessor in pencil without changing camera, crop, major pose/orientation, subject scale, perspective structure, major environment masses, path geometry, object placement, major overlaps, negative spaces, or scene inventory. Do not introduce color, paint, ink, manga tones, or other downstream medium finish as Drawing Stage 4. When an approved Drawing predecessor exists, a downstream registered successor inherits that completed Drawing lockset and may not silently reopen it; if the selected downstream AP explicitly defines a legitimate root or alternate entry, it may begin without requiring a manufactured Finished-Pencils predecessor.
