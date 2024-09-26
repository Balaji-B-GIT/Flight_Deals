#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import time
from data_manager import DataManager
from flight_data import cheapest_flights
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import load_dotenv
import datetime as dt

from flight_search import FlightSearch

load_dotenv("C:/Python/Environmental variables/.env")
MY_LOC = "LON"

dm = DataManager()
fs = FlightSearch()
nm =NotificationManager()

# This portion of code is used to generate and store iata codes in google sheet-----------------------------------------
# sheet_data = dm.get_sheet_data()["prices"]
# for row in sheet_data:
#     city_name = row["city"]
#     id = row["id"]
#     iata = fd.get_iata(city=city_name)
#     dm.put_iata(row=id,data=iata)
#---------------------------------------------------------------------------------------------------------------------

sheet_data = dm.get_sheet_data()["prices"]
today = dt.datetime.now()

departure_date = input("Enter departure date(YYYY-MM-DD):")
return_date = input("Enter return date(YYYY-MM-DD):")

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = fs.available_flights(origin=MY_LOC,
                                   destination=destination["iataCode"],
                                   departure_date=departure_date,
                                   return_date=return_date,
                                   non_stop="true")
    cheapest_flight = cheapest_flights(flights)
    print(cheapest_flight.price)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        nm.send_msg(
            msg_body=f"Low price alert! Only ₹{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.originLocationCode} to {cheapest_flight.destinationLocationCode}, "
                         f"on {cheapest_flight.departureDate} until {cheapest_flight.returnDate}."
        )
    elif cheapest_flight.price == "N/A":
        stopover_flights = fs.available_flights(origin=MY_LOC,
                                       destination=destination["iataCode"],
                                       departure_date=departure_date,
                                       return_date=return_date,
                                       non_stop="false")
        cheapest_stopover_flight = cheapest_flights(stopover_flights)
        print(f"Lower price for stop over flight found to {destination['city']}!")
        nm.send_msg(
            msg_body=f"Low price alert! Only ₹{cheapest_flight.price} to fly "
                     f"from {cheapest_flight.originLocationCode} to {cheapest_flight.destinationLocationCode}, "
                     f"on {cheapest_flight.departureDate} until {cheapest_flight.returnDate}."
        )
    time.sleep(5)

