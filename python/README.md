# geo-location-bd

Bangladesh geo-location data package for divisions, districts, and thanas with easy lookup methods.

## Installation

```bash
pip install geo-location-bd
```

## Usage

```python
from geo_location_bd import GeoLocationEn

geo = GeoLocationEn()
print(geo.get_division_by_id(1))
print(geo.get_division_by_name("barisal"))
print(geo.get_district_by_name("barisal"))
print(geo.get_thana_by_name("amtali"))
```

## Available methods

- `get_divisions()`
- `get_division_by_id(division_id)`
- `get_division_by_name(division_name)`
- `get_districts(division_id=None)`
- `get_district_by_id(district_id)`
- `get_district_by_name(district_name)`
- `get_district_by_division_id(division_id)`
- `get_district_by_division_name(division_name)`
- `get_thanas(district_id=None)`
- `get_thana_by_id(thana_id)`
- `get_thana_by_name(thana_name)`
- `get_thana_by_district_id(district_id)`
- `get_thana_by_district_name(district_name)`
- `get_thana_by_division_id(division_id)`
- `get_thana_by_division_name(division_name)`

Name-based lookups are case-insensitive and ignore surrounding whitespace.
