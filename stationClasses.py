import paho.mqtt.client as mqtt
import time

#function definitions
def on_connect(client, userdata, flags, rc):        #connection feedback
    print("Client "+ client + " connected with result code " + str(rc))

def on_publish(client,userdata,result):             #publish feedback
    print("data published to thingsboard \n")
    pass
def on_subscribe(client, userdata, mid, granted_qos):
    print("Client " + client + " has subscribed successfully")

def on_log(client, userdata, level, buf):
    print("log: ",buf)

class StationA:
    ACCESS_TOKEN='NbIwSmfPyfdSZ81MpHyL'     #access token to write on thingsboard
    broker="demo.thingsboard.io"            #default broker provided by ThingsBoard with its port
    port=1883
    topic = "v1/devices/me/telemetry"       #default topic
    temp = None
    hum = None
    windir = None
    winint = None
    rain = None
    ready = False                           #true if it has enough data to publish to thingsboard
    payload = None
    def set_payload(self, payload):
        self.payload = payload

    def set_temp(self, temp):
        self.temp = temp
        if self.payload is None:     #otherwise I am ready for sure
            if self.hum is not None and self.windir is not None and self.winint is not None and self.rain is not None:
                self.ready = True    #I have a complete set of data and I can publish
    
    def set_hum(self, hum):
        self.hum = hum
        if self.payload is None:
            if self.temp is not None and self.windir is not None and self.winint is not None and self.rain is not None:
                self.ready = True    #I have a complete set of data and I can publish 

    def set_windir(self, windir):
        self.windir = windir
        if self.payload is None:
            if self.hum is not None and self.temp is not None and self.winint is not None and self.rain is not None:
                self.ready = True    #I have a complete set of data and I can publish  

    def set_winint(self, winint):
        self.winint = winint
        if self.payload is None:
            if self.hum is not None and self.windir is not None and self.temp is not None and self.rain is not None:
                self.ready = True    #I have a complete set of data and I can publish    
    def set_rain(self, rain):
        self.rain = rain
        if self.payload is None:
            if self.hum is not None and self.windir is not None and self.winint is not None and self.temp is not None:
                self.ready = True    #I have a complete set of data and I can publish    

    
    def connect_a(self):
        a = mqtt.Client()
        a.on_connect=on_connect
        a.on_publish=on_publish
        a.on_log=on_log
        a.username_pw_set(self.ACCESS_TOKEN)
        print("Client created")
        a.connect(self.broker,self.port,60)
        time.sleep(5)
        a.publish(self.topic,self.payload)

class StationB:
    ACCESS_TOKEN='Nqdsei4qVHggzEFDtZEt'     #access token to write on thingsboard
    broker="demo.thingsboard.io"            #default broker provided by ThingsBoard with its port
    port=1883
    topic = "v1/devices/me/telemetry"       #default topic
    temp = None
    hum = None
    windir = None
    winint = None
    rain = None
    ready = False
    payload = None
    def set_payload(self, payload):
        self.payload = payload

    def set_temp(self, temp):
        self.temp = temp
        if self.payload is None:     #otherwise I am ready for sure
            if self.hum is not None and self.windir is not None and self.winint is not None and self.rain is not None:
                self.ready = True    #I have a complete set of data and I can publish
    
    def set_hum(self, hum):
        self.hum = hum
        if self.payload is None:
            if self.temp is not None and self.windir is not None and self.winint is not None and self.rain is not None:
                self.ready = True    #I have a complete set of data and I can publish 

    def set_windir(self, windir):
        self.windir = windir
        if self.payload is None:
            if self.hum is not None and self.temp is not None and self.winint is not None and self.rain is not None:
                self.ready = True    #I have a complete set of data and I can publish  

    def set_winint(self, winint):
        self.winint = winint
        if self.payload is None:
            if self.hum is not None and self.windir is not None and self.temp is not None and self.rain is not None:
                self.ready = True    #I have a complete set of data and I can publish    
    def set_rain(self, rain):
        self.rain = rain
        if self.payload is None:
            if self.hum is not None and self.windir is not None and self.winint is not None and self.temp is not None:
                self.ready = True    #I have a complete set of data and I can publish    

    def connect_b(self):
        b = mqtt.Client()
        b.on_connect=on_connect
        b.on_publish=on_publish
        b.on_log=on_log
        b.username_pw_set(self.ACCESS_TOKEN)
        print("Client created with id " + self.ID)
        b.connect(self.broker,self.port,60)
        time.sleep(5)
        b.publish(self.topic,self.payload)
        b.disconnect()