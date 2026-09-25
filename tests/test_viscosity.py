import pytest

from petroleum_units import convert


def test_centipoise_to_pascal_second():
    assert convert("dynamic_viscosity", 1000, "cP", "Pa.s") == pytest.approx(1.0)


def test_centistokes_to_square_meter_per_second():
    assert convert("kinematic_viscosity", 1_000_000, "cSt", "m2/s") == pytest.approx(
        1.0
    )
