import unittest
from smartpark.config_parser import ConfigParser

class TestParseConfig(unittest.TestCase):
    def test_parse_config(self): 
        car_park = ConfigParser.parse_config('smartpark/car-park.json')
        self.assertEqual(car_park['location'],'L306')
