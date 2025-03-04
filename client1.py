import socket
import json
import os
from dotenv import load_dotenv
load_dotenv()

address = os.getenv("SERVER_IP")  # IP address
port = int(os.getenv("SERVER_PORT"))  # Port number
# Sample data that you want to send as JSON

with open('trial.json', 'r' ) as json_file:
    data = json_file.read()
    json_data = json.dumps(data)

#print(data)


# Function
def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        while True:
            # Send JSON data (encoded to bytes)
            client.send(json_data.encode())

            response = client.recv(1024).decode()
            if response.lower() == "closed":
                break

            print(f"Received: {response}")
            break

    print("Connection closed")

# Function Declaration
run_client()
