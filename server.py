import requests
from flask import Flask
import json
import csv

def get_access_token():
    url = "https://api.baubuddy.de/index.php/login"
    payload = {
        "username": "365",
        "password": "1"
    }
    headers = {
        "Authorization": "Basic QVBJX0V4cGxvcmVyOjEyMzQ1NmlzQUxhbWVQYXNz",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()["oauth"]["access_token"]

token = get_access_token()

def get_resources():
    url = "https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    #print(response.text)
    return response.json()
    

   
   

# resources = get_resources()

from flask import Flask, request
import json
import csv
from io import StringIO


app = Flask(__name__)

# API endpoint to handle POST request
@app.route('/process_vehicles', methods=['POST'])
def process_vehicles():
    token = get_access_token()
    resources = get_resources()
    if request.method == 'POST':
        client_data = json.loads(request.get_json())
        print(f"len : {len(client_data)}, kurzname : {client_data[0]['kurzname']}")
    return json.dumps(resources), 200 


app.run(host='0.0.0.0', port=8080)

