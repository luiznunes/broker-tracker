# coding=utf-8
import paho.mqtt.client as mqtt
import registers
from configs import config_broker
import json
import os

def set_environments():
    # Read in the file
    with open('parameters.ini.sample', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('PG_HOST', os.environ['PG_HOST'])
    filedata = filedata.replace('PG_DATABASE', os.environ['PG_DATABASE'])
    filedata = filedata.replace('PG_USER', os.environ['PG_USER'])
    filedata = filedata.replace('PG_PASSWD', os.environ['PG_PASSWD'])
    filedata = filedata.replace('PG_PORT', os.environ['PG_PORT'])

    filedata = filedata.replace('MQTT_HOST', os.environ['MQTT_HOST'])
    filedata = filedata.replace('MQTT_PORT', os.environ['MQTT_PORT'])


    # Write the file out again
    with open('parameters.ini', 'w') as file:
        file.write(filedata)


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


set_environments()
params = config_broker()
client = mqtt.Client("Backend")
client.on_connect = on_connect
client.on_message = on_message
client.connect(params['host'], int(params['port']))
client.loop_forever()
