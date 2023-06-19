import unittest
import json
from config_parser import ConfigParser
class TestParseConfig(unittest.TestCase):
    def test_parse_config(self):
        config_string = {'name': "raf-park",
              'total-spaces': 130,
              'total-cars': 0,
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry',
              'is_stuff': False
              }
        config = json.dumps(config_string)
        car_park = ConfigParser.parse_config(config)
        self.assertEqual(car_park['location'],'L306')
        print(car_park,config)
