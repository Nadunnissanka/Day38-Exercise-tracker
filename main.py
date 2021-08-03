import requests
from datetime import datetime
import os

APP_ID = "65986a3e"
API_KEY = "296df3671e4cd5ab5e41ae06371c16a6	"
NUTRITIONIX_API_ENDPIONT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/4f8efd039bee59a2e8700dd020935dc8/myWorkouts/workouts"

text_input = input("Tell me which exercise you did: ")

GENDER = "male"
WEIGHT_KG = 85
HEIGHT_CM = 167
AGE = 22

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": text_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

request = requests.post(url=NUTRITIONIX_API_ENDPIONT, headers=headers, json=parameters)
result = request.json()

today_date = datetime.now().strftime("%d/%m/%y")
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

headers = {"Authorization": "Bearer thisismybearertoken"}
sheety_request = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=headers)
sheety_result = sheety_request.json()
print(sheety_result)
