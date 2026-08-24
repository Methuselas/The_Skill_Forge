"""Repository tests for the SkillForge resolver.

These prove repository-side behavior only: that profiles parse, that a given
request string resolves to a given mode and lane, that declared checks are
reported, that profile card references resolve, and that the completion audit
reports what a record omits.

They prove nothing about a live host. Mode Lock, Stage Lock, Visual Lock,
exact-predecessor accessibility, one-approval-one-transition, and no-silent-
fallback-to-Direct are model- and host-dependent, and only live regression
testing of an installed skill can show whether they held. Tests named
`test_art_profile_declares_*` assert what the YAML says, not what any host does.
"""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_PATH = ROOT / "PASS" / "runtime" / "skillforge_runtime.py"
SPEC = importlib.util.spec_from_file_location("skillforge_runtime", RUNTIME_PATH)
assert SPEC and SPEC.loader
runtime = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runtime)

PROFILE = runtime.read_yaml(ROOT / "PASS" / "runtime" / "profiles" / "art.yaml")
LIBRARY = ROOT / "library"


class SkillForgeRuntimeTests(unittest.TestCase):
    def test_default_art_request_is_stage_informed_direct(self):
        result = runtime.resolve_task(PROFILE, LIBRARY, "Draw a cyberpunk city scene.")
        self.assertEqual(result["mode"], "direct_render")
        self.assertFalse(result["contract"]["stage_artifacts"])
        self.assertTrue(result["contract"]["apply_stage_knowledge"])
        self.assertTrue(result["contract"]["post_render_verification"])

    def test_art_profile_declares_terminal_artifact_only_for_explicit_stage4(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY, "No stages. Go directly to stage 4 for Drawing Finished Pencils."
        )
        self.assertEqual(result["mode"], "direct_render")
        self.assertFalse(result["contract"]["stage_artifacts"])
        self.assertEqual(
            result["contract"]["external_stage_artifacts"],
            "requested_terminal_artifact_only",
        )
        review = result["contract"]["risk_region_review"]
        self.assertTrue(review["enumerate_all_visible_instances"])
        self.assertTrue(review["inspect_full_frame_and_local_scale"])
        self.assertFalse(review["representative_sampling_allowed"])

    def test_explicit_mode_directive_routes_staged(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY, "MODE Staged\nDraw Blu in a cyberpunk alley."
        )
        self.assertEqual(result["mode"], "staged_production")
        self.assertTrue(result["contract"]["approval_gates"])

    def test_finished_terminal_goal_does_not_override_explicit_staged_mode(self):
        request = """MODE Staged
Draw Blu in an extremely dynamic, acrobatic full-body action pose.
The character design itself must be the character in the Blu_ref_sheets.zip
Generate one finished full-character image."""
        result = runtime.resolve_task(PROFILE, LIBRARY, request)
        self.assertEqual(result["mode"], "staged_production")
        self.assertEqual(result["current_stage"], 0)
        self.assertTrue(result["contract"]["terminal_goal_language_does_not_change_active_mode"])
        self.assertTrue(result["contract"]["authoritative_reference_preflight_required"])

    def test_sticky_staged_mode_must_be_reapplied_to_stateless_resolver(self):
        request = """Draw Blu in an extremely dynamic full-body action pose.
Generate one finished full-character image."""
        result = runtime.resolve_task(PROFILE, LIBRARY, request, explicit_mode="staged")
        self.assertEqual(result["mode"], "staged_production")
        self.assertEqual(result["current_stage"], 0)
        self.assertTrue(result["contract"]["stateless_resolver_requires_active_mode_override"])

    def test_ref_sheets_filename_activates_stage0_character_reference_lock(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY,
            "MODE Staged. The character design must match Blu_ref_sheets.zip.",
        )
        self.assertEqual(result["mode"], "staged_production")
        self.assertIn("body-plan and proportion anchor lock", result["risk_checks"])
        self.assertIn("broad silhouette identity lock", result["risk_checks"])
        self.assertNotIn("character identity and face lock", result["risk_checks"])

    def test_explicit_mode_directive_routes_direct(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY, "MODE Direct\nDraw Blu in a cyberpunk alley."
        )
        self.assertEqual(result["mode"], "direct_render")
        self.assertFalse(result["contract"]["stage_artifacts"])

    def test_plain_do_it_in_stages_routes_to_staged_production(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY, "Draw me a red dragon flying over a forest during the day. Do it in stages."
        )
        self.assertEqual(result["mode"], "staged_production")
        self.assertTrue(result["contract"]["approval_gates"])
        self.assertTrue(result["contract"]["stage0_root_anchor_required"])
        self.assertTrue(result["contract"]["one_successor_artifact_per_approval"])

    def test_training_or_drill_routes_to_staged_production(self):
        result = runtime.resolve_task(PROFILE, LIBRARY, "Give me a figure drawing drill for this pose.")
        self.assertEqual(result["mode"], "staged_production")
        self.assertEqual(result["contract"]["stage_thread_scope"], "drawing")
        self.assertEqual(result["contract"]["sequence"], [0, 1, 2, 3, 4])
        self.assertEqual(
            result["contract"]["stage_ap_thread"][4],
            "AP_finish_stage4_as_finished_pencils",
        )
        self.assertTrue(result["contract"]["approval_gates"])
        self.assertTrue(result["contract"]["rollback_enabled"])

    def test_art_profile_declares_artifact_only_handoff_contract(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY,
            "Draw Blu in a cyberpunk alley. I want this to be a staged composition."
        )
        self.assertEqual(result["mode"], "staged_production")
        contract = result["contract"]
        self.assertEqual(
            contract["image_generation_handoff"],
            "AP_prepare_artifact_only_image_generation_handoff",
        )
        self.assertTrue(contract["productive_workflow_vocabulary_suppressed"])
        self.assertTrue(contract["current_artifact_only"])
        self.assertEqual(contract["multi_step_presentation_default"], "forbidden")
        self.assertTrue(contract["staged_mode_persistent_until_exit_or_completion"])
        self.assertTrue(contract["direct_render_fallback_forbidden_while_staged"])
        self.assertTrue(contract["rejection_never_advances"])
        self.assertTrue(contract["invalid_artifact_cannot_anchor_successor"])
        self.assertTrue(contract["registered_successor_required_after_approval"])
        self.assertTrue(contract["stage0_structural_divergence_required"])
        self.assertTrue(contract["stage0_prefer_separate_candidate_images"])
        self.assertEqual(contract["stage0_candidate_budget_owner"], "controller_only")
        self.assertEqual(contract["stage0_native_generation_unit"], "one_candidate_per_call")
        self.assertTrue(contract["stage0_native_multi_output_forbidden"])
        self.assertTrue(contract["stage0_image_facing_batch_vocabulary_forbidden"])
        self.assertTrue(contract["stage_aware_risk_resolution_required"])

    def test_art_profile_declares_stage_handoff_prompts(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY, "Draw me a red dragon flying over a forest during the day. Do it in stages."
        )
        contract = result["contract"]
        self.assertTrue(contract["stage_handoff_prompts_required"])
        self.assertTrue(contract["stage_legal_next_actions_advertised"])
        prompts = contract["stage_handoff_prompt_map"]
        self.assertIn("Select the thumbnail you like", prompts[0])
        self.assertIn("Approve this structure to continue", prompts[1])
        self.assertIn("Approve this mass block to continue", prompts[2])
        self.assertIn("Approve this rough realization to continue", prompts[3])
        self.assertIn("Finished Pencils", prompts[4])
        self.assertIn("approve the Drawing as complete", prompts[4])

    def test_teach_lane_is_independent_from_execution_mode(self):
        # `lane` is card-level semantics: it distinguishes an instructional
        # request from a production one and is orthogonal to execution mode. It
        # does not route into a Teaching package — no domain depends on one.
        teaching = runtime.resolve_task(PROFILE, LIBRARY, "Teach me how to draw this head.")
        self.assertEqual(teaching["lane"], "teach")
        self.assertEqual(teaching["mode"], "direct_render")

        ordinary = runtime.resolve_task(PROFILE, LIBRARY, "Draw this head.")
        self.assertEqual(ordinary["lane"], "skill")
        self.assertEqual(ordinary["mode"], "direct_render")

    def test_resolution_exposes_no_teaching_package_routing(self):
        result = runtime.resolve_task(PROFILE, LIBRARY, "Teach me how to draw this head.")
        self.assertNotIn("teaching", result)
        packages = {
            item["package"]
            for phase in ("pre_production", "post_production")
            for item in result["metaskills"][phase]
        }
        self.assertEqual(packages - {"metaskills"}, set())

    def test_explicit_mode_override_wins(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY, "Give me a figure drawing drill for this pose.", explicit_mode="direct"
        )
        self.assertEqual(result["mode"], "direct_render")
        self.assertIn("override", result["mode_reason"])

    def test_metaskills_activate_by_phase_mode_and_novelty(self):
        direct = runtime.resolve_task(PROFILE, LIBRARY, "Draw a portrait.")
        direct_pre = {x["object_id"] for x in direct["metaskills"]["pre_production"]}
        direct_post = {x["object_id"] for x in direct["metaskills"]["post_production"]}
        self.assertIn("AP_alternate_search_and_control_cycles", direct_pre)
        self.assertNotIn("AP_plan_and_build_work_from_thumbnail_to_final", direct_pre)
        self.assertIn("PAT_verify_result_against_objective_after_production", direct_post)

        staged = runtime.resolve_task(PROFILE, LIBRARY, "Show the stages and brainstorm different directions.")
        staged_pre = {x["object_id"] for x in staged["metaskills"]["pre_production"]}
        self.assertIn("AP_progress_artifact_through_ratified_steps", staged_pre)
        self.assertIn("PAT_generate_novel_options_by_combining_distant_concepts", staged_pre)

    def test_art_risk_checks_are_required_without_making_the_judgment(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY, "Draw her pointing a gun toward the camera with one hand visible."
        )
        checks = set(result["risk_checks"])
        self.assertIn("camera consistency", checks)
        self.assertIn("digit count for every visible hand", checks)
        self.assertIn("weapon-hand contact map", checks)
        self.assertIn("thumb opposition and active/support digit roles", checks)
        self.assertIn("weapon-hand-arm attachment chain", checks)
        self.assertIn("gaze/action alignment", checks)


    def test_staged_stage0_risk_checks_match_low_information_ceiling(self):
        result = runtime.resolve_task(
            PROFILE,
            LIBRARY,
            "MODE Staged. Draw her kneeling while gripping a spear with one visible hand, using these reference sheets as golden truth.",
            current_stage=0,
        )
        self.assertEqual(result["mode"], "staged_production")
        self.assertEqual(result["current_stage"], 0)
        checks = set(result["risk_checks"])
        self.assertIn("gross hand/contact intent", checks)
        self.assertIn("gross support/contact intent", checks)
        self.assertIn("weapon role and gross contact intent", checks)
        self.assertIn("body-plan and proportion anchor lock", checks)
        self.assertNotIn("digit count for every visible hand", checks)
        self.assertNotIn("digit count for every visible weapon hand", checks)
        self.assertNotIn("character identity and face lock", checks)
        self.assertNotIn("costume seam and emblem lock", checks)
        self.assertNotIn("palette lock", checks)

    def test_staged_stage3_restores_detailed_hand_checks_without_palette(self):
        result = runtime.resolve_task(
            PROFILE,
            LIBRARY,
            "MODE Staged. Stage 3: draw her gripping a spear with one visible hand, using these reference sheets as golden truth.",
            current_stage=3,
        )
        self.assertEqual(result["current_stage"], 3)
        checks = set(result["risk_checks"])
        self.assertIn("digit count for every visible hand", checks)
        self.assertIn("digit count for every visible weapon hand", checks)
        self.assertIn("character identity and face lock", checks)
        self.assertIn("costume seam and emblem lock", checks)
        self.assertNotIn("palette lock", checks)

    def test_fresh_staged_resolution_defaults_risk_resolution_to_stage0(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY, "Draw her holding a spear. Do it in stages."
        )
        self.assertEqual(result["mode"], "staged_production")
        self.assertEqual(result["current_stage"], 0)
        self.assertIn("gross hand/contact intent", result["risk_checks"])
        self.assertNotIn("digit count for every visible hand", result["risk_checks"])

    def test_completion_audit_reports_missing_required_or_risk_checks(self):
        resolution = runtime.resolve_task(
            PROFILE, LIBRARY, "Draw her pointing a gun toward the camera with one hand visible."
        )
        incomplete = runtime.verify_completion(
            resolution,
            {"checks": {"instruction_fidelity_check": True}, "risk_checks": {}},
        )
        self.assertFalse(incomplete["passed"])
        self.assertIn("objective_check", incomplete["missing_required_checks"])
        self.assertTrue(incomplete["unresolved_risk_checks"])

        complete_without_local_review = runtime.verify_completion(
            resolution,
            {
                "checks": {"instruction_fidelity_check": True, "objective_check": True},
                "risk_checks": {name: True for name in resolution["risk_checks"]},
            },
        )
        self.assertFalse(complete_without_local_review["passed"])
        self.assertIn("risk_region_inventory_check", complete_without_local_review["missing_required_checks"])
        self.assertIn("local_risk_inspection_check", complete_without_local_review["missing_required_checks"])

        complete = runtime.verify_completion(
            resolution,
            {
                "checks": {
                    "instruction_fidelity_check": True,
                    "objective_check": True,
                    "risk_region_inventory_check": True,
                    "local_risk_inspection_check": True,
                },
                "risk_checks": {name: True for name in resolution["risk_checks"]},
            },
        )
        self.assertTrue(complete["passed"])

    def test_weapon_and_reference_language_activate_hand_and_canon_checks(self):
        result = runtime.resolve_task(
            PROFILE,
            LIBRARY,
            "Use these reference sheets as golden truth and draw Blu firing a pistol in an extreme action pose.",
        )
        checks = set(result["risk_checks"])
        self.assertIn("weapon-hand contact map", checks)
        self.assertIn("digit count for every visible weapon hand", checks)
        self.assertIn("hand-wrist-arm endpoint continuity", checks)
        self.assertIn("character identity and face lock", checks)
        self.assertIn("costume seam and emblem lock", checks)
        self.assertIn("equipment mount lock", checks)
        self.assertIn("digit contract", checks)



