import pytest

from petroleum_units import (
    api_to_density_kg_m3,
    api_to_sg,
    convert_api_gravity,
    density_kg_m3_to_api,
    sg_to_api,
)


def test_api_10_equals_water_specific_gravity():
    assert api_to_sg(10) == pytest.approx(1.0, rel=1e-9)


def test_round_trip_api_sg():
    original = 35.0
    assert sg_to_api(api_to_sg(original)) == pytest.approx(original, rel=1e-9)


def test_typical_wti_crude_oil_gravity():
    assert api_to_sg(39.6) == pytest.approx(0.8270, rel=1e-3)


def test_sg_must_be_positive():
    with pytest.raises(ValueError, match="positive"):
        sg_to_api(0)


def test_density_must_be_positive():
    with pytest.raises(ValueError, match="positive"):
        density_kg_m3_to_api(-5)


def test_convert_api_gravity_dispatcher_round_trip():
    density = convert_api_gravity(35.0, "api", "kg/m3")
    assert density == pytest.approx(api_to_density_kg_m3(35.0))
    assert convert_api_gravity(density, "kg/m3", "api") == pytest.approx(35.0, rel=1e-6)


def test_convert_api_gravity_unknown_unit_raises():
    with pytest.raises(ValueError, match="unknown API-gravity unit"):
        convert_api_gravity(1.0, "bogus", "sg")
