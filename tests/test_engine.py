import pytest

from petroleum_units import convert, list_categories, list_units


def test_list_categories_includes_all_expected():
    categories = list_categories()
    for expected in (
        "length",
        "volume",
        "mass",
        "pressure",
        "temperature",
        "density",
        "flow_rate",
        "dynamic_viscosity",
        "kinematic_viscosity",
        "torque",
        "energy",
        "pressure_gradient",
    ):
        assert expected in categories


def test_list_units_for_known_category():
    assert "m" in list_units("length")
    assert "ft" in list_units("length")


def test_list_units_unknown_category_raises():
    with pytest.raises(ValueError, match="unknown category"):
        list_units("bogus")


def test_convert_identity():
    assert convert("length", 5.0, "m", "m") == pytest.approx(5.0)


def test_convert_unknown_category_raises():
    with pytest.raises(ValueError, match="unknown category"):
        convert("bogus", 1.0, "a", "b")


def test_convert_unknown_from_unit_raises():
    with pytest.raises(ValueError, match="unknown unit"):
        convert("length", 1.0, "bogus", "m")


def test_convert_unknown_to_unit_raises():
    with pytest.raises(ValueError, match="unknown unit"):
        convert("length", 1.0, "m", "bogus")
