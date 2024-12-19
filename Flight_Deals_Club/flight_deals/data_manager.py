from pprint import pprint
from dotenv import load_dotenv
import requests
import os
from requests.auth import HTTPBasicAuth

load_dotenv()


class DataManager:
    def __init__(self):
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.price_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.url_endpoint = os.getenv("SHEETY_URL_ENDPOINT")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}
        self.customer_email_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.price_endpoint, auth=self.authorization)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{self.price_endpoint}/{city["id"]}",
                auth=self.authorization,
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.url_endpoint, auth=self.authorization)
        response.raise_for_status()
        data = response.json()
        self.customer_email_data = data["users"]
        return self.customer_email_data