import pytest

from petroleum_units import convert


def test_one_atmosphere_in_psi():
    assert convert("pressure", 1, "atm", "psi") == pytest.approx(14.6959, rel=1e-4)


def test_one_bar_in_kilopascal():
    assert convert("pressure", 1, "bar", "kPa") == pytest.approx(100.0)


def test_round_trip_psi_bar():
    original = 5000.0
    bar_value = convert("pressure", original, "psi", "bar")
    back = convert("pressure", bar_value, "bar", "psi")
    assert back == pytest.approx(original)
