# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import os
from notification_manager import NotificationManager
import data_manager
from data_manager import DataManager
from flight_data import FlightData

SHEET_NAME = os.getenv("FF_SHEET_NAME")
data_mng = DataManager(SHEET_NAME)
#
# notifications = NotificationManager()
# notifications.send_sms("Test SMS")


def read_sheet():
    print(data_mng.read_sheet())


if __name__ == '__main__':
    # read_sheet()
    print(data_mng.sheet_data)
