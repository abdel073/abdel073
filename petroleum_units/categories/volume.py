from ..engine import Unit, register_category

_UNITS = (
    Unit("cubic_meter", "m3", 1.0),
    Unit("barrel", "bbl", 0.158987294928),
    Unit("us_gallon", "gal_us", 0.003785411784),
    Unit("imperial_gallon", "gal_uk", 0.00454609),
    Unit("liter", "L", 0.001),
    Unit("cubic_foot", "ft3", 0.028316846592),
)

register_category("volume", _UNITS)
