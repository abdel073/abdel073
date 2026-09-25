from ..engine import Unit, register_category

_UNITS = (
    Unit("joule", "J", 1.0),
    Unit("kilojoule", "kJ", 1000.0),
    Unit("btu", "BTU", 1055.05585262),
    Unit("kilowatt_hour", "kWh", 3_600_000.0),
    Unit("calorie", "cal", 4.184),
)

register_category("energy", _UNITS)
