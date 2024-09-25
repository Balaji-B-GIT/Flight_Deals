import requests
import os
from dotenv import load_dotenv
load_dotenv("C:/Python/Environmental variables/.env")
import datetime as dt



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    def cheap_price(self,start,end,departure_date,return_date):
        parameters = {
            "originLocationCode":start,
            "destinationLocationCode":end,
            "departureDate":departure_date,
            "returnDate":return_date,
            "adults":1,
            "nonStop":"true",
            "currencyCode":"GBP",
        }
        header = {
            "Authorization": f"Bearer {os.getenv('amadeus_access_token')}"
        }
        response = requests.get(url=self.url,params=parameters,headers=header)
        return response.json()


    today = dt.datetime.now()
    for i in range(1):
        date = today + dt.timedelta(days=i)
        departure_date = today.strftime("%Y-%m-%d")
        return_date = date.strftime("%Y-%m-%d")
        cheap_price()

