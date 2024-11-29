import requests
from datetime import datetime


APP_ID = "your nutritionix api id"
APP_KEY = "your nutritionix api key"
nutritionix_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = your gender
WEIGHT = your weight
AGE = your age

sheety_url = "Your sheety api url"
BEARER_TOKEN = "Your bearer auth token"

exercise_text = input("Tell me how you exercised today?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "age": AGE,
}

response = requests.post(url=nutritionix_endpoints, json=body, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    response2 = requests.post(url=sheety_url, json=sheet_inputs, headers=headers)
    print(response2.text)

