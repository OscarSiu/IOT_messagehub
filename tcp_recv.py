import socket
import json
import paho.mqtt.client as mqtt


# Define the MQTT broker address and port
broker_address = 'test.mosquitto.org'
broker_port = 1883

# Define the MQTT topic to publish the JSON data to
topic = 'panda/topic'


# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)


# Create a MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    connection, client_address = sock.accept()
    print("Connection from", client_address)

    try:
        # Receive the data in chunks and concatenate them
        data = b''
        while True:
            chunk = connection.recv(1024)
            if not chunk:
                break
            data += chunk

        # Decode the received data as a JSON string
        json_string = data.decode()

        # Parse the JSON string into a Python dictionary
        data = json.loads(json_string)

        # Do something with the data
        # Publish the JSON data to the MQTT broker
        client.publish(topic, json_string)
        # Print a confirmation message
        print("JSON data sent to MQTT broker:", json_string)
        print("Received data:", data)
        print("\n")

    finally:
        # Close the connection
        connection.close()
