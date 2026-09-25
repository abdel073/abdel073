import pytest

from petroleum_units import convert


def test_water_density_in_lb_per_ft3():
    assert convert("density", 1000, "kg/m3", "lb/ft3") == pytest.approx(
        62.428, rel=1e-3
    )


def test_ppg_round_trip():
    original = 9.5
    kg_m3 = convert("density", original, "ppg", "kg/m3")
    back = convert("density", kg_m3, "kg/m3", "ppg")
    assert back == pytest.approx(original)
