import socket
import json
import csv
import keyboard
import os
from dotenv import load_dotenv
load_dotenv()

address = os.getenv("SERVER_IP")  # IP address
port = (os.getenv("SERVER_PORT"))  # Port number
csv_filename = "trial.csv"  # CSV file to save data

# Function to handle the server
def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((address, port))
        server.listen(1)  # The server listens for one incoming connection
        print(f"Server listening on {address}:{port}...")

        # Accept a connection from the client
        conn, addr = server.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # Receive the data from the client
                data = conn.recv(1024)
                if not data:
                    break

                # Decode the JSON data from bytes
                try:
                    json_data = data.decode()
                    parsed_data = json.loads(json_data)
                    print("Received JSON data:", parsed_data)

                    # Save the JSON data to a CSV file
                    save_to_csv(parsed_data)

                    # Send a response to the client
                    response = "Received and saved JSON to CSV successfully"
                    conn.send(response.encode())

                except json.JSONDecodeError:
                    print("Error decoding JSON.")
                    conn.send("Error: Invalid JSON format".encode())
                    break
        print("Connection closed")

# Function to save JSON data to a CSV file
def save_to_csv(json_data):
    # Check if the CSV file exists to write headers (if it's the first time writing)
    file_exists = False
    try:
        with open(csv_filename, 'r', newline='') as f:
            file_exists = True
    except FileNotFoundError:
        pass  # If the file doesn't exist, we'll create it later

    # Open CSV file to append data
    with open(csv_filename, 'a', newline='') as csvfile:
        fieldnames = json_data.keys()  # Use the keys of the JSON as CSV headers

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only if the file is empty or doesn't exist
        if not file_exists:
            writer.writeheader()

        # Write the JSON data as a new row
        writer.writerow(json_data)

    print(f"Data saved to {csv_filename}")


if __name__ == "__main__":
    while True:
        run_server()
        if keyboard.is_pressed("q"):
            break