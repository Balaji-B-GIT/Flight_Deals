from twilio.rest import Client
import os
from dotenv import load_dotenv
from data_manager import DataManager
load_dotenv("C:/Python/Environmental variables/.env")
class NotificationManager:
    def __init__(self):
        self.account_sid = os.getenv("account_sid")
        self.auth_token = os.getenv("auth_token")

    def send_msg(self,msg_body):
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(from_=os.getenv("from_"),
                                         to = os.getenv("to"),
                                         body=msg_body)
