import pytest

from petroleum_units import convert


def test_one_barrel_in_us_gallons():
    assert convert("volume", 1, "bbl", "gal_us") == pytest.approx(42.0, rel=1e-9)


def test_one_barrel_in_cubic_meters():
    assert convert("volume", 1, "bbl", "m3") == pytest.approx(0.158987294928)


def test_round_trip_barrel_liters():
    original = 1000.0
    liters = convert("volume", original, "bbl", "L")
    back = convert("volume", liters, "L", "bbl")
    assert back == pytest.approx(original)
