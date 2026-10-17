# geo-location-bd

Bangladesh geo-location data package for divisions, districts, and thanas with easy lookup methods.

## Features

- Division lookup by ID and case-insensitive name
- District lookup by ID, name, division ID, and division name
- Thana lookup by ID, name, district ID, district name, division ID, and division name
- Built-in in-memory caching for faster repeated access
- English administrative data source included in the package

## Installation

```bash
npm install geo-location-bd
```

## Usage

```js
import { GeoLocationEn } from 'geo-location-bd';

const geo = new GeoLocationEn();

console.log(geo.getDivisionById(1));
console.log(geo.getDivisionByName('barisal'));
console.log(geo.getDistrictByName('barisal'));
console.log(geo.getThanaByName('amtali'));
console.log(geo.getThanaByDivisionName('barisal').slice(0, 5));
```

## Available methods

### Divisions

- `getDivisions()`
- `getDivisionById(divisionId)`
- `getDivisionByName(divisionName)`

### Districts

- `getDistricts(divisionId = null)`
- `getDistrictById(districtId)`
- `getDistrictByName(districtName)`
- `getDistrictByDivisionId(divisionId)`
- `getDistrictByDivisionName(divisionName)`

### Thanas

- `getThanas(districtId = null)`
- `getThanaById(thanaId)`
- `getThanaByName(thanaName)`
- `getThanaByDistrictId(districtId)`
- `getThanaByDistrictName(districtName)`
- `getThanaByDivisionId(divisionId)`
- `getThanaByDivisionName(divisionName)`

> Name-based lookups are case-insensitive and compare after trimming whitespace.

## Data source

This administrative dataset is collected from the Bangladesh Administrative Data repository:
https://github.com/goshamishagar/Bangladesh-Administrative-Data

## License

MIT
