import requests
from datetime import datetime


USERNAME = "#Select your username"
TOKEN = "#Select any token randomly by yourself"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# Date = datetime(year=2024, month=11, day=27)
Date = datetime.now()
Date_req = Date.strftime("%Y%m%d")
# graph_value_endpoint_put_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{Date_req}"
graph_value_endpoint_post = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_value_config = {
    "date": Date_req,
    "quantity": input("How many km did you run today?"),
}

response = requests.post(url=graph_value_endpoint_post, json=graph_value_config, headers=headers)
print(response.text)

# response = requests.put(url=graph_value_endpoint_put_delete, json=graph_value_config, headers=headers)
# print(response.text)
# response = requests.delete(url=graph_value_endpoint_put_delete, json=graph_value_config, headers=headers)
# print(response.text)