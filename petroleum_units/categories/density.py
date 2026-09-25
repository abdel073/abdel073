from ..engine import Unit, register_category

_UNITS = (
    Unit("kg_per_m3", "kg/m3", 1.0),
    Unit("g_per_cm3", "g/cm3", 1000.0),
    Unit("lb_per_ft3", "lb/ft3", 16.01846337396),
    Unit("ppg", "ppg", 119.826427317),
)

register_category("density", _UNITS)
