from stationClasses import StationA, StationB

#building json payload
def build_payload(t,h,wd,wi,r):
    payload = '{"Temperature":"'
    payload += t
    payload += ' Celsius", "Humidity":"'
    payload += h
    payload += '%", "Wind Direction":"'
    payload += wd
    payload += ' degrees", "Wind Intensity":"'
    payload += wi
    payload += ' m/s", "Rain Height":"'
    payload += r
    payload += ' mm/h"}'
    return payload

class message_handler:
    identifier = None
    topic = None
    payload = None
    stationA = None
    stationB = None

    def __init__(self, identifier):
        self.identifier = identifier
        self.stationA = StationA()
        self.stationB = StationB()

    def publish_A(self):
        if self.stationA.ready is True:
            pl = build_payload(self.stationA.temp,self.stationA.hum,self.stationA.windir,self.stationA.winint,self.stationA.rain)
            self.stationA.set_payload(pl)
            self.stationA.connect_a()
        else:
            print("Cannot publish, not enough data")

    def publish_B(self):
        if self.stationB.ready is True:
            pl = build_payload(self.stationB.temp,self.stationB.hum,self.stationB.windir,self.stationB.winint,self.stationB.rain)
            self.stationA.set_payload(pl)
            self.stationA.connect_a()
        else:
            print("Cannot publish, not enough data")

    def handle_A(self):
        print("a")
        if "temp" in self.topic:
            self.stationA.set_temp(self.payload)
        elif "hum" in self.topic:
            self.stationA.set_hum(self.payload)
        elif "windir" in self.topic:
            self.stationA.set_windir(self.payload)
        elif "winint" in self.topic:
            self.stationA.set_winint(self.payload)
        elif "rain" in self.topic:
            self.stationA.set_rain(self.payload)
        self.publish_A()
    
    def handle_B(self):
        print("b")
        if "temp" in self.topic:
            self.stationB.set_temp(self.payload)
        elif "hum" in self.topic:
            self.stationB.set_hum(self.payload)
        elif "windir" in self.topic:
            self.stationB.set_windir(self.payload)
        elif "winint" in self.topic:
            self.stationB.set_winint(self.payload)
        elif "rain" in self.topic:
            self.stationB.set_rain(self.payload)
        self.publish_B()

    def handle_message(self):
        if "stationA" in str(self.topic):
            self.handle_A()
        elif "stationB" in str(self.topic):
            self.handle_B()

    def set_message(self, topic, payload):
        self.topic = topic
        self.payload = payload
        self.handle_message()
    
    
            