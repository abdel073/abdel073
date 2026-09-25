import pytest

from petroleum_units import convert


def test_one_foot_in_meters():
    assert convert("length", 1, "ft", "m") == pytest.approx(0.3048)


def test_one_mile_in_kilometers():
    assert convert("length", 1, "mi", "km") == pytest.approx(1.609344)


def test_round_trip_feet_meters():
    original = 123.45
    meters = convert("length", original, "ft", "m")
    back = convert("length", meters, "m", "ft")
    assert back == pytest.approx(original)
