import random

from paho.mqtt import client as mqtt_client

broker = 'a40883bf34564fb493b81df755dd41cb.s2.eu.hivemq.cloud'
port = 8883
topic = "talking_tree"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'JasonLeonard'
password = '2!fP5zqS$hf8Qw'

def on_connect(client, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(msg):
    if msg.topic == topic:
        filename = "received_image.jpg"
        with open(filename, "wb") as f:
            f.write(msg.payload)
        print(f"Saved image to {filename}")

def run():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.tls_set()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    client.loop_forever()

if __name__ == '__main__':
    run()