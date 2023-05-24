import paho.mqtt.client as paho





# client.publish("lot/sensor", "Hello from Python")


class Sensor:
    def __init__(self, config):
        self.name = config['name']
        self.location = config['location']
        self.topic = config['topic']
        self.broker = config['broker']
        self.port = config['port']
        self.client = paho.Client()
        self.client.connect(self.broker,
                            self.port)
<<<<<<< HEAD
        self.on_detection = None
=======

>>>>>>> be07f7d6ff3831a9ef76f5b07d21a25339330c0f

    def on_detection(self, message):
        self.client.publish(self.topic, message)

    def start_sensing(self):
        while True:
            reply = input("Is there a car?")
            if reply == 'y':
                self.on_detection("Car, I saw a car!!")



if __name__ == '__main__':
    config = {'name': 'super sensor',
              'location': 'L306',
              'topic': "lot/sensor",
              'broker': 'localhost',
              'port': 1883}

    sensor = Sensor(config)
<<<<<<< HEAD
<<<<<<< HEAD
    sensor.on_detection = on_detection
=======
>>>>>>> 3f81815e777a69b411e3d6f4efef1f2326ca7916
=======
>>>>>>> be07f7d6ff3831a9ef76f5b07d21a25339330c0f
    print("Sensor initialized")
    sensor.start_sensing()
