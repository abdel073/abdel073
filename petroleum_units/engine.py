from dataclasses import dataclass


@dataclass(frozen=True)
class Unit:
    name: str
    symbol: str
    to_base_factor: float
    to_base_offset: float = 0.0


_REGISTRY: dict[str, dict[str, Unit]] = {}


def register_category(category: str, units: tuple[Unit, ...]) -> None:
    _REGISTRY[category] = {unit.symbol: unit for unit in units}


def list_categories() -> tuple[str, ...]:
    return tuple(_REGISTRY.keys())


def list_units(category: str) -> tuple[str, ...]:
    if category not in _REGISTRY:
        raise ValueError(
            f"unknown category: {category!r}. Available: {', '.join(list_categories())}"
        )
    return tuple(_REGISTRY[category].keys())


def convert(category: str, value: float, from_symbol: str, to_symbol: str) -> float:
    units = _REGISTRY.get(category)
    if units is None:
        raise ValueError(
            f"unknown category: {category!r}. Available: {', '.join(list_categories())}"
        )

    from_unit = units.get(from_symbol)
    if from_unit is None:
        raise ValueError(
            f"unknown unit {from_symbol!r} for category {category!r}. "
            f"Available: {', '.join(units)}"
        )

    to_unit = units.get(to_symbol)
    if to_unit is None:
        raise ValueError(
            f"unknown unit {to_symbol!r} for category {category!r}. "
            f"Available: {', '.join(units)}"
        )

    base_value = value * from_unit.to_base_factor + from_unit.to_base_offset
    return (base_value - to_unit.to_base_offset) / to_unit.to_base_factor
