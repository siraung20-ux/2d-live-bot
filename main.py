import os
import requests
import json

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

url = "https://thai-lotto-new-api.p.rapidapi.com/api/v1/live"

headers = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "thai-lotto-new-api.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

try:
    data = response.json()
    print(json.dumps(data, indent=2))
except Exception as e:
    print(response.text)
