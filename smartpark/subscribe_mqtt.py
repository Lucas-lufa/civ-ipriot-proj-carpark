import time
import paho.mqtt.client as paho
from paho.mqtt.client import _OnMessage, Client


broker = 'localhost'
port = 1883

def on_message(client, userdata, msg):
    print(f"Received {msg.payload.decode()}")

client = paho.Client()
client.on_message = on_message
client.connect(broker, port)
client.subscribe("lot/sensor")
client.loop_forever()

class Subscribe_QMTT(Client):
    """ Subscribes to a topic """
    def __init__(self, topic="",broker="localhost", port=1882):
        self.topic = topic
        self.broker = broker
        self.port = port
        self.client = Client()

    def on_message(self, client, userdata, msg):
        """ for now print but will be able to pass on. Can be published or used """
        print(f"Received {msg.payload.decode()}")

    client.on_message = on_message
    client.connect(broker, port)
    client.subscribe(topic)
    client.loop_forever()