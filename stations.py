import paho.mqtt.client as mqtt
import random as rnd
import time
import os
#ThingsBoard integration
ACCESS_TOKEN_1=os.environ.get("STATION_A")   #this access token is used by Station A to connect to ThingsBoard
ACCESS_TOKEN_2=os.environ.get("STATION_B")   #this access token is used by Station B to connect to ThingsBoard
broker="demo.thingsboard.io"            #default broker provided by ThingsBoard with its port
port=1883

#function definitions
def on_connect(client, userdata, flags, rc):        #connection feedback
    print("Connected with result code " + str(rc))

def on_publish(client,userdata,result):             #publish feedback
    print("data published to thingsboard \n")
    pass

def get_temperature():                              #random temperature generator
    return '%.2f'%rnd.uniform(-50,50) + " Celsius"

def get_humidity():                                 #random humidity generator
    return '%.2f'%rnd.uniform(0,100) + "%"

def get_wind_direction():                           #random wind direction generator
    return str(rnd.randrange(0,360)) + " degrees"

def get_wind_intensity():                           #random wind intensity generator
    return str(rnd.randrange(0,100)) + " m/s"

def get_rain_height():                              #random rain height generator
    return str(rnd.randrange(0,50)) + " mm/h"

#building json payload
def build_payload():
    payload = '{"Temperature":"'
    payload += get_temperature()
    payload += '", "Humidity":"'
    payload += get_humidity()
    payload += '", "Wind Direction":"'
    payload += get_wind_direction()
    payload += '", "Wind Intensity":"'
    payload += get_wind_intensity()
    payload += '", "Rain Height":"'
    payload += get_rain_height()
    payload += '"}'
    return payload

#instantiating mqtt client for station A
stationA = mqtt.Client()
stationA.on_connect = on_connect
stationA.on_publish = on_publish    
stationA.username_pw_set(ACCESS_TOKEN_1)
print("Station A created successfully")

#instantiating mqtt client for station B
stationB = mqtt.Client()
stationB.on_connect = on_connect
stationB.on_publish = on_publish    
stationB.username_pw_set(ACCESS_TOKEN_2)
print("Station B created successfully")

#connection to thingsboards mqtt broker
stationA.connect(broker,port,60)
stationB.connect(broker,port,60)

topic = "v1/devices/me/telemetry"       #in thingsboard every device has its own topic, which is telemetry

while True:
    payload = build_payload()
    print(payload)
    stationA.publish(topic, payload)    #publish random values to station A telemetries
    time.sleep(5)
    payload = build_payload()
    print(payload)
    stationB.publish(topic, payload)    #publish random values to station B telemetries

stationA.loop_forever()
stationB.loop_forever()