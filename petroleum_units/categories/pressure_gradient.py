from ..engine import Unit, register_category

_UNITS = (
    Unit("pascal_per_meter", "Pa/m", 1.0),
    Unit("kilopascal_per_meter", "kPa/m", 1000.0),
    Unit("bar_per_meter", "bar/m", 100_000.0),
    Unit("psi_per_foot", "psi/ft", 6894.757293168 / 0.3048),
)

register_category("pressure_gradient", _UNITS)
