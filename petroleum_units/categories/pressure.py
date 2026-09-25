from ..engine import Unit, register_category

_UNITS = (
    Unit("pascal", "Pa", 1.0),
    Unit("kilopascal", "kPa", 1000.0),
    Unit("megapascal", "MPa", 1_000_000.0),
    Unit("bar", "bar", 100_000.0),
    Unit("psi", "psi", 6894.757293168),
    Unit("atmosphere", "atm", 101325.0),
    Unit("kgf_per_cm2", "kgf/cm2", 98066.5),
    Unit("mmhg", "mmHg", 133.322368421),
)

register_category("pressure", _UNITS)
