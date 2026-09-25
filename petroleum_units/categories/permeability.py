from ..engine import Unit, register_category

_UNITS = (
    Unit("square_meter", "m2", 1.0),
    Unit("darcy", "D", 9.869233e-13),
    Unit("millidarcy", "mD", 9.869233e-16),
)

register_category("permeability", _UNITS)
