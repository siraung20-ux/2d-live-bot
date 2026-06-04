import os
import requests

url = "https://thai-lotto-new-api.p.rapidapi.com/api/v1/live"

headers = {
    "x-rapidapi-host": "thai-lotto-new-api.p.rapidapi.com",
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers, timeout=60)

print("STATUS:", r.status_code)
print(r.text)
