import requests
from datetime import datetime
# from requests.auth import HTTPBasicAuth
import os

GENDER = "male"
WEIGHT_KG = 81.6466
HEIGHT_CM = 180.34
AGE = 64
sheety_username = os.getenv("SHEETY_USERNAME")
sheety_password = os.getenv("SHEETY_PASSWORD")
SHEETY_PROJECT_NAME = "myWorkouts"
SHEETY_SHEET_NAME = "workouts"
sheety_authentication = 'Basic ' + str(os.getenv("SHEETY_AUTHENTICATION"))

app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{sheety_username}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("APP_KEY"),
}

basic = HTTPBasicAuth(sheety_username, sheety_password)
requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_headers = {
    "Authorization": sheety_authentication
}

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
    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_headers)

