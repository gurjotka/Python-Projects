import os
from venv import create

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your api key"
account_sid = "AC96b048e5047e1f199277c94c23913377"
auth_token = "your_authentication_Key"


parameters = {
    "lat": 28.638880,
    "lon": 77.087150,
    "appid": api_key,
    "cnt":4,
}
response = requests.get(url = OWM_Endpoint, params= parameters)
response.raise_for_status()
weather_data=response.json()
# print(response.status_code)
# weather_id = weather_data["list"][0]["weather"][0]["id"]

will_rain = False
for hour_data in weather_data["list"]:
    weather = hour_data["weather"]
    for day_weather in weather:
        weather_id = day_weather["id"]
        if int(weather_id) < 700:
            will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's gonna rain today. Bring your umbrella",
        from_= "whatsapp:your_twilio_trial_number",
        to = "whatsapp:your_verified_mobile_number"
    )
    print(message.status)
