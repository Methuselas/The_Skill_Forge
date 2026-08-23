"""Regression tests for the Drawing Stage 4 closure contract.

These protect the 2026-08-22 correction: Finished Pencils is Drawing-decision
closure, not one universal pencil style or mark-density target.
"""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
STAGED = ROOT / "library/art/process/staged-drawing"


class Stage4ClosureContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ap = (STAGED / "AP_finish_stage4_as_finished_pencils.md").read_text(encoding="utf-8")
        self.pattern = (STAGED / "PAT_preserve_structure_during_stage4_pencil_finish.md").read_text(encoding="utf-8")
        self.calibration = (STAGED / "PAT_calibrate_stage_information_density_against_precedent.md").read_text(encoding="utf-8")

    def test_finished_pencils_are_resolution_not_one_style(self) -> None:
        self.assertIn("Finished Pencils is a state of Drawing resolution", self.ap)
        self.assertIn("not a mandated pencil style or rendering density", self.ap)
        self.assertIn("Preserve approved decisions, not exploratory marks", self.pattern)

    def test_stage4_mark_expression_can_change_without_redesign(self) -> None:
        for verb in ("delete", "consolidate", "replace", "suppress", "clarify", "add", "re-express"):
            self.assertIn(verb, self.pattern.lower())
        self.assertIn("Stage 4 → Stage 3", self.pattern)
        self.assertIn("very small", self.ap)

    def test_no_universal_focal_tightest_background_quieter_rule(self) -> None:
        forbidden = (
            "highest resolution belongs to the focal",
            "keep distant/subordinate regions quieter",
            "give the lead subject and functional contacts the tightest pencil resolution",
            "focal contours resolve tightly; secondary regions are quieter",
        )
        joined = "\n".join((self.ap.lower(), self.pattern.lower()))
        for phrase in forbidden:
            self.assertNotIn(phrase.lower(), joined)
        self.assertIn("need not be intrinsically less resolved", self.ap)

    def test_stage4_is_explicit_density_calibration_exception(self) -> None:
        self.assertIn("Stage 4 as an explicit calibration exception", self.calibration)
        self.assertIn("resolution threshold, not one universal rendering-density threshold", self.calibration)
        self.assertIn("Current Stage 4 positive visual calibration is validated and current", self.calibration)
        self.assertIn("broken_gate_stage4_positive_warm_hooded_warrior.png", self.calibration)
        self.assertIn("broken_gate_stage4_positive_clean_retention_spear_runner.png", self.calibration)

    def test_rendering_owner_firewall_survives_pencil_medium(self) -> None:
        self.assertIn("even if the physical medium remains pencil or graphite", self.ap)
        self.assertIn("Separately owned Rendering/Ink/Color/Paint work remains downstream", self.calibration)

    def test_old_broken_gate_stage4_is_not_positive_quality_floor(self) -> None:
        self.assertIn("historical under-resolved evidence", self.ap.lower())
        self.assertIn("remains historical under-resolved evidence only", self.calibration.lower())
        self.assertIn("primary long-term reference selection remains open", self.calibration.lower())


if __name__ == "__main__":
    unittest.main()
