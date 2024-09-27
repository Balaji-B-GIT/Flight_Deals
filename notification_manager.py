from twilio.rest import Client
import os
from dotenv import load_dotenv
import smtplib
load_dotenv("C:/Python/Environmental variables/.env")
my_mail = "sampleforpythonmail@gmail.com"
class NotificationManager:
    def __init__(self):
        self.account_sid = os.getenv("account_sid")
        self.auth_token = os.getenv("auth_token")
        self.my_mail = "sampleforpythonmail@gmail.com"

    def send_msg(self,msg_body):
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(from_=os.getenv("from_"),
                                         to = os.getenv("to"),
                                         body=msg_body)
    def send_mail(self,msg_body,user_mail):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.my_mail, password=os.getenv("smtp_app_password"))
            connection.sendmail(from_addr=my_mail,
                                to_addrs=user_mail,
                                msg=msg_body)
