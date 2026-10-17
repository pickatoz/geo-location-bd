from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional


class GeoLocationEn:
    def __init__(self) -> None:
        self._data_cache: Optional[dict[str, Any]] = None

    @staticmethod
    def _normalize_lookup_value(value: Any) -> str:
        return str(value if value is not None else "").strip().lower()

    def get_data(self) -> dict[str, Any]:
        if self._data_cache is not None:
            return self._data_cache

        candidates = [
            Path(__file__).resolve().parents[3] / "data" / "geo_data_en.json",
            Path(__file__).resolve().parents[2] / "data" / "geo_data_en.json",
            Path(__file__).resolve().parents[1] / "data" / "geo_data_en.json",
        ]

        for path in candidates:
            if path.exists():
                with path.open("r", encoding="utf-8") as file_obj:
                    self._data_cache = json.load(file_obj)
                return self._data_cache

        raise FileNotFoundError("geo_data_en.json not found in project root or package data folder")

    def get_divisions(self) -> list[dict[str, Any]]:
        return self.get_data().get("divisions") or []

    def get_division_by_id(self, division_id: Any) -> Optional[dict[str, Any]]:
        target_id = int(division_id)
        for division in self.get_divisions():
            if int(division.get("id")) == target_id:
                return division
        return None

    def get_division_by_name(self, division_name: Any) -> Optional[dict[str, Any]]:
        target_name = self._normalize_lookup_value(division_name)
        for division in self.get_divisions():
            if self._normalize_lookup_value(division.get("name")) == target_name:
                return division
        return None

    def get_districts(self, division_id: Any = None) -> list[dict[str, Any]]:
        divisions = self.get_divisions()

        if division_id is None:
            districts: list[dict[str, Any]] = []
            for division in divisions:
                districts.extend(division.get("districts") or [])
            return districts

        division = self.get_division_by_id(division_id) or self.get_division_by_name(division_id)
        if division is None:
            return []
        return division.get("districts") or []

    def get_district_by_id(self, district_id: Any) -> Optional[dict[str, Any]]:
        target_id = int(district_id)
        for district in self.get_districts():
            if int(district.get("id")) == target_id:
                return district
        return None

    def get_district_by_name(self, district_name: Any) -> Optional[dict[str, Any]]:
        target_name = self._normalize_lookup_value(district_name)
        for district in self.get_districts():
            if self._normalize_lookup_value(district.get("name")) == target_name:
                return district
        return None

    def get_district_by_division_id(self, division_id: Any) -> list[dict[str, Any]]:
        division = self.get_division_by_id(division_id) or self.get_division_by_name(division_id)
        return division.get("districts") if division else []

    def get_district_by_division_name(self, division_name: Any) -> list[dict[str, Any]]:
        division = self.get_division_by_name(division_name)
        return division.get("districts") if division else []

    def get_thanas(self, district_id: Any = None) -> list[dict[str, Any]]:
        districts = self.get_districts()

        if district_id is None:
            thanas: list[dict[str, Any]] = []
            for district in districts:
                thanas.extend(district.get("thanas") or [])
            return thanas

        district = self.get_district_by_id(district_id) or self.get_district_by_name(district_id)
        if district is None:
            return []
        return district.get("thanas") or []

    def get_thana_by_id(self, thana_id: Any) -> Optional[dict[str, Any]]:
        target_id = int(thana_id)
        for thana in self.get_thanas():
            if int(thana.get("id")) == target_id:
                return thana
        return None

    def get_thana_by_name(self, thana_name: Any) -> Optional[dict[str, Any]]:
        target_name = self._normalize_lookup_value(thana_name)
        for thana in self.get_thanas():
            if self._normalize_lookup_value(thana.get("name")) == target_name:
                return thana
        return None

    def get_thana_by_district_id(self, district_id: Any) -> list[dict[str, Any]]:
        district = self.get_district_by_id(district_id) or self.get_district_by_name(district_id)
        return district.get("thanas") if district else []

    def get_thana_by_district_name(self, district_name: Any) -> list[dict[str, Any]]:
        district = self.get_district_by_name(district_name)
        return district.get("thanas") if district else []

    def get_thana_by_division_id(self, division_id: Any) -> list[dict[str, Any]]:
        districts = self.get_district_by_division_id(division_id)
        thanas: list[dict[str, Any]] = []
        for district in districts:
            thanas.extend(district.get("thanas") or [])
        return thanas

    def get_thana_by_division_name(self, division_name: Any) -> list[dict[str, Any]]:
        districts = self.get_district_by_division_name(division_name)
        thanas: list[dict[str, Any]] = []
        for district in districts:
            thanas.extend(district.get("thanas") or [])
        return thanas
