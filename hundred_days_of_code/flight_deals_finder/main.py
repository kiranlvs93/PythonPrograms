import os
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch

SHEET_NAME = os.getenv("FF_SHEET_NAME")
data_mng = DataManager(SHEET_NAME)
flight_search = FlightSearch()
notifications = NotificationManager()

departure_city = "Bengaluru"
ORIGIN_CITY_IATA = "BLR"


def update_iata_code(input_sheet):
    put_body = {"price": {}}
    for row in input_sheet:
        city = row["city"]
        iata_code = row["iataCode"]
        lowest_price = row["lowestPrice"]
        row_no = row["id"]
        print(city, iata_code, lowest_price, row_no, sep=",")
        if iata_code == "":
            row["iataCode"] = flight_search.get_iata_code(city_name=city)
            put_body["price"] = row
            data_mng.update_row(params=put_body, row_num=row_no)
    print("IATA code for all the cities is updated successfully")


if __name__ == '__main__':
    # Update the location IATA code if its empty
    prices_sheet = data_mng.sheet_data["prices"]
    update_iata_code(input_sheet=prices_sheet)

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in prices_sheet:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        if flight.price < destination["lowestPrice"]:
            notifications.send_sms(
                message=f"Low price alert! Only Rs{flight.price} to fly from "
                        f"{flight.origin_city}-{flight.origin_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.out_date} to {flight.return_date}."
            )
