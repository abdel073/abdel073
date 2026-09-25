from ..engine import Unit, register_category

_UNITS = (
    Unit("newton", "N", 1.0),
    Unit("pound_force", "lbf", 4.4482216152605),
    Unit("kilogram_force", "kgf", 9.80665),
    Unit("decanewton", "daN", 10.0),
    Unit("kilonewton", "kN", 1000.0),
)

register_category("force", _UNITS)
