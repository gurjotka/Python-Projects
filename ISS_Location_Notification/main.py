import requests
from datetime import datetime
import smtplib
import random


MY_LAT = 28.613939
MY_LONG = 77.209023

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Kolkata",
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

my_email = "your email@gmail.com"
password = "Your Password"
text_msg = "Look up at ISS, it is near you"


if (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5) and (MY_LAT -5 <= iss_latitude <= MY_LAT + 5):
    if time_now.hour > sunset:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="youremail@yahoo.com",
                                msg=f"Subject: ISS Alert\n\n{text_msg}")





