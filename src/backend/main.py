# coding=utf-8
import paho.mqtt.client as mqtt
import registers
from configs import config_broker
import json


def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe("/tracker")


def on_message(client, userdata, msg):
    print("Message received in the topic " + msg.topic + ": " + str(msg.payload.decode("utf-8")))
    message = str(msg.payload.decode("utf-8"))
    message = json.loads(message)
    try:
        disp_id = message['disp_id']
        command = message['command']
        lat = message['lat']
        lng = message['lng']

        if command == 'set_geo':
            registers.insert_registers(msg.topic, disp_id, lat, lng)

    except Exception as err:
        print(f"Unexpected {err=}")


params = config_broker()
client = mqtt.Client("Backend")
client.on_connect = on_connect
client.on_message = on_message
client.connect(params['host'], int(params['port']))
client.loop_forever()
