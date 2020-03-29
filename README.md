# First Assignment IoT 2020
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
