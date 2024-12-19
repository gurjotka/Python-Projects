#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flights
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
customer_email = data_manager.get_customer_emails()
notification_manager = NotificationManager()

flight_search = FlightSearch()

ORIGIN_CITY_IATA = "DEL"
customer_email_list = [row["yourEmail?"] for row in customer_email]
print(f"Customer Email Data:{customer_email_list}")

if sheet_data[0]["iataCode"] == "TESTING" or sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
    print(f"sheet_data:\n {sheet_data}")


    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting direct flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )

    cheapest_flight = find_cheapest_flights(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"{destination['city']}: ₹{cheapest_flight.price}")
        notification_manager.send_whatsapp(
            title = f"Low flights alert! Only ₹{cheapest_flight.price} to fly ",
            description = f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport},"
                          f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
        for email in customer_email_list:
            notification_manager.send_email(
                email= f"{email}",
                message=f"Low flights alert! Only Rs{cheapest_flight.price} to fly, "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport},"
                          f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )

    time.sleep(2)

    if cheapest_flight.price == "N/A":
        print(f"No direct flights to {destination['city']}. Looking for indirect flights...")
    stopover_flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        is_direct=False
    )
    cheapest_flight = find_cheapest_flights(stopover_flights)
    print(f"Cheapest indirect flight price is: Rs{cheapest_flight.price}")
    # notification_manager.send_whatsapp(
    #     title=f"Low Indirect flights alert! Only ₹{cheapest_flight.price} to fly ",
    #     description=f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport},"
    #                 f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
    # )