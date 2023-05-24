import time
import paho.mqtt.client as paho

broker = 'localhost'
port = 1883

# def on_message(client, userdata, msg):
#     print(f"Received {msg.payload.decode()}")

client = paho.Client()
# client.on_message = on_message
client.connect(broker, port)
client.publish("lot/sensor", "hello")
# client.subscribe("lot/sensor")
# client.loop_forever()