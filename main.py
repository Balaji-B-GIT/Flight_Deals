#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import time
from data_manager import DataManager
from flight_data import cheapest_flights
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import load_dotenv

from flight_search import FlightSearch

load_dotenv("C:/Python/Environmental variables/.env")
MY_LOC = input("Enter your nearest airport IATA code/Country IATA code(ex:LON) :")

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

sheet_data = dm.get_sheet_data()
user_mails = dm.get_users_data()

departure_date = input("Enter departure date(YYYY-MM-DD):")
return_date = input("Enter return date(YYYY-MM-DD):")

# Here looping through row data in sheet_data
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    # 'flights' will store the available flight data for the destination in sheet_data(city)
    flights = fs.available_flights(origin=MY_LOC,
                                   destination=destination["iataCode"],
                                   departure_date=departure_date,
                                   return_date=return_date,
                                   non_stop="true")
    # we send this data to cheapest_flights to get the cheapest flight data in which flight is non-stop
    cheapest_flight = cheapest_flights(flights)
    print(f"Current cheapest price INR {cheapest_flight.price}")
    # If there is no flights is available in non-stop flights then we have to find in multi-stop flights
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = fs.available_flights(origin=MY_LOC,
                                       destination=destination["iataCode"],
                                       departure_date=departure_date,
                                       return_date=return_date,
                                       non_stop="false")
        cheapest_stopover_flight = cheapest_flights(stopover_flights)
        # If there is not a single flight available then print this
        if cheapest_stopover_flight.price == "N/A":
            print(f"Not even a single flight to {destination['city']}")\

        elif cheapest_stopover_flight.price < destination["lowestPrice"]:
            print(f"Lower price for stop over flight found to {destination['city']}!")
            # nm.send_msg(
            #     msg_body=f"Low price alert! Only ₹{cheapest_flight.price} to fly "
            #              f"from {cheapest_flight.originLocationCode} to {cheapest_flight.destinationLocationCode}, "
            #              f"on {cheapest_flight.departureDate} until {cheapest_flight.returnDate}."
            # )

            # If we found cheapest flight then we send mail to all the users in users_mails
            for user in user_mails:
                print(f'sending mail to {user["what'sYourFullName?"]}....')
                mail = user["enterYourEmailAddress"]
                nm.send_mail(msg_body=f"Low price alert! Only INR {cheapest_stopover_flight.price} to fly "
                                      f"from {cheapest_stopover_flight.originLocationCode} to {cheapest_stopover_flight.destinationLocationCode}, "
                                      f"with {cheapest_stopover_flight.stops}stops "
                                      f"on {cheapest_stopover_flight.departureDate} until {cheapest_stopover_flight.returnDate}.",
                             user_mail=mail)

    elif cheapest_flight.price < destination["lowestPrice"] and cheapest_flight != "N/A":
        print(f"Lower price flight found to {destination['city']}!")
        # nm.send_msg(
        #     msg_body=f"Low price alert! Only ₹{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.originLocationCode} to {cheapest_flight.destinationLocationCode}, "
        #                  f"on {cheapest_flight.departureDate} until {cheapest_flight.returnDate}."
        # )
        for user in user_mails:
            print(f'sending mail to {user["what'sYourFullName?"]}....')
            mail = user["enterYourEmailAddress"]
            nm.send_mail(msg_body=f"Low price alert! Only INR {cheapest_flight.price} to fly "
                             f"from {cheapest_flight.originLocationCode} to {cheapest_flight.destinationLocationCode}, "
                             f"on {cheapest_flight.departureDate} until {cheapest_flight.returnDate}.",
                         user_mail=mail)

    time.sleep(5)

