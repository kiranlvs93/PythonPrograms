from twilio.rest import Client
import os


class NotificationManager:
    TWILIO_ACC_ID = ""
    TWILIO_AUTH_TOKEN = ""
    TWILIO_MESSAGING_SERVICE_SID = ""
    TO_NUMBER = ""

    def __init__(self):
        self.TWILIO_ACC_ID = os.getenv("TWILIO_ACC_ID")
        self.TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
        self.TWILIO_MESSAGING_SERVICE_SID = os.getenv("TWILIO_MESSAGING_SERVICE_SID")
        self.TO_NUMBER = os.getenv("TO_NUMBER")

    def send_sms(self, message):
        client = Client(self.TWILIO_ACC_ID, self.TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            messaging_service_sid=self.TWILIO_MESSAGING_SERVICE_SID,
            body=message,
            to=self.TO_NUMBER
        )
        print(message.sid)
