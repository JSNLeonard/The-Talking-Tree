# Name: Jason Leonard

# Project Name: Talking Tree

# File Name: MQTT Send.py

# File Description: This Python script imports necessary modules and libraries such as random, time, os, and paho.mqtt.client for MQTT communication.
# ################# It defines the MQTT broker information, connects to the broker, and sets up callback functions.
# ################# The script prompts the user to enter their name, question, and image filename, constructs a payload, and publishes it to the MQTT broker.
# ################# It also sends the image file over MQTT, renames it with the user's name and a timestamp, and saves it to a specified folder.
# ################# Finally, it stops the MQTT client loop and disconnects from the broker.
# ################# The script enables communication with an MQTT broker to send messages and images while organizing the received files based on user information.

# Imports essential modules and libraries such as Random, Time, OS, and Paho MQTT.
import random
import time
import os
from paho.mqtt import client as mqtt_client

# Define MQTT broker information.
broker = 'a40883bf34564fb493b81df755dd41cb.s2.eu.hivemq.cloud'
port = 8883
message_topic = "Message"
image_topic = "Image"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'JasonLeonard'
password = '2!fP5zqS$hf8Qw'

# Define function to connect to MQTT broker.
def connect_mqtt():

    # Define callback function to handle connection events.
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}")

    # Create MQTT client object.
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.tls_set()
    client.connect(broker, port)
    return client

# Define function to send image over MQTT.
def send_image(client, first_name, last_name, image_filename, image_folder):
    if os.path.exists(image_filename):
        with open(image_filename, "rb") as f:
            image = f.read()
        
        # Generate new image filename with timestamp.
        new_image_filename = f"{first_name}_{last_name}_{int(time.time())}.jpg"
        
        # Publish image to MQTT broker.
        result = client.publish(image_topic, image, qos=1, properties={"responseTopic": "ImageReceived", "correlationData": new_image_filename})
        
        # Check the result of the publish operation.
        status = result[0]
        if status == mqtt_client.MQTT_ERR_SUCCESS:
            print(f"Sent image {image_filename} to topic {image_topic}")
            os.rename(image_filename, os.path.join(image_folder, new_image_filename))
            print(f"Renamed image file to {new_image_filename}")
        else:
            print(f"Failed to send image {image_filename} to topic {image_topic}")
    else:
        print(f"Image file {image_filename} not found")

def run():
    # Set up the image folder.
    image_folder = r"/home/pi/Documents/The-Talking-Tree/Images"
    
    # image_folder = r"C:/Users/Jason/Documents/College Year 4/Semester 2/Final Year Project/The-Talking-Tree/Images"
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    # Connect to the MQTT broker and subscribe to the message topic.
    client = connect_mqtt()
    client.subscribe(message_topic)
    client.loop_start()

    # Get the user's name, question, and image filename.
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    question = input("Enter your question: ")
    image_filename = input("Enter the filename of your image: ")

    # Construct the payload and publish it to the message topic.
    payload = f"{first_name},{last_name},{question},{image_filename}"
    client.publish(message_topic, payload)

    # Send the image over MQTT.
    send_image(client, first_name, last_name, image_filename, image_folder)

    # Stop the MQTT client loop and disconnect from the broker.
    client.loop_stop()
    client.disconnect()

# Run the main function if this file is executed directly.
if __name__ == '__main__':
    run()