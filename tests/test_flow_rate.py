import pytest

from petroleum_units import convert


def test_barrel_per_day_to_cubic_meter_per_day():
    assert convert("flow_rate", 1000, "bbl/d", "m3/d") == pytest.approx(158.987294928)


def test_round_trip_gpm_m3_per_hour():
    original = 500.0
    m3_per_h = convert("flow_rate", original, "gpm", "m3/h")
    back = convert("flow_rate", m3_per_h, "m3/h", "gpm")
    assert back == pytest.approx(original)
