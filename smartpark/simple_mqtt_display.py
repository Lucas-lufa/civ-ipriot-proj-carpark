import mqtt_device
import time
class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""
    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('display')
        self.client.loop_forever()

    def display(self, *args, padding=5):
        left_padding = ""
        if padding != 0:
            left_padding = " " * padding
        print('*' * 20)
        for val in args:
            print(left_padding+val)
            # print(val.strip()) DONETODO extracted free space
            time.sleep(1)
        print('*' * 20)

    def format_data(self, data):
        data = data.replace(', ',',')
        data = data.replace(': ',':')
        return data
    
    def on_message(self, client, userdata, msg):
       data = msg.payload.decode()
       data = self.format_data(data)
       self.display(*data.split(','))
       # I parsed to extract enough free space to make it uniformed and then centered it.
       # TODO: Parse the message and extract free spaces,\
       #  temperature, time

if __name__ == '__main__':
    # TODO: Read config from file
    config = Display.parse_config('smartpark/car-park.json')
    # DONETODO
    # config = {'name': 'display',
    #  'location': 'L306',
    #  'topic-root': "lot",
    #  'broker': 'localhost',
    #  'port': 1883,
    #  'topic-qualifier': 'na'
    #  }
    display = Display(config)

