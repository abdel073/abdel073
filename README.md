# petroleum-units

Convertisseur d'unites pour l'industrie petroliere, couvrant a la fois le
systeme anglo-saxon (imperial/US) et le systeme metrique.

## Categories supportees

| Categorie              | Unites disponibles                                         |
|-------------------------|-------------------------------------------------------------|
| `length`                | m, ft, in, cm, mm, yd, mi, km                                |
| `volume`                | m3, bbl (baril petrolier), gal_us, gal_uk, L, ft3            |
| `mass`                  | kg, lb, t (tonne metrique), long_ton, short_ton              |
| `pressure`               | Pa, kPa, MPa, bar, psi, atm, kgf/cm2, mmHg                   |
| `temperature`            | K, C, F, R                                                   |
| `density`                | kg/m3, g/cm3, lb/ft3, ppg (densite de boue)                  |
| `flow_rate`              | m3/d, m3/h, bbl/d, bbl/h, gpm, L/min                          |
| `dynamic_viscosity`      | Pa.s, cP, P                                                   |
| `kinematic_viscosity`    | m2/s, cSt, St                                                 |
| `torque`                 | N.m, ft.lb                                                    |
| `energy`                 | J, kJ, BTU, kWh, cal                                          |
| `pressure_gradient`      | Pa/m, kPa/m, bar/m, psi/ft                                    |

La densite API (degres API) est traitee a part car sa relation avec la
gravite specifique (SG) n'est pas lineaire : `SG = 141.5 / (131.5 + API)`,
sur la base de la densite de l'eau a 60°F (999.0170125 kg/m3).

## Installation

Aucune dependance externe requise (bibliotheque standard Python 3.10+).

```bash
pip install -e .
```

## Utilisation en ligne de commande

```bash
# Lister les categories disponibles
python -m petroleum_units list

# Lister les unites d'une categorie
python -m petroleum_units list pressure

# Convertir une valeur
python -m petroleum_units convert pressure 5000 psi bar
# -> 5000.0 psi = 344.7378646584 bar

python -m petroleum_units convert volume 1000 bbl m3
# -> 1000.0 bbl = 158.987294928 m3

python -m petroleum_units convert temperature 350 F K
# -> 350.0 F = 449.81666666666666 K

# Conversion de densite API / SG / kg/m3
python -m petroleum_units api 35 api sg
# -> 35.0 api = 0.8498498498498499 sg
```

Ou, apres `pip install -e .`, via le script `petroleum-units` genere
automatiquement :

```bash
petroleum-units convert length 100 m ft
```

## Utilisation comme bibliotheque Python

```python
from petroleum_units import convert, api_to_sg, sg_to_api

# 1 baril en metres cubes
convert("volume", 1, "bbl", "m3")  # 0.158987294928

# Pression : psi -> bar
convert("pressure", 5000, "psi", "bar")

# Gradient de pression : psi/ft -> kPa/m
convert("pressure_gradient", 1, "psi/ft", "kPa/m")

# Densite API 39.6 (WTI) -> gravite specifique
api_to_sg(39.6)  # ~0.827
```

## Tests

```bash
python -m pytest --cov=petroleum_units --cov-report=term-missing
```

47 tests, 95%+ de couverture.
