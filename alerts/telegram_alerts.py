
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_text(message: str) -> bool:
    url = f"{BASE_URL}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    r = requests.post(url, data=data)
    return r.status_code == 200

def send_photo(photo_path: str, caption: str = "") -> bool:
    url = f"{BASE_URL}/sendPhoto"
    with open(photo_path, "rb") as f:
        files = {"photo": f}
        data = {"chat_id": CHAT_ID, "caption": caption}
        r = requests.post(url, data=data, files=files)
    return r.status_code == 200
def send_video(video_path: str, caption: str = "") -> bool:
    url = f"{BASE_URL}/sendVideo"
    with open(video_path, "rb") as f:
        files = {"video": f}
        data = {"chat_id": CHAT_ID, "caption": caption}
        r = requests.post(url, data=data, files=files, timeout=60)
    if r.status_code != 200:
        print("Telegram send_video failed:", r.status_code, r.text)
    return r.status_code == 200
