import requests
import os
from dotenv import load_dotenv
load_dotenv("C:/Python/Environmental variables/.env")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://test.api.amadeus.com/v1/shopping/flight-dates"

    def cheap_price(self,start,end,max_price,date):
        parameters = {
            "origin":start,
            "destination":end,
            "maxPrice":max_price,
            "departureDate":date
        }
        header = {
            "Authorization": f"Bearer {os.getenv('amadeus_access_token')}"
        }
        response = requests.get(url=self.url,params=parameters,headers=header)
        print(response.text)

fs = FlightSearch()

fs.cheap_price(start ="MAD",end="MUC",max_price=1000,date="2024-09-25,2024-12-31")