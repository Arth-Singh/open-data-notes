---
license: cc0-1.0
pretty_name: Open Data Notes (synthetic city-service tables)
language:
  - en
tags:
  - synthetic
  - tabular
  - csv
  - teaching
size_categories:
  - 1K<n<10K
configs:
  - config_name: bus_stop_accessibility_2025
    data_files: data/bus_stop_accessibility_2025.csv
  - config_name: library_opening_hours_2026
    data_files: data/library_opening_hours_2026.csv
  - config_name: street_tree_inventory_sample_2024
    data_files: data/street_tree_inventory_sample_2024.csv
---

# Open Data Notes: synthetic city-service tables

**Every value in this dataset is synthetic.** The tables describe a fictional city. No real city,
place, survey, organisation or person is described, and the numbers must not be used as facts
about anywhere. They are made for teaching: data cleaning, joins, grouping and simple charts.

| table | rows | columns |
|---|---:|---|
| `bus_stop_accessibility_2025.csv` | 1,240 | stop id, name, district, x/y in metres, shelter, bench, step-free access, tactile paving, audio announcements, survey date |
| `library_opening_hours_2026.csv` | 38 | branch id, name, district, opening hours for each day of the week |
| `street_tree_inventory_sample_2024.csv` | 5,000 | tree id, species (common and Latin), district, street, x/y in metres, year planted, trunk diameter, height, condition |

Coordinates are metres on a local grid, not latitude and longitude. Species names are real tree
species; everything about the trees is generated.

## How it was made

`generate.py` builds all three files from a fixed seed with the Python standard library only.
Running `python generate.py` reproduces `data/` byte for byte.

## Companion site

The same tables are described at https://www.arthsingh.com/open-data. That site is part of a
research project on automated web agents: it records visits (time, path, request headers, a keyed
hash of the IP address), as its privacy page explains. It does not set cookies or store full IP
addresses.

## Licence

CC0 1.0. No attribution required.
