import test from 'node:test';
import assert from 'node:assert/strict';

import { GeoLocationEn } from '../src/index.js';

test('division lookups work with ids and case-insensitive names', () => {
  const loc = new GeoLocationEn();

  assert.ok(loc.getDivisions().length > 0);
  assert.equal(loc.getDivisionById(1).name, 'Barisal');
  assert.equal(loc.getDivisionByName('barisal').name, 'Barisal');
  assert.equal(loc.getDivisionByName('BARISAL').name, 'Barisal');
});

test('district lookups work by id, name, and parent division filters', () => {
  const loc = new GeoLocationEn();

  assert.ok(loc.getDistricts().length > 0);
  assert.equal(loc.getDistrictById(1002).name, 'Barisal');
  assert.equal(loc.getDistrictByName('barisal').name, 'Barisal');
  assert.equal(loc.getDistrictByName('BARISAL').name, 'Barisal');

  const districtsForDivision = loc.getDistrictByDivisionId(1);
  assert.ok(districtsForDivision.length > 0);
  assert.equal(loc.getDistrictByDivisionName('barisal')[0].name, 'Barguna');
});

test('thana lookups work by id, name, and parent filters', () => {
  const loc = new GeoLocationEn();

  assert.ok(loc.getThanas().length > 0);
  assert.equal(loc.getThanaById(100001).name, 'Amtali');
  assert.equal(loc.getThanaByName('amtali').name, 'Amtali');
  assert.equal(loc.getThanaByName('AMTALI').name, 'Amtali');

  assert.ok(loc.getThanaByDistrictId(1002).length > 0);
  assert.ok(loc.getThanaByDistrictName('barisal').length > 0);
  assert.ok(loc.getThanaByDivisionId(1).length > 0);
  assert.ok(loc.getThanaByDivisionName('barisal').length > 0);
});
