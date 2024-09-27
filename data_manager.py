import os

import requests
from dotenv import load_dotenv
load_dotenv("C:/Python/Environmental variables/.env")
class DataManager:
    def __init__(self):
        self.price_url = "https://api.sheety.co/f2cc6990c1585bc16e71a2d26e7a6fbf/flightDeals/prices"
        self.user_url = "https://api.sheety.co/f2cc6990c1585bc16e71a2d26e7a6fbf/flightDeals/users"

    def get_sheet_data(self):
        responses_row = requests.get(url = self.price_url)
        data = responses_row.json()
        return data["prices"]

    def get_users_data(self):
        response_mail = requests.get(url = self.user_url)
        data = response_mail.json()
        return data["users"]


    def put_iata(self,row,data):
        header = {
            "Authorization":f"Bearer {os.getenv('sheety_bearer_FD')}"
        }
        parameters = {
            "price":{
                "iataCode":data
            }
        }
        response = requests.put(url=f"{self.price_url}/{row}",json=parameters,headers=header)
        print(response.text)
