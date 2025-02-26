import socket
import csv
import json
import os

from dotenv import load_dotenv
load_dotenv()

address = os.getenv("SERVER_IP") # IP address
port = int(os.getenv("SERVER_PORT")) # Port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((address, port))
    server.listen(1)
    print("Listening on 127.0.0.1:8000")

    client_socket, client_address = server.accept()
    
    with client_socket:
        print(f"Connection from {client_address[0]}:{client_address[1]}")

        data = client_socket.recv(1024).decode() 
        
        jf = json.loads(data)

        with open("trial.csv", 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writerows(jf)
            print("Successful Data")


        client_socket.send("closed".encode())

print("Connection closed")

