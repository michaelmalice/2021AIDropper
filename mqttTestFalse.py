#!/usr/bin/python3
#
import time
import random
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

broker = '10.0.0.43'
state_topic = 'home-assistant/smartcam/person'
delay = 5

# Send a single message to set the mood
publish.single('home-assistant/smartcam/person', 'false', hostname=broker)

# Send messages in a loop
'''client = mqtt.Client("ha-client")
client.connect(broker)
client.loop_start()

while True:
    client.publish(state_topic, random.randrange(0, 50, 1))
    time.sleep(delay)
'''
