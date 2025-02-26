import json
import csv

# Get the path to the JSON file from user input
json_file_path = input("Enter the path to the JSON file: ")

# Open and load the JSON data
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Assuming the JSON data is a list of dictionaries, as this is the most common structure for CSV export
csv_file_path = input("Enter the path to save the CSV file: ")

# Write the data to a CSV file
with open(csv_file_path, 'a') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
    writer.writerows(data)

print(f"CSV file has been saved to {csv_file_path}")
