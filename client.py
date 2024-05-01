import csv
import json
import requests 
import re

def csv_to_json(csv_file, has_headers=True):
    data = []
    with open(csv_file,  'r') as f:
        reader = csv.reader(f,delimiter='\n')
        headers = []
        for i,row in enumerate(reader):
            if i == 0:
                headers = row[0].split(';')
            else:
                elements = row[0].split(';')
                data.append(dict(zip(headers, elements)))
    return data

csv_data = csv_to_json('vehicles_organized.csv')

json_string = json.dumps(csv_data, indent=4)
#print(json_string)

url = "http://0.0.0.0:8080/process_vehicles"  # Replace with your server details
headers = {'Content-Type': 'application/json'}  # Set content type for JSON data

response = requests.post(url, json=json_string, headers=headers)

if response.status_code == 200:
  print("Data processed successfully!")
  # Handle successful response (e.g., print response content)
else:
  print(f"Error: {response.status_code}")
  # Handle error (e.g., print error message)
