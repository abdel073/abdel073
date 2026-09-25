from ..engine import Unit, register_category

_UNITS = (
    Unit("kilogram", "kg", 1.0),
    Unit("pound", "lb", 0.45359237),
    Unit("metric_ton", "t", 1000.0),
    Unit("long_ton", "long_ton", 1016.0469088),
    Unit("short_ton", "short_ton", 907.18474),
)

register_category("mass", _UNITS)
