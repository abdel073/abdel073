import pytest

from petroleum_units import convert


def test_one_psi_per_foot_in_kilopascal_per_meter():
    assert convert("pressure_gradient", 1, "psi/ft", "kPa/m") == pytest.approx(
        22.6203, rel=1e-4
    )
