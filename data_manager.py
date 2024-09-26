import os

import requests
from dotenv import load_dotenv
load_dotenv("C:/Python/Environmental variables/.env")
class DataManager:
    def __init__(self):
        self.url = "https://api.sheety.co/f2cc6990c1585bc16e71a2d26e7a6fbf/flightDeals/prices"

    def get_sheet_data(self):
        responses_row = requests.get(url = self.url)
        return responses_row.json()

    # def get_iata_loc(self,row):
    #     response = requests.get(url=f"{self.url}/{row}")
    #     data = response.json()
    #     return data["price"]["iataCode"]

    def put_iata(self,row,data):
        header = {
            "Authorization":f"Bearer {os.getenv('sheety_bearer_FD')}"
        }
        parameters = {
            "price":{
                "iataCode":data
            }
        }
        response = requests.put(url=f"{self.url}/{row}",json=parameters,headers=header)
        print(response.text)
