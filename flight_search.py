import requests
import os
from dotenv import load_dotenv

from flight_data import FlightData

load_dotenv("C:/Python/Environmental variables/.env")
iata_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
flight_url ="https://test.api.amadeus.com/v2/shopping/flight-offers"
token_url ="https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        self.token = self.generate_token()

    def generate_token(self):
        token_parameters = {
            "grant_type":'client_credentials',
            "client_id":os.getenv("amadeus_key"),
            "client_secret":os.getenv("amadeus_secret")
        }
        response = requests.post(url = token_url,data=token_parameters)
        return response.json()['access_token']


    def get_iata(self,city):
        parameters = {
            "keyword":city,
            "max":1,
            "include": "AIRPORTS",
        }
        header = {
            "Authorization":f"Bearer {os.getenv('amadeus_access_token')}"
        }
        response = requests.get(url=iata_url,params=parameters,headers=header)
        data = response.json()
        try:
            return data["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")


    def available_flights(self,origin,destination,departure_date,return_date,non_stop):
        parameters = {
            "originLocationCode":origin,
            "destinationLocationCode":destination,
            "departureDate":departure_date,
            "returnDate":return_date,
            "adults":1,
            "nonStop":non_stop,
            "currencyCode":"INR",
        }
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=flight_url,params=parameters,headers=header)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None
        return response.json()



