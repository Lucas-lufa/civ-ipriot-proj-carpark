from datetime import datetime

from smartpark.mqtt_device import MqttDevice
import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage


class CarPark(MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self.client.loop_forever()
        self._temperature = None

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return max(available, 0)

    @property
    def temperature(self):
        self._temperature
    
    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def full_sign(self,available_spaces):
        """ returns full sign if the car park is full """
        if available_spaces >= 0:
            return "FULL  FULL,"
        else:
            return f"SPACES: {available_spaces}, "
        
    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        print(
            (
                f"TIME: {readable_time}, "
                + f"SPACES: {self.available_spaces}, "
                + f"TEMPC: {self._temperature}"
            )
        )
        message = (
            f"TIME: {readable_time}, "
            + f"{self.full_sign(self.available_spaces)}"
            + f"TEMPC:   {self._temperature}"
        )
        self.client.publish('display', message)

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()



    def on_car_exit(self):
        self.total_cars -= 1
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode()
        # TODO: Extract temperature from payload
        # self.temperature = ... # Extracted value
        payload_split = payload.split()
        self.temperature = payload_split[1]
        # DONETODO
        if 'exit' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()

    

if __name__ == '__main__':
    # TODO: Read config from file
    # config = {'name': "raf-park",
    #           'total-spaces': 130,
    #           'total-cars': 0,
    #           'location': 'L306',
    #           'topic-root': "lot",
    #           'broker': 'localhost',
    #           'port': 1883,
    #           'topic-qualifier': 'entry',
    #           'is_stuff': False
    #           }
    # DONETODO
    config = CarPark.parse_config('smartpark/car-park.json')
    car_park = CarPark(config)
    print("Carpark initialized")
