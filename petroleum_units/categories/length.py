from ..engine import Unit, register_category

_UNITS = (
    Unit("meter", "m", 1.0),
    Unit("foot", "ft", 0.3048),
    Unit("inch", "in", 0.0254),
    Unit("centimeter", "cm", 0.01),
    Unit("millimeter", "mm", 0.001),
    Unit("yard", "yd", 0.9144),
    Unit("mile", "mi", 1609.344),
    Unit("kilometer", "km", 1000.0),
)

register_category("length", _UNITS)
