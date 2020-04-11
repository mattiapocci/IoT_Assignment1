import paho.mqtt.client as mqtt
from messageHandler import message_handler
import time
import ttn          #necessary to instantiate a ttn HandlerClient
import re
import json
import os

# TTN application settings
app_id = os.environ.get("TTN_APP_ID")
access_key = os.environ.get("TTN_APP_KEY")

# This callback is triggered whenever a new message is published by TTN application
def uplink_callback(msg, client):
    
    print("Received uplink from ", msg.dev_id)
    mess = str(msg.payload_fields)
    # Building payload to get it ready for thingsboard
    regex = re.search('{(.+?)}', mess)
    payload = "{"
    if regex:
        payload += regex.group(1)
    payload += '}'
    print(msg.payload_fields)
    print(payload)
    pl = eval(payload)
    # Adding units of measure
    pl["Temperature"] = str(pl["Temperature"]) + ' Celsius'
    pl["Humidity"] = str(pl["Humidity"]) + '%'
    pl["Wind Direction"] = str(pl["Wind Direction"]) + ' degrees'
    pl["Wind Intensity"] = str(pl["Wind Intensity"]) + ' m/s'
    pl["Rain Height"] = str(pl["Rain Height"]) + ' mm/h'
    payload = json.dumps(pl)
    # Giving the payload to the message handler to publish it to thingsboard
    messHandler.publish(str(msg.dev_id),payload)

messHandler = message_handler(1)
handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
while True:
    pass
mqtt_client.close()