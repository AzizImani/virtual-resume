import os

from dotenv import load_dotenv
import requests


class NotificationSender:

    def __init__(self):
        load_dotenv(override=True)
        self.user = os.getenv("PUSHOVER_USER")
        self.token = os.getenv("PUSHOVER_TOKEN")
        self.url = "https://api.pushover.net/1/messages.json"

    def push(self, message):
        print(f"Push: {message}")
        payload = {"user": self.user, "token": self.token, "message": message}
        requests.post(self.url, data=payload)

