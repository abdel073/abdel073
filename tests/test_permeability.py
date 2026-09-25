import pytest

from petroleum_units import convert


def test_one_darcy_in_millidarcy():
    assert convert("permeability", 1, "D", "mD") == pytest.approx(1000.0)


def test_darcy_in_square_meters():
    assert convert("permeability", 1, "D", "m2") == pytest.approx(9.869233e-13)
