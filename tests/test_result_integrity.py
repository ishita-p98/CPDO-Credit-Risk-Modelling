import json
from pathlib import Path


def test_recorded_results_are_probabilities():
    path = Path(__file__).resolve().parents[1] / "docs" / "VALIDATION_RESULTS.json"
    data = json.loads(path.read_text())
    assert set(data) == {"base", "stress_150bps_year3", "high_initial_spread"}
    for values in data.values():
        assert values["paths"] == 2000
        assert 0 <= values["default_probability"] <= 1
        assert 0 <= values["cash_out_probability"] <= 1
        assert values["default_probability"] + values["cash_out_probability"] <= 1 + 1e-12
        assert values["mean_final_nav"] >= 0
