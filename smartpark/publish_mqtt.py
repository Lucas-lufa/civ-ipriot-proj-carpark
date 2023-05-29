#import time
import paho.mqtt.client as paho
from paho.mqtt.client import Client

broker = 'localhost'
port = 1883

# def on_message(client, userdata, msg):
#     print(f"Received {msg.payload.decode()}")

client = paho.Client()
# client.on_message = on_message
client.connect(broker, port)
client.publish("lot/sensor", "hello World")
# client.subscribe("lot/sensor")
# client.loop_forever()

class Publish_MQTT(Client):
    """ publish over mqtt """
    def __init__(self, message="" ,topic="", broker="localhost", port=1883):
        self.message = message
        self.topic = topic
        self.broker = broker
        self.port = port        
        self.client = Client()

    self.client.connect(broker, port)
    self.client.publish(self.topic, self.message)
