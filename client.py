# Built-in library of socket
import socket
import json

address = "127.0.0.1"  # IP address
port = 8000             # Port number
json_file_path = 'input.json'  # Path to the JSON file

# Function to send the JSON file content to the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((address, port))

    # Read the JSON data from the file
    with open(json_file_path, 'r') as json_file:
        json_data = json_file.read()

    # Send the JSON data to the server
    client.sendall(json_data.encode('utf-8'))  # Send the JSON content as bytes

    # Receive the server's response (optional)
    response = client.recv(1024).decode()
    print(f"Received from server: {response}")
    
print("Connection closed")


