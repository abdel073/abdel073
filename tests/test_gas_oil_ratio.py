import pytest

from petroleum_units import convert


def test_one_scf_per_bbl_in_m3_per_m3():
    assert convert("gas_oil_ratio", 1, "scf/bbl", "m3/m3") == pytest.approx(
        0.17810760667903525
    )


def test_typical_gor_round_trip():
    original = 600.0
    m3_per_m3 = convert("gas_oil_ratio", original, "scf/bbl", "m3/m3")
    back = convert("gas_oil_ratio", m3_per_m3, "m3/m3", "scf/bbl")
    assert back == pytest.approx(original)
