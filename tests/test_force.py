import pytest

from petroleum_units import convert


def test_one_pound_force_in_newtons():
    assert convert("force", 1, "lbf", "N") == pytest.approx(4.4482216152605)


def test_weight_on_bit_klbf_to_kilonewtons():
    thirty_klbf_in_lbf = 30_000.0
    kilonewtons = convert("force", thirty_klbf_in_lbf, "lbf", "kN")
    assert kilonewtons == pytest.approx(133.4466, rel=1e-4)
