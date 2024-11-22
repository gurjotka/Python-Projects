import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "AC96b048e5047e1f199277c94c23913377"
auth_token = os.environ.get("OWM_AUTH_TOKEN")


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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client = proxy_client)
    message = client.messages \
        .create(
        body="It's gonna rain today. Bring your umbrella",
        from_= "whatsapp:your twilio trial number",
        to = "whatsapp:your verified mobile phone number on twilio"
    )
    print(message.status)
