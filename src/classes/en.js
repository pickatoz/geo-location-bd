/**
 * @author Pickatoz
 */

import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

export class GeoLocationEn {
  constructor() {
    this.dataCache = null;
  }

  getData() {
    if (this.dataCache) {
      return this.dataCache;
    }

    const candidates = [
      new URL('../data/geo_data_en.json', import.meta.url),
      new URL('../../data/geo_data_en.json', import.meta.url),
      new URL('../../../data/geo_data_en.json', import.meta.url),
    ];

    let resolvedPath = null;

    for (const candidate of candidates) {
      try {
        readFileSync(fileURLToPath(candidate), 'utf-8');
        resolvedPath = candidate;
        break;
      } catch (error) {
        if (error && error.code !== 'ENOENT') {
          throw error;
        }
      }
    }

    if (!resolvedPath) {
      throw new Error('geo_data_en.json not found');
    }

    const raw = readFileSync(fileURLToPath(resolvedPath), 'utf-8');
    this.dataCache = JSON.parse(raw);

    return this.dataCache;
  }

  normalizeLookupValue(value) {
    return String(value ?? '').trim().toLowerCase();
  }

  getDivisions() {
    return this.getData().divisions || [];
  }

  getDivisionById(divisionId) {
    const targetId = Number(divisionId);
    return this.getDivisions().find((division) => Number(division.id) === targetId) || null;
  }

  getDivisionByName(divisionName) {
    const targetName = this.normalizeLookupValue(divisionName);
    return this.getDivisions().find((division) => this.normalizeLookupValue(division.name) === targetName) || null;
  }

  getDistricts(divisionId = null) {
    const divisions = this.getDivisions();

    if (divisionId === null || divisionId === undefined) {
      return divisions.flatMap((division) => division.districts || []);
    }

    const division = this.getDivisionById(divisionId) || this.getDivisionByName(divisionId);
    return division ? division.districts || [] : [];
  }

  getDistrictById(districtId) {
    const targetId = Number(districtId);
    return this.getDistricts().find((district) => Number(district.id) === targetId) || null;
  }

  getDistrictByName(districtName) {
    const targetName = this.normalizeLookupValue(districtName);
    return this.getDistricts().find((district) => this.normalizeLookupValue(district.name) === targetName) || null;
  }

  getDistrictByDivisionId(divisionId) {
    return this.getDistricts(divisionId);
  }

  getDistrictByDivisionName(divisionName) {
    const division = this.getDivisionByName(divisionName);
    return division ? division.districts || [] : [];
  }

  getThanas(districtId = null) {
    const districts = this.getDistricts();

    if (districtId === null || districtId === undefined) {
      return districts.flatMap((district) => district.thanas || []);
    }

    const district = this.getDistrictById(districtId) || this.getDistrictByName(districtId);
    return district ? district.thanas || [] : [];
  }

  getThanaById(thanaId) {
    const targetId = Number(thanaId);
    return this.getThanas().find((thana) => Number(thana.id) === targetId) || null;
  }

  getThanaByName(thanaName) {
    const targetName = this.normalizeLookupValue(thanaName);
    return this.getThanas().find((thana) => this.normalizeLookupValue(thana.name) === targetName) || null;
  }

  getThanaByDistrictId(districtId) {
    const district = this.getDistrictById(districtId) || this.getDistrictByName(districtId);
    return district ? district.thanas || [] : [];
  }

  getThanaByDistrictName(districtName) {
    const district = this.getDistrictByName(districtName);
    return district ? district.thanas || [] : [];
  }

  getThanaByDivisionId(divisionId) {
    return this.getDistrictByDivisionId(divisionId).flatMap((district) => district.thanas || []);
  }

  getThanaByDivisionName(divisionName) {
    return this.getDistrictByDivisionName(divisionName).flatMap((district) => district.thanas || []);
  }
}
