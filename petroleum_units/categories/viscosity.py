from ..engine import Unit, register_category

_DYNAMIC_UNITS = (
    Unit("pascal_second", "Pa.s", 1.0),
    Unit("centipoise", "cP", 0.001),
    Unit("poise", "P", 0.1),
)

_KINEMATIC_UNITS = (
    Unit("square_meter_per_second", "m2/s", 1.0),
    Unit("centistokes", "cSt", 1e-6),
    Unit("stokes", "St", 1e-4),
)

register_category("dynamic_viscosity", _DYNAMIC_UNITS)
register_category("kinematic_viscosity", _KINEMATIC_UNITS)
