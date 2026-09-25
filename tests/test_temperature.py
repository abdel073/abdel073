import pytest

from petroleum_units import convert


def test_water_freezing_point():
    assert convert("temperature", 0, "C", "F") == pytest.approx(32.0)


def test_water_boiling_point():
    assert convert("temperature", 100, "C", "F") == pytest.approx(212.0)


def test_absolute_zero_in_celsius():
    assert convert("temperature", 0, "K", "C") == pytest.approx(-273.15)


def test_rankine_matches_fahrenheit_scale():
    assert convert("temperature", 32, "F", "R") == pytest.approx(491.67, rel=1e-4)


def test_round_trip_fahrenheit_kelvin():
    original = 350.0
    kelvin = convert("temperature", original, "F", "K")
    back = convert("temperature", kelvin, "K", "F")
    assert back == pytest.approx(original)
