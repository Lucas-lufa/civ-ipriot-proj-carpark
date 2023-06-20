import unittest
from smartpark.simple_mqtt_carpark import CarPark

class TestCarPark(unittest.TestCase):
    def test_full_sign(self):
        config = CarPark.parse_config('smartpark/car-park.json')
        car_park = CarPark(config)