class Stage0ExecutionBoundaryTests(unittest.TestCase):
    STAGE0_AP = ROOT / "library" / "art" / "process" / "staged-drawing" / "AP_run_stage0_rough_composition_search.md"
    HANDOFF_AP = ROOT / "library" / "art" / "process" / "staged-drawing" / "AP_prepare_artifact_only_image_generation_handoff.md"
    GATE_AP = ROOT / "library" / "art" / "process" / "staged-drawing" / "AP_gate_staged_visual_work_by_approval.md"
    PATTERN = ROOT / "library" / "art" / "process" / "staged-drawing" / "PAT_explore_stage0_with_thumbnail_set.md"

    def _productive_contract(self) -> str:
        text = self.STAGE0_AP.read_text(encoding="utf-8")
        return text.split("### Productive Image Contract", 1)[1].split("## Notes", 1)[0].casefold()

    def test_stage0_productive_image_contract_is_singular_and_batch_free(self):
        contract = self._productive_contract()
        self.assertIn("one full-frame loose composition sketch", contract)
        self.assertIn("exactly one rough picture proposition", contract)
        for forbidden in (
            "four to six", "4-6", "4–6", "candidate", "thumbnail set",
            "search", "batch", "controller", "stage",
        ):
            self.assertNotIn(forbidden, contract)

    def test_stage0_active_owners_forbid_native_multi_output(self):
        texts = [
            self.STAGE0_AP.read_text(encoding="utf-8"),
            self.HANDOFF_AP.read_text(encoding="utf-8"),
            self.GATE_AP.read_text(encoding="utf-8"),
            self.PATTERN.read_text(encoding="utf-8"),
        ]
        joined = "\n".join(texts).casefold()
        self.assertGreaterEqual(joined.count("one native image call = one stage 0 candidate"), 2)
        self.assertIn("never use a host multi-output option for stage 0", joined)
        self.assertNotIn("if the host can return several separate images in one request, use that capability", joined)
        self.assertNotIn("if the host supports several separate outputs in one request", joined)


