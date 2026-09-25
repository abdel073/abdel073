from ..engine import Unit, register_category

_SCF_TO_M3 = 0.028316846592

_UNITS = (
    Unit("cubic_meter", "m3", 1.0),
    Unit("standard_cubic_foot", "scf", _SCF_TO_M3),
    Unit("thousand_standard_cubic_feet", "Mscf", _SCF_TO_M3 * 1_000.0),
    Unit("million_standard_cubic_feet", "MMscf", _SCF_TO_M3 * 1_000_000.0),
    Unit("billion_standard_cubic_feet", "Bcf", _SCF_TO_M3 * 1_000_000_000.0),
)

register_category("gas_volume", _UNITS)
