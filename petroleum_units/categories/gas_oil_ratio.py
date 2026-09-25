from ..engine import Unit, register_category

_UNITS = (
    Unit("cubic_meter_per_cubic_meter", "m3/m3", 1.0),
    Unit("standard_cubic_foot_per_barrel", "scf/bbl", 0.17810760667903525),
)

register_category("gas_oil_ratio", _UNITS)
