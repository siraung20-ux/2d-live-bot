import os
import time
import requests

r = requests.get("https://httpbin.org/get", timeout=20)

print(r.status_code)
print(r.text[:200])
url = "https://thai-lotto-new-api.p.rapidapi.com/api/v1/live"

headers = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "thai-lotto-new-api.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY
}

for attempt in range(3):
    try:
        r = requests.get(url, headers=headers, timeout=20)

        print("Status:", r.status_code)
        print(r.text)

        break

    except Exception as e:
        print("Attempt", attempt + 1, "failed:", e)
        time.sleep(5)
