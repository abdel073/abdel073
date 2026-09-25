import argparse
import sys

from . import api_gravity, engine


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="petroleum-units",
        description=(
            "Convertisseur d'unites du domaine petrolier "
            "(systeme anglo-saxon <-> systeme metrique)"
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser(
        "list", help="Lister les categories, ou les unites d'une categorie"
    )
    list_parser.add_argument(
        "category", nargs="?", help="Categorie a detailler (ex: pressure, volume)"
    )

    convert_parser = subparsers.add_parser("convert", help="Convertir une valeur")
    convert_parser.add_argument(
        "category", help="Ex: length, volume, mass, pressure, ..."
    )
    convert_parser.add_argument("value", type=float)
    convert_parser.add_argument("from_unit", help="Symbole d'unite source (ex: bbl)")
    convert_parser.add_argument("to_unit", help="Symbole d'unite cible (ex: m3)")

    api_parser = subparsers.add_parser(
        "api", help="Convertir densite API / gravite specifique (SG) / kg/m3"
    )
    api_parser.add_argument("value", type=float)
    api_parser.add_argument("from_unit", choices=["api", "sg", "kg/m3"])
    api_parser.add_argument("to_unit", choices=["api", "sg", "kg/m3"])

    return parser


def _run_list(category: str | None) -> None:
    if category is None:
        for name in engine.list_categories():
            print(name)
        return
    for symbol in engine.list_units(category):
        print(symbol)


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "list":
            _run_list(args.category)
            return 0

        if args.command == "convert":
            result = engine.convert(
                args.category, args.value, args.from_unit, args.to_unit
            )
            print(f"{args.value} {args.from_unit} = {result} {args.to_unit}")
            return 0

        if args.command == "api":
            result = api_gravity.convert_api_gravity(
                args.value, args.from_unit, args.to_unit
            )
            print(f"{args.value} {args.from_unit} = {result} {args.to_unit}")
            return 0
    except ValueError as exc:
        print(f"Erreur: {exc}", file=sys.stderr)
        return 1

    return 1


if __name__ == "__main__":
    sys.exit(main())
