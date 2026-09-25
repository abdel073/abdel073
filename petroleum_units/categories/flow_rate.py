from ..engine import Unit, register_category

_BBL_TO_M3 = 0.158987294928
_GAL_US_TO_M3 = 0.003785411784

_UNITS = (
    Unit("cubic_meter_per_day", "m3/d", 1.0),
    Unit("cubic_meter_per_hour", "m3/h", 24.0),
    Unit("barrel_per_day", "bbl/d", _BBL_TO_M3),
    Unit("barrel_per_hour", "bbl/h", _BBL_TO_M3 * 24.0),
    Unit("us_gallon_per_minute", "gpm", _GAL_US_TO_M3 * 60.0 * 24.0),
    Unit("liter_per_minute", "L/min", 0.001 * 60.0 * 24.0),
)

register_category("flow_rate", _UNITS)
