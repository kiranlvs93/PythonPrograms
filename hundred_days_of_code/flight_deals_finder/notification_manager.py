from twilio.rest import Client
import os

TWILIO_ACC_ID = os.getenv("TWILIO_ACC_ID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_MESSAGING_SERVICE_SID = os.getenv("TWILIO_MESSAGING_SERVICE_SID")
TO_NUMBER = os.getenv("TO_NUMBER")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_ACC_ID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            messaging_service_sid=TWILIO_MESSAGING_SERVICE_SID,
            body=message,
            to=TO_NUMBER
        )
        print("Message is sent", message.sid)
