#Built in libary of socket
import socket


address = "127.0.0.1" #IP address
port = 8000 #port number
msg = "Hello, server!"  # Message 

#Function
def run_client():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((address, port))

        while True:
            client.send(msg.encode()[:1024])  

            response = client.recv(1024).decode()
            if response.lower() == "closed":
                break

            print(f"Received: {response}")
            break

    print("Connection closed")

#Function Declaration
run_client()
