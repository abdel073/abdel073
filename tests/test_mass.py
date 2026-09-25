import pytest

from petroleum_units import convert


def test_one_kilogram_in_pounds():
    assert convert("mass", 1, "kg", "lb") == pytest.approx(2.20462262185, rel=1e-9)


def test_one_metric_ton_in_kilograms():
    assert convert("mass", 1, "t", "kg") == pytest.approx(1000.0)


def test_short_ton_vs_long_ton():
    short_ton_kg = convert("mass", 1, "short_ton", "kg")
    long_ton_kg = convert("mass", 1, "long_ton", "kg")
    assert short_ton_kg < long_ton_kg
