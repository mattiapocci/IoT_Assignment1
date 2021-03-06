# Assignments of IoT 2020, Master of Engineering in Computer Science, Sapienza University of Rome

# First Assignment
This assignment consists in developing two MQTT clients on our local machine and connect them to a MQTT broker. For this purpose we will use a python script for the two clients and ThingsBoard for the broker.
## Python MQTT Client
The developed python script (stations.py) relies on the publicly available paho-mqtt library [[https://pypi.org/project/paho-mqtt/](https://pypi.org/project/paho-mqtt/)]. This library provides a MQTT implementation, through which we will create our client.
Our clients represent two virtual station, named Station A and Station B, which at regular intervals output the following values:
- Temperature (-50 ... 50 Celsius)
- Humidity (0 ... 100%)
- Wind direction (0 ... 360 degrees)
- Wind intensity (0 ... 100 m/s)
- Rain Height (0 ... 50 mm/h)

In order to output random values, we will use the random python library [[https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)].
## Thingsboard
ThingsBoard is an open-source IoT platform for data collection, processing, visualization, and device management. [[https://github.com/thingsboard/thingsboard](https://github.com/thingsboard/thingsboard)]
This powerful tool comes for free in the demo version, which is sufficient for our purpose, since it offers a MQTT broker, alongside with the possibility to create public dashboards for data visualization (the json file is provided in this github repo).
## Hands on tutorial
Have a look at this article for a full hands-on tutorial: [https://www.linkedin.com/pulse/hands-on-tutorial-implementation-two-virtual-stations-mattia-pocci]
## Video demonstration
For a full video demonstration of the software in action check out this link: [https://youtu.be/22f--kObWeA]
## Public dashboard
Here is the link of the public dashboard: https://demo.thingsboard.io/dashboard/108941e0-6b83-11ea-8e0a-7d0ef2a682d3?publicId=71a3a600-6a11-11ea-ad02-b3576b7d39f1

# Second Assignment
This assignment consists in extending the previous one, replacing the two environmental stations by means of Riot OS applications. Given that a Riot OS application is capable to handle the MQTT-SN protocol, we will develop an MQTT-SN to MQTT bridge, in order to send data to ThingsBoard.
## Hands on tutorial
Have a look at this article for a full hands-on tutorial: [https://www.linkedin.com/pulse/hands-on-tutorial-mqtt-sn-mqtt-bridge-using-python-riot-mattia-pocci]
## Video demonstration
For a full video demonstration of the software in action check out this link: [https://youtu.be/Sbsyoo3aPLI]

# Third Assignment
This assignment consists in replacing the MQTT protocol exploited in the previous assignments with LoRaWAN and TheThingsNetwork [https://www.thethingsnetwork.org/].
To achieve this purpose, we will use the B-L072Z-LRWAN1 LoRa kit [https://www.st.com/en/evaluation-tools/b-l072z-lrwan1.html]. In particular, we will flash a Riot OS firmware on top of them to retrieve sensor data and send them to TTN via LoRaWAN.
Since TTN has a built in MQTT broker, we will slightly modify the previously built Python Bridge in order to publish data to our ThingsBoard dashboard.
## Hands on tutorial
Have a look at this article for a full hands-on tutorial: [https://www.linkedin.com/pulse/hands-on-tutorial-publishing-data-from-iot-lab-via-lorawan-pocci]
## Video demonstration
For a full video demonstration of the software in action check out this link: [https://youtu.be/5NQKkk4fbZo]

# Fourth Assignment
This assignment consists in building a Crowd Sensing Application, using HTML5 and the Generic Sensor API.
To achieve this purpose, we will use Node.js. In particular, since the Generic Sensor API is available only through an https connection, we will set up a local https server.
Our webapp will collect accelerometer data, and will evaluate whether the user is walking or not. At first the estimation will be performed via ThingsBoard (using a rule chain), while in the second part of the assignment it will be performed directly on the user's smartphone via edge computing.
The output of our model will be visible through a ThingsBoard dashboard
The code of this assignment is located in the assignment4 folder of this repo.
## Dashboard
The final public dashboard is available here: [https://demo.thingsboard.io:/dashboard/24f53670-92d9-11ea-9a66-358c6522b855?publicId=71a3a600-6a11-11ea-ad02-b3576b7d39f1]
## Hands on tutorial
Have a look at this article for a full hands-on tutorial: [https://www.linkedin.com/pulse/hands-on-tutorial-crowdsensing-application-using-general-mattia-pocci]
## Video demonstration
For a full video demonstration of the software in action check out this link: [https://youtu.be/UDssyeSuvqM]
