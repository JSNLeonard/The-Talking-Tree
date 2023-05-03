import random
import time
import os

from paho.mqtt import client as mqtt_client

broker = 'a40883bf34564fb493b81df755dd41cb.s2.eu.hivemq.cloud'
port = 8883
topic = "talking_tree"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'JasonLeonard'
password = '2!fP5zqS$hf8Qw'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}")
            
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.tls_set()
    client.connect(broker, port)
    return client

def publish(client):
    filename = "image.jpg"
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            image = f.read()
        result = client.publish(topic, image, qos=1)
        status = result[0]
        if status == mqtt_client.MQTT_ERR_SUCCESS:
            print(f"Sent image {filename} to topic {topic}")
        else:
            print(f"Failed to send image {filename} to topic {topic}")
    else:
        print(f"Image file {filename} not found")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    time.sleep(5)
    client.loop_stop()
    client.disconnect()

if __name__ == '__main__':
    run()