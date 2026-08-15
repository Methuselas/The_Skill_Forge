from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
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

    def test_training_or_drill_routes_to_staged_production(self):
        result = runtime.resolve_task(PROFILE, LIBRARY, "Give me a figure drawing drill for this pose.")
        self.assertEqual(result["mode"], "staged_production")
        self.assertEqual(result["contract"]["sequence"], [0, 1, 2, 3, 4])
        self.assertTrue(result["contract"]["approval_gates"])
        self.assertTrue(result["contract"]["rollback_enabled"])

    def test_teaching_lane_is_independent_from_execution_mode(self):
        teaching = runtime.resolve_task(PROFILE, LIBRARY, "Teach me how to draw this head.")
        self.assertEqual(teaching["lane"], "teach")
        self.assertEqual(teaching["mode"], "direct_render")
        teaching_ids = {item["object_id"] for item in teaching["teaching"]["pre_production"]}
        self.assertIn("AP_teach_craft_from_orientation_to_generation", teaching_ids)

        ordinary = runtime.resolve_task(PROFILE, LIBRARY, "Draw this head.")
        self.assertEqual(ordinary["lane"], "skill")
        self.assertEqual(ordinary["teaching"]["pre_production"], [])

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
        self.assertIn("AP_plan_and_build_work_from_thumbnail_to_final", staged_pre)
        self.assertIn("PAT_generate_novel_options_by_combining_distant_concepts", staged_pre)

    def test_art_risk_checks_are_required_without_making_the_judgment(self):
        result = runtime.resolve_task(
            PROFILE, LIBRARY, "Draw her pointing a gun toward the camera with one hand visible."
        )
        checks = set(result["risk_checks"])
        self.assertIn("camera consistency", checks)
        self.assertIn("digit count", checks)
        self.assertIn("weapon-hand-arm attachment chain", checks)
        self.assertIn("gaze/action alignment", checks)

    def test_completion_gate_blocks_missing_required_or_risk_checks(self):
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

        complete = runtime.verify_completion(
            resolution,
            {
                "checks": {"instruction_fidelity_check": True, "objective_check": True},
                "risk_checks": {name: True for name in resolution["risk_checks"]},
            },
        )
        self.assertTrue(complete["passed"])


if __name__ == "__main__":
    unittest.main()
