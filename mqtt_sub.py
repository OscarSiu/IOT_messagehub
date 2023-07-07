import paho.mqtt.client as mqtt
import requests
import json
from flask import Flask, render_template


# Define the MQTT broker address and port
broker_address = 'test.mosquitto.org'
broker_port = 1883

# Define the MQTT topic to subscribe to
topic = 'panda/topic'

# Create a Flask app instance
app = Flask(__name__)

# Define a variable to store the received data
received_data = {}

# Define the MQTT on_message callback function
def on_message(client, userdata, message):
    global received_data
    # Decode the received message payload as a JSON string
    json_string = message.payload.decode()

    # Parse the JSON string into a Python dictionary
    received_data = json.loads(json_string)
    
    print("Received JSON data:", received_data)
    
    #return {"Sensor data": json_string}, 200
    

# Create a MQTT client instance
client = mqtt.Client()

# Set the on_message callback function
client.on_message = on_message

# Connect to the MQTT broker and subscribe to the topic
client.connect(broker_address, broker_port)
client.subscribe(topic)

@app.route('/')
def index():
	return received_data, 200
	
# Run the flask app
if __name__ == "__main__":

    # Start the MQTT loop to receive messages
    client.loop_start()
    app.run(port=8088, debug=True)
    



