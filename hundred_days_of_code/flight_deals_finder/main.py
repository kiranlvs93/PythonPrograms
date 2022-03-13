import json
import os
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

SHEET_NAME = os.getenv("FF_SHEET_NAME")
data_mng = DataManager(SHEET_NAME)
flight_search = FlightSearch()
#
# notifications = NotificationManager()
# notifications.send_sms("Test SMS")

PUT_BODY = {"price": {}}


def update_iata_code(input_sheet):
    for row in input_sheet:
        city = row["city"]
        iata_code = row["iataCode"]
        lowest_price = row["lowestPrice"]
        row_no = row["id"]
        print(city, iata_code, lowest_price, row_no, sep=",")
        if iata_code == "":
            row["iataCode"] = flight_search.get_iata_code(city_name=city)
            PUT_BODY["price"] = row
            data_mng.update_row(params=PUT_BODY, row_num=row_no)
    print("IATA code for all the cities is updated successfully")


if __name__ == '__main__':

    # Update the location IATA code if its empty
    prices_sheet = data_mng.sheet_data["prices"]
    update_iata_code(input_sheet=prices_sheet)
