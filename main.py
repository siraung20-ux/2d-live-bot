import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

message = """
🚀 2D Live Bot Online

✅ GitHub Actions Connected
✅ Telegram Connected

Testing Message
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHANNEL_ID,
    "text": message
}

r = requests.post(url, json=payload)

print("Status:", r.status_code)
print(r.text)