class ProfileReferenceIntegrityTests(unittest.TestCase):
    """Every card a profile names must exist.

    Profiles carry card references in ordinary contract fields that no schema
    declares — `stage_ap_thread`, `staged_controller`, `image_generation_handoff`.
    Those values are handed to the consumer verbatim, so a typo stays invisible
    until a live run asks for an AP that was never authored. This replaces the
    narrow per-domain assertion that only covered Art's Stage 4 mapping.
    """

    PROFILE_DIR = ROOT / "PASS" / "runtime" / "profiles"

    def test_every_shipped_profile_passes_doctor(self):
        profiles = sorted(self.PROFILE_DIR.glob("*.yaml"))
        self.assertTrue(profiles, "no runtime profiles found")
        for path in profiles:
            with self.subTest(profile=path.name):
                self.assertEqual(runtime.doctor(runtime.read_yaml(path), LIBRARY), [])

    def test_every_profile_card_reference_resolves(self):
        known = runtime._frontmatter_object_ids(LIBRARY)
        for path in sorted(self.PROFILE_DIR.glob("*.yaml")):
            references = runtime._object_id_references(runtime.read_yaml(path))
            for where, object_id in references:
                with self.subTest(profile=path.name, field=where):
                    self.assertIn(object_id, known)

    def test_art_profile_actually_carries_references_to_check(self):
        # Guards the test above against silently passing on an empty set if the
        # reference-shape rule ever stops recognizing PASS object ids.
        references = runtime._object_id_references(PROFILE)
        fields = {where for where, _ in references}
        self.assertTrue(any(field.endswith(".stage_ap_thread.4") for field in fields))
        self.assertTrue(any(field.endswith(".image_generation_handoff") for field in fields))

    def test_doctor_rejects_an_unresolvable_card_reference(self):
        broken = runtime.read_yaml(self.PROFILE_DIR / "art.yaml")
        contract = broken["execution_modes"]["staged_production"]["contract"]
        contract["stage_ap_thread"][4] = "AP_this_ap_was_never_authored"
        problems = runtime.doctor(broken, LIBRARY)
        self.assertTrue(
            any("AP_this_ap_was_never_authored" in problem for problem in problems),
            problems,
        )


if __name__ == "__main__":
    unittest.main()
