import unittest

from geo_location_bd import GeoLocationEn


class GeoLocationEnTests(unittest.TestCase):
    def setUp(self):
        self.geo = GeoLocationEn()

    def test_division_lookups(self):
        self.assertGreater(len(self.geo.get_divisions()), 0)
        self.assertEqual(self.geo.get_division_by_id(1)["name"], "Barisal")
        self.assertEqual(self.geo.get_division_by_name("barisal")["name"], "Barisal")
        self.assertEqual(self.geo.get_division_by_name("BARISAL")["name"], "Barisal")

    def test_district_lookups(self):
        self.assertGreater(len(self.geo.get_districts()), 0)
        self.assertEqual(self.geo.get_district_by_id(1002)["name"], "Barisal")
        self.assertEqual(self.geo.get_district_by_name("barisal")["name"], "Barisal")
        self.assertEqual(self.geo.get_district_by_name("BARISAL")["name"], "Barisal")
        self.assertGreater(len(self.geo.get_district_by_division_id(1)), 0)
        self.assertEqual(self.geo.get_district_by_division_name("barisal")[0]["name"], "Barguna")

    def test_thana_lookups(self):
        self.assertGreater(len(self.geo.get_thanas()), 0)
        self.assertEqual(self.geo.get_thana_by_id(100001)["name"], "Amtali")
        self.assertEqual(self.geo.get_thana_by_name("amtali")["name"], "Amtali")
        self.assertEqual(self.geo.get_thana_by_name("AMTALI")["name"], "Amtali")
        self.assertGreater(len(self.geo.get_thana_by_district_id(1002)), 0)
        self.assertGreater(len(self.geo.get_thana_by_district_name("barisal")), 0)
        self.assertGreater(len(self.geo.get_thana_by_division_id(1)), 0)
        self.assertGreater(len(self.geo.get_thana_by_division_name("barisal")), 0)


if __name__ == "__main__":
    unittest.main()
