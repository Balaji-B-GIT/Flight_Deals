#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from data_manager import DataManager
from flight_data import FlightData
from dotenv import load_dotenv
load_dotenv("C:/Python/Environmental variables/.env")

# This portion of code is used to generate access code--------------------------------------------------------------
# token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
# parameters = {
#     "grant_type":'client_credentials',
#     "client_id":os.getenv("amadeus_key"),
#     "client_secret":os.getenv("amadeus_secret")
# }
# response = requests.post(url = token_url,data=parameters)
# print(response.text)
# ---------------------------------------------------------------------------------------------------------------------

dm = DataManager()
fd = FlightData()

# This portion of code is used to generate and store iata codes in google sheet-----------------------------------------
# sheet_data = dm.get_sheet_data()["prices"]
# for row in sheet_data:
#     city_name = row["city"]
#     id = row["id"]
#     iata = fd.get_iata(city=city_name)
#     dm.put_iata(row=id,data=iata)
#---------------------------------------------------------------------------------------------------------------------
