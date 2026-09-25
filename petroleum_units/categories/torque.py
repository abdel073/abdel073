from ..engine import Unit, register_category

_UNITS = (
    Unit("newton_meter", "N.m", 1.0),
    Unit("foot_pound", "ft.lb", 1.3558179483314),
)

register_category("torque", _UNITS)
