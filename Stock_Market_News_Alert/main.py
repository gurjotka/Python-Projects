import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "Your news api key"
STOCK_API_KEY = "your alpha vantage api key"
account_sid = "Twilio account id"
auth_token = "Authentication Token for your twilio account"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
print(yesterday_data)
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)

positive_difference = abs(day_before_yesterday_closing_price-yesterday_closing_price)
print(positive_difference)

difference_percent = (positive_difference / yesterday_closing_price) * 100
print(difference_percent)

if difference_percent > 5  :
    parameters2 = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    response2 = requests.get(url=NEWS_ENDPOINT, params=parameters2)
    response2.raise_for_status()
    news_data = response2.json()
    three_articles = news_data["articles"][0:3]

    for article in three_articles:
        title = article["title"]
        description = article["description"]
        
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Headline:{title}\nBrief:{description}",
            from_="whatsapp:Your twilio whatsapp number",
            to="whatsapp: Your verified/ your mobile phone whatsapp number"
        )
        print(message.status)


