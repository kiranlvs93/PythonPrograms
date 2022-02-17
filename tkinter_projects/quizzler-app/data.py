import requests

# Coe to fetch the questions from the OPENTDB website.
# Since this program is designed for True False, we are fetching only boolean type of questions
base_url = "https://opentdb.com/api.php"
user_params = {"amount": 5, "category": 20, "type": "boolean"}
response = requests.get(url=base_url, params=user_params)
response.raise_for_status()
question_data = response.json()["results"]
