# Name: Jason Leonard

# Project Name: Talking Tree

# File Name: MQTT Receive.py

# File Description: This Python script imports necessary modules and libraries such as random, time, mariadb, os, and paho.mqtt.client for MQTT communication and database operations.
# ################# It defines the MQTT broker information, connects to the broker, and sets up callback functions.
# ################# The script includes a function to connect to the MQTT broker and another function to insert data into a MariaDB database.
# ################# It also defines a callback function to handle incoming MQTT messages, where it processes the received message payload and inserts the data into the database.
# ################# Additionally, the script saves the received image file to a specified folder using the user's name and a timestamp as the filename.
# ################# The script runs an infinite loop to continuously process incoming MQTT messages and gracefully stops upon a keyboard interrupt.

# Imports essential modules and libraries such as Random, Time, MariaDB, OS, and Paho MQTT.
import random
import time
import mariadb
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
            client.subscribe(message_topic)
            client.subscribe(image_topic)
        else:
            print(f"Failed to connect, return code {rc}")

    # Create MQTT client object.
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.tls_set()
    client.connect(broker, port)
    return client

# Define function to insert data into MariaDB.
def insert_data(first_name, last_name, question, image_filename):
    try:
        conn = mariadb.connect(
            user="root",
            password="TalkingTree2023",
            host="localhost",
            port=3306,
            database="TalkingTree"
        )
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO user_data (first_name, last_name, question, image, timestamp) "
            f"VALUES ('{first_name}', '{last_name}', '{question}', '{image_filename}', NOW())"
        )
        conn.commit()
        print(f"Inserted data into database for {first_name} {last_name}")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
    finally:
        if conn:
            conn.close()

# Define callback function to handle incoming MQTT messages.
def on_message(client, userdata, message):
    global first_name, last_name  # Declare as global to update the outer variables

    if message.topic == message_topic:
        payload = message.payload.decode()
        print(f"Received message '{payload}' from topic '{message.topic}'")
        data = payload.split(",")
        if len(data) != 4:
            print(f"Invalid message format: {payload}")
            return
        first_name, last_name, question, image_filename = data
        insert_data(first_name, last_name, question, image_filename)

    elif message.topic == image_topic:

        # This message contains the image.
        image_data = message.payload

        # Generate the new image filename using the correlation data as the timestamp.
        timestamp = int(time.time())
        image_filename = f"{first_name}_{last_name}_{timestamp}.jpg"

        # Save the image to a file.
        image_folder = r"/home/pi/Documents/The-Talking-Tree/Images"

        # image_folder = r"C:/Users/Jason/Documents/College Year 4/Semester 2/Final Year Project/The-Talking-Tree/Images"
        image_path = os.path.join(image_folder, image_filename)
        with open(image_path, "wb") as file:
            file.write(image_data)
        print(f"Image saved to {image_path}")

def run():

    # Connect to the MQTT broker and subscribe to the message topic.
    client = connect_mqtt()
    client.on_message = on_message
    client.loop_start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:

            # Stop the MQTT client loop and disconnect from the broker.
            client.loop_stop()
            client.disconnect()
            break

# Run the main function if this file is executed directly.
if __name__ == '__main__':
    run()