import requests
import os
from dotenv import load_dotenv
load_dotenv("C:/Python/Environmental variables/.env")

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

    def get_iata(self):
        parameters = {
            "keyword":"Paris"
        }
        header = {
            "Authentication":f"Bearer {os.getenv('amadeus_key')}"
        }
        response = requests.get(url=self.url,params=parameters,headers=header)
        print(response.text)

df = FlightData()
df.get_iata()