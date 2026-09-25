import pytest

from petroleum_units import convert


def test_one_btu_in_joules():
    assert convert("energy", 1, "BTU", "J") == pytest.approx(1055.05585262)


def test_one_kilowatt_hour_in_megajoules():
    kwh_in_joules = convert("energy", 1, "kWh", "J")
    assert kwh_in_joules == pytest.approx(3_600_000.0)
