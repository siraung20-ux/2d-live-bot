import os
import requests

API_KEY = os.getenv("FINNHUB_API_KEY")

url = f"https://finnhub.io/api/v1/quote?symbol=SET.BK&token={API_KEY}"

r = requests.get(url, timeout=30)

print("STATUS:", r.status_code)
print(r.text)
