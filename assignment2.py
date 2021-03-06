import paho.mqtt.client as mqtt
from messageHandler import message_handler
import time
# This is the main script for Assignment 2 of IoT
# Its purpose is to subscribe to our local mqtt-sn broker (mosquitto.rsmb in my case)
# Every time it receives a message, it will send it to the messageHandler, which will do the work
# It is important to note that since my device on thingsboard is an entire station, our local virtual
# station will send the data only when the payload is complete (i.e. when it has every value, this may 
# lead to data loss while the payload is still incomplete)

# Local Broker connection
local_broker="127.0.0.1"
local_port=1886

#function definitions
def on_connect(client, userdata, flags, rc):        #connection feedback
    print("Client "+ client + " connected with result code " + str(rc))

def on_publish(client,userdata,result):             #publish feedback
    print("data published to thingsboard \n")
    pass
def on_subscribe(client, userdata, mid, granted_qos):
    print("Client " + client + " has subscribed successfully")

#def on_message(client, userdata, message):
#    print("Message received: "+ message)
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    payload = str(message.payload.decode("utf-8"))
    print('Sending to message handler the following topic: [' + message.topic + '] and payload: [' + payload + ']')
    handler.set_message(message.topic,payload)
    
def on_log(client, userdata, level, buf):       #used for logging purposes
    print("log: ",buf)

#instantiating or messageHandler
handler = message_handler(1)
#instantiating local subscriber for station A
bridge = mqtt.Client("Bridge")
bridge.on_connect = on_connect
bridge.on_publish = on_publish
bridge.on_subscribe = on_subscribe
bridge.on_message = on_message
print("Local bridge created successfully")

#subscribing to local broker in order to get sensor data
bridge.connect(local_broker,local_port,60)
bridge.subscribe("/sensor/+/data/#")

#the loop forever function handles reconnections
bridge.loop_forever()