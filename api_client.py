import requests,json

# Define the URL of the API
url = "http://localhost:5000/sun-spot-analyser-api/grid"

# Define the data to be sent to the API
data = {
  "size": 3,
  "values": "4,2,3,2,2,1,3,2,1"
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Send the POST request to the API
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

# Print the response from the API
print("Response Status Code:", response.status_code)
print("Response Content:", response.json())

# Get the ID of the created grid
grid_id = response.json()['id']

# Define the URL for getting scores
score_url = f"http://localhost:5000/sun-spot-analyser-api/scores?id={grid_id}"

# Send the GET request to the API
score_response = requests.get(score_url)

# Print the response from the API
print("Score Response Status Code:", score_response.status_code)
print("Score Response Content:", score_response.json())

