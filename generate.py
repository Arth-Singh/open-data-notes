"""Generate the three synthetic Open Data Notes tables.

Every value comes from this script and a fixed seed. No real city, place, survey or person is
described. Run `python generate.py` to rebuild `data/` byte for byte.
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 2026
OUT = Path(__file__).parent / "data"
DISTRICTS = ["North", "Riverside", "Old Town", "Harbour", "Eastfield", "Hillcrest", "Westgate"]
STREET_WORDS = ["Mill", "Station", "Orchard", "Church", "Market", "Bridge", "Park", "Quarry",
                "Willow", "Garden", "Canal", "School", "Chapel", "Meadow", "Forge", "Ash"]
STREET_KINDS = ["Road", "Street", "Lane", "Avenue", "Way", "Hill"]
SPECIES = [
    ("London plane", "Platanus x acerifolia"),
    ("Small-leaved lime", "Tilia cordata"),
    ("Norway maple", "Acer platanoides"),
    ("Silver birch", "Betula pendula"),
    ("Common hornbeam", "Carpinus betulus"),
    ("Rowan", "Sorbus aucuparia"),
    ("Field maple", "Acer campestre"),
    ("Wild cherry", "Prunus avium"),
    ("Pedunculate oak", "Quercus robur"),
    ("Ginkgo", "Ginkgo biloba"),
]
CONDITIONS = ["good", "good", "good", "fair", "fair", "poor", "dead"]


def street(rng: random.Random) -> str:
    return f"{rng.choice(STREET_WORDS)} {rng.choice(STREET_KINDS)}"


def bus_stops(rng: random.Random) -> list[dict]:
    rows = []
    start = date(2025, 3, 3)
    for n in range(1, 1241):
        shelter = rng.random() < 0.55
        rows.append(
            {
                "stop_id": f"BS{n:04d}",
                "stop_name": f"{street(rng)} {rng.choice(['North', 'South', 'East', 'West', ''])}".strip(),
                "district": rng.choice(DISTRICTS),
                "x_m": rng.randint(0, 12_000),
                "y_m": rng.randint(0, 9_000),
                "shelter": "yes" if shelter else "no",
                "bench": "yes" if shelter or rng.random() < 0.2 else "no",
                "step_free_access": "yes" if rng.random() < 0.72 else "no",
                "tactile_paving": "yes" if rng.random() < 0.48 else "no",
                "audio_announcements": "yes" if rng.random() < 0.31 else "no",
                "surveyed_on": (start + timedelta(days=rng.randint(0, 200))).isoformat(),
            }
        )
    return rows


def libraries(rng: random.Random) -> list[dict]:
    rows = []
    for n in range(1, 39):
        large = rng.random() < 0.3
        opens = "09:00" if large else rng.choice(["09:30", "10:00"])
        closes = "20:00" if large else rng.choice(["17:00", "17:30", "18:00"])
        row = {
            "branch_id": f"LB{n:02d}",
            "branch_name": f"{rng.choice(STREET_WORDS)} {'Central ' if large else ''}Library",
            "district": rng.choice(DISTRICTS),
        }
        for day in ("mon", "tue", "wed", "thu", "fri"):
            row[day] = "closed" if not large and rng.random() < 0.12 else f"{opens}-{closes}"
        row["sat"] = "10:00-16:00" if rng.random() < 0.8 else "closed"
        row["sun"] = "12:00-16:00" if large else "closed"
        rows.append(row)
    return rows


def trees(rng: random.Random) -> list[dict]:
    rows = []
    for n in range(1, 5001):
        common, latin = rng.choice(SPECIES)
        planted = rng.randint(1950, 2023)
        age = 2024 - planted
        diameter = max(4, round(age * rng.uniform(0.6, 1.4)))
        rows.append(
            {
                "tree_id": f"T{n:05d}",
                "species_common": common,
                "species_latin": latin,
                "district": rng.choice(DISTRICTS),
                "street": street(rng),
                "x_m": rng.randint(0, 12_000),
                "y_m": rng.randint(0, 9_000),
                "planted_year": planted,
                "trunk_diameter_cm": diameter,
                "height_m": round(min(30.0, 2 + diameter * rng.uniform(0.15, 0.3)), 1),
                "condition": rng.choice(CONDITIONS),
            }
        )
    return rows


def write(name: str, rows: list[dict]) -> None:
    OUT.mkdir(exist_ok=True)
    with (OUT / name).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"{name}: {len(rows)} rows")


def main() -> None:
    rng = random.Random(SEED)
    write("bus_stop_accessibility_2025.csv", bus_stops(rng))
    write("library_opening_hours_2026.csv", libraries(rng))
    write("street_tree_inventory_sample_2024.csv", trees(rng))


if __name__ == "__main__":
    main()
