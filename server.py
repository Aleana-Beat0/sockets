import socket

address = "127.0.0.1"
port = 8000

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((address, port))
        server.listen(1)
        print("Listening on 127.0.0.1:8000")

        client_socket, client_address = server.accept()
        with client_socket:
            print(f"Connection from {client_address[0]}:{client_address[1]}")

            request = client_socket.recv(1024).decode() 
            print(f"Received: {request}")

            client_socket.send("closed".encode())

    print("Connection closed")

run_server()
