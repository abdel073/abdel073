from ..engine import Unit, register_category

_FAHRENHEIT_FACTOR = 5.0 / 9.0
_FAHRENHEIT_OFFSET = 273.15 - 32.0 * _FAHRENHEIT_FACTOR
_RANKINE_FACTOR = 5.0 / 9.0

_UNITS = (
    Unit("kelvin", "K", 1.0),
    Unit("celsius", "C", 1.0, 273.15),
    Unit("fahrenheit", "F", _FAHRENHEIT_FACTOR, _FAHRENHEIT_OFFSET),
    Unit("rankine", "R", _RANKINE_FACTOR),
)

register_category("temperature", _UNITS)
