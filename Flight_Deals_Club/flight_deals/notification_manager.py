import smtplib

from twilio.rest import Client
import os

MY_NUMBER = os.environ["TWILIO_MY_NUMBER"]
TWILIO_WHATSAPP = os.environ["TWILIO_WHATSAPP"]
TWILIO_SMS = os.environ["TWILIO_SMS"]

MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]

    def send_whatsapp(self, title, description):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
                    body=f"Headline:{title}\nBrief:{description}",
                    from_=f"whatsapp:{TWILIO_WHATSAPP}",
                    to=f"whatsapp:{MY_NUMBER}"
        )
        print(message.status)

    def send_sms(self, title, description):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
                    body=f"Headline:{title}\nBrief:{description}",
                    from_=TWILIO_SMS,
                    to=MY_NUMBER
        )
        print(message.status)

    def send_email(self, email, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject: Flight Deals\n\n{message}")
        print("Email sent")

