import pytest

from petroleum_units import convert


def test_one_foot_pound_in_newton_meters():
    assert convert("torque", 1, "ft.lb", "N.m") == pytest.approx(1.3558179483314)
