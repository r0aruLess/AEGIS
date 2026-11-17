"""
Unit tests validating 5x5 defensible risk calculations and FAIR Monte Carlo engine.
"""
import unittest
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from backend.db import calculate_defensible_risk
from backend.fair_engine import run_fair_monte_carlo

class TestRiskEngine(unittest.TestCase):
    def test_defensible_risk_calculation(self):
        inh_s, eff, res_l, res_i, res_s = calculate_defensible_risk(
            inherent_likelihood=4,
            inherent_impact=5,
            control_status="PASSED",
            treatment="Mitigate"
        )
        self.assertEqual(inh_s, 20)
        self.assertEqual(eff, 0.75)
        self.assertLess(res_l, 4)
        self.assertLess(res_i, 5)
        self.assertLess(res_s, inh_s)
        self.assertLessEqual(res_s, 9)

        # FAILED control provides zero mitigation
        inh_s, eff, res_l, res_i, res_s = calculate_defensible_risk(
            inherent_likelihood=5,
            inherent_impact=5,
            control_status="FAILED",
            treatment="Mitigate"
        )
        self.assertEqual(inh_s, 25)
        self.assertEqual(eff, 0.0)
        self.assertEqual(res_s, inh_s)

    def test_fair_monte_carlo_engine(self):
        res = run_fair_monte_carlo(iterations=1000)
        self.assertEqual(res["iterations"], 1000)
        self.assertGreater(res["mean_ale"], 0)
        self.assertLessEqual(res["percentile_10"], res["median_50"])
        self.assertLessEqual(res["median_50"], res["percentile_90_var"])
        self.assertEqual(len(res["histogram_bins"]), 10)

if __name__ == "__main__":
    unittest.main()
