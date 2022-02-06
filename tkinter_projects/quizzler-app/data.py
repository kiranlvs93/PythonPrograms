import requests

base_url = "https://opentdb.com/api.php"
user_params = {"amount": 25, "category": 18, "type": "boolean"}
response = requests.get(url=base_url, params=user_params)
response.raise_for_status()
question_data = response.json()["results"]
