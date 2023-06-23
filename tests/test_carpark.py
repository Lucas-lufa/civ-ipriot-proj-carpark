import unittest
from smartpark.simple_mqtt_carpark import CarPark
import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage

class TestCarPark(unittest.TestCase):
    
    def test_full_sign(self):
        config = CarPark.parse_config('smartpark/car-park.json')
        car_park = CarPark(config)
        
        car_park.total_spaces = 1
        car_park.total_cars = 0
        sign = car_park.full_sign(car_park.available_spaces)
        self.assertEqual(sign,"SPACES: 1, ")

        car_park.on_car_entry()
        sign = car_park.full_sign(car_park.available_spaces)
        self.assertEqual(sign,"FULL  FULL,")
        # car_park.client.loop_stop()
        