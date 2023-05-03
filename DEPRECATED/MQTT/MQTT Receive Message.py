import paho.mqtt.client as mqtt

# Define MQTT broker parameters
broker_url = "a40883bf34564fb493b81df755dd41cb.s2.eu.hivemq.cloud"
broker_port = 8883
username = "JasonLeonard"
password = "2!fP5zqS$hf8Qw"
topic = "talking_tree"

# Define callback function for MQTT message received event
def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode("utf-8")))

# Create MQTT client instance and configure it
client = mqtt.Client()
client.username_pw_set(username=username, password=password)
client.tls_set()
client.connect(broker_url, broker_port)

# Subscribe to the desired topic and start the loop to receive messages
client.subscribe(topic)
client.on_message = on_message
client.loop_forever()