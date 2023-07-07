import socket
import json
import time

# Define the UDP server's IP address and port number
TCP_IP = "127.0.0.1"
TCP_PORT = 12345

count = 1
while True:
    
    
    # Load JSON data from file
    with open('sensor_data.json', 'r') as f:
        data = json.load(f)
    
    #print(data)

    # Convert JSON data to bytes
    encode_data = json.dumps(data).encode('utf-8')

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = (TCP_IP, TCP_PORT)
    sock.connect(server_address)

    # Send the JSON data over the socket
    sock.sendall(encode_data)
    print('Sent data to server, time = ', count)
    count +=1
    
    # Close the socket
    sock.close()

    # Wait for 1 second before sending again
    time.sleep(5)
