import requests
from datetime import datetime
import os

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
NUTRITIONIX_BASE_URL = "https://trackapi.nutritionix.com"
NUTRITIONIX_NUTRIENTS_ENDPOINT = "/v2/natural/nutrients"
NUTRITIONIX_EXERCISE_ENDPOINT = "/v2/natural/exercise"
headers = {"x-app-id": NUTRITIONIX_APP_ID, "x-app-key": NUTRITIONIX_APP_KEY, "x-remote-user-id": "0",
           "Content-Type": "application/json"}


class CalorieCounter:
    calories_intake = 0.0
    calories_burnt = 0.0
    activities = [dict()]

    def get_nutrient_details(self, params):
        """
        Get the nutrition details from the API
        :param params:
        :return:
        """
        response = requests.post(url=NUTRITIONIX_BASE_URL + NUTRITIONIX_NUTRIENTS_ENDPOINT, headers=headers,
                                 json=params)
        print(response.json())
        print(response.raise_for_status())

    def get_exercise_details(self, params):
        """
        Get the exercise details like exercise name, duration and calories burnt from the natural lang input
        :param params:
        :return:
        """
        print("Getting response")
        response = requests.post(url=NUTRITIONIX_BASE_URL + NUTRITIONIX_EXERCISE_ENDPOINT, headers=headers, json=params)
        print(response.json())
        response.raise_for_status()
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")
        exercises = response.json()["exercises"]
        for exercise in exercises:
            activity = {"workout": {'date': date, 'time': time, 'exercise': exercise['name'].capitalize(),
                                    'duration': exercise['duration_min'], 'calories': exercise['nf_calories']}}
            self.activities.append(activity)
