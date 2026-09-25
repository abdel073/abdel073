import pytest

from petroleum_units import convert


def test_one_mmscf_in_cubic_meters():
    assert convert("gas_volume", 1, "MMscf", "m3") == pytest.approx(28316.846592)


def test_bcf_to_mscf():
    assert convert("gas_volume", 1, "Bcf", "Mscf") == pytest.approx(1_000_000.0)


def test_round_trip_scf_m3():
    original = 500_000.0
    m3 = convert("gas_volume", original, "scf", "m3")
    back = convert("gas_volume", m3, "m3", "scf")
    assert back == pytest.approx(original)
