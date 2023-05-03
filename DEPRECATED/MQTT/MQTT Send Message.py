import random
import time

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
    msg_count = 0
    while True:
        time.sleep(1)
        msg = "Hello, MQTT!"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()