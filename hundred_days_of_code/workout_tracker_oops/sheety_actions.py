import requests
import os

SHEETY_API_KEY = os.getenv("SHEETY_API_KEY")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
SHEET_NAME = "workouts"
URL = f"https://api.sheety.co/{SHEETY_API_KEY}/workoutTrackerUsingPython/{SHEET_NAME}"
HEADERS = {"Authorization": SHEETY_AUTH, "Content-Type": "application/json"}


class Sheety:
    def update_sheet(self, params):
        print("Updating the sheet")
        requests.post(url=URL, headers=HEADERS, json=params)
