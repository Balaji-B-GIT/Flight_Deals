import requests
import os
from dotenv import load_dotenv
load_dotenv("C:/Python/Environmental variables/.env")

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

    def get_iata(self,city):
        parameters = {
            "keyword":city,
            "max":1
        }
        header = {
            "Authorization":f"Bearer {os.getenv('amadeus_access_token')}"
        }
        response = requests.get(url=self.url,params=parameters,headers=header)
        data = response.json()
        return data["data"][0]["iataCode"]


df = FlightData()