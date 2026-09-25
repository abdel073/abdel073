WATER_DENSITY_60F_KG_M3 = 999.0170125


def api_to_sg(api: float) -> float:
    return 141.5 / (131.5 + api)


def sg_to_api(sg: float) -> float:
    if sg <= 0:
        raise ValueError("specific gravity must be positive")
    return 141.5 / sg - 131.5


def sg_to_density_kg_m3(sg: float) -> float:
    return sg * WATER_DENSITY_60F_KG_M3


def density_kg_m3_to_sg(density_kg_m3: float) -> float:
    if density_kg_m3 <= 0:
        raise ValueError("density must be positive")
    return density_kg_m3 / WATER_DENSITY_60F_KG_M3


def api_to_density_kg_m3(api: float) -> float:
    return sg_to_density_kg_m3(api_to_sg(api))


def density_kg_m3_to_api(density_kg_m3: float) -> float:
    return sg_to_api(density_kg_m3_to_sg(density_kg_m3))


_API_GRAVITY_UNITS = ("api", "sg", "kg/m3")


def _to_sg(value: float, unit: str) -> float:
    if unit == "api":
        return api_to_sg(value)
    if unit == "sg":
        return value
    if unit == "kg/m3":
        return density_kg_m3_to_sg(value)
    raise ValueError(
        f"unknown API-gravity unit: {unit!r}. Available: {', '.join(_API_GRAVITY_UNITS)}"
    )


def _from_sg(sg: float, unit: str) -> float:
    if unit == "api":
        return sg_to_api(sg)
    if unit == "sg":
        return sg
    if unit == "kg/m3":
        return sg_to_density_kg_m3(sg)
    raise ValueError(
        f"unknown API-gravity unit: {unit!r}. Available: {', '.join(_API_GRAVITY_UNITS)}"
    )


def convert_api_gravity(value: float, from_unit: str, to_unit: str) -> float:
    return _from_sg(_to_sg(value, from_unit), to_unit)
